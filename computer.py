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
    def make_decision(self, discard_pile, deck):
        matching_card = self.get_matching_card(discard_pile[-1])
        # 매칭되는 카드가 없으면 None 반환
        if not matching_card:
            self.addCard(deck) # 덱에서 카드를 가져와 추가
            return None
        # 무작위로 카드를 선택하여 플레이 
        decision_card = random.choice(matching_card)
        return decision_card

    '''
    현재 discard_pile의 맨 위 카드와 매칭되는 카드 목록을 반환 
    Parameter: top_card -> string
    Return: list
    '''
    def get_matching_card(self, top_card):
        matching_card = []
        for card in self.hand:
            if card.color == top_card.color or card.value == top_card.value or card.value == "Wild":
                matching_card.append(card)
        return matching_card

    '''
    computer의 손에서 선택한 카드를 제거
    Parameter: card -> string
    Return: None
    '''
    def paly_card(self, card):
        self.hand.remove(card)

