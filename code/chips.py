from astar import *


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
            
    for i in location_dict:
        y_value = y_length - location_dict[i][1] - 1
        grid[y_value][location_dict[i][0]] = i

    return grid


def manhattan_distance(x_base, x_goal, y_base, y_goal):
    """ Calculates the manhattan distance between two points on the grid"""
    distance = abs(x_base - x_goal) + abs(y_base - y_goal)
    
    return distance


def main():
    location_dict, chip_netlists = csv_reader()
    grid = init_grid(8, 7)
    created_nets = []
    
    for x in grid:
        print(x)
    print('\n')
    
    count_1 = 0

    for route in chip_netlists:
        coördinates_base = location_dict[route[0]]
        coördinates_goal = location_dict[route[1]]

        start = (coördinates_base[0], coördinates_base[1])
        end = (coördinates_goal[0], coördinates_goal[1])
        
        path = astar(grid, start, end)
        
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
        
        for net in created_nets:
            if grid[net[0]][net[1]] == 0:
                grid[net[0]][net[1]] = 1
                count_2 += 1
            else:
                continue
        
        count_1 += 1
                
            
        
    for x in grid:
        print(x)
    print('\n')
        
    print(path)
    print(created_nets)
    print('\n')


if __name__ == "__main__":
    main()
    
    
    
    



