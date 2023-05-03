import pygame
import pygame_gui
import setting
import time

def cardUI(card_manager,color,value,now_card_num,discard_card_flag,str_height):
        tmp = 0
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        width_val = 0.04
        width_interval = 0.05
        height_val = 0.716
        if discard_card_flag == True:
            width_val = 0.45
            height_val = 0.2166
        if color == 'Blue':
            if value == '0':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_0"
                    )
            elif value == '1':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_1"
                    )
            elif value == '2':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_2"
                    )
            elif value == '3':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_3"
                    )
            elif value == '4':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_4"
                    )
            elif value == '5':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_5"
                    )
            elif value == '6':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_6"
                    )
            elif value == '7':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_7"
                    )
            elif value == '8':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_8"
                    )
            elif value == '9':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_9"
                    )
            elif value == "Skip":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_Skip"
                    )
            elif value == "Reverse":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_Reverse"
                    )
            elif value == "Draw Two":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_Draw_Two"
                    )
            elif value == "Draw Four":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Blue_Draw_Four"
                    )
        elif color == "Green":
            if value == '0':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_0"
                    )
            elif value == '1':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_1"
                    )
            elif value == '2':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_2"
                    )
            elif value == '3':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_3"
                    )
            elif value == '4':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_4"
                    )
            elif value == '5':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_5"
                    )
            elif value == '6':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_6"
                    )
            elif value == '7':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_7"
                    )
            elif value == '8':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_8"
                    )
            elif value == '9':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_9"
                    )
            elif value == "Skip":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_Skip"
                    )
            elif value == "Reverse":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_Reverse"
                    )
            elif value == "Draw Two":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_Draw_Two"
                    )
            elif value == "Draw Four":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Green_Draw_Four"
                    )
        elif color == "Red":
            if value == '0':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_0"
                    )
            elif value == '1':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_1"
                    )
            elif value == '2':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_2"
                    )
            elif value == '3':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_3"
                    )
            elif value == '4':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_4"
                    )
            elif value == '5':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_5"
                    )
            elif value == '6':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_6"
                    )
            elif value == '7':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_7"
                    )
            elif value == '8':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_8"
                    )
            elif value == '9':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_9"
                    )
            elif value == "Skip":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_Skip"
                    )
            elif value == "Reverse":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_Reverse"
                    )
            elif value == "Draw Two":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_Draw_Two"
                    )
            elif value == "Draw Four":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Red_Draw_Four"
                    )
        elif color == "Yellow":
            if value == '0':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_0"
                    )
            elif value == '1':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_1"
                    )
            elif value == '2':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_2"
                    )
            elif value == '3':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_3"
                    )
            elif value == '4':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_4"
                    )
            elif value == '5':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_5"
                    )
            elif value == '6':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_6"
                    )
            elif value == '7':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_7"
                    )
            elif value == '8':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_8"
                    )
            elif value == '9':
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_9"
                    )
            elif value == "Skip":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_Skip"
                    )
            elif value == "Reverse":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_Reverse"
                    )
            elif value == "Draw Two":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_Draw_Two"
                    )
            elif value == "Draw Four":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Yellow_Draw_Four"
                    )
        elif color == "Wild":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Wild_Any"
                )
        elif color == "Wild Draw Four":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Wild_Draw_Four_Any"
                )
        elif color == "Wild Draw Two":
                tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((int(width*width_val)+int(width*width_interval*now_card_num), int(height*height_val)), (int(width*0.1175), int(height*0.235))),
                        text="",
                        manager=card_manager,
                        starting_height = str_height,
                        object_id="#Wild_Draw_Two_Any"
                )
        return tmp

def DeckUi(card_manager):
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        Deck_button = pygame_gui.elements.UIButton(
                                relative_rect=pygame.Rect((int(width*0.225),int(height*0.2166)),(int(width*0.1175), int(height*0.235))),
                                text="",
                                manager=card_manager,
                                object_id="#Deck"
                        )
        return Deck_button

def computerCardUi(computer_card_manager,number_of_computer,card_num):
        width = pygame.display.get_surface().get_width()
        height = pygame.display.get_surface().get_height()
        tmp = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect(int(width*0.775)+int(width*0.0125*card_num),int(height*0.0833)+int(height*0.2*number_of_computer),int(width*0.05),int(height*0.1)),
                        text="",
                        starting_height=card_num,
                        manager=computer_card_manager,
                        object_id="#computer_card"
                )

        return tmp



                    
