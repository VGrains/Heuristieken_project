import sys

class Grid():
    def __init__(self, gates_file, algorithm):
        self.gates = self.load_gates(gates_file, algorithm)


    def load_gates(self, gates_file, algorithm):       
        # Open the csv file and add all gates and their coordinates to a dictionary
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
                
            # Determine the size of the grid (+2 because gates are never placed on the edges)
            length_x = max(lengths_x) + 2
            length_y = max(lengths_y) + 2
            
            self.init_grid(length_y, length_x, algorithm)
            
            return self.gates
        
    
    def init_grid(self, x_grid, y_grid, algorithm):
        # Create a grid with only 0's
        self.grid = [[[0 for x in range(x_grid)] for y in range(y_grid)] for z in range(8)]

        # Determine which grid the user wants
        grid_type = str(algorithm['option'])
        
        print(grid_type)
        
        if grid_type == "extended neighbours" or grid_type == "extended upstairs neighbours":
            for gate in self.gates:
                # Place a 'y' on the grid for gate extended neighbours
                self.grid[self.gates[gate][0]][self.gates[gate][1] + 1][self.gates[gate][2] + 1] = 'y'
                self.grid[self.gates[gate][0]][self.gates[gate][1] - 1][self.gates[gate][2] - 1] = 'y'
                self.grid[self.gates[gate][0]][self.gates[gate][1] + 1][self.gates[gate][2] - 1] = 'y'
                self.grid[self.gates[gate][0]][self.gates[gate][1] - 1][self.gates[gate][2] + 1] = 'y'

                if grid_type == "extended upstairs neighbours":
                    for i in range(1, 8):
                    # Place a 'y' on the grid for gate extended upstairs neighbours
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1] + 1][self.gates[gate][2]] = 'y'
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1] - 1][self.gates[gate][2]] = 'y'
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1]][self.gates[gate][2] + 1] = 'y'
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1]][self.gates[gate][2] - 1] = 'y'
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1] + 1][self.gates[gate][2] + 1] = 'y'
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1] - 1][self.gates[gate][2] - 1] = 'y'
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1] + 1][self.gates[gate][2] - 1] = 'y'
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1] - 1][self.gates[gate][2] + 1] = 'y'

        if grid_type == "neighbours" or grid_type == "upstairs neighbours" or grid_type == "extended neighbours" or grid_type == "extended upstairs neighbours":
            for gate in self.gates:
                # Place an 'x' on the grid for gate neighbours
                self.grid[self.gates[gate][0]][self.gates[gate][1] + 1][self.gates[gate][2]] = 'x'
                self.grid[self.gates[gate][0]][self.gates[gate][1] - 1][self.gates[gate][2]] = 'x'
                self.grid[self.gates[gate][0]][self.gates[gate][1]][self.gates[gate][2] + 1] = 'x'
                self.grid[self.gates[gate][0]][self.gates[gate][1]][self.gates[gate][2] - 1] = 'x'
                self.grid[self.gates[gate][0] + 1][self.gates[gate][1]][self.gates[gate][2]] = 'x'

                # Place an 'x' on the grid for gate upstairs neighbours
                if grid_type == "upstairs neighbours" or grid_type == "extended upstairs neighbours":
                    for i in range(2, 8):
                        self.grid[self.gates[gate][0] + i][self.gates[gate][1]][self.gates[gate][2]] = 'x'                 
            
        # Place gate numbers on the grid
        for gate in self.gates:
            self.grid[self.gates[gate][0]][self.gates[gate][1]][self.gates[gate][2]] = int(gate)
            
        return self.grid
        
    def heatmap(self, gate_locations, collisions):  
    
        for route in collisions:
            if route not in gate_locations.values():
                self.grid[route[0]][route[1]][route[2]] = collisions[route]
        
        
        for gate in self.gates:
            self.grid[self.gates[gate][0]][self.gates[gate][1]][self.gates[gate][2]] = int(gate)
            
        return self.grid


    def __repr__(self):
        return self.grid  