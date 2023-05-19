import pygame
import pygame_gui
import setting
from UI import *
import setting_menu
import cardUi
import Game
import Player
import computer
import random
import sys
import select
import achievement
import datetime
import configparser
import achievement_list

pygame.init()

def gameUisetting():
    #창 가로세로 변수지정  
    width = pygame.display.get_surface().get_width()

    height = pygame.display.get_surface().get_height()

    #스크린, 배경화면 지정 (문제 생기면 이거 원래대로 바꿔보기)
    screen = pygame.display.set_mode((width,height))
    gameBackground = pygame.image.load("data/images/board.png")
    
    return (width,height,screen,gameBackground)



def gameUiLoop(computer_num,player_name,computer_game_mode,game_mode): 
    width,height,screen,gameBackground = gameUisetting()
    print(computer_game_mode)

    #pygame_gui UIManager 지정
    ui_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")
    card_manager = pygame_gui.UIManager((width, height), "data/themes/card_theme.json")
    computer_card_manager = pygame_gui.UIManager((width, height), "data/themes/computerCard_theme.json")
    
    #UI파일의 GameGui클래스 인스턴스 생성
    ui = GameGui(ui_manager)

    #Player파일의 Player클래스의 인스턴스 생성
    players = []
    players.append(Player.Player(player_name))

    #Computer 인스턴스 생성
    for i in range(computer_num):
        players.append(computer.Computer(f"computer{i+1}"))

    #Gamek파일의 Game클래스의 인스턴스 생성
    game = Game.Game(players)

    #플레이어, 컴퓨터에게 카드 5장씩 분배
    game.distrib_card(5,computer_game_mode,computer_num+1)

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

    #현재 색 버튼 객체 생성
    nowColorButton = ui.nowColorButton(game.discard_deck.cards[-1])
    

    #버튼 객체(플레이어랑 컴퓨터)를 담은 리스트 만들기 and 그리기
    player_card_button_list = []
    computer_card_button_list = [ [] for i in range(computer_num)]
    for i, card in enumerate(game.players[0].hand):
        color = card.color
        value = card.value
        player_card_button_list.append(cardUi.cardUI(card_manager,color,value,i,False,i+1))
  
    for i in range(computer_num):
        for j in range(len(game.players[i+1].hand)):
            computer_card_button_list[i].append(cardUi.computerCardUi(computer_card_manager,i,j))


    #게임판 Ui 그려주는 메소드 실행
    user_board = ui.userBoard(player_name)
    main_board = ui.mainBoard()
    computer_uiList = ui.computerBoard(computer_num)
    if "mode B" not in computer_game_mode:
        deck_button = cardUi.DeckUi(card_manager)
    uno_button = ui.unoButton(main_board)
    

    #플레이어 리스트 생성(current Turn 표시하기 위해), 인덱스 변수 생성
    Player_list = [player_name]
    for i in range(computer_num):
        Player_list.append(f"Computer {i+1}")

    #Game파일 Turn클래스의 인스턴스 생성
    game_turn = Game.Turn(computer_num+1)   

    #Game 메인 루프 실행 전 변수 선언
    if "mode D" in computer_game_mode:
        remain_time = 11
    else:
        remain_time = 16
    clock = pygame.time.Clock()
    running = True
    time_delta = clock.tick(60)/1000.0
    colorSelectButton= False

    # 업적 관련 플래그 변수 선언
    draw_skill_flag = False

    def set_achiev(player_index, achiev_index, check_flag):
        if check_flag:
            # 유저가 조건을 만족하는 경우
            if player_index == 0:
                if not achievement.get_state(achiev_index):
                    date = datetime.datetime.now()
                    achievement.set_state(achiev_index, date)
        else:
            # 다른 플레이어가 조건을 만족하는 경우
            if player_index != 0:
                if not achievement.get_state(achiev_index):
                    date = datetime.datetime.now()
                    achievement.set_state(achiev_index, date)

    #타이머시작
    start_time = time.time()
    #################################
    while running:
        '''
        if game.can_press_uno(game.players[game_turn.current_player]):
            current_text = ui.rendering_currentTurn(game.players[game_turn.current_player].name, main_board)
            ui_manager.update(time_delta)
            ui_manager.draw_ui(screen)
            pygame.display.flip()
            wait_and_say_uno(game,uno_button,game_turn,ui_manager,time_delta,screen)
            nowColorButton.kill()
            uno_button.kill()
            current_text.kill()
            tmp =  rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager,ui,main_board,computer_card_manager)
            player_card_button_list = tmp[0]
            computer_card_button_list = tmp[1]
            nowColorButton = tmp[2]
            uno_button = tmp[3]
        '''
        #5턴 마다 색깔 무작위
        if ('mode C' in computer_game_mode) and (game_turn.randomTurn == 5):
            game_turn.randomTurn = 0
            nowColorButton.kill()
            randomColor = random.choice(['Red', 'Green', 'Yellow', 'Blue'])
            game.discard_deck.cards[-1].color = randomColor
            nowColorButton = ui.nowColorButton(game.discard_deck.cards[-1])
        #현재 턴 label 글자 랜더링
        current_text = ui.rendering_currentTurn(game.players[game_turn.current_player].name, main_board)

        pygame.display.flip() # 화면을 업데이트
        #컴퓨터 턴 동작
        if game_turn.current_player != 0:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        stopGameLoop(screen,time_delta)

                        width,height,screen,gameBackground = gameUisetting()
                        card_manager = pygame_gui.UIManager((width, height), "data/themes/card_theme.json")    
                        computer_card_manager = pygame_gui.UIManager((width, height), "data/themes/computerCard_theme.json")
                        ui_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")
                        #게임판 다시 그리기
                        ui = GameGui(ui_manager)
                        user_board = ui.userBoard("You")
                        main_board = ui.mainBoard()
                        computer_uiList = ui.computerBoard(computer_num)
                        current_text.kill()
                        current_text = ui.rendering_currentTurn(game.players[game_turn.current_player].name, main_board)
                        #카드들 다시 그리기
                        tmp =  rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager,ui,main_board,computer_card_manager)
                        player_card_button_list = tmp[0]
                        computer_card_button_list = tmp[1]
                        nowColorButton = tmp[2]
                        uno_button = tmp[3]

                        start_time = time.time()          

            
           
            #제한시간은 플레이어에게만 표시되도록
            time_label.kill()
            ui_manager.update(time_delta)
            card_manager.update(time_delta)
            computer_card_manager.update(time_delta)
            screen.blit(pygame.transform.scale(gameBackground,(pygame.Surface.get_width(screen),pygame.Surface.get_height(screen))),(0,0))
            ui_manager.draw_ui(screen)
            card_manager.draw_ui(screen)
            computer_card_manager.draw_ui(screen)
            pygame.display.flip() # 화면을 업데이트

            print(f"{game_turn.current_player} : {game.players[game_turn.current_player].hand}")             
            ifWin_player = game_turn.current_player
            ####잠시 3초 동안 정지#########################    
            
            limit_time = time.time() + 3
            while time.time() < limit_time:
                 for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit() 
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            stopGameLoop(screen,time_delta)

                            width,height,screen,gameBackground = gameUisetting()
                            card_manager = pygame_gui.UIManager((width, height), "data/themes/card_theme.json")    
                            computer_card_manager = pygame_gui.UIManager((width, height), "data/themes/computerCard_theme.json")
                            ui_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")
                            #게임판 다시 그리기
                            ui = GameGui(ui_manager)
                            user_board = ui.userBoard("You")
                            main_board = ui.mainBoard()
                            computer_uiList = ui.computerBoard(computer_num)
                            current_text.kill()
                            current_text = ui.rendering_currentTurn(game.players[game_turn.current_player].name, main_board)
                            #카드들 다시 그리기
                            if "mode B" not in computer_game_mode:
                                deck_button = cardUi.DeckUi(card_manager)
                            tmp =  rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager,ui,main_board,computer_card_manager)
                            player_card_button_list = tmp[0]
                            computer_card_button_list = tmp[1]
                            nowColorButton = tmp[2]
                            uno_button = tmp[3]

                            start_time = time.time()
                            ui_manager.update(time_delta)
                            card_manager.update(time_delta)
                            computer_card_manager.update(time_delta)
                            screen.blit(pygame.transform.scale(gameBackground,(pygame.Surface.get_width(screen),pygame.Surface.get_height(screen))),(0,0))
                            ui_manager.draw_ui(screen)
                            card_manager.draw_ui(screen)
                            computer_card_manager.draw_ui(screen)
                            pygame.display.flip() # 화면을 업데이트
                            
        #########################################################

            for index in range(len(game.players[game_turn.current_player].hand[:])):
                ####pygame.time.delay(300)
                card = game.players[game_turn.current_player].hand[index]
                
                flag = game.players[game_turn.current_player].canPlay(card,game.discard_deck)
                if flag == 1:
                    print(card)
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
                        if "mode B" not in computer_game_mode:
                            game.players[game_turn.current_player].setCard(game.dumy_deck,4)
                        break
                    elif card.value == 'Draw Two':
                        game.add_to_discard(card)
                        del game.players[game_turn.current_player].hand[index]
                        game_turn.next_direction()
                        if "mode B" not in computer_game_mode:
                            game.players[game_turn.current_player].setCard(game.dumy_deck,2)
                        break
                elif flag == 2:
                    print(card)
                    game.add_to_discard(card)
                    del game.players[game_turn.current_player].hand[index]
                    break
                elif flag == 3:
                    print(card)
                    dic = {'Blue':0, 'Green':0, 'Red':0, 'Yellow':0}
 
                    for tmp in  game.players[game_turn.current_player].hand:
                        if tmp.color in dic:
                            dic[tmp.color] += 1
    
                    card.value = max(dic, key=dic.get)

                    game.add_to_discard(card)
                    del game.players[game_turn.current_player].hand[index]
                    game_turn.next_direction()
                    if card.color == 'Wild': 
                        pass
                    elif card.color == 'Wild Draw Four':
                        if "mode B" not in computer_game_mode:
                            game.players[game_turn.current_player].setCard(game.dumy_deck,4)
                        break
                    elif card.color == 'Wild Draw Two':
                        if "mode B" not in computer_game_mode:
                            game.players[game_turn.current_player].setCard(game.dumy_deck,2)
  
                        break
                    break
                elif flag == 4:
                    continue
            else:
                game.players[game_turn.current_player].setCard(game.dumy_deck)
                game_turn.next_direction()
                
                print(f"{game_turn.current_player} : {len(game.players[game_turn.current_player].hand)}")
            if len(game.players[ifWin_player].hand) == 0:
                # 패배 업적 달성
                set_achiev(ifWin_player, 1, False)
                ui.winner(game_turn,game,ifWin_player,screen,time_delta)
                running = False
                break

            nowColorButton.kill()
            uno_button.kill()
            tmp =  rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager,ui,main_board,computer_card_manager)
            player_card_button_list = tmp[0]
            computer_card_button_list = tmp[1]
            nowColorButton = tmp[2]
            uno_button = tmp[3]
            if "mode D" in computer_game_mode:
                remain_time = 11
            else:
                remain_time = 16
            start_time = time.time()
            current_text.kill()
            current_text = ui.rendering_currentTurn(game.players[game_turn.current_player].name, main_board)
            game.reset_say_uno()

        
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
                    computer_card_manager = pygame_gui.UIManager((width, height), "data/themes/computerCard_theme.json")
                    card_manager =  pygame_gui.UIManager((width, height), "data/themes/card_theme.json")
                    #게임판 다시 그리기
                    ui = GameGui(ui_manager)
                    user_board = ui.userBoard("You")
                    main_board = ui.mainBoard()
                    computer_uiList = ui.computerBoard(computer_num)
                    current_text.kill()
                    current_text = ui.rendering_currentTurn(game.players[game_turn.current_player].name, main_board)
                    #카드들 다시 그리기
                    if "mode B" not in computer_game_mode:
                        deck_button = cardUi.DeckUi(card_manager)
                    tmp =  rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager,ui,main_board,computer_card_manager)
                    player_card_button_list = tmp[0]
                    computer_card_button_list = tmp[1]
                    nowColorButton = tmp[2]
                    uno_button = tmp[3]

                    start_time = time.time()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if ("mode B" not in computer_game_mode) and (event.ui_element == deck_button) and (game_turn.current_player == 0):
                    game.pop_from_dumy(game.players[game_turn.current_player])
                    color = game.players[0].hand[-1].color
                    value = game.players[0].hand[-1].value
                    card_button = cardUi.cardUI(card_manager,color,value,len(game.players[0].hand)-1,False,len(game.players[0].hand)+1)
                    player_card_button_list.append(card_button)
                    #시간초 리셋하고 턴 넘기기
                    if "mode D" in computer_game_mode:
                        remain_time = 11
                    else:
                        remain_time = 16
                    game_turn.next_direction()
                    game.reset_say_uno()
                    colorSelectButton = False
                    try:
                        RedColor.kill()
                        BlueColor.kill()
                        GreenColor.kill()
                        YellowColor.kill()
                    except:
                        pass
                try:
                    if event.ui_element == RedColor:
                        colorValue ="Red"

                    elif event.ui_element == BlueColor:
                        colorValue ="Blue"

                    elif event.ui_element == YellowColor:
                        colorValue ="Yellow"

                    elif event.ui_element == GreenColor:
                        colorValue ="Green"
                except:
                    pass
                    
                for i, player_card_button in enumerate(player_card_button_list[:]):
                    if (event.ui_element == player_card_button) and (game_turn.current_player == 0):
                        ###여기가 카드 눌렀을 때 생기는 곳
                        card = game.players[0].hand[i]

                        if colorSelectButton:
                            flag = 3
                        else:
                            flag = game.players[0].canPlay(card,game.discard_deck)
                        if flag == 1:
                            if card.value in ['1','2','3','4','5','6','7','8','9','0']:
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.next_direction()
                                game.reset_say_uno()
                            elif card.value == 'Skip':
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.skip_direction()
                                game.reset_say_uno()
                            elif card.value == 'Reverse':
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.reverse_direction()
                                game_turn.next_direction()
                                game.reset_say_uno()
                            elif card.value == 'Draw Four':
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.next_direction()
                                game.reset_say_uno()
                                if "mode B" not in computer_game_mode:
                                    game.players[game_turn.current_player].setCard(deck = game.dumy_deck,num = 4)
                            elif card.value == 'Draw Two':
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.next_direction()
                                game.reset_say_uno()
                                if "mode B" not in computer_game_mode:
                                    game.players[game_turn.current_player].setCard(deck = game.dumy_deck,num = 2)
                        elif flag == 2:
                            game.add_to_discard(card)
                            del game.players[game_turn.current_player].hand[i]
                            game_turn.next_direction()
                            game.reset_say_uno()
                        elif flag == 3:
                            if colorSelectButton:
                                card.value = colorValue
                                game.add_to_discard(card)
                                del game.players[game_turn.current_player].hand[i]
                                game_turn.next_direction()
                                game.reset_say_uno()
                                colorSelectButton = False
                                RedColor.kill()
                                BlueColor.kill()
                                GreenColor.kill()
                                YellowColor.kill()

                                if card.color == 'Wild Draw Four':
                                    if "mode B" not in computer_game_mode:
                                        game.players[game_turn.current_player].setCard(deck = game.dumy_deck, num = 4)
                                elif card.color == 'Wild Draw Two':
                                    if "mode B" not in computer_game_mode:
                                        game.players[game_turn.current_player].setCard(deck = game.dumy_deck, num = 2)
                            else:
                                RedColor,BlueColor,YellowColor,GreenColor = selectColor(ui_manager,game,game_turn,card_manager,player_card_button_list)
                                colorSelectButton = True


                                   



                            #선택한 색을 wild카드의 value로 지정


                        elif flag == 4:
                            print("can not play a card")
                            continue
                        
                        nowColorButton.kill()
                        uno_button.kill()
                        tmp =  rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager,ui,main_board,computer_card_manager)
                        player_card_button_list = tmp[0]
                        computer_card_button_list = tmp[1]
                        nowColorButton = tmp[2]
                        uno_button = tmp[3]
                        if "mode D" in computer_game_mode:
                            remain_time = 11
                        else:
                            remain_time = 16

            card_manager.process_events(event)
            ui_manager.process_events(event)
        #이겼을 때
        if len(game.players[0].hand) ==0:
            print('qqqq')
            if game_mode != 'Single':
                config = configparser.ConfigParser()
                config.read('storymode.ini')
                if game_mode == 'mode A':
                    config.set('StoryMode','mode B','1')
                elif game_mode == 'mode B':
                    config.set('StoryMode','mode C','1')
                elif game_mode == 'mode C':    
                    config.set('StoryMode','mode D','1')
                
                with open('storymode.ini','w') as configfile:
                    config.write(configfile)
                print('eeeee')


            ui.winner(game_turn,game,0,screen,time_delta)
            tmp = True
            while tmp:
                #print('ddd')
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()           
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            print('llllllllllllll')
                            tmp = False
            running = False
            print('cccc')
            return

        #Player 0초 될때까지 카드 선택 안하면 카드 한 장 먹고 턴 넘김
        if (remain_time < 1) and (game_turn.current_player==0):
            if "mode B" not in computer_game_mode:
                game.pop_from_dumy(game.players[game_turn.current_player])
                color = game.players[0].hand[-1].color
                value = game.players[0].hand[-1].value
                card_button = cardUi.cardUI(card_manager,color,value,len(game.players[0].hand)-1,False,len(game.players[0].hand)+1)
                player_card_button_list.append(card_button)
                #시간초 리셋하고 턴 넘기기
                if "mode D" in computer_game_mode:
                    remain_time = 11
                else:
                    remain_time = 16
            game_turn.next_direction()
            game.reset_say_uno()
            colorSelectButton = False
            try:
                RedColor.kill()
                BlueColor.kill()
                GreenColor.kill()
                YellowColor.kill()
            except:
                pass            
          

        
        #시간 타이머 작동

        if game_turn.current_player == 0:
            tmp = ui.timer(main_board,remain_time,start_time,game_turn)
            remain_time = tmp[0]
            start_time = tmp[1]
            time_label = tmp[2]

        #ui메소드 호출
        ui_manager.update(time_delta)
        card_manager.update(time_delta)
        computer_card_manager.update(time_delta)
        screen.blit(pygame.transform.scale(gameBackground,(pygame.Surface.get_width(screen),pygame.Surface.get_height(screen))),(0,0))
        ui_manager.draw_ui(screen)
        card_manager.draw_ui(screen)
        computer_card_manager.draw_ui(screen)
        pygame.display.flip() # 화면을 업데이트
        #타이머,턴 랜더링 삭제
        time_label.kill()
        current_text.kill()
        

        # 턴마다 모든 플레이어의 덱 당 카드 수를 계산하여 컴퓨터가 우노를 외치는 함수입니다.
        # 매 턴 시작 시 이 함수를 부릅니다.
        # 이 함수 호출 뒤에는 game.reset_say_uno()가 호출되어야 합니다. (이 함수 설명은 Game.py 참조)
        # 유저가 우노 버튼을 누를 시에는 이 함수 말고 game.press_uno_by_user(player) < 이거 사용하시면 됩니다.
def wait_and_say_uno(game,uno_button,game_turn,ui_manager,time_delta,screen):
    wait_time = random.randrange(3000, 5000)
    limit_time = time.time() + (wait_time/1000)
    while time.time() < limit_time:

        for event in pygame.event.get():
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == uno_button:
                    game.press_uno_by_user(game.players[0],game.players[game_turn.current_player])
                    return
            ui_manager.process_events(event)
        
        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)
        
    game.press_uno_by_computer(game.players[game_turn.current_player])


def stopGameLoop(screen,time_delta):
    width = pygame.display.get_surface().get_width()
    height = pygame.display.get_surface().get_height()
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
    
    ac_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(int(width*0.325),int(height*0.5833),int(width*0.33125),int(height*0.0833)),
                                 text="Achievement",
                                 manager=esc_manager,
                                 starting_height = 2,
                                 object_id=ObjectID(class_id="@ESC_button")
                                 )
    esc_exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(int(width*0.325),int(height*0.6833),int(width*0.33125),int(height*0.0833)),
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
                    running = False
                    break
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == esc_setting_button:
                    print("setting")
                    setting_menu.get_menu(True, False, False)
                    return
                
                elif event.ui_element == esc_exit_button:
                    pygame.quit()

                elif event.ui_element == ac_button:
                    achievement_list.show_achievement(True)
                    return
                    

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

def rendering_every_cards_again(game,computer_card_button_list,player_card_button_list,card_manager,ui,main_board,computer_card_manager):

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
            computer_card_button_list[i].append(cardUi.computerCardUi(computer_card_manager,i,j))

    #discard 다시 그리기
    color = game.discard_deck.cards[-1].color
    value = game.discard_deck.cards[-1].value
    cardUi.cardUI(card_manager,color,value,0,True,1)
    
    #현재 색 다시 그리기
    nowColorButton = ui.nowColorButton(game.discard_deck.cards[-1])

    #우노버튼 다시 그리기
    uno_button = ui.unoButton(main_board)

    return (player_card_button_list,computer_card_button_list,nowColorButton,uno_button)

def selectColor(ui_manager,game,game_turn,card_manager,player_card_button_list):
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    RedColor = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(int(width*0.15)+int(width*0.125*0),int(height*0.48333),int(width*0.0625
                                                                                ),int(height*0.0833)),
                text="",
                manager=ui_manager,
                starting_height = 2,
                object_id="#Red"
        )
    BlueColor = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(int(width*0.15)+int(width*0.125*1),int(height*0.48333),int(width*0.0625
                                                                                ),int(height*0.0833)),
                text="",
                manager=ui_manager,
                starting_height = 2,
                object_id="#Blue"
        )

    YellowColor = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(int(width*0.15)+int(width*0.125*2),int(height*0.48333),int(width*0.0625
                                                                                ),int(height*0.0833)),
                text="",
                manager=ui_manager,
                starting_height = 2,
                object_id="#Yellow"
        )

    GreenColor = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(int(width*0.15)+int(width*0.125*3),int(height*0.48333),int(width*0.0625
                                                                                ),int(height*0.0833)),
                text="",
                manager=ui_manager,
                starting_height = 2,
                object_id="#Green"
        ) 
    return (RedColor,BlueColor,YellowColor,GreenColor)


gameUiLoop(2,"You",['mode C', 'Common', 'None', 'None', 'None'],'Single')  
