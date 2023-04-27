class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def getHand(self):
        return self.hand
    
    '''
    덱에서 카드를 뽑아 player 손에 추가
    Parameter: deck -> list
    Return: None
    '''
    def addCard(self, deck):
        card = deck.draw_card() # deck에서 pop한 것과 연결
        self.hand.append(card)

    '''
    player가 카드를 낼 수 있는지 확인
    Parameter: color -> string, value -> string
    Return: boolean
    '''
    def canPlay(self, color, value):
        for card in self.hand:
            if "Wild" in card:
                return True
            elif color in card or value in card:
                return True
        return False
    
    '''
    player가 카드를 플레이
    Parameter: card_index, discard_pile, color, value
    Return: boolean
    '''
    def playCard(self, card_index, discard_pile, color, value):
        card = self.hand[card_index]
        if self.canPlay(color, value):
            self.hand.pop(card_index) # 손에서 카드 제거
            discard_pile.append(card) # 카드를 카드 더미에 추가
            return True
        else:
            print("선택한 카드를 플레이할 수 없음")
            return False

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