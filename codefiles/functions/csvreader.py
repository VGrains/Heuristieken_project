import sys


def csv_reader():
    """ 
    Loads the location of chips and the netlists from csv files
    Returns the location of chips as a dictionary where the key is the chip and the value is a list of the coordinates.
    Returns the netlists as a nested list.
    """
    # Ask user for an input netlist and grab the right files.
    infile_netlist = int(input("Which netlist would you like to use? Enter an integer between 1 and 6. "))
    if infile_netlist == 1 or infile_netlist == 2 or infile_netlist == 3:
        infile_netlist = "../data/chip_1/netlist_{}.csv".format(infile_netlist)
        infile_print = "../data/chip_1/print_1.csv"
    elif infile_netlist == 4 or infile_netlist == 5 or infile_netlist == 6:
        infile_netlist = "../data/chip_2/netlist_{}.csv".format(infile_netlist)
        infile_print = "../data/chip_2/print_2.csv"
    else:
        print("It looks like the entered integer does not match with one of the netlists. Please try again.")
        sys.exit(0)
    
    # Open the chip print and put all gates with their location in a dictionary.
    with open(infile_print, "r") as csv:
        chip_locations = []
        next(csv)
        
        for line in csv:
            chip_locations.append(line.strip().split(", "))

        location_dict = {}
        for location in chip_locations:
            location_dict[location[0]] = [0, int(location[1]), int(location[2])]

    # Open the netlist and put all combinations in a list.
    with open(infile_netlist, "r") as csv:
        chip_netlists = []
        next(csv)
        
        for line in csv:
            chip_netlists.append(line.strip().split(", "))
        
    return location_dict, chip_netlists