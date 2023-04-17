import random
from Card import CardClass
from itertools import combinations
import setting
import pygame

class DeckClass:
    def __init__(self):
        self.cards = []
        colors = ["Red", "Green", "Yellow", "Blue"]
        values = [0,1,2,3,4,5,6,7,8,9, "Draw_Two", "Skip", "Reverse"]
        wilds = ["Wild", "Wild_Draw_Four"]
        
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
        self.draw_sound()
        for x in range(numCards):
            cardsDrawn.append(self.cards.pop(0))
        return cardsDrawn
    
    #카드 리스트에서 가능한 모든 조합을 반환
    def find_combinations(cards):       

        combos = []
        for r in range(3, len(cards)+1):
            for combo in combinations(cards, r):
                combos.append(combo)
        return combos
    
    def __len__(self):
        return len(self.cards)
    
    def draw_sound():
          draw_se = pygame.mixer.Sound("draw.mp3 경로")
          draw_se.set_volume(setting.get_music_se())
          draw_se.play()

    


    