from codefiles.classes import grid, grid_mod
from codefiles.functions import netlist, manhattan, plot
from codefiles.algoritmes import astar, relax, neighbours
import timeit


if __name__ == '__main__':
    
    start = timeit.default_timer()
    # Create a grid from our data
    obj = grid_mod.Grid_mod('data/chip_1/print_1.csv')
    grid = obj.__repr__()
    
    netlist = netlist.load_netlists('data/chip_1/netlist_1.csv')
    
    gate_locations = obj.gates
    
    print(gate_locations)
 
    routes, final_grid = neighbours.astar_grid(netlist, gate_locations, grid)
    
    for x in final_grid:
        print('\n')
        for y in x:
            print(y)
     
    ideal_score = sum(manhattan.manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist)
    current_score = sum(len(routes[route]) -1 for route in routes)
    
    md_routes = {route:manhattan.manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist}
    min_md_sorted = {k: v for k, v in sorted(md_routes.items(), key=lambda item: item[1])}
    smallest_routes_first = [x for x in min_md_sorted]
    stop = timeit.default_timer()
    
    print("Ideal: ", ideal_score)
    print("Current: ", current_score)
    print('Runtime: ', stop - start)

    plot.plot_3dgraph(gate_locations, routes)

    
    
