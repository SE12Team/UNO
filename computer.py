import random
from Player import Player 

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
    '''
    computer가 선택할 카드를 결정
    Parameter: discard_pile -> list, deck -> list
    Return: tuple (index, color, value), None
    '''
    def make_decision(self, color, value, deck):
        matching_card = self.get_matching_card(color, value)
        # 매칭되는 카드가 없으면 None 반환
        if not matching_card:
            self.setCard(deck) # 덱에서 카드를 가져와 추가
            return None
        # 무작위로 카드를 선택하여 플레이 
        decision_card = random.choice(matching_card)
        self.hand.remove(decision_card)
        return decision_card

    '''
    현재 discard_pile의 맨 위 카드와 매칭되는 카드 목록을 반환 
    Parameter: top_card -> string
    Return: list
    '''
    def get_matching_card(self, color, value):
        matching_card = []
        for card in self.hand:
            if card.color == color or card.value == value or card.color == "Wild":
                matching_card.append(card)
        return matching_card

    # '''
    # computer의 손에서 선택한 카드를 제거
    # Parameter: card -> string
    # Return: None
    # '''
    # def paly_card(self, card):
    #     self.hand.remove(card)

    '''
    콤보를 사용하여 카드 플레이 
    Parameter: discard_pile -> list, deck -> list, color -> string, value -> string
    Return: None
    '''
    def playCombo(self, deck, color, value):
        combo_cards = [] # 콤보에 사용될 카드들을 담을 리스트
        matching_card = self.get_matching_card(color, value) # 현재 매칭되는 카드들 가져오기
        
        # 매칭되는 카드가 없으면 덱에서 카드를 가져와 추가
        if not matching_card:
            self.setCard(deck)
            return None
        
         # 현재 매칭되는 카드들 중에서 기술 카드와 숫자 카드를 분리하여 combo_cards 리스트에 추가
        for card in matching_card:
            if card.value in ['Reverse', 'Skip']:
                combo_cards.append(card)
            elif card.value.isnumeric(): # 숫자 카드를 뒤쪽에 배치 
                combo_cards.append(card)
        
        # 콤보 기술을 사용할 수 있는 경우
        if len(combo_cards) >= 2:
            # 무작위로 2장의 기술카드를 선택하여 플레이
            combo = random.sample(combo_cards, 2)
            for card in combo:
                self.playCard(self.hand.index(card), color, value)
            return combo
        else:
            return None

