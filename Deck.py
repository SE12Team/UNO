import random
from Card import CardClass

class DeckClass:
    def __init__(self):
        self.cards = []
        colors = ["Red", "Green", "Yellow", "Blue"]
        values = [0,1,2,3,4,5,6,7,8,9, "Draw Two", "Skip", "Reverse"]
        wilds = ["Wild", "Wild Draw Four"]
        
        # Add normal cards
        for color in colors:
            for value in values:
                card = CardClass(color, value)
                if value == 0: # Only one 0 card per color
                    self.cards.append(card)
                else:
                    self.cards.append(card)
                    self.cards.append(card)
        
        # Add wild cards
        for wild in wilds:
            for i in range(4):
                card = CardClass(wild, "Any")
                self.cards.append(card)
        
        random.shuffle(self.cards)
    
    def drawCards(self, numCards):
        cardsDrawn = []
        for x in range(numCards):
            cardsDrawn.append(self.cards.pop(0))
        return cardsDrawn
    
    def popCards(self):
        return self.cards.pop(0)
    