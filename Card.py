import pygame

'''
    1. draw(self, screen, pos):
        usage:
            카드를 지정한 위치에 그림.
        parameter:
            1. screen: 화면 영역
            2. pos: 카드 이미지가 그려질 위치(x, y)
        return:
            none

    2. set_size(self, ratio):
        usage:
            카드의 이미지를 주어진 비율로 조절함.
        parameter:
            1. ratio: 수정할 카드 비율
        return:
            none

    3. flip(self):
        usage:
            카드를 뒤집음.
            현재 카드가 앞면을 보이는 경우 뒷면, 뒷면을 보이는 경우 앞면으로 바꿈.
        parameter:
            none
        return:
            none

    4. rotate(self, angle):
        usage:
            카드를 주어진 각도에 따라 회전시킴.
        parameter:
            1. angle: 수정할 카드 각도
        return:
            none
    
    5. check_isWild(self)
        usage:
            현재 카드가 와일드 카드인지 확인.
        parameter:
            none
        return:
            BOOLEAN값
'''

class Card:
    def __init__(self, color, value, ratio=0.4):
        self.color = color # 카드 색
        self.value = value # 카드 숫자
        self.origin_image_front = pygame.image.load(f"../images/{color}_{value}.png") # 원본 카드의 앞면 이미지
        self.origin_image_back = pygame.image.load("../images/Deck.png") # 원본 카드의 뒷면 이미지
        self.image_front = self.origin_image_front # 카드 앞면 이미지
        self.image_back = self.origin_image_back # 카드 뒷면 이미지
        self.image = self.image_front # 현재 눈에 보이는 카드 이미지
        self.set_size(self, ratio) # 비율에 따른 카드 이미지 조정
        
    def __repr__(self): 
        return f"{self.color} {self.value}"
    
    def draw(self, screen, pos):
        screen.blit(self.image, pos)
    
    def set_size(self, ratio):
        origin_width, origin_height = self.origin_image_front.get_size()
        width, height = int(origin_width * ratio), int(origin_height * ratio)

        self.image_front = pygame.transform.scale(self.origin_image_front, (width, height))
        self.image_back = pygame.transform.scale(self.origin_image_back, (width, height))

        # 카드 이미지 크기 조정
        if self.image == self.image_front:
            self.image = self.image_front
        else:
            self.image = self.image_back

    def flip(self):
        if self.image == self.image_front:
            self.image = self.image_front
        else:
            self.image = self.image_back

    def rotate(self, angle):
        self.image_front = pygame.transform.rotate(self.image_front, angle)
        self.image_back = pygame.transform.rotate(self.image_back, angle)
        self.image = pygame.transform.rotate(self.image, angle)
    
    # 와일드 카드인 경우 스크린에 색 고르는 창 출력, 선택한 색 게임 보드에 반영 필요
    def check_isWild(self):
        if 'Wild' in self.color:
            return True
        else:
            return False