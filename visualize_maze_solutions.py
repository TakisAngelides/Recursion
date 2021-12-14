import matplotlib.pyplot as plt
import numpy as np

def get_maze():

    maze = np.zeros((6, 6), dtype = 'int')
    maze[0][5] = 1
    maze[1][5] = 1
    maze[2][5] = 1
    maze[2][4] = 1
    maze[2][3] = 1
    maze[2][2] = 1
    maze[2][1] = 1
    maze[3][1] = 1
    maze[4][1] = 1
    maze[4][2] = 1
    maze[4][3] = 1
    maze[5][3] = 1
    maze[1][3] = 1
    maze[3][0] = 1
    maze[3][5] = 1
    maze[4][5] = 1
    maze[5][2] = 1 # uncomment this to see that the solve function finds all possible solutions

    return maze

maze = get_maze()

with open('solutions.txt', 'r') as f:

    line = f.readline()
    while line:

        row = line.strip().split(',')
        row.remove('')
        row = [int(element) for element in row]
        y = [row[i] for i in range(len(row)) if i % 2 == 0]
        x = [row[i] for i in range(len(row)) if i % 2 == 1]
        plt.scatter(x[0], y[0], color = 'green', zorder = 2, label = 'Start')
        plt.plot(x, y, color = 'blue', zorder = 1)
        plt.scatter(x[-1], y[-1], color = 'r', zorder = 3, label = 'Finish')
        plt.imshow(maze, zorder = 0)
        plt.legend()
        plt.show()
        line = f.readline()