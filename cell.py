import pygame
from constants import *

#initalizes Cell values

class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
    
    #Sets Cell Values to generated Sudoku Values
    def set_cell_value(self,value):
        self.value=value
    
    #Sets Cell value to user input value
    def set_skecthed_value(self,value):
        self.value=value

    #Draws value of generated sudoku values in center of cell
    def draw(self):

        number_font=pygame.font.Font(None,FONT_SIZE)

        if self.value== "0":
            number_type=None
            #pygame.draw.rect(self.screen,(255,0,0),(self.width*self.col,self.height*self.row,200,200),LINE_WIDTH)
        else:
            number_type=number_font.render(self.value,0,(0,0,0))
            #pygame.draw.rect(self.screen,(255,0,0),(self.width*self.col,self.height*self.row,200,200),LINE_WIDTH)
            number_rect=number_type.get_rect(center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            self.screen.blit(number_type, number_rect)

    #Draws value of user input values in top left of cell in grey
    def user_draw(self):
        number_font=pygame.font.Font(None,FONT_SIZE)

        if self.value== "0":
            number_type=None
            #pygame.draw.rect(self.screen,(255,0,0),(self.width*self.col,self.height*self.row,200,200),LINE_WIDTH)
        else:
            number_type=number_font.render(self.value,0,(192,192,192))
            #pygame.draw.rect(self.screen,(255,0,0),(self.width*self.col,self.height*self.row,200,200),LINE_WIDTH)
            number_rect=number_type.get_rect(center=(25+self.col*self.width, 25+self.row*self.height))
            self.screen.blit(number_type, number_rect)
