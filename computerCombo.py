import random
from computer import Computer

class comCombo(Computer):
    def __init__(self, name, hand):
        super().__init__(name, hand)

    '''
    콤보를 사용하여 카드 플레이 
    Parameter: discard_pile -> list, deck -> list, color -> string, value -> string
    Return: None
    '''
    def playCombo(self, discard_pile, deck, color, value):
        combo_cards = [] # 콤보에 사용될 카드들을 담을 리스트
        matching_card = self.get_matching_card(discard_pile[-1]) # 현재 매칭되는 카드들 가져오기
        
        # 매칭되는 카드가 없으면 덱에서 카드를 가져와 추가
        if not matching_card:
            self.setCard(deck)
            return None
        
         # 현재 매칭되는 카드들 중에서 기술 카드와 숫자 카드를 분리하여 combo_cards 리스트에 추가
        for card in matching_card:
            card_color, card_value = card.split() # 카드의 color와 value를 분리
            if card_value in ['Reverse', 'Skip']:
                combo_cards.append(card)
            elif card_value.isnumeric(): # 숫자 카드를 뒤쪽에 배치 
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
        