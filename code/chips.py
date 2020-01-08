import csv


def csv_reader():
    """ 
    Loads the location of chips and the netlists from csv files
    Returns the location of chips as a dictionary where the key is the chip and the value is a list of the coördinates.
    Returns the netlists as a nested list.
    """
    with open("example_print.csv", "r") as csv:
        chip_locations = []
        next(csv)
        
        for line in csv:
            chip_locations.append(line.strip().split(", "))

        location_dict = {}
        
        for location in chip_locations:
            location_dict[location[0]] = [int(location[1]), int(location[2])]

    # Load netlists data from csv files
    with open("example_netlist.csv", "r") as csv:
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
    for x in grid:
        print(x)

    for route in chip_netlists:
        coördinates_base = location_dict[route[0]]
        coördinates_goal = location_dict[route[1]]

        print(manhattan_distance(coördinates_base[0], coördinates_goal[0], coördinates_base[1], coördinates_goal[1]))
    
if __name__ == "__main__":
    main()
    
    
    
    



