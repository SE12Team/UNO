import pygame
import setting
import pygame_gui

def drawStoryMode():
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    screen = pygame.display.set_mode((pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen)))
    background = pygame.image.load("./image/storyModeMap.jpeg")
    gui_manager = pygame_gui.UIManager((width,height))



    clock = pygame.time.Clock()
    running = True

    while running:
        #타임
        time_delta = clock.tick(60)/1000
    

        screen.blit(pygame.transform.scale(background,(width,height)),(0,0))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                setting.running = False
            gui_manager.process_events(event)
            
        pygame.display.update()

drawStoryMode()