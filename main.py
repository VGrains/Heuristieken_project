
from codefiles.classes import grid, grid_mod
from codefiles.functions import netlist, manhattan, plot, collisions, md_sorting
from codefiles.algoritmes import astar, relax, neighbours
from codefiles.functions.csvwriter import *
import timeit


if __name__ == '__main__':
    
    start = timeit.default_timer()
    
    # Create a grid from our data
    obj = grid_mod.Grid_mod('data/chip_1/print_1.csv')
    # obj = grid.Grid('data/chip_1/print_1.csv')

    grid = obj.__repr__()
    
    # netlist = netlist.load_netlists('data/chip_1/chip_1_netlist_1_succes.csv')
    netlist = netlist.load_netlists('data/chip_1/netlist_2.csv')

    
    gate_locations = obj.gates


    routes, final_grid = relax.relax(netlist, gate_locations, grid)
    # routes, final_grid = neighbours.astar_grid(netlist, gate_locations, grid)
     
    ideal_score = sum(manhattan.manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist)
    current_score = sum(len(routes[route]) -1 for route in routes)    
    stop = timeit.default_timer()
    
    csv_writer_tuplelist(netlist)
    csv_writer_finalroutes(routes)
    collisions_dict = collisions.calculate_collisions(routes, gate_locations)
    total = collisions.total_collisions(collisions_dict)


    collisions_dict = collisions.calculate_collisions(routes, gate_locations)
    total = collisions.total_collisions(collisions_dict)
    print("Ideal: ", ideal_score)
    print("Current: ", current_score)
    print('Runtime: ', stop - start)
    print('Collisions: ', total)
    print('Collisions: ', collisions)
    
    for route in collisions_dict:
        if route not in gate_locations.values():
            grid[route[0]][route[1]][route[2]] = collisions_dict[route]




    for x in grid:
        print('\n')
        for y in x:
            print(y)









    
    
    # new_routes = routes

    # plot.plot_3dgraph(gate_locations, new_routes)
    

    
    
