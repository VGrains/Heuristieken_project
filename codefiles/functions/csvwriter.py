import csv

""" Asks the user for an output filename and outputs the final netlist as csv. """
def csv_writer_tuplelist(tuplelist):
    # Ask user for an output filename.
    outfile = input("Enter filename for tuplelist output: ")
    outfile = "resultaten/{}.csv".format(outfile)
    
    # Creates a csv-file with the final netlist.
    with open(outfile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str("start, end")])
        for pair in tuplelist:
            writer.writerow([pair])

""" Asks the user for an output filename and outputs the created routes as csv. """
def csv_writer_finalroutes(final_routes):
    # Ask user for an output filename.
    outfile = input("Enter filename for wires output: ")
    outfile = "resultaten/{}.csv".format(outfile)
    
    # Creates a csv-file with the created routes.
    with open(outfile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str("net, wires")])
        for route in final_routes:
            writer.writerow([str(route) + str(', "') + str(final_routes[route]) + str('"')])


    
