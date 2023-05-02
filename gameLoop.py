import pygame
import pygame_gui
import setting
from UI import *
import setting_menu
import cardUi
import Game
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

    #Player파일의 Player클래스의 인스턴스 생성
    players = []
    players.append(Player.Player("You"))

    #Computer 인스턴스 생성
    for i in range(computer_num):
        players.append(computer.Computer(f"computer{i+1}"))

    #Gamek파일의 Game클래스의 인스턴스 생성
    game = Game.Game(players)

    #플레이어, 컴퓨터에게 카드 5장씩 분배
    game.distrib_card(5)

    #discard_deck 시작카드 추가 및 그리기 및 discard버튼 객체 생성
    tmp = game.dumy_deck.draw_card()
    while (tmp.color == "Wild") or (tmp.color == "Wild Draw Four") or (tmp.color == "Wild Draw Two") or (tmp.value == 'Skip') or (tmp.value == 'Reverse') or (tmp.value == 'Draw Two') or (tmp.value == 'Draw Four'):
        game.dumy_deck.cards.append(tmp)
        game.dumy_deck.shuffle()
        tmp = game.dumy_deck.draw_card()
    game.add_to_discard(tmp)
    color = tmp.color
    value = tmp.value
    discard_button = cardUi.cardUI(card_manager,color,value,0,True,1)

    #버튼 객체(플레이어랑 컴퓨터)를 담은 리스트 만들기 and 그리기
    player_card_button_list = []
    computer_card_button_list = [ [] for i in range(computer_num)]
    for i, card in enumerate(game.players[0].hand):
        color = card.color
        value = card.value
        player_card_button_list.append(cardUi.cardUI(card_manager,color,value,i,False,i+1))
  
    for i in range(computer_num):
        for j in range(len(game.players[i+1].hand)):
            computer_card_button_list[i].append(cardUi.computerCardUi(card_manager,i,j))


    #게임판 Ui 그려주는 메소드 실행
    user_board = ui.userBoard("You")
    main_board = ui.mainBoard()
    computer_uiList = ui.computerBoard(computer_num)
    deck_button = cardUi.DeckUi(card_manager)
    uno_button = ui.unoButton(main_board)
    

    #플레이어 리스트 생성(current Turn 표시하기 위해), 인덱스 변수 생성
    Player_list = ["You"]
    for i in range(computer_num):
        Player_list.append(f"Computer {i+1}")

    #Game파일 Turn클래스의 인스턴스 생성
    game_turn = Game.Turn(computer_num+1)   

    #Game 메인 루프 실행 전 변수 선언
    remain_time = 16
    clock = pygame.time.Clock()
    running = True
    time_delta = clock.tick(60)/1000.0
    #타이머시작
    start_time = time.time()
    #################################
    while running:

        #현재 턴 label 글자 랜더링
        
        current_text = ui.rendering_currentTurn(game.players[game_turn.current_player].name, main_board)
        # ui_manager.update(time_delta)
        # card_manager.update(time_delta)
        # screen.blit(pygame.transform.scale(gameBackground,(pygame.Surface.get_width(screen),pygame.Surface.get_height(screen))),(0,0))
        # ui_manager.draw_ui(screen)
        # card_manager.draw_ui(screen)
        pygame.display.flip() # 화면을 업데이트
        #컴퓨터 턴 동작
        if game_turn.current_player != 0:
            print(f"discard : {game.discard_deck.cards[-1].color}, {game.discard_deck.cards[-1].value}")
            #제한시간은 플레이어에게만 표시되도록
            time_label.kill()
            ui_manager.update(time_delta)
            card_manager.update(time_delta)
            screen.blit(pygame.transform.scale(gameBackground,(pygame.Surface.get_width(screen),pygame.Surface.get_height(screen))),(0,0))
            ui_manager.draw_ui(screen)
            card_manager.draw_ui(screen)
            pygame.display.flip() # 화면을 업데이트

            print(f"{game_turn.current_player} : {game.players[game_turn.current_player].hand}")             

            for index in range(len(game.players[game_turn.current_player].hand)):
                card = game.players[game_turn.current_player].hand[index]
                flag = game.players[game_turn.current_player].canPlay(card,game.discard_deck)
                if flag == 1:
                    if card.value in ['1','2','3','4','5','6','7','8','9','0']:
                        game.add_to_discard(card)
                        del game.players[game_turn.current_player].hand[index]
                        game_turn.next_direction()
                        break
                    elif card.value == 'Skip':
                        game.add_to_discard(card)
                        del game.players[game_turn.current_player].hand[index]
                        game_turn.skip_direction()
                        break
                    elif card.value == 'Reverse':
                        game.add_to_discard(card)
                        del game.players[game_turn.current_player].hand[index]
                        game_turn.reverse_direction()
                        game_turn.next_direction()
                        break
                    elif card.value == 'Draw Four':
                        game.add_to_discard(card)
                        del game.players[game_turn.current_player].hand[index]
                        game_turn.next_direction()
                        game.players[game_turn.current_player].setCard(game.dumy_deck,4)
                        break
                    elif card.value == 'Draw Two':
                        game.add_to_discard(card)
                        del game.players[game_turn.current_player].hand[index]
                        game_turn.next_direction()
                        game.players[game_turn.current_player].setCard(game.dumy_deck,2)
                        break
                elif flag == 2:
                    game.add_to_discard(card)
                    del game.players[game_turn.current_player].hand[index]
                    break
                elif flag == 3:
                    #와일드 카드의 value를 자신이 가장 많이 들고 있는 색의 색으로 바꿈
                    dic = {'Blue':0, 'Green':0, 'Red':0, 'Yellow':0}
                    for tmp in  game.players[game_turn.current_player].hand:
                        if tmp.color in dic:
                            dic[tmp.color] += 1

                    print(card)        
                    card.value = max(dic, key=dic.get)
                    print(card)

                    game.add_to_discard(card)
                    game_turn.next_direction()
                    if card.color == 'Wild': 
                        del game.players[game_turn.current_player].hand[index]
                    elif card.color == 'Wild Draw Four':
                        game.players[game_turn.current_player].setCard(game.dumy_deck,4)
                        del game.players[game_turn.current_player].hand[index]
                        break
                    elif card.color == 'Wild Draw Two':
                        game.players[game_turn.current_player].setCard(game.dumy_deck,2)
                        del game.players[game_turn.current_player].hand[index]
                        break
                    break
                elif flag == 4:
                    continue
            else:
                game.players[game_turn.current_player].setCard(game.dumy_deck)
                game_turn.next_direction()
            time.sleep(3)
            tmp =  rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager)
            player_card_button_list = tmp[0]
            computer_card_button_list = tmp[1]
            remain_time = 16
            start_time = time.time()


#################################################################
            #이벤트 큐(이벤트 감지)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()           
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stopGameLoop(screen,time_delta)
                    width,height,screen,gameBackground = gameUisetting()
                    ui_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")
                    #게임판 다시 그리기
                    ui = GameGui(ui_manager)
                    user_board = ui.userBoard("You")
                    main_board = ui.mainBoard()
                    computer_uiList = ui.computerBoard(computer_num)
                    #카드들 다시 그리기
                    #################

                    start_time = time.time()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if (event.ui_element == deck_button) and (game_turn.current_player == 0):
                    if len(game.players[0].hand) <= 12:
                        game.pop_from_dumy(game_turn.current_player)
                        color = game.players[0].hand[-1].color
                        value = game.players[0].hand[-1].value
                        card_button = cardUi.cardUI(card_manager,color,value,len(game.players[0].hand)-1,False,len(game.players[0].hand)+1)
                        player_card_button_list.append(card_button)
                        #시간초 리셋하고 턴 넘기기
                        remain_time = 16
                        game_turn.next_direction()
                    else:
                        print("can not draw") 
                    
                for i, player_card_button in enumerate(player_card_button_list):
                    if (event.ui_element == player_card_button) and (game_turn.current_player == 0):
                        card = game.players[0].hand[i]
                        flag = game.players[game_turn.current_player].canPlay(card,game.discard_deck)
                        if flag == 1:
                            if card.value in ['1','2','3','4','5','6','7','8','9','0']:
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.next_direction()
                            elif card.value == 'Skip':
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.skip_direction()
                            elif card.value == 'Reverse':
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.reverse_direction()
                                game_turn.next_direction()
                            elif card.value == 'Draw Four':
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.next_direction()
                                game.players[game_turn.current_player].setCard(game.dumy_deck,4)
                            elif card.value == 'Draw Two':
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.next_direction()
                                game.players[game_turn.current_player].setCard(game.dumy_deck,2)
                        elif flag == 2:
                            game.add_to_discard(card)
                            del game.players[game_turn.current_player].hand[i]
                            game_turn.next_direction()
                        elif flag == 3:
                            #와일드 카드의 value를 자신이 가장 많이 들고 있는 색의 색으로 바꿈
                            dic = {'Blue':0, 'Green':0, 'Red':0, 'Yellow':0}
                            for card in  game.players[game_turn.current_player].hand:
                                if card.color in dic:
                                    dic[card.color] += 1
                            print(card)        
                            card.value = max(dic, key=dic.get)
                            print(card)
                            game.add_to_discard(card)
                            game_turn.next_direction()
                            if card.color == 'Wild Draw Four':
                                game.players[game_turn.current_player].setCard(game.dumy_deck,4)
                            elif card.color == 'Wild Draw Two':
                                game.players[game_turn.current_player].setCard(game.dumy_deck,2)
                            del game.players[game_turn.current_player].hand[i]
                        elif flag == 4:
                            print("can not play a card")
                            continue

                        tmp =  rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager)
                        player_card_button_list = tmp[0]
                        computer_card_button_list = tmp[1]
                        remain_time = 16

            card_manager.process_events(event)
            ui_manager.process_events(event)


        
        #Player 0초 될때까지 카드 선택 안하면 카드 한 장 먹고 턴 넘김
        if (remain_time < 1) and (game_turn.current_player==0) and(len(game.players[0].hand)<=12) :
            game.pop_from_dumy(game_turn.current_player)
            color = game.players[0].hand[-1].color
            value = game.players[0].hand[-1].value
            card_button = cardUi.cardUI(card_manager,color,value,len(game.players[0].hand)-1,False,len(game.players[0].hand)+1)
            player_card_button_list.append(card_button)
            #시간초 리셋하고 턴 넘기기
            remain_time = 16
            game_turn.next_direction()

        
        #시간 타이머 작동

        if game_turn.current_player == 0:
            tmp = ui.timer(main_board,remain_time,start_time,game_turn)
            remain_time = tmp[0]
            start_time = tmp[1]
            time_label = tmp[2]

        #ui메소드 호출
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
            

def nextTurn(currentTurn,reverse,Player_list):
    
    if reverse:
        currentTurn -= 1
        if currentTurn == -1:
            currentTurn = len(Player_list)-1
    else:
        currentTurn += 1
        currentTurn % len(Player_list)
    return currentTurn 

def rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager):

    #플레이어 카드 버튼 지우기
    for i in range(len(player_card_button_list)):
        player_card_button_list[i].kill()

    player_card_button_list.clear()
    
    #플레이어 카드 버튼 다시 그리기
    for i,card in enumerate(game.players[0].hand):
        color = card.color
        value = card.value
        player_card_button_list.append(cardUi.cardUI(card_manager,color,value,i,False,i+1))
    
    #컴퓨터 카드 버튼 지우기
    for i in range(len(game.players)-1):
        while computer_card_button_list[i]:
            computer_card_button_list[i][-1].kill()
            del computer_card_button_list[i][-1]
       

    #컴퓨타 카드 버튼 다시 그리기
    computer_card_button_list = [ [] for i in range(len(game.players)-1)]
    
    for i in range(len(game.players)-1):
        for j in range(len(game.players[i+1].hand)):
            computer_card_button_list[i].append(cardUi.computerCardUi(card_manager,i,j))

    #discard 다시 그리기
    color = game.discard_deck.cards[-1].color
    value = game.discard_deck.cards[-1].value
    cardUi.cardUI(card_manager,color,value,0,True,1)
    
    return (player_card_button_list,computer_card_button_list)
    

gameUiLoop(3)
