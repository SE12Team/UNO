import pygame
import random
from Deck import Deck
from Player import Player
from computer import Computer

class Turn:
    def __init__(self, players_num):
        # players 리스트의 첫 번째 인자가 항상 먼저 시작
        self.randomTurn = 0
        self.players_num = players_num
        self.current_player = 0
        self.direction = 1

    def next_direction(self):
        # 다음 플레이어로 턴을 넘김
        index = self.current_player
        index = (index + self.direction) % self.players_num
        self.current_player = index
        self.randomTurn += 1
        return index

    def skip_direction(self):
        # 한 턴 건너뛰기
        index = self.current_player
        index = ((index + 1) + self.direction) % self.players_num
        self.current_player = index
        return index

    def reverse_direction(self):
        # 턴 방향을 반대로 바꿈
        self.direction *= -1

class Game:
    def __init__(self, players):
        self.dumy_deck = Deck() # 처음 생성되는 카드 리스트들 모인 곳
        self.discard_deck = Deck()
        self.discard_deck.reset() # 버려진 카드들 모이는 곳
        self.color = ''
        self.players = players
        self.winner = self.players[0]
        self.say_uno = False

    # 덱 생성 및 카드 분배
    def distrib_card(self, card_num,computer_game_mode,player_num):
        self.dumy_deck.shuffle()
        
        for player in self.players:
            if "mode A" in computer_game_mode: 
                self.dumy_deck = player.setCard(self.dumy_deck, player_num,card_num,stage = 'A')
            elif 'mode B' in computer_game_mode:
                print("mode B@")
                self.dumy_deck = player.setCard( self.dumy_deck,player_num, card_num,stage = 'B')
            else:
                self.dumy_deck = player.setCard( self.dumy_deck,player_num, card_num)

    def show_winner(self):
        print(self.winner, " wins!")

    def is_game_over(self):
        is_end = False
        for player in self.players:
            if len(player.getHand()) == 0:
                self.winner = player
                self.show_winner()
                is_end = True
        return is_end

    # discard_deck에 카드 추가
    def add_to_discard(self, card):
        self.discard_deck.addCard(card)
    
    # dumy_deck에서 카드 가져오기
    def pop_from_dumy(self, current_player, num=1):
        self.dumy_deck = current_player.setCard(self.dumy_deck, num)

    # 우노 판별
    # 플레이어 중 누군가 카드 2장 남았을 시 우노 외치기 가능
    def can_press_uno(self, player):
        can_press = False
        if len(player.hand) == 2:
            can_press = True
        return can_press

    # 유저 플레이어가 우노 외치기
    def press_uno_by_user(self, player, current_player):
        if self.can_press_uno(current_player):
            required_player = current_player
            for selected_player in self.players:
                if len(selected_player.hand) == 2:
                    required_player = selected_player
            if (required_player != player) and not self.say_uno:
                # 다른 플레이어 덱에 카드 2장이 남은 경우
                self.pop_from_dumy(required_player, 1)
                self.say_uno = True
            print(f"{player.name} said UNO!")
            print(required_player.hand)
        else:
            print("UNO cannot be said at this time.")
    
    # 컴퓨터 플레이어가 우노 외치기
    def press_uno_by_computer(self, current_player):
        random_computer = random.randint(1, len(self.players)-1)
        self.press_uno_by_user(self.players[random_computer], current_player)

    
    # self.say_uno 값에 따라 턴 당 누군가 먼저 우노를 외쳤으면 그 다음에는 우노를 외치지 못하도록 막기 때문에, 매 턴마다 이 함수를 불러 self.say_uno = False 로 만들어줘야 합니다.
    def reset_say_uno(self):
        self.say_uno = False
