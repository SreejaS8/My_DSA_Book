class Solution(object):
    def solveSudoku(self, board):
        """
        Solves the Sudoku puzzle in place using backtracking with constraint propagation.
        :type board: List[List[str]]
        :rtype: None
        """
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        self.empty_cells = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    self.empty_cells.append((i, j))
                else:
                    num = board[i][j]
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[(i // 3) * 3 + j // 3].add(num)

        self.solve(board, 0)

    def solve(self, board, index):
        if index == len(self.empty_cells):
            return True 

        row, col = self.empty_cells[index]
        box_index = (row // 3) * 3 + col // 3

        for num in map(str, range(1, 10)): 
            if num not in self.rows[row] and num not in self.cols[col] and num not in self.boxes[box_index]:
                board[row][col] = num
                self.rows[row].add(num)
                self.cols[col].add(num)
                self.boxes[box_index].add(num)

                if self.solve(board, index + 1):
                    return True 

                board[row][col] = "."
                self.rows[row].remove(num)
                self.cols[col].remove(num)
                self.boxes[box_index].remove(num)

        return False

board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
solution = Solution()
print(solution.solveSudoku(board))

for row in board:
    print(row)