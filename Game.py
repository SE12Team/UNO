import pygame
from Board import BoardClass
from Player import PlayerClass
from Deck import DeckClass
from Card import CardClass
from CoumputerPlayer import ComputerPlayer
import setting
import lobby

class Game:
    def __init__(self, player_names):
        self.board = BoardClass()
        self.player_names = player_names
        self.players = [PlayerClass(name, self.board.deck.drawCards(1)) for name in player_names]
        self.current_player_index = 0
        self.button_pressed = False

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
        uno_button_width = 0
        
        # 타이머
        countdown_event = pygame.USEREVENT +1
        pygame.time.set_timer(countdown_event, 1000)

        current_player = self.players[self.current_player_index]
        
        paused = True
        running = True
        while running:

            setting.screen.blit(pygame.transform.scale(setting.play_background, (pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen))), (0,0))
            pygame.draw.rect(setting.screen, (100,100,100), (self.width*0.75,0,self.width*0.25,self.height))
            result_uno = self.uno_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    setting.running = False
                elif event.type == countdown_event:
                    self.total_time -= 1
                    # 타이머 리셋
                    if self.total_time == 0:
                        self.total_time = 15
                        pygame.time.set_timer(countdown_event, 1000)
                if event.type == pygame.MOUSEBUTTONDOWN:
                # 우노버튼 위치에 올리면 색 변하기
                    if uno_button_rect.collidepoint(event.pos):
                        uno_button_color = (255,0,0)
                        uno_button_width = 2
                        if len(current_player.getHand()) == 1:
                            self.button_pressed = True

                            if self.button_pressed:
                                if self.players[1].uno():
                                    for i in range(1, len(self.players)):
                                        self.players[i].addCardToHand(self.board.deck.popCards())
                                    print("Computer added 1 card")
                                    print(self.players[1].getHand()) 
                                else:
                                    self.players[0].addCardToHand(self.board.deck.popCards())
                                    print("Player added 2 card")
                        else:
                            self.button_pressed = True
                            if self.button_pressed:
                                self.players[0].addCardToHand(self.board.deck.popCards())
                                print("Player added 1 card") 
                                print(self.players[1].getHand()) 
                                print(self.players[0].getHand()) 
                        self.button_pressed = False 
 
                elif event.type == pygame.MOUSEMOTION:
                    if uno_button_rect.collidepoint(event.pos):
                        uno_button_color = (255,0,0)
                        uno_button_width = 2
                    else:
                        uno_button_color = (100,100,100)
                          

            # 그리기
            time_text = self.font.render(str(self.total_time), True, (0, 0, 0))
            self.screen.blit(time_text, (self.width*0.05,self.height*0.08))
            self.draw_deck()            
            pygame.draw.rect(self.screen, uno_button_color, uno_button_rect, 0, 2)
            pygame.draw.rect(self.screen, (100,100,100), uno_button_rect, uno_button_width, 2)
            self.screen.blit(uno_button_text, uno_button_text_rect)
            self.draw_player_hands()
            pygame.display.flip()

            self.clock.tick(60)

    def uno_pressed(self):
        if self.button_pressed:
            return True
        else:
            return False
        
     

    def draw_deck(self):
        deck_image = pygame.image.load('./images/deck.png')
        deck_image = pygame.transform.scale(deck_image, (self.width*0.16,self.height*0.3))
        deck_rect = deck_image.get_rect()
        deck_rect.x = self.width*0.29
        deck_rect.y = self.height*0.2
        current_card = pygame.image.load('./images/Red_0.png') # 현재 카드랑 이미지랑 연결 필요 
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
        pygame.display.update(card)

        com_rects = [ComHands(self.players, self.width*0.75, 0+i*(self.height*0.2), self.width*0.25, self.height*0.2, (0,0,0), 'Computer', i+1) for i in range(5)]
        for com_rect in com_rects:
            com_rect.draw(self.screen)  

                 
    def pause(self):
        # 일시정지
        pass
            

    def handle_events(self, key_loc):
        # 게임 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 마우스 클릭 이벤트 처리
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked_card = self.screen.find_clicked_card(mouse_pos, self.players[self.current_player_index])
            if clicked_card:
                self.select_card(clicked_card)

    def find_clicked_card(self, pos, current_player):
        pass

    def select_card(self, card_index):
        current_player = self.players[self.current_player_index]
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


class ComHands (lobby.Computer):
    def __init__(self, players, x, y, width, height, color, text="", num=""):
        super().__init__(x, y, width, height, color, text, num)
        self.font = pygame.font.Font('freesansbold.ttf', int(pygame.Surface.get_height(setting.screen)*0.02))
        self.back = pygame.image.load('./images/deck.png')
        self.players = players

    def draw(self, surface):
        surface_width = pygame.Surface.get_width(surface)
        surface_height = pygame.Surface.get_height(surface)
        computer_rec = pygame.draw.rect(surface, self.color, self.rect, 1,1)

        if self.text:
            text_surface = self.font.render(self.text, True, "black")
            text_rect = text_surface.get_rect(topleft=self.rect.topleft)
            surface.blit(text_surface, text_rect)
        
        x = pygame.image.load('./images/Red_0.png')
        x = pygame.transform.scale(x, (computer_rec.width*0.12,computer_rec.height*0.23))

        for player in self.players:
            for value in range(0, len(player.getHand())):
                surface.blit(x, (surface_width - (computer_rec.width*0.05+(computer_rec.width*0.05)*value), computer_rec.height*0.71))

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