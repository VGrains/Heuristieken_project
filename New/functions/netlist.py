import csv


def load_netlists(netlist_file):
    """ Load all the connections out of the csv file. """
       
    # Load netlists data from csv files
    with open(netlist_file, "r") as csv:
        chip_netlists = []
        next(csv)
        
        for line in csv:
            chip_netlists.append(line.strip().split(", "))
            
        netlist = [(route[0], route[1]) for route in chip_netlists]
            
    return netlist