
from codefiles.classes import grid, grid_mod
from codefiles.functions import netlist, manhattan, plot, collisions, md_sorting
from codefiles.algoritmes import astar, relax, neighbours
from codefiles.functions.csvwriter import *
import timeit


if __name__ == '__main__':
    
    start = timeit.default_timer()
    
    # Create a grid from our data
    obj = grid_mod.Grid_mod('data/chip_1/print_1.csv')

    grid = obj.__repr__()
    
    netlist = netlist.load_netlists('data/chip_1/netlist_2.csv')

    
    gate_locations = obj.gates

    sorted_netlist = md_sorting.md_sort(gate_locations, netlist)

    # routes, final_grid = relax.relax(netlist, gate_locations, grid)
    routes, final_grid = neighbours.astar_grid(sorted_netlist, gate_locations, grid)
     
    ideal_score = sum(manhattan.manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist)
    current_score = sum(len(routes[route]) -1 for route in routes)
    # collisions = collisions.calculate_collisions(routes)
    
    stop = timeit.default_timer()
    
    csv_writer_tuplelist(netlist)
    csv_writer_finalroutes(routes)
    
    print("Ideal: ", ideal_score)
    print("Current: ", current_score)
    print('Runtime: ', stop - start)
    # print('Collisions: ', collisions)
    
    new_routes = routes

    plot.plot_3dgraph(gate_locations, new_routes)
    

    
    
