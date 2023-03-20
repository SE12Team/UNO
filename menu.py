from UnoGame_module import *

pygame.init()

def draw_mainMenu(key_loc):
    global menu_command
    btnSinglePlay = Button("Single Play",(33,52),True if key_loc == 0 else False)
    btnSetting = Button("Setting",(33,61),True if key_loc == 1 else False)
    btnExit = Button("Exit",(33,70),True if key_loc == 2 else False)
    btnSinglePlay.draw()
    btnSetting.draw()
    btnExit.draw()
    if btnSinglePlay.check_clicked():
        menu_command = 1
    elif btnSetting.check_clicked():
        menu_command = 2
    elif btnExit.check_clicked():
        menu_command = 3
    
    instance_list=[btnSinglePlay,btnSetting,btnExit]

    return instance_list

def draw_singlePlay():
    print("싱글플레이어 모드")


def draw_setting():
    print("환경설정")


def keyControl(event,key_loc,instance_list):
    global menu_command
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if key_loc - 1 >= 0:
                key_loc -= 1
        elif event.key == pygame.K_DOWN:
            if key_loc + 1 < len(instance_list):
                key_loc += 1
        elif event.key == pygame.K_RETURN:
            if pygame.Rect.colliderect(instance_list[key_loc].button,instance_list[key_loc].button):
                menu_command = key_loc+1
    return key_loc

pygame.display.set_caption("UNO game")
fps = 60
timer = pygame.time.Clock() #시간을 다루는 객체 느낌?


main_menu = True
running = True
key_loc = 0
menu_command = 0    
screen.blit(pygame.transform.scale(background,(width,height)),(0,0))

while running:
    timer.tick(fps) # 화면의 초당 프레임 수 설정

    if main_menu:
        instance_list = draw_mainMenu(key_loc)
        if menu_command != 0: # main 메뉴에서 버튼이 클릭되면 ...
            main_menu = False
            if menu_command == 1:
                draw_singlePlay()
            elif menu_command == 2:
                draw_setting()
            elif menu_command == 3:
                pygame.quit()
        menu_command = 0

    else:
        main_menu = draw_mainMenu(key_loc)
        if menu_command > 1:
            pass


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            videoResize(event)
        elif event.type == pygame.KEYDOWN:
            key_loc = keyControl(event,key_loc,instance_list)
        
                
    pygame.display.flip() # 화면을 업데이트
pygame.quit() 