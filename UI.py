import pygame
import pygame_gui

import time
from pygame_gui.core import ObjectID
import json
import re
    
class GameGui:
    def __init__(self,ui_manager):
        self.ui_manager = ui_manager
        
    def computerBoard(self,computer_num):
        if computer_num > 5:
            computer_num = 5
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        computer_uiList = [0]*(computer_num+1)
        for i in range(computer_num):
            tmp = pygame_gui.elements.UIPanel(relative_rect=(int(width*0.7625),int(height*0.0083)+int(height*0.2)*i,int(width*0.23125),int(height*0.1918)),
                                                starting_layer_height=100,
                                                manager=self.ui_manager,
                                                object_id=ObjectID(class_id="@Computer_panels")
                                                )
            computer_uiList[i+1] = tmp

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(-5,0,100,30),
                                        text = f"computer{i+1}",
                                        manager = self.ui_manager,
                                        container = computer_uiList[i+1],
                                        object_id=ObjectID(class_id="@Computer_panerl_fonts")    
                                        )
            
        return computer_uiList
        
    def userBoard(self,userName):
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        #유저보드 panel 객체 생성
        user_board = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(0,int(height*0.59166),int(width*0.76),int(height*0.5)),
                                                starting_layer_height=1,
                                                manager=self.ui_manager,
                                                object_id=ObjectID(object_id="#UserBoard")
                                                )
        #플레이어 이름 글자 객체 생성
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0,-10,100,100),
                                        text = userName,
                                        manager = self.ui_manager,
                                        container = user_board,
                                        object_id=ObjectID(object_id="#UserName")    
                                        )
        
        return user_board
        

    def mainBoard(self):
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        #메인보드 panel 객체생성
        main_board = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(0,0,int(width*0.76),int(height*0.5933)),
                                                starting_layer_height=1,
                                                manager=self.ui_manager,
                                                object_id=ObjectID(object_id="#MainBoard")
                                                )
        return main_board

    def rendering_currentTurn(self,current_trun_text,main_board):  
        #현재 턴 글자 객체 생성

        current_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0,-10,400,100),
                                        text = f"Trun : {current_trun_text}",
                                        manager = self.ui_manager,
                                        container = main_board,
                                        object_id=ObjectID(object_id="#CurrentTurn")    
                                        )
        return current_text
        

    def timer(self,main_board,remain_time,start_time,game_turn):
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        end_time = time.time()
        remain_time = remain_time - (end_time-start_time)
        start_time = time.time()
        timer_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(int(width*0.4),-5,400,100),
                                        text = f"{int(remain_time)}second",
                                        manager = self.ui_manager,
                                        container = main_board,
                                        object_id=ObjectID(object_id="#Timertime")   
                                        )
        if remain_time <= 0:
            game_turn.next_direction()
            remain_time = 16
        return (remain_time,start_time,timer_label)
    
    

    def unoButton(self,main_board):
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        button_layout_rect = pygame.Rect(0, 0, int(width*0.125), int(height*0.1))
        button_layout_rect.bottomright = (-20, -20)
        uno_button =pygame_gui.elements.UIButton(
                            relative_rect=button_layout_rect,
                            text="Uno",
                            manager=self.ui_manager,
                            container=main_board,
                            object_id="#UnoButton",
                            anchors={'right': 'right',
                            'bottom': 'bottom'}
                    )
        return uno_button
    
    def nowColorButton(self,card):
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        now_color = 0
        if card.color in ['Wild', 'Wild Draw Four', 'Wild Draw Two']:
            color = card.value
        else:
            color = card.color

        if color == "Red":
            now_color = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.6375),int(height*0.2833),int(width*0.0625
                                                                                ),int(height*0.0833)),
                        text="",
                        manager=self.ui_manager,
                        starting_height = 2,
                        object_id="#Red"
                )
        elif color == "Blue":
            now_color = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.6375),int(height*0.2833),int(width*0.0625
                                                                                ),int(height*0.0833)),
                        text="",
                        manager=self.ui_manager,
                        starting_height = 2,
                        object_id="#Blue"
                )
        elif color == "Yellow":
            now_color = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.6375),int(height*0.2833),int(width*0.0625
                                                                                ),int(height*0.0833)),
                        text="",
                        manager=self.ui_manager,
                        starting_height = 2,
                        object_id="#Yellow"
                )
        elif color == "Green":
            now_color = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.6375),int(height*0.2833),int(width*0.0625
                                                                                ),int(height*0.0833)),
                        text="",
                        manager=self.ui_manager,
                        starting_height = 2,
                        object_id="#Green"
                )        
        return now_color
    
    def winner(self,game_turn,game,ifWin_player,screen,time_delta):
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        win_manager = pygame_gui.UIManager((width, height),"data/themes/UI_theme.json")
        win_panel = pygame_gui.elements.UIPanel(relative_rect = pygame.Rect((int(width*0.1875),int(height*0.25)),(int(width*0.625),int(height*0.5833))),
                                            starting_layer_height=1,
                                            manager = win_manager,
                                            object_id=ObjectID(object_id="#win_panel")
                                            )
        win_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(int(width*0.3),int(height*0.4),int(width*0.375),int(height*0.1666)),
                                        text = f"{game.players[ifWin_player].name} Win!!",
                                        manager = win_manager,
                                        object_id=ObjectID(object_id="#win_label")    
                                        )

        max_wait_time = 5000
        start_time = pygame.time.get_ticks()
        while True:
            win_manager.draw_ui(screen)
            win_manager.update(time_delta)
            pygame.display.flip()
            elapsed_time = pygame.time.get_ticks() - start_time

            if elapsed_time >= max_wait_time:

                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:                    
                        return
def updateJson():
    with open('./data/themes/card_theme.json','r') as f:
        info_json = json.load(f)
    
    with open('./data/themes/computerCard_theme.json','r') as cf:
        info_computer_json = json.load(cf)

    info_json = json.dumps(info_json) # dict to str
    info_computer_json = json.dumps(info_computer_json)

    width = pygame.display.get_surface().get_width()

    if width == 800:
        info_json = re.sub('data.images.[a-z]*','data.images.small',info_json)
        info_json = re.sub('0,0,[0-9]+,[0-9]+','0,0,94,141',info_json)
        info_computer_json = re.sub('data.images.[a-z]*','data.images.small',info_computer_json)
        info_computer_json = re.sub('0,0,[0-9]+,[0-9]+','0,0,40,60',info_computer_json)
    elif width == 1280:
        info_json = re.sub('data.images.[a-z]*','data.images.medium',info_json)
        info_json = re.sub('0,0,[0-9]+,[0-9]+','0,0,150,225',info_json)
        info_computer_json = re.sub('data.images.[a-z]*','data.images.medium',info_computer_json)
        info_computer_json = re.sub('0,0,[0-9]+,[0-9]+','0,0,64,96',info_computer_json)
    elif width == 1600:
        info_json = re.sub('data.images.[a-z]*','data.images.large',info_json)
        info_json = re.sub('0,0,[0-9]+,[0-9]+','0,0,188,282',info_json)
        info_computer_json = re.sub('data.images.[a-z]*','data.images.large',info_computer_json)
        info_computer_json = re.sub('0,0,[0-9]+,[0-9]+','0,0,80,120',info_computer_json)
    info_json = json.loads(info_json)
    info_computer_json = json.loads(info_computer_json)
        

    with open('./data/themes/card_theme.json','w') as f:
        json.dump(info_json,f)
         
    with open('./data/themes/computerCard_theme.json','w') as f:
        json.dump(info_computer_json,f)
         