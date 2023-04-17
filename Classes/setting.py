import pygame
import configparser, os

thisfolder = os.path.dirname(os.path.abspath(__file__))
inifile = os.path.join(thisfolder, 'settings.ini')
inifile_sound = os.path.join(thisfolder, 'settings_sound.ini')

config = configparser.RawConfigParser()
config_sound = configparser.RawConfigParser()
config.read(inifile)
config_sound.read(inifile_sound)

# Set Mod
def set_mod(mod):
    config.set('Mod', 'mod', str(mod))
def set_sound(sound):
    config.set('Mod', 'Sound', str(sound))
def set_screen(size):
    config.set('Mod', 'Screen', str(size))
    screen_size = get_screen(size)
    pygame.display.set_mode(screen_size, pygame.RESIZABLE)
def set_colorblind(state):
    config.set('Mod', 'colorblind', str(state))

# Set Control
def set_keymap_left(key):
    config.set('Control', 'left', str(key))
def set_keymap_right(key):
    config.set('Control', 'right', str(key))
def set_keymap_up(key):
    config.set('Control', 'up', str(key))
def set_keymap_down(key):
    config.set('Control', 'down', str(key))
def set_keymap_uno(key):
    config.set('Control', 'uno', str(key))
def set_keymap_time(key):
    config.set('Control', 'time', str(key))
def set_keymap_check(key):
    config.set('Control', 'check', str(key))
def set_keymap_by_index(index, key):
    if index == 0:
        set_keymap_left(key)
    elif index == 1:
        set_keymap_right(key)
    elif index == 2:
        set_keymap_up(key)
    elif index == 3:
        set_keymap_down(key)
    elif index == 4:
        set_keymap_uno(key)
    elif index == 5:
        set_keymap_time(key)
    elif index == 6:
        set_keymap_check(key)

# Set Sound
def set_music_bm(value):
    if value > 1.0:
        value-= 1.0
    config_sound.set('Sound', 'BM', str(value))
    save_sound() # 음악 설정은 바뀐 뒤 바로 적용
def set_music_se(value):
    if value > 1.0:
        value-= 1.0
    config_sound.set('Sound', 'SE', str(value))
    save_sound() # 음악 설정은 바뀐 뒤 바로 적용
def set_music_all(value):
    if value > 1.0:
        value-= 1.0
    config_sound.set('Sound', 'all', str(value))
    set_music_bm(value)
    set_music_se(value)
    save_sound() # 음악 설정은 바뀐 뒤 바로 적용
def set_music_by_index(index, value):
    if index == 0:
        set_music_all(value)
    elif index == 1:
        set_music_bm(value)
    elif index == 2:
        set_music_se(value)
    save_sound()

# Get Mod
def get_mod_num():
    return config.getint('Mod', 'mod')
def get_sound_bool():
    return config.getboolean('Mod', 'Sound')
def get_screen_num():
    return config.getint('Mod', 'Screen')
def get_colorblind_bool():
    return config.getboolean('Mod', 'colorblind')

def get_mod(value):
    if(value == 0):
        return 'Single Play'
    elif(value == 1):
        return 'Multi Play'
    else:
        return 'Story Play'
def get_sound(value):
    if value:
        return "ON"
    else:
        return "OFF"
def get_screen(value):
    if(value == 0):
        return (800, 600)
    elif(value == 1):
        return (1280, 960)
    else:
        return (1600, 1200)
def get_colorblind(value):
    if value:
        return "ON"
    else:
        return "OFF"

def get_mod_all(index):
    if(index == 0):
        return str(get_mod(get_mod_num()))
    elif(index == 1):
        return str(get_sound(get_sound_bool()))
    elif(index == 2):
        return str(get_screen(get_screen_num())[0]) + 'x' + str(get_screen(get_screen_num())[1])
    elif(index == 3):
        return str(get_colorblind(get_colorblind_bool()))
    else:
        return ''

# Get Control
def get_keymap_left():
    return config.getint('Control', 'left')
def get_keymap_right():
    return config.getint('Control', 'right')
def get_keymap_up():
    return config.getint('Control', 'up')
def get_keymap_down():
    return config.getint('Control', 'down')
def get_keymap_uno():
    return config.getint('Control', 'uno')
def get_keymap_time():
    return config.getint('Control', 'time')
def get_keymap_check():
    return config.getint('Control', 'check')

def get_keymap_all(index):
    if(index == 0):
        return str(pygame.key.name(get_keymap_left()))
    elif(index == 1):
        return str(pygame.key.name(get_keymap_right()))
    elif(index == 2):
        return str(pygame.key.name(get_keymap_up()))
    elif(index == 3):
        return str(pygame.key.name(get_keymap_down()))
    elif(index == 4):
        return str(pygame.key.name(get_keymap_uno()))
    elif(index == 5):
        return str(pygame.key.name(get_keymap_time()))
    elif(index == 6):
        return str(pygame.key.name(get_keymap_check()))
    else:
        return ''

# Get Sound
def get_music_all():
    if get_sound_bool():
        value = float(config_sound.get('Sound', 'all'))
        if value > 1.0:
            value -= 1.0
    else:
        value = 0.0
    return value
def get_music_bm():
    if get_sound_bool():
        value = float(config_sound.get('Sound', 'BM'))
        if value > 1.0:
            value -= 1.0
    else:
        value = 0.0
    return value
def get_music_se():
    if get_sound_bool():
        value = float(config_sound.get('Sound', 'SE'))
        if value > 1.0:
            value -= 1.0
    else:
        value = 0.0
    return value

def get_music_total(index):
    if index == 0:
        return get_music_all()
    elif index == 1:
        return get_music_bm()
    elif index == 2:
        return get_music_se()
    else:
        return ''

# Get Section's option list
def get_mod_list():
    return config.options('Mod')
def get_control_list():
    return config.options('Control')
def get_control_list_all():
    control_list = []
    control_list_num = []
    control_tuple = config.items('Control')
    for control in control_tuple:
        value = int(control[1])
        control_list.append(pygame.key.name(value))
        control_list_num.append(value)
    return (control_list, control_list_num)
def get_music_list():
    original_music_list = config_sound.options('Sound')
    music_list = []
    for option in original_music_list:
        music_list.append(option.upper())
    return music_list


# Rollback settings
def mod_back():
    set_mod(0) # SOLO MOD
    set_sound(True) # ON
    set_screen(0) # 800x600
    set_colorblind(False) # OFF
def control_back():
    set_keymap_left(1073741904) # ←
    set_keymap_right(1073741903) # →
    set_keymap_up(1073741906) # ↑
    set_keymap_down(1073741905) # ↓
    set_keymap_uno(117) # u
    set_keymap_time(116) # t
    set_keymap_check(13) # Enter
def music_back():
    set_music_all(0.8)
    set_music_bm(0.8)
    set_music_se(0.8)
    save_sound() # 음악 설정은 바뀐 뒤 바로 적용

# Save Settings
def save():
    with open(inifile, 'w') as configfile:
        config.write(configfile)
        
def save_sound():
    with open(inifile_sound, 'w') as configfile_sound:
        config_sound.write(configfile_sound)

# 동원 기여
running = True
main_menu = True
screen = pygame.display.set_mode(((get_screen(get_screen_num()))), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
background = pygame.image.load("/Users/kimdogyeong/Desktop/Uno_project/images/menuBackground.png")
play_background = pygame.image.load("/Users/kimdogyeong/Desktop/Uno_project/images/playBackground.png")