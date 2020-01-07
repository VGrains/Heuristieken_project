y_as = 7
x_as = 8
grid = [[0 for x in range(x_as)] for y in range(y_as)]
chips = {'A' : (1,5),
        'B' : (6,5),
        'C' : (4,4),
        'D' : (6,2),
        'E' : (3,1)}
for i in chips:
    y_value = y_as - chips[i][1] - 1
    grid[y_value][chips[i][0]] = i

for x in grid:
    print(x)
