from .manhattan import *

def md_sort(gate_locations, netlist):
    """ Load all the connections out of the csv file. """    
    
    md_routes = {route:manhattan_distance(gate_locations[route[0]][1], gate_locations[route[1]][1], gate_locations[route[0]][2], gate_locations[route[1]][2]) for route in netlist}
    
    min_md_sorted = {k: v for k, v in sorted(md_routes.items(), key=lambda item: item[1])}
    
    smallest_routes_first = [x for x in min_md_sorted]
    
    return smallest_routes_first