import copy
import random
from codefiles.classes import node

def astar_elevator(netlist, gate_locations, grid):
    """ 
    Iterates over the given netlist and tries to lay a route.
    Tries for every layer in the grid.
    Returns a final_routes dictionary with the netlist route as key and the route as a list of tuples (z, x, y coördinates).
    Also returns the final grid. 
    """
    final_routes = {}
    
    # Loop until all routes are completed
    while len(final_routes) < len(netlist):
        copy_grid = copy.deepcopy(grid)
        fail = False
        for route in netlist:
            # Get the coordinates from the dictionary with the locations of the chips
            coordinates_base = gate_locations[route[0]]
            coordinates_goal = gate_locations[route[1]]

            # Set the start and end chips
            start = (coordinates_base[0], coordinates_base[1], coordinates_base[2])
            end = (coordinates_goal[0], coordinates_goal[1], coordinates_goal[2])
            
            layers = [0, 1, 2, 3, 4, 5, 6, 7]
            
            # Iterate over every layer in the grid
            for layer in layers:
                
                # If the layer is not 0, 
                if layer != 0:
                    new_grid = copy_grid

                    # Find a route to the given layer from the start point
                    step1 = elevator(layer, start, new_grid)
                        
                    # If no route can be found and the iteration is on the last layer, update the netlist and start over
                    if step1 == None and layer == 7:
                        # Move the route that breaks the algorithm to the front of the routeslist
                        netlist.remove(route)
                        netlist.insert(0, route)
                        print("finished routes: ", len(final_routes))
                        final_routes.clear()
                        fail = True
                        break

                    # Else if no route can be found but there are still more layers, continue to the next one
                    elif step1 == None:
                        continue
                    
                    # Update the grid with 1's instead of 0's for the layed route
                    new_grid = adjust_grid(step1, new_grid)
                    
                    # Find a route to the given layer from the end point
                    step2 = elevator(layer, end, new_grid)

                    if step2 == None and layer == 7:
                        netlist.remove(route)
                        netlist.insert(0, route)
                        print("finished routes: ", len(final_routes))
                        final_routes.clear()
                        fail = True
                        break

                    elif step2 == None:
                        continue
                    
                    new_grid = adjust_grid(step2, new_grid)

                    # Find a path between the two new points on the layer
                    path = skyroute(step1, step2, new_grid)
                    
                    if path == None and layer == 7:
                        netlist.remove(route)
                        netlist.insert(0, route)
                        print("finished routes: ", len(final_routes))
                        final_routes.clear()
                        fail = True
                        break

                    adjusted_grid = adjust_grid(path, new_grid)
                    copy_grid = adjusted_grid
            
                    # Set the route as value in the final_routes dict, with the netlist points as key
                    final_routes[route] = path
                    break
                
                # Try to find a path on the lowest layer (Layer 0)
                path = astar(copy_grid, start, end)

                # If no path can be found, continue to the next layer
                if path == None:
                    continue
                
                # Adjust the grid
                copy_grid = adjust_grid(path, copy_grid)
                final_routes[route] = path
                break
                
            if fail == True:
                break
               
    return final_routes, copy_grid


def adjust_grid(route, grid):
    """ Adjusts the grid based on the locations in the given route """

    for location in route:
        # If the position in the route is the end destination, dont make it a 1. 
        if location == route[-1]:
            grid[location[0]][location[1]][location[2]] = 0

        # Else if the location on the grid is not a 1, make it one.
        elif grid[location[0]][location[1]][location[2]] == 0 or grid[location[0]][location[1]][location[2]] == 'x' or grid[location[0]][location[1]][location[2]] == 'y':
            grid[location[0]][location[1]][location[2]] = 1
        else:
            continue

    return grid


def elevator(level, start, grid):
    """
    Elevates the location of a gate to a level and find a route to the new point.
    Returns the path from the original location to the new location. 
    """

    # Adjacent squares of the point directly above the gate
    surroundings = [(0, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (0, -1, -1), (0, 1, -1), (0, 1, 1), (0, -1, 1)]

    # Try to find a route to an adjacent square
    for new_position in surroundings:
        new_start = (level + new_position[0], start[1] + new_position[1], start[2] + new_position[2])
        path = astar(grid, start, new_start)

        if path == None:
            continue
        
    return path

def skyroute(startroute, endroute, grid):
    """ 
    Finds a route between the two elevated points.
    Returns the three routes stitched together to form one route.
    """
    # Find the start and end point
    start = startroute[-1]
    end = endroute[-1]
    path = astar(grid, start, end)

    # If a path is found, stitch the routes together
    if path != None: 
        for location in reversed(startroute[:-1]):
            path.insert(0, location)

        for location in reversed(endroute[:-1]):
            path.insert(len(path), location)

        return path

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end 
    start_node = node.Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = node.Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

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
        
        for new_position in [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)]: # Adjacent squares
            
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2])

            # Make sure within range
            if node_position[1] > (len(maze[0]) - 1) or node_position[1] < 0 or node_position[2] > (len(maze[0][len(maze)-1]) -1) or node_position[2] < 0 or node_position[0] < 0 or node_position[0] > len(maze) - 1:
                continue
            
            # Make sure walkable terrain
            if node_position == end_node.position:
                new_node = node.Node(current_node, node_position)
            
                # Append
                children.append(new_node)
                continue
            
            if maze[node_position[0]][node_position[1]][node_position[2]] != 0:
                continue

            # Create new node
            new_node = node.Node(current_node, node_position)
            
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
                # H: Manhattan distance to end point
                child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    # check if the new path to children is worst or equal 
                    # than one already in the open_list (by measuring g)
                    if child == open_node and child.g >= open_node.g:
                        break
                else:
                    # Add the child to the open list
                    open_list.append(child)