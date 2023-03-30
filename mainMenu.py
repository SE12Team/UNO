from UnoGame_module import *
import setting_menu
import setting

pygame.init()

def draw_mainMenu():
    setting.screen.blit(pygame.transform.scale(background,(width,height)),(0,0))
    global key_loc
    global menu_command
    if setting.main_menu:
        instance_list = mainMenuBtn(key_loc)
        if menu_command != 0: # main 메뉴에서 버튼이 클릭되면 ...
            setting.main_menu = False
            if menu_command == 1:
                draw_singlePlay()
            elif menu_command == 2:
                setting.main_menu = False
                setting_menu.get_menu(True, False, False) #
            elif menu_command == 3:
                setting.running = False
        menu_command = 0

    else:
        #setting.main_menu = mainMenuBtn(key_loc)
        #if menu_command > 1:
            pass


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            setting.running = False
        elif event.type == pygame.VIDEORESIZE:
            videoResize(event)
        elif event.type == pygame.KEYDOWN:
            key_loc = keyControl(event,key_loc,instance_list)

def keyControl(event,key_loc,instance_list):
    global menu_command
    if event.key == setting.get_keymap_up(): # pygame.K_UP
        if key_loc - 1 >= 0:
            key_loc -= 1
    elif event.key == setting.get_keymap_down(): # pygame.K_DOWN
        if key_loc + 1 < len(instance_list):
            key_loc += 1
    elif event.key == setting.get_keymap_check(): # pygame.K_RETURN
        if pygame.Rect.colliderect(instance_list[key_loc].button,instance_list[key_loc].button):
            menu_command = key_loc+1
    return key_loc

def mainMenuBtn(key_loc):
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





pygame.display.set_caption("UNO game")
fps = 60
timer = pygame.time.Clock() #시간을 다루는 객체 느낌?




key_loc = 0
menu_command = 0    




while setting.running:
    timer.tick(fps) # 화면의 초당 프레임 수 설정
    draw_mainMenu()
    
        
                
    pygame.display.flip() # 화면을 업데이트

pygame.quit() 