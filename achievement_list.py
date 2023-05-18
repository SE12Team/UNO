import pygame
import achievement
import setting


# 화면 크기 설정
SCREEN_WIDTH = pygame.Surface.get_width(setting.screen)
SCREEN_HEIGHT = pygame.Surface.get_height(setting.screen)

# 화면 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('업적 리스트')

BLACK = (0, 0, 0)
GRAY = (120, 120, 120)
RECT_GRAY = (170, 170, 170)
WHITE = (255, 255, 255)

pygame.init()

# 메인 루프
def show_achievement(achiev_flag):
    # 스크롤 관련 변수 초기화
    scroll_speed = 2
    scroll_position = 0

    font = achievement.get_font()
    title_font = achievement.get_title_font()
    icons = achievement.get_icons()
    titles = achievement.get_titles()[0]
    contents = achievement.get_contents()[0]
    dates = achievement.get_dates()

    while achiev_flag:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                achiev_flag = False

        # 배경 그리기
        screen.fill(WHITE)

        # 스크롤 된 업적 리스트 그리기
        y = 0
        for index in range(achievement.get_length()):
            # 각 업적 칸의 위치 계산
            font_color = BLACK
            rect_color = WHITE
            if not achievement.get_state(index):
                font_color = GRAY

            rect = pygame.Rect(SCREEN_WIDTH/4, y - scroll_position, SCREEN_WIDTH, icons[index].get_width())

            # 각 업적 칸 그리기
            pygame.draw.rect(screen, rect_color, rect)

            # 아이콘 그리기
            screen.blit(icons[index], (rect.left + 10, rect.top))

            # 업적 타이틀 그리기
            title_text = title_font.render(titles[index], True, font_color)
            screen.blit(title_text, (rect.left + 100, rect.top + 20))

            # 업적 내용 그리기
            description_text = font.render(contents[index], True, font_color)
            screen.blit(description_text, (rect.left + 100, rect.top + 40))

            # 업적 달성 일자 그리기
            if achievement.get_state(index):
                date_text = font.render(dates[index], True, font_color)
                screen.blit(date_text, (rect.left + 100, rect.top + 60))
            # 다음 업적 칸을 위해 y 값 증가
            y += 100

        # 스크롤 업데이트
        keys = pygame.key.get_pressed()
        if keys[setting.get_keymap_up()]:
            scroll_position += scroll_speed
        if keys[setting.get_keymap_down()]:
            scroll_position -= scroll_speed

        # 스크롤 범위 제한
        max_scroll_position = int(achievement.get_length()) * 100 - SCREEN_HEIGHT
        scroll_position = max(0, min(scroll_position, max_scroll_position))

        # 화면 업데이트
        pygame.display.flip()

# 게임 종료
# pygame.quit()