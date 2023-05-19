import pygame
import configparser, os
import setting

# Pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = pygame.Surface.get_width(setting.screen)
SCREEN_HEIGHT = pygame.Surface.get_height(setting.screen)

thisfolder = os.path.dirname(os.path.abspath(__file__))
inifile = os.path.join(thisfolder, 'achievement.ini')
config = configparser.RawConfigParser()
config.read(inifile)

# Save Settings
def save():
    with open(inifile, 'w') as configfile:
        config.write(configfile)

def set_date(index, date):
    # date = datetime.datetime.now()
    date_str = str(date.year) + '/' + str(date.month) + '/' + str(date.day)
    config.set('date', str(index), date_str)
    save()

def set_state_true(index):
    config.set('acheivement', str(index), bool(True))
    save()

def set_state(index, date):
    set_state_true(index)
    set_date(index, date)

def get_state(index):
    return config.getboolean('acheivement', str(index))

def get_length():
    acheiv_list = config.items('acheivement')
    return len(acheiv_list)

# 도전과제 아이콘 로드
def get_icons():
    icon_images = []
    icon_locked_images = []
    for file_name in os.listdir("./data/images/icons"):
        if file_name.endswith(".png"):
            icon = pygame.image.load(os.path.join("./data/images/icons", file_name))
            scaled_icon = pygame.transform.scale(icon, (icon.get_width()/2.2, icon.get_height()/2.2))
            icon_images.append(scaled_icon)
    for file_name in os.listdir("./data/images/icons/locked"):
        if file_name.endswith(".png"):
            icon = pygame.image.load(os.path.join("./data/images/icons/locked", file_name))
            scaled_icon = pygame.transform.scale(icon, (icon.get_width()/2.2, icon.get_height()/2.2))
            icon_locked_images.append(scaled_icon)
    
    for index in range(get_length()):
        state = get_state(index) 
        if not state:
            icon_images[index] = icon_locked_images[index]
    return icon_images

def get_titles():
    challenge_titles = []
    for file_name in os.listdir("./data/achivement"):
        if file_name.endswith("title.txt"):
            with open(os.path.join("./data/achivement", file_name), "r", encoding="utf-8") as f:
                challenge_titles.append(f.read().split('\n'))
    return challenge_titles

def get_contents():
    challenge_texts = []
    for file_name in os.listdir("./data/achivement"):
        if file_name.endswith("contents.txt"):
            with open(os.path.join("./data/achivement", file_name), "r", encoding="utf-8") as f:
                challenge_texts.append(f.read().split('\n'))
    return challenge_texts

def get_dates():
    challenge_dates = []
    for index in range(get_length()):
        date = config.get('date', str(index))
        challenge_dates.append(date)
    return challenge_dates

def get_font():
    font_path = "./data/fonts/NanumBarunGothic.ttf"
    font = pygame.font.Font(font_path, int(SCREEN_WIDTH/60))
    return font

def get_title_font():
    font_path = "./data/fonts/NanumBarunGothic.ttf"
    font = pygame.font.Font(font_path, int(SCREEN_WIDTH/50))
    font.set_bold(True)
    return font