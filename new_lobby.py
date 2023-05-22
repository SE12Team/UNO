import pygame
import pygame_gui
import setting
import time
import gameLoop


def lobby_screen(draw_bm):
    #화면 생성
    screen = pygame.display.set_mode((pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen)))

    #요소 생성
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    font = pygame.font.SysFont('freesansbold.ttf', int(width*0.05))
    clock = pygame.time.Clock()
    time_delta = clock.tick(60)/1000.0
    player_name = "You"

    #manager 객체 생성
    lobby_ui_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")
    
    #컴퓨터 DropMenu생성
    computer_list = [pygame_gui.elements.UIDropDownMenu(relative_rect= pygame.Rect(int(width*0.5125),int(height*0.15)+int(height*0.15*i),int(width*0.25),int(height*0.1166)),
                                       starting_option = "None",
                                       manager=lobby_ui_manager,
                                       options_list = ["None","Common","mode A","mode B", "mode C", "mode D"],
                                       object_id="#lobby_computer",
                                       expand_on_option_click=False
                                       ) for i in range(5)]
    
    #Back 버튼 생성
    backButton = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.1875),int(height*0.6666),int(width*0.25),int(height*0.1666)),
                        text="Back",
                        manager=lobby_ui_manager,
                )
    
    #gamestart 버튼 생성
    startButton = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(int(width*0.1875),int(height*0.43),int(width*0.25),int(height*0.1666)),
                    text="Game Start",
                    manager=lobby_ui_manager,
            )
    
    #플레이어 text생성
    player_text = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(int(width*0.1875),int(height*0.2),int(width*0.25),int(height*0.1666)),
                                                      manager=lobby_ui_manager,
                                                      initial_text="        You",
                                                      placeholder_text="Please choose a name"
                                                      )
    computer_game_mode = ["None"]*5
    print(computer_game_mode)
    running = True
    while running:
        setting.screen.blit(pygame.transform.scale(setting.background,(pygame.Surface.get_width(setting.screen),pygame.Surface.get_height(setting.screen))),(0,0))
        pygame.draw.rect(setting.screen, 'light gray',(width*0.12,height*0.083,width*0.75,height*0.85) ,0,5)
        pygame.draw.rect(setting.screen, 'dark gray', (width*0.12,height*0.083,width*0.75,height*0.85),10,5)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                setting.running = False
            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                print(event.text.strip())
                player_name = event.text.strip()
            elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == computer_list[0]:
                    print("Selected option 0:", event.text)
                    computer_game_mode[0] = event.text
                elif event.ui_element == computer_list[1]:
                    print("Selected option 1:", event.text)
                    computer_game_mode[1] = event.text
                elif event.ui_element == computer_list[2]:
                    print("Selected option 2:", event.text)
                    computer_game_mode[2] = event.text
                elif event.ui_element == computer_list[3]:
                    print("Selected option 3:", event.text)
                    computer_game_mode[3] = event.text
                elif event.ui_element == computer_list[4]:
                    print("Selected option 4:", event.text)
                    computer_game_mode[4] = event.text            

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == backButton:
                    running = False
                elif event.ui_element == startButton:
                    draw_bm.fadeout(1000)
                    computer_num = 5-computer_game_mode.count("None")
                    if computer_num >= 1:
                        gameLoop.gameUiLoop(computer_num,player_name,computer_game_mode,"Single")
            lobby_ui_manager.process_events(event)

            
        lobby_ui_manager.update(time_delta)
        
        lobby_ui_manager.draw_ui(screen)
        pygame.display.flip()


