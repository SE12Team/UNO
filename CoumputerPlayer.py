import random
import time 
from Player import PlayerClass


class ComputerPlayer(PlayerClass):
    def __init__(self, name, board, hand):
        super().__init__(name, hand)
        self.board = board
    
    def select_card(self):
        current_card = self.board.getLastCard()
        playable_cards = [card for card in self.hand if self.board.canPlay(card, self.hand)]

        # 현재 플레이어가 낼 수 있는 카드가 있으면, 랜덤하게 선택해서 놓음
        if playable_cards:
            selected_card = random.choice(playable_cards)
            self.removeCard(selected_card)
            self.board.play_card(selected_card)
        
            # 플레이어가 카드를 다 소진했으면 게임 종료
            if len(self.getHand()) == 0:
                self.is_game_over()
        
            # 턴을 다음 플레이어에게 넘김
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
        
        # 현재 플레이어가 낼 수 있는 카드가 없으면, 카드를 뽑음
        else:
            drawn_card = self.board.deck.draw_card()
            self.addCardToHand(drawn_card)
            self.select_card()
        
    def uno(self):
        if len(self.hand) == 1:
            time.sleep(random.uniform(0.5, 1)) # 0.5초에서 1초 사이로 무작위로 대기
            return True
        else:
            return False
    
    # def combo(self):
    #     combos = []
    #     for i in range(2, len(self.cards) + 1):
    #         for subset in itertools.combinations(self.cards, i):
    #             if self.isValidCombo(subset):
    #                 combo = Combo()
    #                 for card in subset:
    #                     combo.addCard(card)
    #                 combos.append(combo)
    #    return [combo.getValue() for combo in combos if len(combo.getValue()) >= 2]
    
    def isValidCombo(self, cards):
        if len(cards) < 2:
            return False
        
        first_card = cards[0]
        for card in cards[1:]:
            if card.color != first_card.color and card.value != first_card.value and card.value not in ["wild", "wild_draw_four"]:
                return False
        
        return True
    
    #콤보 기능 구현 
    def playCard(self, current_card):
        playable_cards = self.getPlayableCards(current_card)
        if len(playable_cards) == 0:
            drawn_card = self.drawCard()
            print(f"{self.name} drew {drawn_card}")
            if drawn_card.isPlayable(current_card):
                self.removeCardFromHand(drawn_card)
                return drawn_card
            else:
                return None
        else:
            # check if any special card and wild card combinations are possible
            for i in range(len(playable_cards)):
                if playable_cards[i].value in ["draw_two", "skip", "reverse"]:
                    for j in range(len(playable_cards)):
                        if playable_cards[j].value in ["wild", "wild_draw_four"]:
                            for k in range(len(self.cards)):
                                if self.cards[k].value == current_card.value and self.cards[k].color != playable_cards[j].color:
                                    # combine special card, wild card, and a matching color card
                                    combo = [playable_cards[i], playable_cards[j], self.cards[k]]
                                    print(f"{self.name} played combo {combo}")
                                    for c in combo:
                                        self.removeCardFromHand(c)
                                    return combo
                elif playable_cards[i].value in ["wild", "wild_draw_four"]:
                    for j in range(len(self.cards)):
                        if self.cards[j].value == current_card.value and self.cards[j].color != playable_cards[i].color:
                            # combine wild card and a matching color card
                            combo = [playable_cards[i], self.cards[j]]
                            print(f"{self.name} played combo {combo}")
                            for c in combo:
                                self.removeCardFromHand(c)
                            return combo
            # if no special card and wild card combination is possible, play the first playable card
            card_to_play = playable_cards[0]
            print(f"{self.name} played {card_to_play}")
            self.removeCardFromHand(card_to_play)
            return card_to_play
        
class Combo:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getValue(self):
        return [card.value for card in self.cards]
