import pygame

class CardClass:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.image_filename = f"images/{color}_{value}.png"
        self.is_special = False
        self.is_wild = False
        self.image = pygame.image.load(self.image_filename)  # 이미지 로드
        self.rect = self.image.get_rect()  # 이미지의 rect 속성 설정
        
    def __repr__(self):
        return f"{self.color} {self.value}"
    
    def getImage(self):
        return "images/{}_{}.png".format(self.color, self.value)

class SpecialCard(CardClass):
    def __init__(self, color, value):
        super().__init__(color, value)
        if value in ["Draw_Two", "Skip", "Reverse"]:
            self.is_special = True

class WildCard(CardClass):
    def __init__(self, color, value):
        super().__init__(color, value)
        if value in ["Wild", "Wild_Draw_Four"]:
            self.is_wild = True
