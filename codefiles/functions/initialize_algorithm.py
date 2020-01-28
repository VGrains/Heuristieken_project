from codefiles.classes.grid import *
from codefiles.functions import netlist, manhattan, plot, collisions, collisions_route
from codefiles.functions.netlist import *
from codefiles.algoritmes import relax

def initialize_algorithm():
    """ Prompt the user for all information that's needed to initialize the algorithm settings """
    
    # Create algorithm list and variables
    algorithm = {}
    variable_1 = 0
    variable_2 = 0
    variable_3 = 0
    
    # Greet the user and prompt for the netlist
    print("Welcome to main.py for chips & circuits!")
    netlist = get_netlist()
    
    # Prompt user for algorithm input 
    algorithm_options = {0:"regular", 1:"lava", 2:"neighbours", 3:"elevator", 4:"extended upstairs neighbours", 
                        5:"extended neighbours", 6:"upstairs neighbours"}
    algorithm_option = get_algoritm()
    algorithm['option'] = algorithm_options[algorithm_option - 1]
    
    # Prompt user for which way the netlist should be sorted
    sorting_options = {0:"no sorting", 1:"manhattan distance", 2:"collisions"}
    sorting_option = get_sorting()
    algorithm['sort'] = sorting_options[sorting_option - 1]
       
    # Get the needed variables depending on which variation will be used
    variable_1, variable_2 = get_variables(algorithm)
    
    # Determine which extra heuristic is to be added
    extra_options = {0:"nothing", 1:"countdown", 2:"turned-up"}
    extra_option = get_extra_option()
    algorithm['extra'] = extra_options[extra_option - 1]
        
    # Determine the extra option with countdown
    if algorithm['extra'] == "countdown":
        variable_3 = get_countdown_variable()
        algorithm['variable_3'] = variable_3
        
        count_options = {0:"neighbour_down", 1:"collision_down"}
        count_option = get_count_option()
        algorithm['count_var'] = count_options[count_option - 1]
    
    if netlist == 1 or netlist == 2 or netlist == 3:
        obj = Grid('data/chip_1/print_1.csv', algorithm)
        netlist = "data/chip_1/netlist_{}.csv".format(netlist)
    elif netlist == 4 or netlist == 5 or netlist == 6:
        obj = Grid('data/chip_2/print_2.csv', algorithm)
        netlist = "data/chip_2/netlist_{}.csv".format(netlist)
    else:
        print("\nIt looks like you chose an invalid netlist. Please re-run the code and choose a valid netlist.")
        sys.exit()
    
    netlist = load_netlists(netlist)
    
    return algorithm, netlist, obj
    
def get_netlist():
    """ Asks the user which netlist to load into the algorithm """
    print("Which netlist would you like to use for the algorithm?\n")
    print("[ 1 ] Netlist 1          length: 30\n[ 2 ] Netlist 2          length: 40\n[ 3 ] Netlist 3          length: 50\n[ 4 ] Netlist 4          length: 40\n[ 5 ] Netlist 5          length: 50\n[ 6 ] Netlist 6          length: 60\n")
    netlist = validate_input(6)
    return netlist

def get_algoritm():
    """ Prompts user which heuristic variation he/she wants to use """
    print("Okay, which heuristic variation do you want to run?")
    print("[ 1 ] Default A*           - This is the default A* algorithm without any heuristics")
    print("[ 2 ] Lava                 - The lava algorithm is a variation on A*, where the default A* is run first without constraints. After the first run the number of collisions is calculated on each location, and is made the cost.")
    print("[ 3 ] Neighbours           - The Neighbours algorithm is a variation of A* where the direct neighbours are given a (custom) cost.")
    print("[ 4 ] Elevator             - The Elevator algorithm tries every layer to plot a route, beginning with the lowest layer. If that is not possible, the algorithm finds a route from the start and endpoint to the specified layer, and finds a route in between the two points at the layer.")
    print("[ 5 ] Extended upstairs N. - This is an extention of the Neighbours algorithm, where the neighbours of neighbours are given cost values. This includes all of the vertical layers.")
    print("[ 6 ] Extended Neighbours  - This is an extention of the Neighbours algorithm, where the neighbours of neighbours are given cost values.")
    print("[ 7 ] Upstairs Neighbours  - This is the same as the Neighbours algorithm, except the vertical neighbours are also given cost values.")

    heuristic_option = validate_input(7)
    return heuristic_option

def get_sorting():
    """ Prompts user how he/she wants to sort the netlist """
    print("\nNow, so how do you want to sort the netlist?\n")
    print("[ 1 ] No sorting         - The netlist will not be touched.")
    print("[ 2 ] Manhattan distance - For every connection, the manhattan distance will be calculated and the netlist will be sorted on smallest distance first.")
    print("[ 3 ] Collisions         - The netlist is looped over once without the collision constraint, and the netlist will be sorted on routes with the most collisions.")

    sorting_option = validate_input(3)
    return sorting_option

def get_variables(algorithm):
    """ Prompts for variable 1 and 2 """
    variable_1 = 0
    variable_2 = 0

    if algorithm['option'] == 'lava':
        print("For lava you need to enter a multiplier. Enter a positive integer between 1 and 10! \n")
        variable_1 = validate_input(10)
        algorithm['variable_1'] = variable_1
    
    if algorithm['option'] == "neighbours" or algorithm['option'] == "upstairs neighbours":
        print("For neighbours you need to enter a cost value for the neighbours. Enter a positive integer between 1 and 10! \n")
        variable_1 = validate_input(10)
        algorithm['variable_1'] = variable_1

    if algorithm['option'] == "extended neighbours" or algorithm['option'] == "extended upstairs neighbours":
        print("\nFor this variation you need to enter two values. The first is for the direct neighbours.")
        variable_1 = validate_input(9999)
        print("\nThe second is for the extended neighbours.")
        variable_2 = validate_input(9999)
        algorithm['variable_1'] = variable_1
        algorithm['variable_2'] = variable_2

    return variable_1, variable_2

def get_extra_option():
    """ Asks the user whether he wants to use an extra heuristic """
    print("\nWe have a few additional heuristics, please choose the option you want to add.")
    print("[ 1 ] Nothing            - No extra heuristic will be added.")
    print("[ 2 ] Countdown          - The cost of the nodes will drop by a certain amount every time a route is layed.")
    print("[ 3 ] Turned up          - The algorithm will try to lay a route from A -> B and from B -> A. The route that is layed is the route that is the shortest.")
    extra_option = validate_input(3)

    return extra_option

def get_countdown_variable():
    """ Prompts for a countdown value """
    print("For this heuristic you need to enter an interval that counts down the value:")
    variable_3 = validate_input(10)
    return variable_3

def get_count_option():
    """ Prompts for a count value """
    print("\nOf what nodes do you want the value to decrease?")
    print("[ 1 ] Neighbours     - The cost of the neighbouring nodes of gates will be affected.")
    print("[ 2 ] Collisions     - The cost value of the nodes which are deciced by number the collisions will be affected.")
    count_option = validate_input(2)

    return count_option

def validate_input(nr_of_choices):
    """ Validates the user input """
    while True:
        try:
            option = int(input(f"Please enter an integer between 1 and {nr_of_choices}: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if option > nr_of_choices or option < 1:
            print(f"Thats not an integer between 1 and {nr_of_choices}! Please try again. ")
            continue
        else:
            break

    return option

    
    
    
    
    