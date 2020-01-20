
def get_datafiles():
    while True:
        gates = input("Welcome, please specify the path to the file in which you have the coördinates of the gates specified.\n")
        try:
            test = open(gates, 'r')
        except FileNotFoundError:
            print("This file could not be found, please try again.")

    while True:
        netlist = input("Now please specify the path to your netlist file.\n")
        try:
            test = open(netlist, 'r')
        except FileNotFoundError:
            print("This file could not be found, please try again.")   
    
    return gates, netlist