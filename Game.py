import pygame
from Deck import Deck
from Player import Player
from computer import Computer

class Turn:
    def __init__(self, players_num):
        # players 리스트의 첫 번째 인자가 항상 먼저 시작
        self.players_num = players_num
        self.current_player = 0
        self.direction = 1

    def next_direction(self):
        # 다음 플레이어로 턴을 넘김
        index = self.current_player
        index = (index + self.direction) % self.players_num
        self.current_player = index
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

    # 덱 생성 및 카드 분배
    def distrib_card(self, card_num):
        self.dumy_deck.shuffle()
        for player in self.players:
            self.dumy_deck = player.setCard(self.dumy_deck, card_num)

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
    def pop_from_dumy(self,current_turn,iter_num=1):
        for _ in range(iter_num):
            self.players[current_turn].hand.append(self.dumy_deck.draw_card())
    
