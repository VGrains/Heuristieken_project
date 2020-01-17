from classes import grid
from functions import netlist, manhattan, plot
from codefiles import astar





if __name__ == '__main__':
    
    # Create a grid from our data
    obj = grid.Grid('print_1.csv')
    grid = obj.__repr__()
    
    netlist = netlist.load_netlists('netlist_2.csv')
    
    gate_locations = obj.gates
    
    print(gate_locations)
 
    
    routes, copy_grid = astar.astar_grid(netlist, gate_locations, grid)
    print(routes)
    for x in copy_grid:
        print('\n')
        for y in x:
            print(y)
     
    ideal_score = sum(manhattan.manhattan_distance(gate_locations[route[0]][0], gate_locations[route[1]][0], gate_locations[route[0]][1], gate_locations[route[1]][1]) for route in netlist)
    current_score = sum(len(routes[route]) - 1 for route in routes)
    
    print("ideal: ", ideal_score)
    print("current: ", current_score)
    
    plot.plot_3dgraph(gate_locations, routes)

    
    
