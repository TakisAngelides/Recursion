import numpy as np
import matplotlib.pyplot as plt

solutions = [] # will store all the possible solutions for the maze problem

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

def get_legal_moves(m, loc, p):

    legal_moves = []

    row = loc[0]
    col = loc[1]

    if row+1 <= len(m)-1 and [row+1, col] not in p: # a legal move is defined by the maze m having a 1 on that square rather than a 0 and also that square is not in the path list already, the second condition is to avoid going backwards and in loops
        if m[row+1][col]:
            legal_moves.append([row+1, col]) # explore going downwards first, this legal move will be the first to be tried in the solve function since it is appended first in the legal_moves list

    if col-1 >= 0 and [row, col-1] not in p:
        if m[row][col-1]:
            legal_moves.append([row, col-1])

    if col+1 <= len(m[0])-1 and [row, col+1] not in p:
        if m[row][col+1]:
            legal_moves.append([row, col+1])

    if row-1 >= 0:
        if m[row-1][col] and [row-1, col] not in p:
            legal_moves.append([row-1, col])

    return legal_moves

def solve(m, s, p):

    """
    :param m: this is a list of lists representing the maze as a matrix
    :param s: this is a list with two elements [row, column] representing where we start from on the maze
    :param p: this is a list of two element lists [[row, column], [row, column], ... ] representing the path from entry
    to exit of the maze, we initialize this to just p = [s] when we first call the function

    :return: this function returns nothing but prints all possible solutions to the maze
    """

    if s[0] != len(m)-1: # recursion stopping condition - if this is false we have reached the bottom of the maze and are finished so we print p

        for legal_move in get_legal_moves(m, s, p): # if the above condition is true it means we have not reached the bottom of the maze and we keep exploring legal moves

            p.append(legal_move) # if its legal to go to a square we go there and call solve starting from that new square
            solve(m, legal_move, p) # recursion

            p.remove(legal_move) # backtracking

        return

    print(p)
    # Write the solution to a text file
    with open('solutions.txt', 'a') as f:
        for square in p:
            f.write(f'{square[0]},{square[1]},')
        f.write('\n')
    return

maze = get_maze()

solve(maze, [0, 5], [[0, 5]])
