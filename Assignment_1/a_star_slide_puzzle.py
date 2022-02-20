# A General A* Function and its Application to Slide Puzzles
# CS 470/670 at UMass Boston

import numpy as np
from collections import deque
import bisect


example_1_start = np.array([[2, 8, 3],
                           [1, 6, 4],
                           [7, 0, 5]])

example_1_goal = np.array([[1, 2, 3],
                           [8, 0, 4],
                           [7, 6, 5]])

example_2_start = np.array([[ 2,  6,  4,  8],
                            [ 5, 11,  3, 12],
                            [ 7,  0,  1, 15],
                            [10,  9, 13, 14]])

example_2_goal = np.array([[ 1,  2,  3,  4],
                           [ 5,  6,  7,  8],
                           [ 9, 10, 11, 12],
                           [13, 14, 15,  0]])

# For a given current state, move, and goal, compute the new state and its h'-score and return them as a pair. 
def make_node(state, row_from, col_from, row_to, col_to, goal):
    # Create the new state that results from playing the current move. 
    (height, width) = state.shape
    new_state = np.copy(state)
    new_state[row_to, col_to] = new_state[row_from, col_from]
    new_state[row_from, col_from] = 0
    
    # Count the mismatched numbers and use this value as the h'-score (estimated number of moves needed to reach the goal).
    mismatch_count = 0
    for i in range(height):
        for j in range(width):
            if new_state[i, j] > 0 and new_state[i, j] != goal[i, j]:
                mismatch_count += 1
   
    return (new_state, mismatch_count)

# For given current state and goal state, create all states that can be reached from the current state
# (i.e., expand the current node in the search tree) and return a list that contains a pair (state, h'-score)
# for each of these states.   
def slide_expand(state, goal):
    node_list = []
    (height, width) = state.shape
    (empty_row, empty_col) = np.argwhere(state == 0)[0]     # Find the position of the empty tile
    
    # Based on the position of the empty tile, find all possible moves and add a pair (new_state, h'-score)
    # for each of them.
    if empty_row > 0:
        node_list.append(make_node(state, empty_row - 1, empty_col, empty_row, empty_col, goal))
    if empty_row < height - 1:
        node_list.append(make_node(state, empty_row + 1, empty_col, empty_row, empty_col, goal))
    if empty_col > 0:
        node_list.append(make_node(state, empty_row, empty_col - 1, empty_row, empty_col, goal))
    if empty_col < width - 1:
        node_list.append(make_node(state, empty_row, empty_col + 1, empty_row, empty_col, goal))
    
    return node_list

# For a given current state, move, and goal, compute the new state and its h'-score and return them as a pair. 
def make_node_improved(state, row_from, col_from, row_to, col_to, goal):
    # Create the new state that results from playing the current move. 
    (height, width) = state.shape
    new_state = np.copy(state)
    new_state[row_to, col_to] = new_state[row_from, col_from]
    new_state[row_from, col_from] = 0
    
    # Count the mismatched numbers and use this value as the h'-score (estimated number of moves needed to reach the goal).
    # Improving the scoring so that we can run example_2
    mismatch_count = 0
    for i in range(height):
        for j in range(width):
            
            # going to try the manhattan distance
            if new_state[i, j] > 0 and new_state[i, j] != goal[i, j]:
                (goal_x, goal_y) = np.argwhere(goal == new_state[i, j])[0]
                mismatch_count += abs(i - goal_x) + abs(j - goal_y)
   
    return (new_state, mismatch_count)

# For given current state and goal state, create all states that can be reached from the current state
# (i.e., expand the current node in the search tree) and return a list that contains a pair (state, h'-score)
# for each of these states.   
def slide_expand_improved(state, goal):
    node_list = []
    (height, width) = state.shape
    (empty_row, empty_col) = np.argwhere(state == 0)[0]     # Find the position of the empty tile
    
    # Based on the position of the empty tile, find all possible moves and add a pair (new_state, h'-score)
    # for each of them.
    if empty_row > 0:
        node_list.append(make_node_improved(state, empty_row - 1, empty_col, empty_row, empty_col, goal))
    if empty_row < height - 1:
        node_list.append(make_node_improved(state, empty_row + 1, empty_col, empty_row, empty_col, goal))
    if empty_col > 0:
        node_list.append(make_node_improved(state, empty_row, empty_col - 1, empty_row, empty_col, goal))
    if empty_col < width - 1:
        node_list.append(make_node_improved(state, empty_row, empty_col + 1, empty_row, empty_col, goal))
    
    return node_list
  
# def a_star(start, goal, expand):     
#     ancestors = []
#     ancestors.append(start)
#     open_cells = []
#     closed_cells = []
#     open_cells.append(start)

#     # while there is open cells to look into
#     while open_cells:
#         lowest = 100000
#         # get a list of the possible moves
#         node_list = expand(open_cells.pop(), goal)
        
#         # for each possible move, check the h-value to find the first lowest
#         for node in node_list:
#             (state, h_value) = node
#             # if this move would be the goal, return the move and the ancestors to that move
#             if h_value == 0:
#                 ancestors.append(state)
#                 return ancestors
            
#             # otherwise find the lowest h-value
            
#             # this is for the first iteration, when closed_cells is empty
#             if len(closed_cells) == 0:
#                 if lowest > h_value:
#                     lowest = h_value
#                     next_node = state
#                     continue
            
#             # this is for every other iteration of the loop, when closed_cells has something
#             for closed_cell in closed_cells:
#                 if lowest > h_value:
#                    lowest = h_value
#                    next_node = state
#                 elif np.array_equal(closed_cell, state):
#                     continue
#                 break
        
#         # otherwise add the next move to open_cells and closed_cells to loop
#         open_cells.append(next_node)   # this will get popped in the next iteration of the loop
#         ancestors.append(next_node)    # this is going to add to the return value if there is a solution
#         closed_cells.append(next_node) # this prevents looping
        
    
#     # exit with no solution
#     return []

# attempt 2
def a_star(start, goal, expand):
    
    # initialize the two arrays
    open_cells =  [start]
    closed_cells = []
    ancestors = []
    next_node = [start]
    lowest = 100000
    target_maximum = 100001
    # while there are unexplored nodes, check for solution
    while open_cells:
        node = open_cells.pop()
        # if this current node is the solution, return with the path
        if np.array_equal(node, goal):
            ancestors.append(node)
            return ancestors
        
        # expand to all possible moves
        unordered_list = expand(node, goal)
        closed_cells.append(node)
        
        # for every move, make sure that it wasn't checked already, then if it wasn't add it to M.
        # sort the unordered list of possible moves
        
        ordered_list = []
        for state, h_value in unordered_list:
            if h_value < lowest:
                lowest = h_value
                ordered_list.append(state)
            else:
                ordered_list.insert(0, state)
        
        # check if that possible move has been a part of the opened or closed list, is so, skip it.\
        while ordered_list:
            open_cells.append(ordered_list.pop(0))
        
        if target_maximum <= lowest:
            break
        target_maximum = lowest
        ancestors.append(open_cells[-1])
    # return with no solution
    return []

# Find and print a solution for a given slide puzzle, i.e., the states we need to go through 
# in order to get from the start state to the goal state.
def slide_puzzle_solver(start, goal):
    # solution = a_star(start, goal, slide_expand)
    solution = a_star(start, goal, slide_expand_improved)
    if len(solution) == 0:
        print('This puzzle has no solution. Please stop trying to fool me.')
        return
        
    (height, width) = start.shape
    if height * width >= 10:            # If numbers can have two digits, more space is needed for printing
        digits = 2
    else:
        digits = 1
    horizLine = ('+' + '-' * (digits + 2)) * width + '+'
    for step in range(len(solution)):
        state = solution[step]
        for row in range(height):
            print(horizLine)
            for col in range(width):
                print('| %*d'%(digits, state[row, col]), end=' ')
            print('|')
        print(horizLine)
        if step < len(solution) - 1:
            space = ' ' * (width * (digits + 3) // 2)
            print(space + '|')
            print(space + 'V')

slide_puzzle_solver(example_2_start, example_2_goal)