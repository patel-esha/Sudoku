import math, random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = int(row_length)
        self.removed_cells = int(removed_cells)
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.box_length = math.sqrt(row_length)
        # constructor for the SD class
        # row_length is always 9
        # removed_cells depends on difficulty level chosen
        # easy - 30 / medium - 40 / hard - 50

    def get_board(self):
        return self.board
        # returns a 2D python list of numbers, represents the board

    def print_board(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=' ')
            print()
        # displays the board to the console

    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        else:
            return True
        # returns a boolean value
        # determines if num is contained in the given row

    def valid_in_col(self, col, num):
        for i in range(self.row_length):
            if self.board[i][col] == num:
                return False
        return True
        # returns a boolean value
        # determines if num is contained in the given column

    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == num:
                    return False
        return True
        # returns a boolean value
        # determines if num is contained in the 3x3 box
        # from (row_start, col_start) to (row_start + 2, col_start + 2)

    def is_valid(self, row, col, num):
        if not self.valid_in_col(col, num):
            return False
        if not self.valid_in_row(row, num):
            return False
        row = row - row % 3
        col = col - col % 3
        return self.valid_in_box(row, col, num)
      
        # returns if it is valid to enter num at (row, col) in the board
        # this is done by checking the appropriate row, column, and box

    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                while self.board[i][j] == 0:
                    random_num = int(random.randint(1, 9))
                    if self.valid_in_box(row_start, col_start, random_num):
                        self.board[i][j] = random_num
        # randomly fills in values in the 3x3 box
        # from (row_start, col_start) to (row_start + 2, col_start + 2)
        # uses unused_in_box to ensure no value occurs in the box twice

    def fill_diagonal(self):
        x = 0
        y = 0
        while x <= 6 and y <= 6:
            self.fill_box(x, y)
            x += 3
            y += 3
# fills the three boxes along the main diagonal of the board
        # first major step in the generation of a Sudoku

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            row = int(row)
            col = int(col)
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.print_board()
        print()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        cells = 0
        while cells != self.removed_cells:
            row_coordinate = int(random.randint(0, 8))
            col_coordinate = int(random.randint(0, 8))
            if self.board[row_coordinate][col_coordinate] != 0:
                self.board[row_coordinate][col_coordinate] = 0
                cells += 1
        # removes the appropriate number of cells from the board
        # does so by randomly generating (row, col) coordinates of the board and setting the value to 0
        # this method should be called after generating the Sudoku solution


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.print_board()
    board = sudoku.get_board()
    sudoku.remove_cells()
    print()
    sudoku.print_board()
    board = sudoku.get_board()
    return board


generate_sudoku(9, 30)
