import pygame
import pygame_gui
import setting
import time
from pygame_gui.core import ObjectID
    
class GameGui:
    def __init__(self,ui_manager):
        self.ui_manager = ui_manager
        
    def computerBoard(self,computer_num):
        if computer_num > 5:
            computer_num = 5
        width = pygame.Surface.get_width(setting.screen)
        height = pygame.Surface.get_height(setting.screen)
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
        width = pygame.Surface.get_width(setting.screen)
        height = pygame.Surface.get_height(setting.screen)
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
        width = pygame.Surface.get_width(setting.screen)
        height = pygame.Surface.get_height(setting.screen)
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
        width = pygame.Surface.get_width(setting.screen)
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
        width = pygame.Surface.get_width(setting.screen)
        height = pygame.Surface.get_height(setting.screen)
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