import pygame
import pygame_gui
import setting
    
def videoResize(event,screen,background):
    screen = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
    screen.blit(pygame.transform.scale(background,(event.w,event.h)),(0,0))
    
class Ui:
    def __init__(self,ui_manager):
        self.ui_manager = ui_manager
        
    def computerUI(self,computer_num):
        #for i in range(computer_num):
            panel = pygame_gui.elements.UIPanel(relative_rect=(100,100,400,300),
                                                starting_layer_height=100,
                                                manager=self.ui_manager,
                                                )
        
            