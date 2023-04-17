from Deck import DeckClass
from itertools import combinations

class BoardClass:
    def __init__(self):
        self.deck = DeckClass()
        self.discardPile = []
        self.players = players
        self.currentPlayerIndex = 0
        self.currentColor = None
        self.currentValue = None
        self.direction = 1
        self.winner = None

    def canPlay(self, card, playerHand):
        """
        카드를 낼 수 있는지 확인
        """
        if "Wild" in str(card):  # Any wild card can be played
            return True
        elif card.color == self.currentColor or card.value == self.currentValue:  # Matching color or value card can be played
            return True
        elif isinstance(card.value, str):  # Special cards can be played if they match the current color
            for c in playerHand:
                if c.color == self.currentColor:
                    return False
            return True
        return False


    def playCard(self, cardIndex):
        """
        현제 플레이어의 손패에서 카드를 냄
        """
        player = self.getCurrentPlayer()
        card = player.playCard(cardIndex)
        self.discardPile.append(card)
        self.currentColor = card.color
        self.currentValue = card.value
        if isinstance(card.value, str):
            self.handleSpecialCard(card)
        else:
            self.moveToNextPlayer()

    def handleSpecialCard(self, card):
        """
        특수카드가 나왔을때의 로직 처리
        """
        player = self.getNextPlayer()
        if card.value == "Skip":
            #print(f"{player.name} was skipped!")
            self.moveToNextPlayer()
        elif card.value == "Reverse":
            #print("Game direction reversed!")
            self.direction *= -1
            self.moveToNextPlayer()
        elif card.value == "Draw Two":
            drawCards = self.deck.drawCards(2)
            player.addCardToHand(drawCards)
            #print(f"{player.name} drew 2 cards and lost a turn!")
            self.moveToNextPlayer()
        elif card.value == "Wild":
            color = input(f"{player.name}, choose a color (red, green, yellow, blue): ")
            card.color = color
            self.moveToNextPlayer()
        elif card.value == "Wild Draw Four":
            color = input(f"{player.name}, choose a color (red, green, yellow, blue): ")
            card.color = color
            drawCards = self.deck.drawCards(4)
            player.addCardToHand(drawCards)
            print(f"{player.name} drew 4 cards and lost a turn!")
            self.moveToNextPlayer()

    def getCurrentPlayer(self):
        """
        현제 플레이어의 인덱스 반환 
        """
        return self.players[self.currentPlayerIndex]

    def getNextPlayer(self):
        """
        방향에 근거해 다음 플레이어의 인덱스 반환
        """
        nextPlayerIndex = self.currentPlayerIndex + self.direction
        if nextPlayerIndex == len(self.players):
            nextPlayerIndex = 0
        elif nextPlayerIndex < 0:
            nextPlayerIndex = len(self.players) - 1
        return self.players[nextPlayerIndex]

    def moveToNextPlayer(self):
        """
        다음 플레이어로 이동
        """
        player = self.getNextPlayer()
        self.currentPlayerIndex = self.players.index(player)
        self.currentColor = None
        self.currentValue = None
        
    def getLastCard(self):
        """
        게임 종료 후 마지막으로 낸 카드를 반환
        """
        if len(self.discardPile) > 0:
            return self.discardPile[-1]
        elif len(self.deck.cards) > 0:
            return self.deck.cards[-1]
        
    def checkWinner(self):
        """
        Check if a player has won the game.
        """
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player.name
                return True
        return False
    
    def getBoard(self):
        """
        Return the current state of the game board.
        """
        boardState = {
            "deckSize": len(self.deck.cards),
            "discardPile": [str(card) for card in self.discardPile],
            "players": [],
            "currentPlayerIndex": self.currentPlayerIndex,
            "currentColor": str(self.currentColor),
            "currentValue": str(self.currentValue),
            "direction": self.direction,
            "winner": self.winner
        }

        for player in self.players:
            boardState["players"].append({
                "name": player.name,
                "hand": [str(card) for card in player.hand],
                "numCards": len(player.hand)
            })

        return boardState

    def gameOver(self):
        pass

