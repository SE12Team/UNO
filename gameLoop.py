import pygame
import pygame_gui
import setting
from UI import *
import setting_menu
import cardUi
import Deck
import Player
import computer


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

    #Deck파일의 Deckclass의 인스턴스 생성
    deck = Deck.DeckClass()

    #Player파일의 Player클래스의 인스턴스 생성
    player = Player.Player("You")


    #메소드 실행
    user_board = ui.userBoard("You")
    main_board = ui.mainBoard()
    computer_uiList = ui.computerBoard(computer_num)
    deck_button = cardUi.DeckUi(card_manager,width,height)
    uno_button = ui.unoButton(main_board)
    
    
    #시작카드(덱 옆에 있는 카드) -> now_card_button: 시작카드 버튼 객체, now_card_instacne 카드 인스턴스 
    now_card_button, now_card_instacne = cardUi.now_card_draw(deck,card_manager)
    

    #플레이어 리스트 생성(current Turn 표시하기 위해), 인덱스 변수 생성
    Player_list = ["You"]
    for i in range(computer_num):
        Player_list.append(f"Computer {i+1}")
    currentTurn = 0
    
    #플레이어의 카드 버튼 리스트, 컴퓨터들의 버튼 2차원 리스트(행:컴퓨터 열:컴퓨터카드)
    card_button_list = []
    computer_card_button_list = [ [] for i in range(computer_num)]


    #카드 나눠주기 및 컴퓨터 인스턴스 생성
    for i in range(5):
        tmp = player_draw_card_deck(player,currentTurn,deck,card_manager,width,height,Player_list)
        card_button_list.append(tmp[2])

    computer_instance_list = [0]* (computer_num)

    for i in range(computer_num):
        computer_instance_list[i]=computer.Computer(f"computer{i+1}")
        for j in range(5):
            card_button = cardUi.computerCardUi(card_manager,width,height,i,len(computer_instance_list[i].hand))
            computer_card_button_list[i].append(card_button)
            computer_instance_list[i].setCard(deck)


    #Game 메인 루프 실행 전 변수 선언
    remain_time = 16
    clock = pygame.time.Clock()
    running = True


    #타이머시작
    start_time = time.time()
    #################################
    while running:
        #플레이어 카드 그리기 
        
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
                if (event.ui_element == deck_button) and (currentTurn == 0):
                    if len(player.hand) <= 12:
                        tmp = player_draw_card_deck(player,currentTurn,deck,card_manager,width,height,Player_list)
                        remain_time, currentTurn, card_button = tmp
                        card_button_list.append(card_button)
                    else:
                        print("can not draw") 
                for i, player_card_button in enumerate(card_button_list):
                    if (event.ui_element == player_card_button) and ((currentTurn == 0)):
                        print(player.hand[i].color)
                        if player.hand[i].color == now_card_instacne.color:
                            card_button_list[i].kill()
                            del card_button_list[i]
                            player_card_button.kill()
                            del player.hand[i]
                            card_button_list = just_paint_card(width,height,player,computer_instance_list,computer_card_button_list,card_button_list,card_manager)

                            

            '''
            elif event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
                for i, player_card_button in enumerate(card_button_list):
                    if event.ui_element == player_card_button:
                        time.sleep(0.2)
                        
                        card_button_list[i] = 0
                        player_card_button.kill()
                        color = player.hand[i].color
                        value = player.hand[i].value
                        tmp = cardUi.cardUI(width,height,card_manager,color,value,i,False,2)
                        card_button_list[i] = tmp
                        
                        print(i)
            
            elif event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                for i, player_card_button in enumerate(card_button_list):
                    if event.ui_element == player_card_button:
                        print(f'Test button unhovered {i}')
                        just_paint_card(width,height,player,computer_instance_list,computer_card_button_list,card_button_list,card_manager)
            '''
            card_manager.process_events(event)
            ui_manager.process_events(event)


        
        #Player 0초 될때까지 카드 선택 안하면 카드 한 장 먹고 턴 넘김
        if (remain_time < 1) and (currentTurn == 0) and(len(player.hand)<=12) :
            tmp = player_draw_card_deck(player,currentTurn,deck,card_manager,width,height,Player_list)
            remain_time, currentTurn, card_button = tmp
            card_button_list.append(card_button)

        #시간 타이머 작동 
        tmp = ui.timer(main_board,remain_time,start_time,currentTurn)
        remain_time = tmp[0]
        start_time = tmp[1]
        time_label = tmp[2]
        currentTurn = tmp[3]%(computer_num+1)
        time_delta = clock.tick(60)/1000.0
    
        #ui메소드 호출
        current_text = ui.currentTurn(Player_list[currentTurn],main_board)

        ui_manager.update(time_delta)
        card_manager.update(time_delta)
        screen.blit(pygame.transform.scale(gameBackground,(pygame.Surface.get_width(screen),pygame.Surface.get_height(screen))),(0,0))
        ui_manager.draw_ui(screen)
        card_manager.draw_ui(screen)
        pygame.display.flip() # 화면을 업데이트
        #타이머,턴 랜더링 삭제
        time_label.kill()
        current_text.kill()


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
            
def player_draw_card_deck(player,currentTurn,deck,card_manager,width,height,Player_list):
                    player.setCard(deck)
                    tmp = player.hand[-1]
                    color = tmp.color
                    value = tmp.value
                    card_button = cardUi.cardUI(width,height,card_manager,color,value,len(player.hand)-1,False,len(player.hand)+1)
                    remain_time = 16
                    currentTurn = nextTurn(currentTurn,False,Player_list)
                    return (remain_time,currentTurn,card_button)

def nextTurn(currentTurn,reverse,Player_list):
    
    if reverse:
        currentTurn -= 1
        if currentTurn == -1:
            currentTurn = len(Player_list)-1
    else:
        currentTurn += 1
        currentTurn % len(Player_list)
    return currentTurn 

def just_paint_card(width,height,player,computer_instance_list,computer_card_button_list,card_button_list,card_manager):

    #플레이어 카드 버튼 지우기
    for i in range(len(card_button_list)):
        card_button_list[i].kill()

    while card_button_list:
        del card_button_list[0]
    
    #플레이어 카드 버튼 다시 그리기

    for i,card in enumerate(player.hand):
        color = card.color
        value = card.value
        card_button_list.append(cardUi.cardUI(width,height,card_manager,color,value,i,False,i))
    
    return card_button_list
    

gameUiLoop(3)
