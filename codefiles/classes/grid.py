import csv

class Grid():
    def __init__(self, gates_file):
        self.gates = self.load_gates(gates_file)


    def load_gates(self, gates_file):
        """ Load all the gates out of the csv file. """
        
        with open(gates_file, "r") as csv:
            gate_locations = []
            next(csv)
        
            for line in csv:
                gate_locations.append(line.strip().split(", "))

            self.gates = {}
        
            lengths_x = []
            lengths_y = []
            
            for location in gate_locations:
                self.gates[location[0]] = (0, int(location[1]), int(location[2]))
                lengths_x.append(int(location[1]))
                lengths_y.append(int(location[2]))
                
            
            length_x = max(lengths_x) + 2
            length_y = max(lengths_y) + 2
            
            self.init_grid(length_y, length_x)
            
            return self.gates
        
    
    def init_grid(self, x_grid, y_grid):
        """ Initialize the grid in a correct way """
        
        self.grid = [[[0 for x in range(x_grid)] for y in range(y_grid)] for z in range(7)]
        
        for gate in self.gates:
            self.grid[self.gates[gate][0]][self.gates[gate][1]][self.gates[gate][2]] = int(gate)
        
        return self.grid


    def __repr__(self):
        return self.grid