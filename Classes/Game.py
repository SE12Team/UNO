import pygame
from Board import BoardClass
from Player import PlayerClass
from Deck import DeckClass
from Card import CardClass
import setting
import lobby

class Game:
    def __init__(self, player_names):
        self.board = BoardClass()
        self.player_names = player_names
        self.players = [PlayerClass(name, self.board.deck.drawCards(7)) for name in player_names]
        self.current_player_index = 0

        # Create players
        #for i in range(num_players):
        #    name = input("Enter player name: ")
        #    self.players.append(Player(name))
                        
        # Start game by flipping first card
        first_card = self.board.deck.drawCards(1)[0]
        self.board.discardPile.append(first_card)
        self.board.currentColor = first_card.color
        self.board.currentValue = first_card.value

        pygame.init()
        self.width = pygame.Surface.get_width(setting.screen)
        self.height = pygame.Surface.get_height(setting.screen)
        self.screen = pygame.display.set_mode((pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen)))
        self.font = pygame.font.Font('freesansbold.ttf', int(pygame.Surface.get_height(setting.screen)*0.05))
        pygame.display.set_caption("Uno Game")
        self.clock = pygame.time.Clock()
        self.total_time = 15

    def run(self):
        key_loc = None
        while not self.is_game_over():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.draw_game()
            self.draw_player_hands()
            self.handle_events(key_loc)
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
        self.screen.blit(pygame.transform.scale(setting.play_background, (pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen))), (0,0))
        pygame.draw.rect(setting.screen, (100,100,100), (self.width*0.75,0,self.width*0.25,self.height))
        uno_button_rect = pygame.Rect(self.width*0.1,self.height*0.4, self.width*0.1,self.height*0.08)
        uno_button_color = (100,100,100)
        uno_button_text = self.font.render('UNO', True, (0,0,0))
        uno_button_text_rect = uno_button_text.get_rect(center=uno_button_rect.center)
        uno_button_width = 0

        # 그리기
        time_text = self.font.render(str(self.total_time), True, (0, 0, 0))
        self.screen.blit(time_text, (self.width*0.05,self.height*0.08))
        self.draw_deck()            
        pygame.draw.rect(self.screen, uno_button_color, uno_button_rect, 0, 2)
        pygame.draw.rect(self.screen, (100,100,100), uno_button_rect, uno_button_width, 2)
        self.screen.blit(uno_button_text, uno_button_text_rect)
        self.draw_player_hands()  # 손패 그리기
        pygame.display.flip()

    def draw_deck(self):
        deck_image = pygame.image.load('/Users/kimdogyeong/Desktop/Uno_project/images/Deck.png')
        deck_image = pygame.transform.scale(deck_image, (self.width*0.16,self.height*0.3))
        deck_rect = deck_image.get_rect()
        deck_rect.x = self.width*0.29
        deck_rect.y = self.height*0.2
        current_card = pygame.image.load(self.board.getLastCard().getImage())
        #current_card = BoardClass.current_card
        current_card = pygame.transform.scale(current_card, (self.width*0.16,self.height*0.3))
        self.screen.blit(current_card, (self.width*0.5,self.height*0.2))


        for event in pygame.event.get():  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if deck_rect.collidepoint(event.pos):
                    deck_rect.y = self.height*0.15
            elif event.type == pygame.MOUSEMOTION:
                if deck_rect.collidepoint(event.pos):
                   deck_rect.y = self.height*0.15
                else:
                    deck_rect.y = self.height*0.2

        self.screen.blit(deck_image, deck_rect)
       

    
    def draw_player_hands(self):
        pygame.draw.rect(setting.screen, (228,220,207), (0,self.height*0.6,self.width*0.75,self.height*0.4))
        You_text = self.font.render('You', True, (0,0,0))
        self.screen.blit(You_text, (self.width*0.05,self.height*0.63))

        current_player = self.players[self.current_player_index]
        card_list = []
        img_position = [0, self.height*0.71]
        for i in range(0, len(current_player.getHand())):
            played_card = current_player.getHand()[i]
            card_color = played_card.color
            card_type = played_card.value
            img_loader = Loadimg(img_position, card_color, card_type)
            img_position[0] += self.width*0.05
            img_loader.update_pos(img_position)
            card_list.append(img_loader)

        for card in card_list:
            card.draw(self.screen)
        pygame.display.update()



    def handle_events(self, key_loc):
        # 게임 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                clicked_card = self.find_clicked_card(mouse_pos, self.players[self.current_player_index])
                if clicked_card:
                    self.select_card(clicked_card)
        self.draw_game()
        self.draw_player_hands()
        pygame.display.update()
                    
        # 마우스 클릭 이벤트 처리
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            clicked_card = self.find_clicked_card(mouse_pos, self.players[self.current_player_index])
            if clicked_card:
                self.select_card(clicked_card)

    def find_clicked_card(self, pos, current_player):
        for card in current_player.getHand():
            if card.rect.collidepoint(pos):  # 카드가 눌렸는지 확인합니다.
                return card  # 카드 객체를 반환합니다.
        return None  # 해당 카드가 없는 경우 None을 반환합니다.


    def select_card(self, clicked_card):
        current_player = self.players[self.current_player_index]
        
        if self.board.canPlay(clicked_card, current_player.getHand()):
            self.board.playCard(clicked_card)
            current_player.removeCard(clicked_card)
            if len(current_player.getHand()) == 0:
                self.is_game_over()
            # 게임판(Board) 상황 업데이트
            last_card = self.board.getLastCard()
            self.board.currentColor = last_card.color
            self.board.currentValue = last_card.value
            # 다음 플레이어로 변경
            self.current_player_index = (self.current_player_index + 1) % len(self.players)



    def show_winner(self):
        # 우승자 보여주기
        pass


class ComHands (lobby.Computer):
    def __init__(self, x, y, width, height, color, text="", num=""):
        super().__init__(x, y, width, height, color, text, num)
        self.font = pygame.font.Font('freesansbold.ttf', int(pygame.Surface.get_height(setting.screen)*0.02))
        self.back = pygame.image.load('./images/deck.png')

    def draw(self, surface):
        surface_width = pygame.Surface.get_width(surface)
        surface_height = pygame.Surface.get_height(surface)
        pygame.draw.rect(surface, self.color, self.rect, 1,1)
        if self.text:
            text_surface = self.font.render(self.text, True, "black")
            text_rect = text_surface.get_rect(topleft=self.rect.topleft)
            surface.blit(text_surface, text_rect)

class Loadimg:
    def __init__(self, pos, color, type):
        self.width = pygame.Surface.get_width(setting.screen)
        self.height = pygame.Surface.get_height(setting.screen)
        self.pos = pos
        self.color = color
        self.type = type
        self.img = pygame.image.load(CardClass(self.color, self.type).getImage())
        self.img = pygame.transform.scale(self.img, (self.width*0.12,self.height*0.23))
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
    def update_pos(self, new_pos):
        self.rect.topleft = new_pos
    def draw(self, surface):
        surface.blit(self.img, self.rect)
    

if __name__ == '__main__':
    uno = Game(["Player 1", "Player 2"])
    uno.run()
