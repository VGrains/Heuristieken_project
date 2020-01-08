
import csv


# Load locations data from csv files
with open("example_print.csv", "r") as csv:
    chip_locations = []
    next(csv)
    
    for line in csv:
        chip_locations.append(line.strip().split(", "))
    
    print(chip_locations)
    print('\n')
    
    location_dict = {}
    
    for location in chip_locations:
        location_dict[location[0]] = [location[1], location[2]]
    
    print(location_dict)
    print('\n')


# Load netlists data from csv files
with open("example_netlist.csv", "r") as csv:
    chip_netlists = []
    next(csv)
    
    for line in csv:
        chip_netlists.append(line.strip().split(", "))
            
    print(chip_netlists)
    print('\n')



# Initiate 2 dimensional array
y_as = 7
x_as = 8

grid = [[0 for x in range(x_as)] for y in range(y_as)]
        
for i in location_dict:
    y_value = y_as - int(location_dict[i][1])- 1
    grid[y_value][int(location_dict[i][0])] = i

for x in grid:
    print(x)
    
    
    
    
    



