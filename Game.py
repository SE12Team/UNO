import pygame
from Deck import Deck
from Player import Player

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
        self.winner = self.players[0]

    def start(self, card_num):
        # 덱을 생성 카드 분배
        self.deck.generate()
        self.deck.shuffle()
        for player in self.players:
            # 플레이어에게 카드 분배
            player.setCard(self.deck)

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
    def __init__(self, players):
        self.deck = Deck()
        self.board_deck = self.deck.reset()
        self.players = players
        self.turn = Turn(players)
        self.winner = self.players[0]

    def start(self, card_num):
        # 덱을 생성 카드 분배
        self.deck.generate()
        self.deck.shuffle()
        for player in self.players:
            # 플레이어에게 카드 분배
            player.setCard(self.deck, card_num)

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

    # 현재 턴인 플레이어
    def select_card(self, card_index):
        current_player = self.turn.current_player
        selected_card = current_player.getHand()[card_index]

        # 마지막 카드와 색 또는 숫자가 일치하는지 검사
        last_card = self.board.getLastCard()
        if selected_card.matches(last_card):
            # 현재 플레이어가 선택한 카드를 게임판에 놓음
            self.board.playCard(selected_card)

            # 현재 플레이어가 선택한 카드를 손에서 제거
            current_player.removeCard(card_index)

            # 플레이어가 카드를 다 소진했으면 게임 종료
            if len(current_player.getHand()) == 0:
                self.is_game_over()

            # 턴을 다음 플레이어에게 넘김
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def show_winner(self):
        # 우승자 보여주기
        pass

    def is_game_over(self):
        is_end = False
        for player in self.players:
            if len(player.getHand()) == 0:
                self.winner = player
                is_end = True
        return is_end