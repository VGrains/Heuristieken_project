from codefiles.classes import grid
from codefiles.functions import netlist, manhattan, plot
from codefiles.algoritmes import astar, relax


if __name__ == '__main__':
    
    # Create a grid from our data
    obj = grid.Grid('print_1.csv')
    grid = obj.__repr__()
    
    netlist = netlist.load_netlists('netlist_1.csv')
    
    gate_locations = obj.gates
    
    print(gate_locations)
 
    routes = astar.astar_grid(netlist, gate_locations, grid)
    for x in copy_grid:
        print('\n')
        for y in x:
            print(y)
     
    ideal_score = sum(manhattan.manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist)
    current_score = sum(len(routes[route]) -1 for route in routes)
    
    md_routes = {route:manhattan.manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist}
    min_md_sorted = {k: v for k, v in sorted(md_routes.items(), key=lambda item: item[1])}
    smallest_routes_first = [x for x in min_md_sorted]

    print("ideal: ", ideal_score)
    print("current: ", current_score)

    plot.plot_3dgraph(gate_locations, routes)

    
    