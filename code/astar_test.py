import numpy as np

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def csv_reader():
    """ 
    Loads the location of chips and the netlists from csv files
    Returns the location of chips as a dictionary where the key is the chip and the value is a list of the coordinates.
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


def return_path(current_node, maze):
    path = []
    nr_rows, nr_columns = np.shape(maze)
    
    result = [[-1 for i in range(nr_columns)] for j in range(nr_rows)]
    current = current_node
    
    while current is not None:
        path.append(current.position)
        current = current.parent
    
    # Return a reversed path: we need to see the route from start to end
    path = path[::-1]
    start_value = 0
    
    # Update the path from start to end
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    
    return result


def search(maze, cost, start, end):
    """ Returns a list of tuples as a path """
    
    # Create a start node
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    
    # Create an end node
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0
    
    # Create a list with all nodes which are still open for exploration
    still_visit_list = []
    
    # Create a list with all visited nodes
    visited_list = []
    
    # Make sure the start node doesn't end up in de visited list
    still_visit_list.append(start_node)
    
    # Avoid an infinite loop
    iterations = 0
    max_iterations = (len(maze) // 2) ** 10
    
    # Define a way to move
    move = [[-1, 0], # Up
            [0, -1], # Left
            [1, 0], # Down
            [0, 1]] # Right
            
    
    # Find out how many rows and columns the maze
    nr_rows, nr_columns = np.shape(maze)
    
    while len(still_visit_list) > 0:
        
        iterations += 1
        
        # Get currend node
        current_node = still_visit_list[0]
        current_index = 0
        
        
        for index, item in enumerate(still_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        
        # Stop when there are too many iterations
        if iterations > max_iterations:
            print("Shit, there are too many iterations WE GIVE UP!")
            return return_path(current_node, maze)
        
        # Get the current node out of the still_visit add to visited
        still_visit_list.pop(current_index)
        visited_list.append(current_node)
        
        # Goal reached?
        if current_node == end_node:
            return return_path(current_node, maze)
        print(current_node)
        # Generate children
        children = []
        
        for new_position in move:
            
            # Get node positions
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])
            
            # Make sure moves are within range or constraints
            if (node_position[0] > (nr_rows - 1) or
                node_position[0] < 0 or
                node_position[1] > (nr_columns - 1) or
                node_position[1] < 0):
                continue
            
            # Make sure the route is possible
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            
            # Create new node
            new_node = Node(current_node, node_position)
            
            children.append(new_node)
            
            for child in children:
                
                # Search entire visited list
                if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                    continue
                
                # Create f, g and h values
                child.g = current_node.g + cost
                
                child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                            ((child.position[1] - end_node.position[1]) ** 2))
                
                child.f = child.g + child.h
                
                # Child is already in the still visit list and cost is already lower
                if len([i for i in still_visit_list if child == i and child.g > i.g]) > 0:
                    continue
                
                
                # Add the child to the still visit list
                still_visit_list.append(child)
            

def main():
    location_dict, chip_netlists = csv_reader()
    grid = init_grid(8, 7)
    created_nets = []
    
    for x in grid:
        print(x)
    print('\n')
    
    count_1 = 0

    for route in chip_netlists:
        coordinates_base = location_dict[route[0]]
        coordinates_goal = location_dict[route[1]]

        start = (coordinates_base[0], coordinates_base[1])
        end = (coordinates_goal[0], coordinates_goal[1])
        
        path = astar(grid, start, end)
        
        for coordinate in path:
            if not coordinate in created_nets:
                created_nets.append(coordinate)
        
        print(created_nets)
        print("\n")


    
if __name__ == '__main__':

    maze = [[0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    
    start = [0, 0] # starting position
    end = [4,5] # ending position
    cost = 1 # cost per movement

    path = search(maze, cost, start, end)
    print(path)