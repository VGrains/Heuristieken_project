import csv

class Connections():
    def __init__(self, netlist_file):


    def load_netlists(self, netlist_file):
        """ Load all the connections out of the csv file. """
        
        with open(gates_file, "r") as csv:
            gate_locations = []
            next(csv)
        
            for line in csv:
                gate_locations.append(line.strip().split(", "))

            self.gates = {}
        
            lengths_x = []
            lengths_y = []
            
            for location in gate_locations:
                self.gates[location[0]] = [0, int(location[1]), int(location[2])]
                lengths_x.append(int(location[1]))
                lengths_y.append(int(location[2]))
                
            
            length_x = max(lengths_x) + 2
            length_y = max(lengths_y) + 2
            
            self.init_grid(length_y, length_x)
            
            return self.gates