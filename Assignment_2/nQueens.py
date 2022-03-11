import math
import copy
import random
class nQueens:

    def __init__(self, n):
        self.n = n
        self.assignment = [-1] * n  # each element is the row index for corresponding column, -1 means no assignment yet
        self.domain = [list(range(n)) for _ in range(n)]  # available values (rows) for each column (variable)
        self.unassigned_columns = [i for i in range(n)]  # none of the columns are assigned yet
        self.backtrack_counter = 0

        self.solve_and_print()


    def select_next_variable(self):
        """
        :return: Next unassigned variable (column) in line
        """

        return self.unassigned_columns[0]

    def is_consistent(self, col, val):
        """
        Check if assigning val to col will be consistent with the rest of the assigments
        :return: true of consistent, false otherwise
        """
        assigned_columns = [i for i in range(self.n) if i != col and i not in self.unassigned_columns]
        for i in assigned_columns:
            col_distance = abs(i - col)
            row_distance = abs(self.assignment[i] - val)
            if row_distance == 0 or row_distance == col_distance:
                return False
        return True

    def select_next_variable_improved(self):
        """
        Finds and returns the variable with the fewest legal values
        :return: Variable with the least amount of legal values
        """
        
        lowest = 0 # this is the index of the lowest domain variable
        for index in self.unassigned_columns:
            if len(self.domain[index]) < len(self.domain[lowest]):
                lowest = index
        return self.unassigned_columns[lowest]



    def forward_checking(self, var):
        """
        Updates the domain of values and returns it
        :param var: Current column to check
        :return: Updated domain
        """

        # Fill in the body

        return []

    def ac3(self, var):
        """
        Updates the domain of values and returns it
        :param var: Current column to check
        :return: Updated domain
        """
        queue = copy.copy(self.unassigned_columns)
        while not queue == []:
            pass

        return []


    def backtrack(self):
        """
        Recursive backtracking function
        :return:a solution (final problem state) if there is one, otherwise it returns [].
        """
        self.backtrack_counter += 1

        if len(self.unassigned_columns) == 0:
            return self.assignment

        # Select the next unassigned column
        var = self.select_next_variable()
        
        # Iterate through values for var
        for val in self.domain[var]:
            if self.is_consistent(var, val):
                self.assignment[var] = val
                self.unassigned_columns.remove(var)

                result = self.backtrack()
                if result:
                    return result

                self.assignment[var] = -1
                self.unassigned_columns.append(var)  # reassign var to the unassigned columns

        return []


    def backtrack_improved(self, inference):
        """
        Recursive backtracking function
        :param inference: an inference method such as forward chaining or ac3
        :return:a solution (final problem state) if there is one, otherwise it returns [].
        """


        self.backtrack_counter += 1
        
        if len(self.unassigned_columns) == 0:
            return self.assignment
        
        # find the next variable
        var = self.select_next_variable_improved()
        
        
        

        # Fill in the body
        return []




    def solve_and_print(self):

        solution = self.backtrack()
        # solution = self.backtrack_improved(self.forward_checking)
        # solution = self.backtrack_improved(self.ac3)

        if solution.count(-1) == len(solution):
            print('Sorry, there is no solution to the %d-queens problem.' % (self.n))
        else:
            print('Solution: ' + str(solution))
            for x in range(0, self.n):
                for y in range(0, self.n):
                    if solution[x] == y:
                        print('Q', end=' ')
                    else:
                        print('-', end=' ')
                print('')

        print("Backtracking is called %d times" % self.backtrack_counter)



nq = nQueens(8)