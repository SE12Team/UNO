import pygame
from Board import BoardClass
from Player import PlayerClass
from Deck import DeckClass
from Card import CardClass

class Game:
    def __init__(self, player_names):
        self.board = BoardClass()
        self.player_names = player_names
        self.players = [PlayerClass(name, self.board.deck.drawCards(7)) for name in player_names]
        self.current_player_index = 0

        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Uno Game")
        self.clock = pygame.time.Clock()
        self.total_time = 15

    def run(self):
        while not self.is_game_over():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.handle_events()
            self.draw_game()
            pygame.display.update()

        self.show_winner()

    def draw_game(self):
        # 게임 화면 그리기
        self.screen.fill((255, 255, 255))

        # draw cards on screen
        card_width = 60
        card_height = 100
        x = 50
        y = 400
        for card in self.players[0].getHand():
            card_image = pygame.image.load(card.imagePath)
            card_image = pygame.transform.scale(card_image, (card_width, card_height))
            card_rect = card_image.get_rect()
            card_rect.x = x
            card_rect.y = y
            self.screen.blit(card_image, card_rect)
            x += card_width + 10

        # 우노 버튼
        uno_button_rect = pygame.Rect(50, 50, 80, 40)
        uno_button_color = (100, 100, 100)
        uno_button_text = pygame.font.SysFont('arial', 20).render('UNO', True, (0, 0, 0))
        uno_button_text_rect = uno_button_text.get_rect(center=uno_button_rect.center)
        uno_button_width = 0

        # 타이머
        countdown_event = pygame.USEREVENT + 1
        pygame.time.set_timer(countdown_event, 1000)

        paused = True
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == countdown_event:
                    self.total_time -= 1
                    # 타이머 리셋
                    if self.total_time == 0:
                        self.total_time = 15
                        pygame.time.set_timer(countdown_event, 1000)
                if uno_button_rect.collidepoint(event.pos):
                    pass
                elif event.type == pygame.MOUSEMOTION:
                    if uno_button_rect.collidepoint(event.pos):
                        uno_button_color = (255, 0, 0)
                        uno_button_width = 2
                else:
                    uno_button_color = (100, 100, 100)
                    uno_button_width = 0

        # 화면에 그리기
        time_text = pygame.font.SysFont('arial', 20).render(str(self.total_time), True, (0, 0, 0))
        self.screen.blit(time_text, (50, 20))
        pygame.draw.rect(self.screen, uno_button_color, uno_button_rect, 0, 2)
        pygame.draw.rect(self.screen, (100, 100, 100), uno_button_rect, uno_button_width, 2)
        self.screen.blit(uno_button_text, uno_button_text_rect)
        pygame.display.flip()

    pygame.quit()