import numpy as np
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        k = np.array([[int(i) if i !='.' else 0  for i in board[j] ] for j in range(9)])

        def possibilites(puzzle, num, column, row):
            """Check if a given value is valid for a given position in a given puzzle
               puzzle: numpy.array a 9x9 array representing the puzzle grid
               num: int the number value to check
               column: int the column of the position to check in the puzzle array
               row: int the row of the position to check in the puzzle array
               returns False if num is not a valid value for the given position
               otherwise, returns True
            """
            if num in puzzle[row]:
                return False
            if num in puzzle[:,column]:
                return False

            box_start_col = (column//3)*3
            box_start_row = (row//3)*3
            if num in puzzle[box_start_row:box_start_row+3, box_start_col:box_start_col+3]:
                return False
            return True

        def empty_pos(puzzle):
            """Check if there are any remaining empty positions in the puzzle
               puzzle: numpy.array a 9x9 array representing the puzzle grid
               Returns False if the puzzle is solved (no empty positions)
               Otherwise, retuns a tuple containing the location in the array of the first empty space"""
            for row_id, row in enumerate(puzzle):
                for column_id, value in enumerate(row):
                    if value == 0:
                        return row_id, column_id
            return False

        def solve(puzzle):
            """Attempt to solve the puzzle
               puzzle: numpy.array a 9x9 array representing the puzzle grid
               returns True if the puzzle is already solved or if the solve attempt is successful
               otherwise, returns False"""
            position = empty_pos(puzzle)
            if not position:
                return True

            i, j = position

            for num in range(1, 10):
                if possibilites(puzzle, num, j, i):
                    puzzle[i][j] = num
                    #print('{}\n'.format(puzzle))

                    if solve(puzzle):
                        return True
                    puzzle[i][j] = 0
            return False

        def filled(puzzle):
            """Checks if the puzzle is complete (all cells are filled).
               puzzle: numpy.array a 9x9 array representing the puzzle grid
               Returns True if not all positions are filled, otherwise returns False"""
            return not puzzle.all()


        while filled(k):
            solve(k)
            
        board[:] = [[str(i) for i in k[j] ] for j in range(9)]