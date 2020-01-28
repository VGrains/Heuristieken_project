import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_3dgraph(chip_locations, routes):
    """ Creates an interactive 3d graph of the gates and wires """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Add the chips as points
    x = []
    y = []

    for i in chip_locations:
        x.append(chip_locations[i][1])
        y.append(chip_locations[i][2])

    # Add the z coordinates for the gates, which are always zero
    z = [0 for i in x]
    plt.yticks(np.arange(min(y), max(y) + 1, 1.0))
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    
    ax.set_zticks([0, 1, 2, 3, 4, 5, 6, 7])
    ax.scatter(x,y,z,s=75, c='r', marker='s')
    
    # Add the routes as wires
    for x in routes:
        wires_x = []
        wires_y = []
        wires_z = []
        for y in routes[x]:
            wires_x.append(y[1])
            wires_y.append(y[2])
            wires_z.append(y[0])

        ax.plot(wires_x, wires_y, wires_z)
    
    


    plt.show()