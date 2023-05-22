import pygame
import pygame_gui
import setting
import time
import gameLoop


def multi_lobby_screen(mode, draw_bm):
    screen = pygame.display.set_mode((pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen)))
    
    #요소 생성
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    font = pygame.font.SysFont('freesansbold.ttf', int(width*0.05))
    clock = pygame.time.Clock()
    time_delta = clock.tick(60)/1000.0

    #manager 객체 생성
    multiLobby_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")

    #text생성
    if mode == 'enter':
        ip_text = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(int(width*0.25),int(height*0.2),int(width*0.5),int(height*0.13)),
                                                        manager=multiLobby_manager,
                                                        initial_text="        Enter the ip",
                                                        placeholder_text="Please choose a name"
                                                        )
    
    port_text = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(int(width*0.25),int(height*0.35),int(width*0.5),int(height*0.13)),
                                                      manager=multiLobby_manager,
                                                      initial_text="        Enter the port number",
                                                      placeholder_text="Please choose a name"
                                                      )
    
    password_text = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(int(width*0.25),int(height*0.5),int(width*0.5),int(height*0.13)),
                                                      manager=multiLobby_manager,
                                                      initial_text="        Enter the password",
                                                      placeholder_text="Please choose a name"
                                                      )
    enterButton = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.25),int(height*0.67),int(width*0.23),int(height*0.15)),
                        text="Enter",
                        manager=multiLobby_manager
                )
    
    backButton  = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.52),int(height*0.67),int(width*0.23),int(height*0.15)),
                        text="Back",
                        manager=multiLobby_manager
                )
    
    running = True
    while running:
        setting.screen.blit(pygame.transform.scale(setting.background,(pygame.Surface.get_width(setting.screen),pygame.Surface.get_height(setting.screen))),(0,0))
        pygame.draw.rect(setting.screen, 'light gray',(width*0.12,height*0.083,width*0.75,height*0.85) ,0,5)
        pygame.draw.rect(setting.screen, 'dark gray', (width*0.12,height*0.083,width*0.75,height*0.85),10,5)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_element == ip_text:
                    print(event.text.strip())
                    ip = event.text.strip()
                elif event.ui_element == port_text:
                    print(event.text.strip())
                    port = event.text.strip()
                elif event.ui_element == password_text:
                    print(event.text.strip())
                    password = event.text.strip()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == backButton:
                    running = False


            multiLobby_manager.process_events(event)


        multiLobby_manager.update(time_delta)
        
        multiLobby_manager.draw_ui(screen)
        pygame.display.flip()

#multi_lobby_screen('enter')