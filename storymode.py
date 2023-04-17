import pygame
import setting
import pygame_gui
import pygame.freetype

pygame.init()
pygame.font.init()
class circle_button:
    def __init__(self,screen,pos,text,):
        self.getWidth = pygame.Surface.get_width(setting.screen)
        self.getHeight = pygame.Surface.get_height(setting.screen)
        self.font = pygame.font.Font('freesansbold.ttf',int(self.getHeight*0.0416))
        self.screen = screen
        self.pos = pos
        self.text = text
        self.loc = pygame.rect.Rect((pos[0],pos[1]), (10,10))



    def draw(self,btnLoc):
        if btnLoc:
            pygame.draw.circle(self.screen, 'red', self.pos, self.getWidth*0.025, width=int(self.getWidth*0.00625))
        else:
            pygame.draw.circle(self.screen, 'gray', self.pos, self.getWidth*0.025, width=int(self.getWidth*0.00625))
        pygame.draw.circle(self.screen, 'white', self.pos, self.getWidth*0.02, width=int(self.getWidth*0.025))
        txt = self.font.render(self.text, True,'black')
        self.screen.blit(txt,(self.pos[0],self.pos[1]+10))
        

    def check_clicked(self):
        if self.Rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False 

def btnControl(event,btnLoc,instance_list):
    tmp = btnLoc
    if event.key == setting.get_keymap_right():
        if btnLoc < 4:
            btnLoc += 1

        else: 
            btnLoc = 1
    elif event.key == setting.get_keymap_left():
        if btnLoc > 1:
            btnLoc -= 1
        else:
            btnLoc = 4
    elif event.key == setting.get_keymap_check(): # pygame.K_RETURN
        if pygame.Rect.colliderect(instance_list[btnLoc].loc, instance_list[btnLoc].loc):
            print("STAGE %d!!" % btnLoc)


    instance_list[tmp].draw(False)
    instance_list[btnLoc].draw(True)
    return btnLoc
def drawStoryMode():
    btnLoc = 1
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load("./image/storyModeMap.jpeg")

    clock = pygame.time.Clock()
    running = True
    screen.blit(pygame.transform.scale(background,(width,height)),(0,0))
    
    btn_instance_list = [0]*5
    A_button = circle_button(screen,(width*0.1625,height*0.4),'STAGE 1')
    btn_instance_list[1] = A_button
    A_button.draw(True if btnLoc == 1 else False)
    B_button = circle_button(screen,(width*0.125,height*0.833),'STAGE 2')
    btn_instance_list[2] = B_button
    B_button.draw(True if btnLoc == 2 else False)
    C_button = circle_button(screen,(width*0.525,height*0.55),'STAGE 3')
    btn_instance_list[3] = C_button
    C_button.draw(True if btnLoc == 3 else False)
    D_button = circle_button(screen,(width*0.7125,height*0.1),'STAGE 4')
    btn_instance_list[4] = D_button
    D_button.draw(True if btnLoc == 4 else False)
    
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                setting.running = False
            elif event.type == pygame.KEYDOWN:
                btnLoc = btnControl(event,btnLoc,btn_instance_list)
            

        pygame.display.update()


