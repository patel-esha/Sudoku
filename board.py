import pygame
from constants import *
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:
    #initalizes Cell values
    def __init__(self,width,height,screen,difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        self.board=SudokuGenerator.get_board()
        #sets row and col = 9 for 81 cells in sudoku board
        self.cells=[[Cell(self.board[i][j], i, j, self.height//9,
                            self.width//9) for j in range(9)] for i in range(9)]

    #Draws Outline of Sudoku Grid
    def draw(self):

        for x in range(1, 10):
            if x%3==0:
                pygame.draw.line(self.screen, LINE_COLOR, (0, CELL_SIZE * x),
                             (WIDTH, CELL_SIZE * x), LINE_WIDTH*4)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (0, CELL_SIZE * x),
                             (WIDTH, CELL_SIZE * x), LINE_WIDTH)

        for x in range(1, 9):
            if x%3==0:
                pygame.draw.line(self.screen, LINE_COLOR, (CELL_SIZE * x, 0),
                             (CELL_SIZE * x, CELL_HEIGHT), LINE_WIDTH*4)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (CELL_SIZE * x, 0),
                             (CELL_SIZE * x, CELL_HEIGHT), LINE_WIDTH) 

        #draws cell values
        for x in range(9):
            for y in range(9):
                self.cells[x][y].draw(self.screen)                     
               
    #selects the current cell value
    def select(self,row,col):
        return self.board[row][col]

    #Returns tuple of row and col values
    def click(self,x,y):
        if self.board[x][y] != 0:
            return x,y
        else:
            return None

    #sets value of selected cell to 0
    def clear(self):
        self.select=0

    #sets value of selected cell to Sketched value
    def sketch(self,value):
        self.select=value
        
    #sets value of selected cell to user input
    def place_number(self,value):
        self.select=value

    #resets value of self.cells to self.board values
    def reset_to_original(self):
        for x in range(0,8):
            for y in range(0,8):
                self.cells[x][y]==self.board[x][y]

    #Checks if any cells are still zero, and if so returns False
    def is_full(self):
        for i in range(0,8):
            for j in range(0,8):
                if self.board[i][j]==0:
                    return False
        
        return True

    #updates all 
    def update_board(self):
        for x in range(0,8):
            for y in range(0,8):
                self.board[x][y]==self.cells[x][y]


    #checks if any cells are zero, and if so, returns row and col of empty cell
    def find_empty(self):
        for x in range(0,8):
            for y in range(0,8):
                if self.board[x][y]==0:
                    return x,y

    #check if self.cells matches self.board(and doesn't equal zero), and if so, returns True
    def check_board(self):
        for x in range(0,8):
            for y in range(0,8):
                if self.cells[x][y]==self.board[x][y] and self.board[x][y] != 0:
                    continue
                else:
                    return False
        
        return True
