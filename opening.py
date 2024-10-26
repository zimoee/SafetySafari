import pygame
import sys
import os

# 初始化 Pygame
pygame.init()

# 設定顯示視窗大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Map Adventure")

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 玩家設定
player_pos = [400, 300]
player_size = 50

# 學校的位置
school_rect = pygame.Rect(600, 400, 100, 100)

# 字體設定
font = pygame.font.Font(None, 60)

# 顯示歡迎畫面
def show_welcome_screen():
    screen.fill(WHITE)
    welcome_text = font.render('Welcome to XXX World', True, BLACK)
    text_rect = welcome_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(welcome_text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)  # 停留 3 秒

    screen.fill(WHITE)
    going_to_school_text = font.render('XXX is on his way to school...', True, BLACK)
    text_rect = going_to_school_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(going_to_school_text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)  # 停留 3 秒

# 顯示結束提示畫面
def show_end_screen():
    screen.fill(WHITE)
    end_text = font.render('As soon as he steps into the classroom,', True, BLACK)
    text_rect1 = end_text.get_rect(center=(screen_width // 2, screen_height // 2 - 30))
    screen.blit(end_text, text_rect1)

    end_text2 = font.render('the earthquake struck...', True, BLACK)
    text_rect2 = end_text2.get_rect(center=(screen_width // 2, screen_height // 2 + 30))
    screen.blit(end_text2, text_rect2)

    pygame.display.flip()
    pygame.time.delay(3000)  # 停留 3 秒

# 開始遊戲之前顯示歡迎畫面
show_welcome_screen()

# 主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5

    # 碰到學校時執行 try.py 並顯示結束提示
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    if player_rect.colliderect(school_rect):
        show_end_screen()  # 顯示結束提示
        os.system('python main.py')  # 開啟並運行 try.py
        pygame.quit()  # 結束 Pygame
        sys.exit()  # 結束程式

    # 清空畫面
    screen.fill(WHITE)

    # 畫學校的位置
    pygame.draw.rect(screen, GREEN, school_rect)
    # 畫玩家
    pygame.draw.rect(screen, RED, player_rect)

    # 更新畫面
    pygame.display.flip()
    pygame.time.delay(30)

# 結束 Pygame
pygame.quit()
sys.exit()
