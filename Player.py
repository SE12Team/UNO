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
    def canPlay(self, card_index, deck_card):
        can_play = False
        card = self.hand[card_index]

        if "Wild" in card:
            can_play = True
        elif deck_card.color in card or deck_card.value in card:
            can_play = True
        return can_play
    
    '''
    player가 카드를 플레이
    Parameter: card_index, discard_pile, color, value
    Return: boolean
    '''
    def playCard(self, card_index, deck_card):
        if self.canPlay(card_index, deck_card):
            self.hand.pop(card_index) # 손에서 카드 제거
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