import pygame
import setting

pygame.init()

width = setting.get_screen(setting.get_screen_num())[0]
height = setting.get_screen(setting.get_screen_num())[1]
#screen = pygame.display.set_mode((width,height),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
background = pygame.image.load("./image/menuBackground.png")

# 버튼 클래스
class Button:

    def __init__(self,txt,pos,key_loc):
        self.getWidth = pygame.Surface.get_width(setting.screen)
        self.getHeight = pygame.Surface.get_height(setting.screen)
        self.font = pygame.font.Font('freesansbold.ttf',int(self.getHeight*0.041))
        self.text = txt
        self.pos = (int((pos[0]/100)*self.getWidth),int((pos[1]/100)*self.getHeight))
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (self.getWidth*0.325,self.getHeight*0.07)) # 사각형 객체
        self.key_loc = key_loc
    def draw(self):
        if self.key_loc:
            pygame.draw.rect(setting.screen, 'red', self.button,0,5)
        else:
            pygame.draw.rect(setting.screen, 'light gray', self.button,0,5)
        pygame.draw.rect(setting.screen, 'dark gray', self.button,5,5)
        txt = self.font.render(self.text, True,'black')
        setting.screen.blit(txt,(self.pos[0]+int(self.getWidth*0.015),self.pos[1]+int((self.getHeight*0.015))))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False 

def videoResize(event):
    setting.screen = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
    setting.screen.blit(pygame.transform.scale(background,(event.w,event.h)),(0,0))