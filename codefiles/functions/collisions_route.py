def collisions_sort(routes, gate_locations):  
    """ 
    Calculates the number of collisions of a given route with other routes on the grid. 
    Returns a dictionary with the route as key and the number of collisions as value.
    """ 
    
    # Append all nodes from the routes in to one list
    all_nodes = []
    for route in routes:
        for node in routes[route]:
            all_nodes.append(node)

    # Iterate over every node in the routes
    collisions = {}
    for route in routes:
        collisions[route] = 0
        for node in routes[route]:
            # Count how many times the current node appears in the all nodes list, if it appears more than once, it has a collision
            for current_node in all_nodes:
                if node == current_node and node not in gate_locations.values():
                    collisions[route] += 1

    # Sort the dictionary on the routes with the largest number of collisions first
    collisions_sorted = {route : nr_of_collisions for route, nr_of_collisions in reversed(sorted(collisions.items(), key=lambda item: item[1]))}
 
    # Create a new netlist, with the routes with the most collisions first
    collisions_netlist = []
    for key in collisions_sorted.keys():
        collisions_netlist.append(tuple(key))
    
    return collisions_netlist