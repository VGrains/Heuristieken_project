import copy
import random
import sys

from codefiles.classes import node


def astar_grid(netlist, gate_locations, grid, algorithm):
    """ Load and update the A* searches on """

    
    # Initialize the needed variables for the algorithm
    final_routes = {}
    netlist_list = []
    high_score = 0
    collision_add = 0
    neighbour_add = 0
    extended_neighbour_add = 0
    
    # Set values for Node "add-costs"
    if algorithm['option'] == 'lava':
        collision_add = algorithm['variable_1']
    if algorithm['option'] == 'neighbours' or algorithm['option'] == 'upstairs neighbours':
        neighbour_add = algorithm['variable_1']
    if algorithm['option'] == 'extended neighbours' or algorithm['option'] == 'extended upstairs neighbours':
        neighbour_add = algorithm['variable_1']
        extended_neighbour_add = algorithm['variable_2']
        
    
    # Make sure A* keeps searching until the whole netlist is completed
    while len(final_routes) < len(netlist):
        copy_grid = copy.deepcopy(grid)
        
        # Iterate through the netlist
        for route in netlist:
            
            # Get the coordinates from the dictionary with the locations of the chips
            coordinates_base = gate_locations[route[0]]
            coordinates_goal = gate_locations[route[1]]
            
            # Set the start and end chips
            start = (coordinates_base[0], coordinates_base[1], coordinates_base[2])
            end = (coordinates_goal[0], coordinates_goal[1], coordinates_goal[2])
            
            # Calculate a path using the A-star algoritm
            path = astar(copy_grid, start, end, gate_locations, collision_add, neighbour_add, extended_neighbour_add, algorithm)
    
            # Start the path on the other side to check for a better score
            if algorithm['extra'] == 'turned_up':
                start = (coordinates_goal[0], coordinates_goal[1], coordinates_goal[2])
                end = (coordinates_base[0], coordinates_base[1], coordinates_base[2])
                
                path_2 = astar(copy_grid, start, end, gate_locations, collision_add, neighbour_add, extended_neighbour_add, algorithm)
                
                if len(path_2) > len(path):
                    path = path_2
    
    
            # If A* didn't succeed to find a path
            if path == None:
                
                # Set values for Node "add-costs"
                if algorithm['option'] == 'lava':
                    collision_add = algorithm['variable_1']
                if algorithm['option'] == 'neighbours' or algorithm['option'] == 'upstairs neighbours':
                    neighbour_add = algorithm['variable_1']
                if algorithm['option'] == 'extended neighbours' or algorithm['option'] == 'extended upstairs neighbours':
                    neighbour_add = algorithm['variable_1']
                    extended_neighbour_add = algorithm['variable_2']
               
                
                # Move the route that breaks the algorithm to the front of the routeslist
                netlist_copy = copy.deepcopy(netlist)
                netlist_list.append(netlist_copy)
                netlist.remove(route)
                netlist.insert(0, route)
                
                
                # Keep track on the score
                if len(final_routes) > high_score:
                    high_score = len(final_routes)
                print("finished routes: ", len(final_routes))
                print("high_score: ", high_score)
                
                final_routes.clear()
                
                # Prevent infinite loop by checking if this specific path already has been taken
                if netlist in netlist_list:
                    print("Sorry, can't find the solution..")
                    sys.exit(0)
                
                break
           
            # Adjust the grid for the current iterations route
            for location in path:
                
                grid_location = copy_grid[location[0]][location[1]][location[2]]
                
                # Update the grid and add the path that's been taken by changing the value to a 'I'
                if grid_location == 0 or grid_location == 'x' or grid_location == 'y' or grid_location not in gate_locations:
                    copy_grid[location[0]][location[1]][location[2]] = "I"
            
                # Else continue
                else:
                    continue

            # Set the route as value in the final_routes dict, with the netlist as key
            final_routes[route] = path
            
            
            if algorithm['extra'] == 'countdown' and collision_add >= 1:
                if algorithm['count_var'] == 'collision_down' and collision_add >= 1:
                    collision_add - algorithm['variable_3']
                elif algorithm['count_var'] == 'neighbour_down' and neighbours_add >= 1:
                    neighbours_add - algorithm['variable_3']
                else:
                    continue
            
    return final_routes, copy_grid


def astar(grid, start, end, gate_locations, collision_add, neighbour_add, extended_neighbour_add, algorithm):
    """ Returns a list of tuples as a path from the given start to the given end in the given maze """
    # Create start and end node
    start_node = node.Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = node.Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    
    
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    
    # Save original costs
    neighbour_cost = neighbour_add
    collision_cost = collision_add
    extended_neighbour_cost = extended_neighbour_add

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        
        # Generate children
        children = []
        
        # Define the possible moves
        for new_position in [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)]: # Adjacent squares
            
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2])
            
            
            # Make sure within range
            if node_position[1] > (len(grid[0]) - 1) or node_position[1] < 0 or node_position[2] > (len(grid[0][len(grid)-1]) -1) or node_position[2] < 0 or node_position[0] < 0 or node_position[0] > len(grid) - 1:
                continue
            
            # Make sure walkable terrain
            if node_position == end_node.position:
                new_node = node.Node(current_node, node_position)
            
                # Append
                children.append(new_node)
                continue
                
            add_cost = 0
            
            
            if algorithm['option'] == 'regular':
                node_position = [node_position[0], node_position[1], node_position[2]]
            
            # Check whether to add costs based on location in the grid
            if grid[node_position[0]][node_position[1]][node_position[2]] == 'I':
                continue
            elif grid[node_position[0]][node_position[1]][node_position[2]] == 'x':
                add_cost = int(neighbour_cost)
            elif grid[node_position[0]][node_position[1]][node_position[2]] == 'y':
                add_cost = int(extended_neighbour_cost)
            elif grid[node_position[0]][node_position[1]][node_position[2]] != 0 and node_position not in gate_locations.values():
                add_cost = int(grid[node_position[0]][node_position[1]][node_position[2]]) * int(algorithm['variable_1'])
            
                
            # Create new node
            new_node = node.Node(current_node, node_position)
            new_node.h = add_cost
            
            # Append
            children.append(new_node)
    
        # Loop through children
        for child in children:
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    break
            else:
                
                # Create the f, g, and h values
                child.g = current_node.g + 1
                
                # H: Manhattan distance to end point + add the possible extra costs based on Node value
                child.h = child.h + abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
                child.f = child.g + child.h
                
                # Child is already in the open list
                for open_node in open_list:
                    
                    # check if the new path to children is worst or equal 
                    if child == open_node and child.g >= open_node.g:
                        break
                else:
                    # Add the child to the open list
                    open_list.append(child)



