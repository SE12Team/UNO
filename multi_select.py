import pygame
import pygame_gui
import setting
import gameLoop
import multiLobby
def multi_select():
    screen = pygame.display.set_mode((pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen)))

    #요소 생성
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    font = pygame.font.SysFont('freesansbold.ttf', int(width*0.05))
    clock = pygame.time.Clock()
    time_delta = clock.tick(60)/1000.0

    #manager 객체 생성
    multi_select_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")

    #버튼 생성(enter, )
    enterButton = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.3),int(height*0.2),int(width*0.4),int(height*0.1666)),
                        text="Enter",
                        manager=multi_select_manager
                )
    
    createButton = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.3),int(height*0.4),int(width*0.4),int(height*0.1666)),
                        text="Create",
                        manager=multi_select_manager
                )
    backButton = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.3),int(height*0.6),int(width*0.4),int(height*0.1666)),
                        text="Back",
                        manager=multi_select_manager
                )
    running = True
    while running:
        setting.screen.blit(pygame.transform.scale(setting.background,(pygame.Surface.get_width(setting.screen),pygame.Surface.get_height(setting.screen))),(0,0))
        pygame.draw.rect(setting.screen, 'light gray',(width*0.12,height*0.083,width*0.75,height*0.85) ,0,5)
        pygame.draw.rect(setting.screen, 'dark gray', (width*0.12,height*0.083,width*0.75,height*0.85),10,5)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == enterButton:
                    multiLobby.multi_lobby_screen('enter')
                elif event.ui_element == createButton:
                    multiLobby.multi_lobby_screen('create')
                elif event.ui_element == backButton:
                    running = False
            
            multi_select_manager.process_events(event)





        multi_select_manager.update(time_delta)
        
        multi_select_manager.draw_ui(screen)
        pygame.display.flip()
#multi_select()