import pygame
import setting
import time

import gameLoop
# 상수 정의
EMPTY_COLOR = (255, 255, 255)
PLAYER_COLOR = (255, 255, 0)
COMPUTER_COLOR = (100,100,100)
GAMESTART_COLOR = (0, 255, 0)
BACK_COLOR = (0, 0, 255)

def input_text_on_surface(screen, font, surface_rect):
    text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == setting.get_keymap_check(): # pygame.K_RETURN
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        surface = pygame.Surface(surface_rect.size)
        surface.fill((255, 255, 255))
        input_box = pygame.Rect(0, 0, surface_rect.width, surface_rect.height)
        pygame.draw.rect(surface, (0, 0, 0), input_box, 2)
        text_surface = font.render(text, True, (0, 0, 0))
        surface.blit(text_surface, (5, 5))

        screen.blit(surface, surface_rect)
        pygame.display.update(surface_rect)


class Computer:
    computer_num = 0
    def __init__(self, x, y, width, height, color, text="", num=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.strNum = str(num) 
        self.text = text + self.strNum


    def draw(self, surface, font):
        pygame.draw.rect(surface, self.color, self.rect,0,5)
        pygame.draw.rect(surface, "dark gray", self.rect,3,5)
        if self.text:
            text_surface = font.render(self.text, True, "black")
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def lobby_screen():
    Computer.computer_num = 0

    # 화면 생성
    screen = pygame.display.set_mode((pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen)))


    # 폰트 생성

    # 요소 생성
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    font = pygame.font.SysFont('freesansbold.ttf', int(width*0.05))
    empty_rects = [Computer(width*0.212, height*0.15 + i* (height*0.14), width*0.25, height*0.14, EMPTY_COLOR, "empty", i+1) for i in range(5)]
    player_rect = Computer(width*0.562, height*0.283, width*0.212, height*0.2, PLAYER_COLOR, "Player")
    gamestart_rect = Computer(width*0.562, height*0.5, width*0.212, height*0.13, GAMESTART_COLOR, "Gamestart")
    back_rect = Computer(width*0.562, height*0.65, width*0.212, height*0.13, BACK_COLOR, "Back")

    # 게임 루프
    running = True
    while running:
        setting.screen.blit(pygame.transform.scale(setting.background,(pygame.Surface.get_width(setting.screen),pygame.Surface.get_height(setting.screen))),(0,0))
        pygame.draw.rect(setting.screen, 'light gray',(width*0.12,height*0.083,width*0.75,height*0.85) ,0,5)
        pygame.draw.rect(setting.screen, 'dark gray', (width*0.12,height*0.083,width*0.75,height*0.85),10,5)
        #pygame.draw.rect(setting.screen, 'dark gray', (0,0,pygame.Surface.get_width(setting.screen),pygame.Surface.get_height(setting.screen)),10,5)
        # 이벤트 처리
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                setting.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for empty_rect in empty_rects:
                    if empty_rect.is_clicked(pos):
                        if empty_rect.color == EMPTY_COLOR:
                            Computer.computer_num += 1
                            empty_rect.text = "Computer" + empty_rect.strNum
                            empty_rect.color = COMPUTER_COLOR 
                        else:
                            Computer.computer_num -= 1
                            empty_rect.text = "empty" + empty_rect.strNum
                            empty_rect.color = EMPTY_COLOR
                if player_rect.is_clicked(pos):
                    surface_rect = pygame.Rect(width*0.587, height*0.341, width*0.163, height*0.083)
                    player_name = input_text_on_surface(screen, font, surface_rect)
                    player_rect.text = player_name
                elif gamestart_rect.is_clicked(pos):
                    pass
                    gameLoop.gameUiLoop(Computer.computer_num)
                    return

                elif back_rect.is_clicked(pos):
                    time.sleep(0.1)
                    running = False

        # 그리기
        for empty_rect in empty_rects:
            empty_rect.draw(screen, font)
        player_rect.draw(screen, font)
        gamestart_rect.draw(screen, font)
        back_rect.draw(screen, font)
        pygame.display.update()


    


