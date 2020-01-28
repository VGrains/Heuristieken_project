from codefiles.classes.grid import *
from codefiles.functions import netlist, manhattan, plot, collisions, collisions_route, initialize_algorithm, initialize_grid, initialize_netlist
from codefiles.algoritmes.good_astar import astar_grid
from codefiles.functions.csvwriter import *
from codefiles.algoritmes.elevator import astar_elevator

import timeit


if __name__ == '__main__':
    
    # Initialize all the settings for the algorithm
    algorithm, netlist, obj = initialize_algorithm.initialize_algorithm()
    
    # Get grid object and gate locations
    grid, gate_locations = initialize_grid.initialize_grid(algorithm, netlist, obj)
    
    # Get the netlist sorted correctly
    netlist = initialize_netlist.initialize_netlist(algorithm, netlist, gate_locations, grid)
    
    # Start the time
    start = timeit.default_timer()
    
    # Run the A* algorithm
    if algorithm['option'] == "elevator":
        routes, final_grid = astar_elevator(netlist, gate_locations, grid)
    else:
        routes, final_grid = astar_grid(netlist, gate_locations, grid, algorithm)
        
    
    # Get the final statistics to inform the user
    stop = timeit.default_timer()
    ideal_score = sum(manhattan.manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], \
                     gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist)    
    current_score = sum(len(routes[route]) -1 for route in routes)
    
    
    # Ask user whether he wants to create output csv files
    output = input("\nWould you like to save the succesful netlist order and the created wires? Type 'y' or 'n': ")
    if output == "y":
        csv_writer_tuplelist(netlist)
        csv_writer_finalroutes(routes)
    
    # Print statistics
    print("\nThank you for running this code package! The statistics are:")
    print("Ideal: ", ideal_score)
    print("Current: ", current_score)
    print('Runtime: ', stop - start)
    
    # Plot the 3D graph
    plot.plot_3dgraph(gate_locations, routes)
    

    
    
