from algoritmes.astar import astar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv
from functions.csvwriter import *
from functions.csvreader import *


def init_grid(x_length, y_length, location_dict):
    """ Initialises a 2 dimensional array the the location of chips for visualisation purposes """
    grid = [[[0 for x in range(x_length)] for y in range(y_length)] for z in range(7)]

    for location in location_dict:
        grid[location_dict[location][0]][location_dict[location][1]][location_dict[location][2]] = int(location)

    return grid


def manhattan_distance(x_base, x_goal, y_base, y_goal):
    """ Calculates the manhattan distance between two points on the grid"""
    distance = abs(x_base - x_goal) + abs(y_base - y_goal)
    
    return distance


def plot_3dgraph(chip_locations, routes):
    """ Creates an interactive 3d graph of the chips and circuits """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Add the chips as points
    x = []
    y = []
    print(chip_locations)
    for i in chip_locations:
        x.append(chip_locations[i][1])
        y.append(chip_locations[i][2])

    z = [0 for i in x]
    
    ax.scatter(x,y,z,s=75, c='r', marker='s')
    
    # Add the routes as wires
    for x in routes:
        wires_x = []
        wires_y = []
        wires_z = []
        for y in routes[x]:
            wires_x.append(y[1])
            wires_y.append(y[2])
            wires_z.append(y[0])

        ax.plot(wires_x, wires_y, wires_z)
    
    plt.yticks(np.arange(min(y), max(y), 1.0))
    outfilename = input("Enter filename for the output image: ")
    outfilename = "../resultaten/{}.png".format(outfilename)
    plt.savefig(outfilename, bbox_inches='tight')
    plt.show()


def find_routes(tuplelist, location_dict, min_md, grid, final_routes, finished_routes):
    finished_routes = finished_routes
    restart = True
    while restart == True:
        for route in tuplelist:
            coordinates_base = location_dict[route[0]]
            coordinates_goal = location_dict[route[1]]

            min_md[route] = manhattan_distance(coordinates_base[1], coordinates_goal[1], coordinates_base[2], coordinates_goal[2])

        # Calculate the ideal circuit length by adding up all the manhattan distances
        ideal_score = sum(min_md[x] for x in min_md)

        # Sort the routes by length
        min_md_sorted = {k: v for k, v in sorted(min_md.items(), key=lambda item: item[1])}
        smallest_routes_first = [x for x in min_md_sorted]
        # print(f"smalles routes sorted: {smallest_routes_first}")

        i = 1
        for route in tuplelist:
            # print(f"route {i}: {route}")
            # # print(f"finished routes: {finished_routes}")
            # print(f"finished routes: {len(finished_routes)}")
            if len(finished_routes) == 30:
                restart = False
                return restart
            i += 1

            # Get the coordinates from the dictionary with the locations of the chips
            coordinates_base = location_dict[route[0]]
            coordinates_goal = location_dict[route[1]]

            # Set the start and end chips
            start = (coordinates_base[0], coordinates_base[1], coordinates_base[2])
            end = (coordinates_goal[0], coordinates_goal[1], coordinates_goal[2])

            # Calculate a path using the A-star algoritm
            path = astar(grid, start, end)

            if path == None:            
                # Move the route that breaks the algorithm to the front of the routeslist
                collision_route = route
                tuplelist.remove(route)
                tuplelist.insert(0, collision_route)
            
                final_routes.clear()
                print(f"finished routes: {len(finished_routes)}")
                finished_routes.clear()
                restart == False
                return restart
            
            # Adjust the grid for the current iterations route
            for location in path:
                # If the position in the grid is a letter, don't make it a '1'
                if grid[location[0]][location[1]][location[2]] != 0 and grid[location[0]][location[1]][location[2]] != 1:
                    continue

                # Else change the zero to a '1'
                else:
                    grid[location[0]][location[1]][location[2]] = 1

            # Set the route as value in the final_routes dict, with the netlist as key
            final_routes[route] = path
            finished_routes.append(route)


def main():
    location_dict, chip_netlists = csv_reader()
    grid = init_grid(13, 18, location_dict)
    final_routes = {}
    min_md = {}

    # Calculate route between the two chips
    tuplelist = [(route[0], route[1]) for route in chip_netlists]
    print(f"tuplelist: {tuplelist}")
    print(f"length tuplelist: {len(tuplelist)}")

    finished_routes = []

    find_routes(tuplelist, location_dict, min_md, grid, final_routes, finished_routes)
    while len(finished_routes) < 30:
        grid = init_grid(13, 18, location_dict)
        find_routes(tuplelist, location_dict, min_md, grid, final_routes, finished_routes)
    # while restart:
    #     find_routes(tuplelist, location_dict, min_md, grid, final_routes, restart)
    print(f"finished routes: {finished_routes}")
    print(f"final routes: {final_routes}")
    for route in final_routes:
        for coordinate in final_routes[route]:
            print(f"coordinate {coordinate}")
    print(f"grid: {grid}")

    # Save succesful netlist and final routes to csv files.
    csv_writer_tuplelist(tuplelist)
    csv_writer_finalroutes(final_routes)  

    # Plot a visualisation of the chips and circuits
    plot_3dgraph(location_dict, final_routes)

    ideal_score = sum(manhattan_distance(location_dict[route[0]][0], location_dict[route[1]][0], location_dict[route[0]][1], location_dict[route[1]][1]) for route in chip_netlists)
    current_score = sum(len(final_routes[route]) - 1 for route in final_routes)


if __name__ == "__main__":
    main()
    
    
    
    



