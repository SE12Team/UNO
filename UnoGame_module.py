import pygame
pygame.init()
# 버튼 클래스
class Button:
    
    def __init__(self,txt,pos):
        self.font = pygame.font.Font('freesansbold.ttf',int(pygame.Surface.get_height(screen)*0.041))
        self.text = txt
        self.pos = (int((pos[0]/100)*pygame.Surface.get_width(screen)),int((pos[1]/100)*pygame.Surface.get_height(screen)))
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (pygame.Surface.get_width(screen)*0.325,pygame.Surface.get_height(screen)*0.07)) # 사각형 객체

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button,0,5)
        pygame.draw.rect(screen, 'dark gray', self.button,5,5)
        txt = self.font.render(self.text, True,'black')
        screen.blit(txt,(self.pos[0]+15,self.pos[1]+9))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False 

def videoResize(event):
    screen = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
    screen.blit(pygame.transform.scale(background,(event.w,event.h)),(0,0))

    

width = 800
height = 600
screen = pygame.display.set_mode((width,height),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)




background = pygame.image.load("../image/menuBackground.png")