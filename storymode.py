import pygame
import setting
import pygame_gui
import pygame.freetype
import time


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
        self.loc = pygame.rect.Rect((pos[0]-10,pos[1]-10), (50,50))

    

    def draw(self,btnLoc):
        if btnLoc:
            pygame.draw.circle(self.screen, 'red', self.pos, self.getWidth*0.025, width=int(self.getWidth*0.00625))
        else:
            pygame.draw.circle(self.screen, 'gray', self.pos, self.getWidth*0.025, width=int(self.getWidth*0.00625))
        pygame.draw.circle(self.screen, 'white', self.pos, self.getWidth*0.02, width=int(self.getWidth*0.025))
        txt = self.font.render(self.text, True,'black')
        self.screen.blit(txt,(self.pos[0],self.pos[1]+10))
        

    def check_clicked(self):
        if self.loc.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False 

def btnControl(event,btnLoc,instance_list,screen):
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
    instance_list[tmp].draw(False)
    instance_list[btnLoc].draw(True)

    if event.key == setting.get_keymap_check(): # pygame.K_RETURN
        if pygame.Rect.colliderect(instance_list[btnLoc].loc, instance_list[btnLoc].loc):
            print("STAGE %d!!" % btnLoc)
            askBattle(screen,btnLoc)

    return btnLoc
def askBattle(screen,click_stage_num):
    screen = screen
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    pygame.draw.rect(setting.screen, 'light gray',(width*0.175,height*0.333,width*0.625,height*0.333) ,0,5)
    pygame.draw.rect(setting.screen, 'dark gray', (width*0.175,height*0.333,width*0.625,height*0.333),5,5)
    font = pygame.font.Font('freesansbold.ttf',int(height*0.045))
    txt = font.render("Do you want to play the game?", True,'black')
    screen.blit(txt,(width*0.225,height*0.383))

    yesBox = pygame.draw.rect(setting.screen, 'dark gray', (width*0.25,height*0.483,width*0.212,height*0.083),0,5)
    noBox = pygame.draw.rect(setting.screen, 'dark gray', (width*0.5,height*0.483,width*0.212,height*0.083),0,5)
    font_ysno = pygame.font.Font('freesansbold.ttf',int(height*0.05))
    txt_Yes = font_ysno.render("Yes", True,'black')
    txt_No = font_ysno.render("No", True,'black')
    screen.blit(txt_Yes,(width*0.325,height*0.5))
    screen.blit(txt_No,(width*0.581,height*0.5))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                pass
        if yesBox.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Game.gotoGamePy_story(click_stage_num)
            print("YES!",click_stage_num)
            time.sleep(0.1)
        elif noBox.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            running = False
            time.sleep(0.1)
        pygame.display.update()

    
def clicked_stage(btn_instance_list):
    if btn_instance_list[1].check_clicked():
        return 1
    elif btn_instance_list[2].check_clicked():
        return 2
    elif btn_instance_list[3].check_clicked():
        return 3
    elif btn_instance_list[4].check_clicked():
        return 4
    elif btn_instance_list[5].collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        return 5
    else:
        return 0
            
def drawStoryMode():
    btnLoc = 1
    width = pygame.Surface.get_width(setting.screen)
    height = pygame.Surface.get_height(setting.screen)
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load("./images/storyModeMap.jpeg")


    running = True
    
    btn_instance_list = [0]*6
    A_button = circle_button(screen,(width*0.1625,height*0.4),'STAGE 1')
    btn_instance_list[1] = A_button
    
    B_button = circle_button(screen,(width*0.125,height*0.833),'STAGE 2')
    btn_instance_list[2] = B_button
    
    C_button = circle_button(screen,(width*0.525,height*0.55),'STAGE 3')
    btn_instance_list[3] = C_button
    
    D_button = circle_button(screen,(width*0.7125,height*0.1),'STAGE 4')
    btn_instance_list[4] = D_button
   
    
    while running:
        screen.blit(pygame.transform.scale(background,(width,height)),(0,0))
        back_btn = pygame.draw.rect(setting.screen, 'light gray',(600,520,150,50) ,0,5)
        pygame.draw.rect(setting.screen, 'dark gray', (600,520,150,50),5,5)
        btn_instance_list[5] = back_btn
        font = pygame.font.Font('freesansbold.ttf',int(height*0.045))
        txt = font.render("Back", True,'black')
        screen.blit(txt,(640,532))
        A_button.draw(True if btnLoc == 1 else False)
        B_button.draw(True if btnLoc == 2 else False)
        C_button.draw(True if btnLoc == 3 else False)
        D_button.draw(True if btnLoc == 4 else False)
        
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                setting.running = False
            elif event.type == pygame.KEYDOWN:
                btnLoc = btnControl(event,btnLoc,btn_instance_list,screen)

        
        click_stage_num = clicked_stage(btn_instance_list)
        
        if click_stage_num == 0:
            pass
        elif click_stage_num == 5:
            running = False
        else:
            time.sleep(0.1)
            askBattle(screen,click_stage_num)

        pygame.display.update()
        
