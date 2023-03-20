from UnoGame_module import *

pygame.init()

def draw_mainMenu():
    command = 0
    btnSinglePlay = Button("Single Play",(33,52))
    btnSetting = Button("Setting",(33,61))
    btnExit = Button("Exit",(33,70))
    btnSinglePlay.draw()
    btnSetting.draw()
    btnExit.draw()

    if btnSinglePlay.check_clicked():
        command = 1
    elif btnSetting.check_clicked():
        command = 2
    elif btnExit.check_clicked():
        command = 3

    return command

def draw_singlePlay():
    print("싱글플레이어 모드")


def draw_setting():
    print("환경설정")



pygame.display.set_caption("UNO game")
fps = 60
timer = pygame.time.Clock() #시간을 다루는 객체 느낌?

main_menu = True
menu_command = 0    
running = True

screen.blit(pygame.transform.scale(background,(width,height)),(0,0))
while running:
    timer.tick(fps) # 화면의 초당 프레임 수 설정

    if main_menu:
        menu_command = draw_mainMenu()
        if menu_command != 0: # main 메뉴에서 버튼이 클릭되면 ...
            main_menu = False
            if menu_command == 1:
                draw_singlePlay()
            elif menu_command == 2:
                draw_setting()
            elif menu_command == 3:
                pygame.quit() 
    else:
        main_menu = draw_mainMenu()
        if menu_command > 1:
            pass


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            videoResize(event)
        if event.type == pygame.KEYDOWN:
            pass

    pygame.display.flip() # 화면을 업데이트
pygame.quit() 