import pygame #遊戲模組

pygame.init() #遊戲模組啟動
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #產生畫布
pygame.display.set_caption("My first pygame!")

BLACK  = (0,0,0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN   = (0, 255, 255)
MEG    = (255, 0, 255)
GRAY   = (192, 192, 192)

displayscreen.fill(GRAY) #讓顏色填滿畫布
#pygame.draw.line(畫布名稱, color, start, end, thickness)
pygame.draw.line(displayscreen, GREEN, (0, WINDOW_HEIGHT//2), (WINDOW_WIDTH,WINDOW_HEIGHT//2), 3)
pygame.draw.line(displayscreen, RED, (WINDOW_WIDTH//2, 0), (WINDOW_WIDTH//2,WINDOW_HEIGHT), 5)

#pygame.draw.circle(畫布名稱，顏色，中心點，半徑，thickness) thickness=0(填滿), 1,2...10:線條寬度
pygame.draw.circle(displayscreen, CYAN, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(displayscreen, CYAN, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 180, 0)

#pygame.draw.rect(畫布名稱，顏色， (topleft-x, topleft-y, width, height), thickness) thickness=0:填滿, 1, 2, ...10線條寬度
pygame.draw.rect(displayscreen, BLUE, (0, 0, WINDOW_WIDTH, 100), 0 )

running = True
while running:
    for event in pygame.event.get(): #抓取畫布上所有的事件
        #print(event)
        if event.type == pygame.QUIT: #事件的type==Quit(按下結束鍵)
            running = False

    pygame.display.update() #畫布的更新

pygame.quit() #遊戲模組結束