from codefiles.classes.grid import *
from codefiles.functions import collisions
from codefiles.functions.collisions_route import *
from codefiles.algoritmes import relax

def initialize_grid(algorithm, netlist, obj):
    """ Initialize the grid settings """
    
    grid = obj.__repr__()    
    gate_locations = obj.gates
    
    if algorithm['option'] == "lava":
        routes, final_grid = relax.relax(netlist, gate_locations, grid)
        collisions_dict = collisions.calculate_collisions(routes, gate_locations)
        obj_lava = obj.heatmap(gate_locations, collisions_dict)
        grid = obj_lava
    
    return grid, gate_locations