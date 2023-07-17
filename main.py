import pygame, sys
from constants import *

#Set constants
#WIDTH = 800
#HEIGHT = 600
#BG_COLOR = (255, 255, 255)
#BUTTON_COLOR = (128, 128, 128)
#LINE_COLOR = (0, 0, 0)

def draw_main_menu(screen):
    #Initialize fonts
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    #Set background color
    screen.fill(BG_COLOR)

    #Initialize and draw title
    title_surface = start_title_font.render('Welcome to Sudoku', 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150)
    )

    #Initialize and draw buttons
    #Initilize text
    easy_text = button_font.render('Easy', 0, LINE_COLOR)
    medium_text = button_font.render('Medium', 0, LINE_COLOR)
    hard_text = button_font.render('Hard', 0, LINE_COLOR)
    quit_text = button_font.render('Quit', 0, LINE_COLOR)

    #Initialize surfaces
    easy_surface = pygame.Surface((easy_text.get_size()[0]+20, easy_text.get_size()[1] + 20))
    easy_surface.fill(BUTTON_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0]+20, medium_text.get_size()[1]+20))
    medium_surface.fill(BUTTON_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0]+20, hard_text.get_size()[1]+20))
    hard_surface.fill(BUTTON_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    quit_surface = pygame.Surface((quit_text.get_size()[0]+20, quit_text.get_size()[1]+20))
    quit_surface.fill(BUTTON_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    #Initialize rectangles
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 - 225, HEIGHT // 1.5))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2 + 225, HEIGHT // 1.5))
    quit_rectangle = quit_surface.get_rect(center=(WIDTH//2, HEIGHT // 1.25))

    #Draw to screen
    screen.blit(title_surface, title_rectangle)
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    screen.blit(quit_surface, quit_rectangle)
    pygame.display.update()
  #Loop to check for events in order to update screen per pygame functionality and return to main function
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if quit_rectangle.collidepoint(event.pos):
            pygame.quit()
          elif (easy_rectangle.collidepoint(event.pos)
          or medium_rectangle.collidepoint(event.pos)
          or hard_rectangle.collidepoint(event.pos)):
            break

    


def draw_game_over(screen):
    pass

if __name__ == '__main__':
    #Initialize the pygame instance and draw the screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    draw_main_menu(screen)

    #Create main run loop
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
              

    pygame.quit()



