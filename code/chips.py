from astar import astar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def csv_reader():
    """ 
    Loads the location of chips and the netlists from csv files
    Returns the location of chips as a dictionary where the key is the chip and the value is a list of the coördinates.
    Returns the netlists as a nested list.
    """
    
    with open("../data/example/example_print.csv", "r") as csv:
        chip_locations = []
        next(csv)
        
        for line in csv:
            chip_locations.append(line.strip().split(", "))

        location_dict = {}
        
        for location in chip_locations:
            location_dict[location[0]] = [int(location[1]), int(location[2])]


    # Load netlists data from csv files
    with open("../data/example/example_netlist.csv", "r") as csv:
        chip_netlists = []
        next(csv)
        
        for line in csv:
            chip_netlists.append(line.strip().split(", "))
        
    return location_dict, chip_netlists


def init_grid(x_length, y_length):
    """ Initialises a 2 dimensional array the the location of chips for visualisation purposes """
    location_dict, _ = csv_reader()
    grid = [[0 for x in range(x_length)] for y in range(y_length)]
            
    for location in location_dict:
        grid[location_dict[location][0]][location_dict[location][1]] = location

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
    z = [0, 0, 0, 0, 0]
    for i in chip_locations:
        x.append(chip_locations[i][0])
        y.append(chip_locations[i][1])

    ax.scatter(x,y,z,s=75, c='r', marker='s')

    # Add the routes as wires
    for x in routes:
        wires_x = []
        wires_y = []
        for y in routes[x]:
            wires_x.append(y[0])
            wires_y.append(y[1])

        wires_z = [0 for x in wires_x]
        ax.plot(wires_x, wires_y, wires_z)

    plt.show()


def main():
    location_dict, chip_netlists = csv_reader()
    grid = init_grid(8, 7)
    final_routes = {}

    # Calculate route between the two chips
    for route in chip_netlists:

        # Get the coördinates from the dictionary with the locations of the chips
        coördinates_base = location_dict[route[0]]
        coördinates_goal = location_dict[route[1]]
        print(f"route {route}")

        # Set the start and end chips
        start = (coördinates_base[0], coördinates_base[1])
        end = (coördinates_goal[0], coördinates_goal[1])
<<<<<<< HEAD
        print(f"start {start}")
        print(f"end {end}")
        
        path = astar(grid, start, end)
        print(f"path {path}")
        
        for coordinate in path:
            created_nets.append(coordinate)
        
        print(created_nets)
        print("\n")
        
        
        # for net in created_nets:
#             if grid[net[1]][net[0]] != 0 or grid[net[1]][net[0]] != 1:
#                 if count == 0:
#                     pass
#                 else:
#                     continue
#             else:
#                 grid[net[1]][net[0]] = 1
#
#             count += 1
        count_2 = 0
        
=======

        # Calculate a path using the A-star algoritm
        path = astar(grid, start, end)

        # Adjust the grid for the current iterations route
>>>>>>> 501a7f5be85f447bb4c9d27f36520e6409affe44
        for location in path:
            # If the position in the grid is a letter, don't make it a '1'
            if grid[location[0]][location[1]] != 0 and grid[location[0]][location[1]] != 1:
                continue
<<<<<<< HEAD
        #     location_1 = 7 - int(location[1]) - 1
        #     print(location[1])
        #     print(location_1)
        #     if grid[location[0]][location_1] != 1:
        #         grid[location[0]][location_1] = 1
        #         count_2 += 1
        
        # count_1 += 1
                
        for x in grid:
            print(x)
        print('\n')
        
    print("path")
    print(path)
    print(created_nets)
    print('\n')
=======
>>>>>>> 501a7f5be85f447bb4c9d27f36520e6409affe44

            # Else change the zero to a '1'
            else:
                grid[location[0]][location[1]] = 1

        # Set the route as value in the final_routes dict, with the netlist as key
        final_routes[str(route)] = path

    # Plot a visualisation of the chips and circuits
    plot_3dgraph(location_dict, final_routes)
    

if __name__ == "__main__":
    main()
    
    
    
    



