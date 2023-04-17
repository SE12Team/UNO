import random
import time 

class PlayerClass:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __repr__(self):
        return self.name

    def getHand(self):
        return self.hand

    def addCardToHand(self, card):
        self.hand.append(card)

    def removeCardFromHand(self, card):
        self.hand.remove(card)

    def hasCard(self, colors, value):
        for card in self.hand:
            if "Wild" in card.color: 
                return True
            elif colors in card.color or value in card.value:
                return True
        return False
    
    def select_card(self, card):
        current_player = self.players[self.current_player_index]
        current_player.removeCard(card)
        self.board.play_card(card)
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        
    def uno(self):
        if len(self.hand) == 1:
            time.sleep(random.uniform(0.5, 1)) # 0.5초에서 1초 사이로 무작위로 대기
            return True
        else:
            return False