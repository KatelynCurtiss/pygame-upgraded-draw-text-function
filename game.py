from ast import main
import pygame
import sys
import config

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def show_name(first_name, last_name, middle_name=None):
  
    if middle_name:
        output = f"{first_name} {middle_name} {last_name}"
    else:
        output = f"{first_name} {last_name}"
    return output


print(show_name("John", "Jenkins")) 
print(show_name("John", "Jenkins", "Michael")) 
    
def draw_text(screen, text, font_size, font_name, font_color, position,          anti_aliased =True, italic=False, bold=False):

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    
    
    font_name = "FreeMono.ttf"
    font_color1 = config.RED  
    font_color2 = config.PURPLE
    font_color3 = config.ORANGE
    font_size_normal = 36
    font_size_bold_italic = 30
    font_size_custom = 48

  
    custom_font_name = 'FiraCode-Regular.ttf'

    
    text_position_1 = [50, 50]
    text_position_2 = [225, 135]
    text_position_3 = [220, 370]

    running = True
    while running:



        running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) 
        


        pygame.display.flip()

        clock.tick(config.FPS) 

    pygame.quit()

    sys.exit()
if __name__ == "__main__":

    main()