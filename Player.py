class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def getHand(self):
        return self.hand

    '''
    처음 게임 시작 시 카드를 분배
    Parameter: deck -> list, num -> int
    Return: None
    '''
    # num 지정하지 않을 시 한 장만 손패에 가져옴
    def setCard(self, deck, num=1):
        for _ in range(num):
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
        discard_color = discard.color
        discard_value = discard.value
        if discard_color in ['Wild', 'Wild Draw Four', 'Wild Draw Two']:
            discard_color , discard_value = discard_value, discard_color
        if (card.color == discard_color):
            return 1
            # discard_deck.cards.append(self.hand[i])
            # del self.hand[i]
            
        elif (card.value == discard_value) and (card.value in ['1','2','3','4','5','6','7','8','9','0']):
            return 2
        elif card.color in ['Wild', 'Wild Draw Four', 'Wild Draw Two']:
            #자기가 가장 많이 들고 있는 색깔로 와일드 카드 색 바꾸고 냄
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