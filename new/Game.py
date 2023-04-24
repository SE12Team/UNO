import pygame
from Deck import Deck

class Turn:
    def __init__(self, players):
        # players 리스트의 첫 번째 인자가 항상 먼저 시작
        self.players = players
        self.current_player = players[0]
        self.direction = 1

    def next_direction(self):
        # 다음 플레이어로 턴을 넘김
        index = self.players.index(self.current_player)
        index = (index + self.direction) % len(self.players)
        self.current_player = self.players[index]
        return self.current_player

    def skip_direction(self):
        # 한 턴 건너뛰기
        index = self.players.index(self.current_player)
        index = ((index + 1) + self.direction) % len(self.players)
        self.current_player = self.players[index]
        return self.current_player

    def reverse_direction(self):
        # 턴 방향을 반대로 바꿈
        self.direction *= -1


class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.turn = Turn(players)

    def start(self, card_num):
        # 덱을 생성 카드 분배
        self.deck.generate()
        # for player in self.players:
            # player.draw(self.deck, 7)
        self.deck.deal(card_num, self.players)

    def play(self, card):
        # 카드를 놓음
        current_player = self.turn.current_player

        if card.can_play(self):
            current_player.play(card, self)
            if current_player.is_winner():
                print(current_player.name, " wins!")
                return True

            if isinstance(current_player, ComputerPlayer):
                self.computer_player_move()
            else:
                self.turn.next_player()

            return False

    def computer_player_move(self):
        # 컴퓨터 플레이어가 카드를 놓음
        possible_plays = self.computer_player.get_possible_plays(self)
        if possible_plays:
            card = self.computer_player.choose_card_to_play(possible_plays)
            self.play(card)
        else:
            self.computer_player.draw(self.deck, 1)
            self.turn.next_player()

class Game:
    def __init__(self, players, computer_player):
        self.deck = Deck()
        self.players = players
        self.computer_player = computer_player
        self.turn = Turn(players)

    def start(self):
        # 게임을 시작함
        self.deck.shuffle()
        for player in self.players:
            player.draw(self.deck, 7)
        self.computer_player.draw(self.deck, 7)

    def play(self, card):
        # 카드를 놓음
        current_player = self.turn.current_player

        if card.can_play(self):
            current_player.play(card, self)
            if current_player.is_winner():
                print(current_player.name, " wins!")
                return True

            if isinstance(current_player, ComputerPlayer):
                self.computer_player_move()
            else:
                self.turn.next_player()

            return False

    def computer_player_move(self):
        # 컴퓨터 플레이어가 카드를 놓음
        possible_plays = self.computer_player.get_possible_plays(self)
        if possible_plays:
            card = self.computer_player.choose_card_to_play(possible_plays)
            self.play(card)
        else:
            self.computer_player.draw(self.deck, 1)
            self.turn.next_player()
