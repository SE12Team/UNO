import pygame
import pygame_gui
import setting
from UI import *

pygame.init()


    
    
def gameUiLoop(computer_num): 
    #창 가로세로 변수지정  
    width = 800
    height = 600
    
    #스크린, 배경화면 지정
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    gameBackground = pygame.image.load("data/images/board.png")

    #pygame_gui UIManager 지정
    ui_manager = pygame_gui.UIManager((width, height))

    
    clock = pygame.time.Clock()
    
    #UI파일의 Ui클래스 인스턴스 생성
    ui = Ui(ui_manager)
    
    #Game 메인 루프
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        
        
        #이벤트 큐(이벤트 감지)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #창 크기가 바뀌면
            elif event.type == pygame.VIDEORESIZE:
                videoResize(event,screen,gameBackground)
                
                
            ui_manager.process_events(event)
       
        screen.blit(pygame.transform.scale(gameBackground,(pygame.Surface.get_width(screen),pygame.Surface.get_height(screen))),(0,0))
        
        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)
        
        ui.computerUI(computer_num)
        
        
        pygame.display.flip() # 화면을 업데이트
        pygame.display.update()
        
gameUiLoop(4)