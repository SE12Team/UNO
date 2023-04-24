import pygame
import setting
import random
from Card import Card

'''
    1. generate(self):
        usage:
            임의의 덱을 생성하여 self.cards 리스트에 저장함.
        parameter:
            none
        return:
            none

    2. shuffle(self):
        usage:
            카드 순서를 랜덤으로 섞음.
        parameter:
            none
        return:
            none

    3. draw_card(self):
        usage:
            덱의 맨 앞 카드를 냄.
        parameter:
            none
        return:
            덱의 맨 앞 카드

    4. reset(self):
        usage:
            덱의 카드를 전부 리셋함.
        parameter:
            none
        return:
            none

    5. count(self):
        usage:
            덱의 카드 갯수를 반환함.
        parameter:
            none
        return:
            덱의 카드 갯수

    6. deal(self, card_value, players):
        usage:
            카드를 일정 갯수만큼 플레이어에게 분배.
        parameter:
            1. card_value: 나눠줄 카드 갯수
            2. players: 분배 받을 프레이어 리스트
        return:
            none
'''

class DeckClass:
    def __init__(self):
        self.cards = []
        self.generate()
    
    def generate(self):
        colors = ['Red', 'Green', 'Yellow', 'Blue']
        values = [str(num) for num in range(0, 10)]
        skills = ['Skip', 'Reverse', 'Draw Two', 'Change'] # 플레이어 건너뛰기, 진행 방향 반전, 카드 2개 뽑기, 상대와 카드 변경
        wilds = ['Wild', 'Wild Draw Four', 'Wild Draw Two']
        
        # 모든 색상의 숫자 카드는 2개씩 생성
        for color in colors:
            for value in values:
                card = Card(color, value)
                for _ in range(2):
                    self.cards.append(card)
                    
            for skill in skills:
                card = Card(color, skill)
                for _ in range(2):
                    self.cards.append(card)
        
        # 와일드 카드 4개 생성
        for wild in wilds:
            for _ in range(4):
                card = Card(wild, 'Any')
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    # 덱의 맨 앞 카드 내기
    def draw_card(self):
        draw_se = pygame.mixer.Sound("../sound/se/draw.mp3")
        draw_se.set_volume(setting.get_music_se())
        draw_se.play() # 효과음 한 번 재생

        return self.cards.pop(0)

    def reset(self):
        self.cards = []
        self.generate()

    # 현재 덱의 카드 개수를 반환
    def count(self):
        return len(self.cards)
    
    def deal(self, card_value, players):
        # card_value 숫자만큼 players에게 전달
        for _ in range(card_value):
            for player in players:
                card = self.draw_card()
                # 플레이어 댁에 카드 추가
                # player.hand.add_card(card)