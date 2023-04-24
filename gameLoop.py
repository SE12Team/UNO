import pygame
import pygame_gui
import setting
from UI import *
import setting_menu

pygame.init()

def gameUisetting():
    #창 가로세로 변수지정  
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    
    #스크린, 배경화면 지정 (문제 생기면 이거 원래대로 바꿔보기)
    screen = pygame.display.set_mode((width,height))
    gameBackground = pygame.image.load("data/images/board.png")
    
    return (width,height,screen,gameBackground)



def gameUiLoop(computer_num): 
    width,height,screen,gameBackground = gameUisetting()


    #pygame_gui UIManager 지정
    ui_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")
    card_manager = pygame_gui.UIManager((width, height), "data/themes/card_theme.json")
    
    
    #UI파일의 GameGui클래스 인스턴스 생성
    ui = GameGui(ui_manager)

    #메소드 실행
    user_board = ui.userBoard("You")
    main_board = ui.mainBoard()
    computer_uiList = ui.computerBoard(computer_num)

    Blue_1 =  pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((100, 100), (94, 141)),
                        text="",
                        manager=card_manager,
                        object_id="#Bule_0"
                    )
    Blue_2 =  pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((150, 100), (94, 141)),
                        text="",
                        manager=card_manager,
                        object_id="#Bule_0"
                    )
    #Game 메인 루프 실행 전 변수 선언
    remain_time = 16
    clock = pygame.time.Clock()
    running = True

    #타이머시작
    start_time = time.time()
    #################################
    while running:
        
        
        #이벤트 큐(이벤트 감지)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()           
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stopGameLoop(screen,time_delta)
                    width,height,screen,gameBackground = gameUisetting()
                    ui_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")
                    ui = GameGui(ui_manager)
                    user_board = ui.userBoard("You")
                    main_board = ui.mainBoard()
                    computer_uiList = ui.computerBoard(computer_num)
                    
                    start_time = time.time()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == Blue_1:
                    print("blue1")
                if event.ui_element == Blue_2:
                    print("blue2")
                    
            card_manager.process_events(event)
            ui_manager.process_events(event)

        


        #시간 타이머 작동 
        tmp = ui.timer(main_board,remain_time,start_time)
        remain_time = tmp[0]
        start_time = tmp[1]
        time_label = tmp[2]
        time_delta = clock.tick(60)/1000.0
    
    #ui메소드 호출
        ui.currentTurn("Computer 1",main_board)

        ui_manager.update(time_delta)
        card_manager.update(time_delta)
        screen.blit(pygame.transform.scale(gameBackground,(pygame.Surface.get_width(screen),pygame.Surface.get_height(screen))),(0,0))
        ui_manager.draw_ui(screen)
        card_manager.draw_ui(screen)
        pygame.display.flip() # 화면을 업데이트
        #타이머 랜더링 삭제
        time_label.kill()


def stopGameLoop(screen,time_delta):
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    esc_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")

    esc_panel = pygame_gui.elements.UIPanel(relative_rect = pygame.Rect((int(width*0.1875),int(height*0.25)),(int(width*0.625),int(height*0.5833))),
                                            starting_layer_height=1,
                                            manager = esc_manager,
                                            object_id=ObjectID(object_id="#ESC_window")
                                            )
    
    esc_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(int(width*0.3),int(height*0.3),int(width*0.375),int(height*0.1666)),
                                        text = "Paused",
                                        manager = esc_manager,
                                        object_id=ObjectID(object_id="#ESC_label")    
                                        )
    
    
    esc_setting_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(int(width*0.325),int(height*0.4833),int(width*0.33125),int(height*0.0833)),
                                 text="setting",
                                 manager=esc_manager,
                                 starting_height = 2,
                                 object_id=ObjectID(class_id="@ESC_button")
                                 )
    
    esc_exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(int(width*0.325),int(height*0.5833),int(width*0.33125),int(height*0.0833)),
                                 text="Program Exit",
                                 manager=esc_manager,
                                 starting_height = 2,
                                 object_id=ObjectID(class_id="@ESC_button")
                                 )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()           
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    
                    running =False
                    break
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == esc_setting_button:
                    print("setting")
                    setting_menu.get_menu(True, False, False)
                    return
                
                elif event.ui_element == esc_exit_button:
                    pygame.quit()

            esc_manager.process_events(event)

        esc_manager.draw_ui(screen)
        esc_manager.update(time_delta)
        pygame.display.flip()
            
gameUiLoop(3)

