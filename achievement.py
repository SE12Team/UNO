import pygame
import configparser, os
import setting

# Pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = pygame.display.get_surface().get_width() # 800
SCREEN_HEIGHT = pygame.display.get_surface().get_height() # 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("도전과제 리스트 테스트")

# 한글 폰트 로드
font_path = "./data/fonts/NanumBarunGothic.ttf"
font = pygame.font.Font(font_path, int(SCREEN_WIDTH/60))

thisfolder = os.path.dirname(os.path.abspath(__file__))
inifile = os.path.join(thisfolder, 'achievement.ini')
config = configparser.RawConfigParser()
config.read(inifile)

# Save Settings
def save():
    with open(inifile, 'w') as configfile:
        config.write(configfile)

# 업적 달성 여부
def get_state(index):
    return config.getboolean('acheivement', index)

# 업적 달성 만들기
def set_state_true(index):
    save()
    return config.set('acheivement', index, bool(True))

# 도전과제 아이콘 로드
icon_images = []
for file_name in os.listdir("./data/images/icons"):
    if file_name.endswith(".png"):
        icon = pygame.image.load(os.path.join("./data/images/icons", file_name))
        scaled_icon = pygame.transform.scale(icon, (icon.get_width()/1.8, icon.get_height()/1.8))
        icon_images.append(scaled_icon)

# 도전과제 설명 로드
challenge_texts = []
for file_name in os.listdir("./data/achivement"):
    if file_name.endswith(".txt"):
        with open(os.path.join("./data/achivement", file_name), "r", encoding="utf-8") as f:
            challenge_texts.append(f.read().split('\n'))

# 스크롤바 설정
scrollbar_width = 15
scrollbar_height = SCREEN_HEIGHT * SCREEN_HEIGHT / (len(icon_images) * 100)
scrollbar_rect = pygame.Rect(SCREEN_WIDTH - scrollbar_width, 0, scrollbar_width, SCREEN_HEIGHT)

# 화면 업데이트 함수
def update_screen(scroll_pos):
    screen.fill((255, 255, 255))
    for i, icon_image in enumerate(icon_images):
        # 아이콘 위치 계산
        icon_x = SCREEN_WIDTH / 5
        icon_y = i * 100 - scroll_pos
        # 아이콘 그리기
        screen.blit(icon_image, (icon_x, icon_y))
        # 도전과제 설명 그리기
        challenge_text_surface = font.render(' '.join(challenge_texts[0][i]), True, (0, 0, 0))
        screen.blit(challenge_text_surface, (icon_x + icon_images[0].get_width() + 20, icon_y + 40))
    # 스크롤바 그리기
    scrollbar_rect.y = scroll_pos * (SCREEN_HEIGHT - scrollbar_height) / (len(icon_images) * 100 - SCREEN_HEIGHT)
    pygame.draw.rect(screen, (192, 192, 192), scrollbar_rect)

# 초기 스크롤 위치
scroll_pos = 0

# 게임 루프
clock = pygame.time.Clock()
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            scroll_pos = max(scroll_pos - 100, 0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            scroll_pos = min(scroll_pos + 100, len(icon_images) * 100 - SCREEN_HEIGHT)

    # 화면 업데이트
    update_screen(scroll_pos)

    # 화면 갱신
    pygame.display.flip()

    # 프레임 제한
    clock.tick(60)

