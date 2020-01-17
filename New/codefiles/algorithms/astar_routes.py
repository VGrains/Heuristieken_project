from classes.grid import Grid

def find_routes(tuplelist, location_dict, grid):
    finished_routes = finished_routes
    
    for route in tuplelist:
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
            grid = init_grid(13, 18, location_dict)
            find_routes(tuplelist, location_dict, grid)
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
            
    return final_routes