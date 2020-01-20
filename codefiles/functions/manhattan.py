def manhattan_distance(x_base, x_goal, y_base, y_goal):
    """ Calculates the manhattan distance between two points on the grid"""
    distance = abs(x_base - x_goal) + abs(y_base - y_goal)
    
    return distance