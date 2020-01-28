import copy


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


def relax(netlist, gate_locations, grid):
    final_routes = {}
    
    while len(final_routes) < len(netlist):
        copy_grid = copy.deepcopy(grid)
        
        
        for route in netlist:
            # Get the coordinates from the dictionary with the locations of the chips
            
            coordinates_base = gate_locations[route[0]]
            coordinates_goal = gate_locations[route[1]]

            # Set the start and end chips
            start = (coordinates_base[0], coordinates_base[1], coordinates_base[2])
            end = (coordinates_goal[0], coordinates_goal[1], coordinates_goal[2])

            # Calculate a path using the A-star algoritm
            path = astar(copy_grid, start, end)

            if path == None:            
                # Move the route that breaks the algorithm to the front of the routeslist

                netlist.remove(route)
                netlist.insert(0, route)
                print("finished routes: ", len(final_routes))
                final_routes.clear()
                break
    
            # Adjust the grid for the current iterations route
            for location in path:
                # If the position in the grid is a letter, don't make it a '1'
                if copy_grid[location[0]][location[1]][location[2]] != 0 and copy_grid[location[0]][location[1]][location[2]] != 1:
                    continue

                # Else change the zero to a '1'
                else:
                    copy_grid[location[0]][location[1]][location[2]] = 1

            # Set the route as value in the final_routes dict, with the netlist as key
            final_routes[route] = path
            
    return final_routes, copy_grid

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
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
        
            # Create new node
            new_node = Node(current_node, node_position)
            
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

def to_the_sky(route):

    old_route = route
    new_route = []
    for x in old_route:
        x = (x[0] + 1, x[1], x[2])
        new_route.append(x)
    
    new_route.insert(0, old_route[0])
    new_route.insert(len(new_route), old_route[-1])
    
    return new_route

def calculate_collisions(routes):
    collisions = {}
    for x in routes:
        collisions[x] = 0
        for y in routes[x]:
            for i in routes:
                if y in routes[i]:
                    collisions[x] += 1
                
    collisions_sorted = {k: v for k, v in reversed(sorted(collisions.items(), key=lambda item: item[1]))}

    return collisions_sorted
    
            