import random
from Deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def getHand(self):
        return self.hand

    '''
    처음 게임 시작 시 카드를 분배
    Parameter: deck -> list, num -> int, stage -> string
    Return: deck 
    '''
    # num 지정하지 않을 시 한 장만 손패에 가져옴
    def setCard(self, deck, num=1, stage='s'): 
        if stage:  # 싱글모드, 스토리 3,4
            deck.shuffle()
            for _ in range(num):
                card = deck.draw_card()
                self.hand.append(card)
        elif stage == 'A':
            random.shuffle(deck.hand[:80]) # 리스트 앞 쪽 숫자 카드 셔플
            random.shuffle(deck.hand[81:]) # 리스트 뒷 쪽 기술카드 셔플 
            for _ in range(5):
                probability = random.uniform(0, 1)
                if probability < 0.6:
                    card = deck.draw_card() # 뒷쪽의 기술카드 pop
                else:
                    deck.hand.remove(deck.hand[0])
                    card = deck.draw_card(0) # 앞 쪽의 숫자카드 pop
                if card:
                    self.hand.append(card)
        elif stage == 'B':
            deck.shuffle()
            for _ in range(26): # 총 카드수 108개 중 현재카드 1개를 빼고 플레이어들에게 모두 나눠줌.
                card = deck.draw_card()
                self.hand.append(card)
        return deck

    '''
    덱에서 카드를 뽑아 player 손에 추가
    Parameter: deck -> list
    Return: None
    '''
    # def addCard(self, deck):
    #     card = deck.draw_card()
    #     self.hand.append(card)

    '''
    player가 카드를 낼 수 있는지 확인
    Parameter: color -> string, value -> string
    Return: boolean
    '''
    def canPlay(self, card, discard_deck):
        discard = discard_deck.cards[-1]
        if discard.color in ['Wild', 'Wild Draw Four', 'Wild Draw Two']:
            discard_color = discard.value
            discard_value = ""
        else:
            discard_color = discard.color
            discard_value = discard.value
        #if discard_color in ['Wild', 'Wild Draw Four', 'Wild Draw Two']:
        #    discard_color , discard_value = discard_value, discard_color
        if (card.color == discard_color):
            return 1
            # discard_deck.cards.append(self.hand[i])
            # del self.hand[i]
            
        elif (card.value == discard_value) and (card.value in ['1','2','3','4','5','6','7','8','9','0']):
            return 2
        elif card.color in ['Wild', 'Wild Draw Four', 'Wild Draw Two']:
            return 3
        else:
            return 4
    
    '''
    player가 카드를 플레이
    Parameter: card_index, discard_pile, color, value
    Return: boolean
    '''
    # def playCard(self,discard_deck):
    #    if self.canPlay(discard_deck):
    #        return_card = self.hand.pop(card_index) # 손에서 카드 제거
    #        return return_card
    #    else:
    #        print("선택한 카드를 플레이할 수 없음")
    #        return -1

    '''
    player 손의 카드 리스트 보여주기
    Parameter: self.hand -> list
    Return: None
    '''
    def showHand(self):
        for card in self.hand:
            print(card)
        print("")
    
    '''
    player가 승리했는지 여부를 반환
    Return: boolean
    '''
    def hasWon(self):
        return len(self.hand) == 0