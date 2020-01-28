from codefiles.classes.grid import *
from codefiles.functions.collisions_route import *
from codefiles.functions.manhattan import *
from codefiles.algoritmes import relax

def initialize_netlist(algorithm, netlist, gate_locations, grid):
    """ Prepares the netlist for the algorithm """
    
    if algorithm['sort'] == "no sorting":
        netlist = netlist
    elif algorithm['sort'] == "manhattan distance":
        md_routes = {route:manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], \
                    gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist}
        min_md_sorted = {k: v for k, v in sorted(md_routes.items(), key=lambda item: item[1])}
        netlist = [x for x in min_md_sorted]
    elif algorithm['sort'] == "collisions":
        collision_routes, routes_final_grid = relax.relax(netlist, gate_locations, grid)
        netlist = collisions_sort(collision_routes, gate_locations)
    
    return netlist