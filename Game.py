import pygame
from Board import BoardClass
from Player import PlayerClass
from Deck import DeckClass
import setting
import lobby

class Game:
    def __init__(self, player_names):
        self.board = BoardClass()
        self.player_names = player_names
        self.players = [PlayerClass(name, self.board.deck.drawCards(7)) for name in player_names]
        self.current_player_index = 0

        pygame.init()
        self.width = pygame.Surface.get_width(setting.screen)
        self.height = pygame.Surface.get_height(setting.screen)
        self.screen = pygame.display.set_mode((pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen)))
        self.font = pygame.font.Font('freesansbold.ttf', int(pygame.Surface.get_height(setting.screen)*0.05))
        pygame.display.set_caption("Uno Game")
        self.clock = pygame.time.Clock()
        self.total_time = 15

    def run(self):
        while not self.is_game_over():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.draw_game()
            self.handle_events()
            pygame.display.update()

        self.show_winner()

    def is_game_over(self):
        for player in self.players:
            if len(player.getHand()) == 0:
                self.board.winner = player
                return True
        return False

    def draw_game(self):
        # 게임 화면 그리기

        # 우노 버튼
        uno_button_rect = pygame.Rect(self.width*0.1,self.height*0.4, self.width*0.1,self.height*0.08)
        uno_button_color = (100,100,100)
        uno_button_text = self.font.render('UNO', True, (0,0,0))
        uno_button_text_rect = uno_button_text.get_rect(center=uno_button_rect.center)
        
        # 타이머
        countdown_event = pygame.USEREVENT +1
        pygame.time.set_timer(countdown_event, 1000)
        
        
        runing = True
        while True:

            setting.screen.blit(pygame.transform.scale(setting.play_background, (pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen))), (0,0))
            pygame.draw.rect(setting.screen, (100,100,100), (self.width*0.75,0,self.width*0.25,self.height))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    setting.running = False
                elif event.type == countdown_event:
                    self.total_time -= 1
                    if self.total_time == 0:
                        self.total_time = 15
                        pygame.time.set_timer(countdown_event, 1000)
                if event.type == pygame.MOUSEBUTTONDOWN:
                # Reset the timer when the UNO button is pressed
                    if uno_button_rect.collidepoint(event.pos):
                        pass

            if uno_button_rect.collidepoint(pygame.mouse.get_pos()):
                uno_button_color = (255,0,0)
            else:
                uno_button_color = (100,100,100)
            
            # 그리기
            time_text = self.font.render(str(self.total_time), True, (0, 0, 0))
            self.screen.blit(time_text, (self.width*0.05,self.height*0.08))
            self.draw_deck()
            self.draw_player_hands()
            pygame.draw.rect(self.screen, uno_button_color, uno_button_rect, 0, 2)
            self.screen.blit(uno_button_text, uno_button_text_rect)
            pygame.display.flip()

            self.clock.tick(60)

    def draw_deck(self):
        deck_imag = pygame.image.load('./image/deck.png')
        deck_imag = pygame.transform.scale(deck_imag, (self.width*0.16,self.height*0.3))
        self.screen.blit(deck_imag, (self.width*0.29,self.height*0.2))

        current_card = pygame.image.load('./image/Red_0.png') # 현재 카드랑 이미지랑 연결 필요 
        #current_card = BoardClass.current_card
        current_card = pygame.transform.scale(current_card, (self.width*0.16,self.height*0.3))
        self.screen.blit(current_card, (self.width*0.5,self.height*0.2))
    
    def draw_player_hands(self):
        pygame.draw.rect(setting.screen, (228,220,207), (0,self.height*0.6,self.width*0.75,self.height*0.4))
        You_text = self.font.render('You', True, (0,0,0))
        self.screen.blit(You_text, (self.width*0.05,self.height*0.63))
        x = pygame.image.load('./image/Blue_5.png')
        x = pygame.transform.scale(x, (self.width*0.12,self.height*0.23))

        for i in range(0, len(self.players[0].getHand())):
            self.screen.blit(x, (self.width*0.05+(self.width*0.05)*i, self.height*0.71))

        com_rects = [ComHands(self.width*0.75, 0+i*(self.height*0.2), self.width*0.25, self.height*0.2, (0,0,0), 'Computer', i+1) for i in range(5)]
        for com_rect in com_rects:
            com_rect.draw(self.screen)   
                 
               

    def handle_events(self):
        # 게임 이벤트 처리
        pass

    def show_winner(self):
        # 우승자 보여주기
        pass

class ComHands (lobby.Computer):
    def __init__(self, x, y, width, height, color, text="", num=""):
        super().__init__(x, y, width, height, color, text, num)
        self.font = pygame.font.Font('freesansbold.ttf', int(pygame.Surface.get_height(setting.screen)*0.02))
        self.back = pygame.image.load('./image/deck.png')

    def draw(self, surface):
        surface_width = pygame.Surface.get_width(surface)
        surface_height = pygame.Surface.get_height(surface)
        pygame.draw.rect(surface, self.color, self.rect, 1,1)
        if self.text:
            text_surface = self.font.render(self.text, True, "black")
            text_rect = text_surface.get_rect(topleft=self.rect.topleft)
            surface.blit(text_surface, text_rect)
            

if __name__ == '__main__':
    uno = Game('user')
    uno.run()