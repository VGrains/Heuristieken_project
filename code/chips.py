from astar import astar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def csv_reader():
    """ 
    Loads the location of chips and the netlists from csv files
    Returns the location of chips as a dictionary where the key is the chip and the value is a list of the coordinates.
    Returns the netlists as a nested list.
    """
    
    with open("../data/chip_1/print_1.csv", "r") as csv:
        chip_locations = []
        next(csv)
        
        for line in csv:
            chip_locations.append(line.strip().split(", "))

        location_dict = {}
        
        for location in chip_locations:
            location_dict[location[0]] = [0, int(location[1]), int(location[2])]


    # Load netlists data from csv files
    with open("../data/chip_1/netlist_1.csv", "r") as csv:
        chip_netlists = []
        next(csv)
        
        for line in csv:
            chip_netlists.append(line.strip().split(", "))
        
    return location_dict, chip_netlists


def init_grid(x_length, y_length):
    """ Initialises a 2 dimensional array the the location of chips for visualisation purposes """
    location_dict, _ = csv_reader()
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
    plt.show()

def main():
    location_dict, chip_netlists = csv_reader()
    grid = init_grid(25, 25)
    final_routes = {}
    min_md = {}

    # Calculate route between the two chips
    tuplelist = [(route[0], route[1]) for route in chip_netlists]

    for route in tuplelist:
        coördinates_base = location_dict[route[0]]
        coördinates_goal = location_dict[route[1]]

        min_md[route] = manhattan_distance(coördinates_base[1], coördinates_goal[1], coördinates_base[2], coördinates_goal[2])

    # Calculate the ideal circuit length by adding up all the manhattan distances
    ideal_score = sum(min_md[x] for x in min_md)

    # Sort the routes by length
    min_md_sorted = {k: v for k, v in sorted(min_md.items(), key=lambda item: item[1])}
    smallest_routes_first = [x for x in min_md_sorted]

    for route in smallest_routes_first:

        # Get the coordinates from the dictionary with the locations of the chips
        coordinates_base = location_dict[route[0]]
        coordinates_goal = location_dict[route[1]]

        # Set the start and end chips
        start = (coordinates_base[0], coordinates_base[1], coordinates_base[2])
        end = (coordinates_goal[0], coordinates_goal[1], coordinates_goal[2])

        # Calculate a path using the A-star algoritm
        path = astar(grid, start, end)
        
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

    # Plot a visualisation of the chips and circuits
    plot_3dgraph(location_dict, final_routes)

    ideal_score = sum(manhattan_distance(location_dict[route[0]][0], location_dict[route[1]][0], location_dict[route[0]][1], location_dict[route[1]][1]) for route in chip_netlists)
    current_score = sum(len(final_routes[route]) - 1 for route in final_routes)


if __name__ == "__main__":
    main()
    
    
    
    



