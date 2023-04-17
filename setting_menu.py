import pygame
import setting


pygame.init()

# Set the window size and caption
WINDOW_SIZE = setting.get_screen(setting.get_screen_num())
pygame.display.set_caption("UNO GAME Menu")
# screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

# Set font
# font = pygame.font.Font(None, 40)
font = pygame.font.Font('freesansbold.ttf', int(pygame.Surface.get_height(setting.screen)*0.05))
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 205, 18)

# Main loop
menu_flag = True # 메인 화면
control_flag = False # 사용자 커스터마이징 입력 키 화면
music_flag = False # 음량 설정 화면

# global 변수 설정
MOD = int(setting.get_mod_num())
SOUND = bool(setting.get_sound_bool())
SCREEN = int(setting.get_screen_num())
COLORBLIND = bool(setting.get_colorblind_bool())
volume_bar_width = setting.screen.get_width()/6
volume_bar_height = 20
background = pygame.image.load("./image/menuBackground.png")

# setting option list
options = setting.get_mod_list() + ['Set Control', 'Set Sound Detail', 'rollback', 'save', 'close']
options_control = setting.get_control_list() + ['rollback', 'save', 'back to menu']
options_music = setting.get_music_list() + ['rollback', "sound", 'back to menu', 'close']
initial_control = setting.get_control_list_all()
selected_option = 0

# setting 텍스트 정렬
def get_common_option_rec(option_text, is_option, i):
    option_rect = option_text.get_rect()
    if is_option:
        # screen.get_width: 전체 스크린 가로 길이(창 가로 길이로 바꾸기)
        # screen.get_width: 전체 스크린 세로 길이(창 세로 길이로 바꾸기)
        option_rect.center = (setting.screen.get_width()/3, setting.screen.get_height()/7 + i * (pygame.Surface.get_height(setting.screen)*0.08))
        option_rect.left = setting.screen.get_width()/4
    else:
        option_rect.center = (setting.screen.get_width()/2, setting.screen.get_height()/7 + i * (pygame.Surface.get_height(setting.screen)*0.08))
        option_rect.right = setting.screen.get_width() - setting.screen.get_width()/4
    return option_rect

def get_volume(type):
    if type == 0:
        volume = setting.get_music_all()
    elif type == 1:
        volume = setting.get_music_bm()
    else:
        volume = setting.get_music_se()
    return volume

def get_volume_bar(i, is_first, input_volume, text):
    global volume_bar_width
    global volume_bar_height
    text_rect = get_common_option_rec(text, False, i)
    volume_bar_x = setting.screen.get_width() - setting.screen.get_width()/2.5
    volume_bar_y = setting.screen.get_height()/7.9 + i * 45

    # 음량 조절 바
    volume_bar = pygame.draw.rect(setting.screen, white, (volume_bar_x, volume_bar_y, volume_bar_width, volume_bar_height), 2)

    # 음량 조절 바의 현재 음량 위치
    if not is_first:
        setting.set_music_by_index(i, input_volume)
    volume = get_volume(i)

    # 음량 조절 바의 현재 음량 위치
    volume_position = int(volume_bar_width * volume)
    volume_bar_inner = pygame.draw.rect(setting.screen, white, (volume_bar_x, volume_bar_y, volume_position, volume_bar_height))

    return volume_bar

def change_process(option, is_next):
    flag = True
    if option == 0:
        global MOD
        if (MOD == 0):
            MOD = 1
        else:
            MOD = 0
        setting.set_mod(MOD)
    elif option == 1:
        global SOUND
        if SOUND:
            SOUND = False
        else:
            SOUND = True
        setting.set_sound(SOUND)
    elif option == 2:
        global SCREEN
        if is_next:
            if SCREEN < 2:
                SCREEN = SCREEN + 1
            else:
                SCREEN = 0
        else:
            if SCREEN != 0:
                SCREEN = SCREEN - 1
            else:
                SCREEN = 2
        setting.set_screen(SCREEN)
    elif option == 3:
        global COLORBLIND
        if COLORBLIND:
            COLORBLIND = False
        else:
            COLORBLIND = True
        setting.set_colorblind(COLORBLIND)
    return flag

def menu_process(option, is_next, is_enter, is_option):
    global control_flag
    global music_flag

    mod_len = len(setting.get_mod_list())
    flag = True
    if option < mod_len and not is_option:
        if not control_flag:
            change_process(option, is_next)
    elif option == mod_len:
        if is_enter:
            print("set control")
            control_flag = True
    elif option == (mod_len + 1):
        if is_enter:
            print("set sound detail")
            music_flag = True
    elif option == (mod_len + 2):
        if is_enter:
            print("set rollback")
            setting.mod_back()
    elif option == (mod_len + 3):
        if is_enter:
            print("save mod setting")
            setting.save()
    elif option == (mod_len + 4):
        if is_enter:
            print("menu exit")
            flag = False
            setting.main_menu = True
    return flag

def change_control_process(option, value, is_clicked):
    global initial_control
    if not is_clicked:
        initial_control[0][option] = pygame.key.name(value) # 문자 저장
        initial_control[1][option] = value # 수 저장

def control_process(option, value, is_clicked):
    global control_flag
    global initial_control
    control_len = len(setting.get_control_list())
    flag = True
    if option < control_len:
        if control_flag:
            change_control_process(option, value, is_clicked)
    elif option == control_len:
        if((value == setting.get_keymap_check()) or is_clicked):
            print("set rollback")
            setting.control_back()
            initial_control = setting.get_control_list_all()
    elif option == (control_len + 1):
        if((value == setting.get_keymap_check()) or is_clicked):
            print("save control setting")
            for i, value in enumerate(initial_control[1]):
                setting.set_keymap_by_index(i, value)
            setting.save()
    else:
        if((value == setting.get_keymap_check()) or is_clicked):
            print("back to setting menu")
            flag = False
    return flag

def change_music_process(option, value, is_clicked, is_add):
    def get_value(value, is_clicked, is_add):
        if not is_clicked:
            current_value = setting.get_music_total(option)
            if is_add:
                if((current_value + value) <= 1):
                    value = current_value + value
                else:
                    value = 1.0
            else:
                if((current_value - value) >= 0):
                    value = current_value - value
                else:
                    value = 0.0
        return value

    if not is_clicked:
        result_value = "{:.4f}".format(get_value(value, is_clicked, is_add))
        if option == 0: # all
            setting.set_music_all(float(result_value))
        elif option == 1: # BM
            setting.set_music_bm(float(result_value))
        else: # CE
            setting.set_music_se(float(result_value))

def music_process(option, value, is_clicked, is_add):
    global music_flag

    music_len = len(setting.get_music_list())
    func_music_flag = True
    func_menu_flag = True

    if option < music_len:
        if music_flag:
            if not is_clicked:
                change_music_process(option, value, is_clicked, is_add)
            else:
                setting.set_music_by_index(option, value)
    elif option == music_len:
        print("set rollback")
        setting.music_back()
    elif option == (music_len + 1):
        global SOUND
        if SOUND:
            print("sound off")
            SOUND = False
        else:
            print("sound on")
            SOUND = True
        setting.set_sound(SOUND)
        setting.save()
    elif option == (music_len + 2):
        print("back to setting menu")
        func_music_flag = False
    else:
        print("close menu")
        func_music_flag = False
        func_menu_flag = False
    return (func_menu_flag, func_music_flag)

# 키보드의 상태를 빠르게 확인하여 키가 눌린 상태인지 확인
def change_volume_bar():
    if music_flag:
        checked_key = pygame.key.get_pressed()
        if checked_key[setting.get_keymap_check()] :
            if(selected_option < len(setting.get_music_list())):
                music_process(selected_option, 0.005, False, True)
        elif checked_key[setting.get_keymap_right()]:
            if(selected_option < len(setting.get_music_list())):
                music_process(selected_option, 0.005, False, True)
        elif checked_key[setting.get_keymap_left()]:
            if(selected_option < len(setting.get_music_list())):
                music_process(selected_option, 0.005, False, False)

def get_menu(main_flag, keymap_flag, sound_flag):
    global menu_flag
    global control_flag
    global music_flag

    global selected_option
    global volume_bar_width
    global volume_bar_height

    menu_flag = main_flag
    control_flag = keymap_flag
    music_flag = sound_flag

    while menu_flag:
        font = pygame.font.Font('freesansbold.ttf', int(pygame.Surface.get_height(setting.screen)*0.05))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_flag = False
                setting.running = False
                
            elif event.type == pygame.KEYDOWN:
                if not control_flag and not music_flag:
                    # 모드 설정
                    if event.key == setting.get_keymap_up():
                        selected_option = (selected_option - 1) % len(options)
                    elif event.key == setting.get_keymap_down():
                        selected_option = (selected_option + 1) % len(options)
                    elif event.key == setting.get_keymap_check():
                        menu_flag = menu_process(selected_option, True, True, False)
                    elif event.key == setting.get_keymap_right():
                        menu_flag = menu_process(selected_option, True, False, False)
                    elif event.key == setting.get_keymap_left():
                        menu_flag = menu_process(selected_option, False, False, False)
                elif not control_flag and music_flag:
                    # 볼륨 설정
                    if event.key == setting.get_keymap_up():
                        selected_option = (selected_option - 1) % len(options_music)
                    elif event.key == setting.get_keymap_down():
                        selected_option = (selected_option + 1) % len(options_music)
                    elif event.key == setting.get_keymap_check():
                        if(selected_option >= len(setting.get_music_list())):
                            (menu_flag, music_flag) = music_process(selected_option, 0.0, False, False)
                else:
                    # 키맵 설정
                    if event.key == setting.get_keymap_up():
                        selected_option = (selected_option - 1) % len(options_control)
                    elif event.key == setting.get_keymap_down():
                        selected_option = (selected_option + 1) % len(options_control)
                    else:
                        print("event.key : ", event.key)
                        control_flag = control_process(selected_option, event.key, False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if control_flag:
                    option_list = options_control
                elif music_flag:
                    option_list = options_music
                else:
                    option_list = options
                for i, option in enumerate(option_list):
                    # 선택된 옵션 처리
                    option_text = font.render(option, True, black)
                    option_rect = get_common_option_rec(option_text, True, i)
                    font_color = black

                    if control_flag:
                        if i < len(setting.get_control_list()):
                            font_value = initial_control[0][i]
                        else:
                            font_value = ''
                    elif music_flag:
                        if i < len(setting.get_music_list()):
                            font_value = str(setting.get_music_total(i) * 100)
                            font_color = 'light gray' # black
                        else:
                            if i == (len(setting.get_music_list()) + 1):
                                font_value = setting.get_mod_all(1)
                            else:
                                font_value = ''
                    else:
                        font_value = setting.get_mod_all(i)
                    value_text = font.render(font_value, True, font_color)
                    
                    if music_flag:
                        value_rect = get_volume_bar(i, True, 0, value_text)
                    else:
                        value_rect = get_common_option_rec(value_text, False, i)

                    if option_rect.collidepoint(mouse_pos):
                        selected_option = i
                        if control_flag:
                            control_flag = control_process(selected_option, 0, True)
                        elif music_flag:
                            volume = get_volume(selected_option)
                            (menu_flag, music_flag) = music_process(selected_option, volume, True, False)
                        else:
                            menu_flag = menu_process(selected_option, True, True, True)
                    if value_rect.collidepoint(mouse_pos):
                        selected_option = i
                        if control_flag:
                            control_flag = control_process(selected_option, 0, True)
                        elif music_flag:
                            change_volume_bar()
                            volume = get_volume(selected_option)
                            if(i < len(setting.get_music_list()) or i == (len(setting.get_music_list()) + 1)):
                                music_process(selected_option, volume, True, True)
                        else:
                            menu_flag = change_process(selected_option, True)

        change_volume_bar()
        
        # 메뉴 화면 그리기
        # screen.fill(black)

        # 동원 기여
        setting.screen.blit(pygame.transform.scale(background,(pygame.Surface.get_width(setting.screen),pygame.Surface.get_height(setting.screen))),(0,0))
        pygame.draw.rect(setting.screen, 'light gray',(pygame.Surface.get_width(setting.screen)*0.187,pygame.Surface.get_height(setting.screen)*0.083,pygame.Surface.get_width(setting.screen)*0.625,pygame.Surface.get_height(setting.screen)*0.83) ,0,5)
        pygame.draw.rect(setting.screen, 'dark gray', (pygame.Surface.get_width(setting.screen)*0.187,pygame.Surface.get_height(setting.screen)*0.083,pygame.Surface.get_width(setting.screen)*0.625,pygame.Surface.get_height(setting.screen)*0.83),10,5)

        if control_flag:
            option_list = options_control
        elif music_flag:
            option_list = options_music
        else:
            option_list = options

        for i, option in enumerate(option_list):
            font_color = black

            # options 출력
            if i == selected_option:
                option_text = font.render(option, True, 'dark gray') # (option, True, yellow) 
            else:
                option_text = font.render(option, True, black)
            option_rect = get_common_option_rec(option_text, True, i)
            setting.screen.blit(option_text, option_rect)

            #options value 출력
            if control_flag:
                if i < len(setting.get_control_list()):
                    font_value = initial_control[0][i]
                else:
                    font_value = ''
            elif music_flag:
                if i < len(setting.get_music_list()):
                    font_value = str("{:.0f}".format(setting.get_music_total(i) * 100))
                    font_color = 'light gray' # black
                else:
                    if i == (len(setting.get_music_list()) + 1):
                        font_value = setting.get_mod_all(1)
                    else:
                        font_value = ''
            else:
                font_value = setting.get_mod_all(i)

            value_text = font.render(font_value, True, font_color)
            value_rect = get_common_option_rec(value_text, False, i)

            # 음량바 그리기
            if music_flag and (i < len(setting.get_music_list())):
                value_rect = get_volume_bar(i, True, 0, value_text)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    volume_bar_x = setting.screen.get_width() - setting.screen.get_width()/2.5

                    if value_rect.collidepoint(mouse_pos):
                        selected_option = i
                        (mouse_x, mouse_y) = mouse_pos
                        volume = int((mouse_x - (volume_bar_x - volume_bar_width)) / volume_bar_width * 100) # 음량 값 조절
                        value_rect = get_volume_bar(i, False, volume/100, value_text)
            setting.screen.blit(value_text, value_rect)
        
        pygame.display.flip()

# 메뉴 실행 테스트
# get_menu(True, False, False)

# pygame.quit()
