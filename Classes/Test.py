from Card import CardClass
from Deck import DeckClass
from Player import PlayerClass

# Deck 객체 생성
deck = DeckClass()
player1 = PlayerClass("Ace",deck.drawCards(7))
print(player1.getHand())


