import pygame
import sys
import os
import time

pygame.init()

# 設定顯示視窗大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("9am Class")

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 玩家設定
player_pos = [400, 300]
player_size = 50

# 學校的位置和大小
school_rect = pygame.Rect(600, 400, 100, 100)

# 字體設定
font = pygame.font.Font(None, 60)

# 載入地圖圖片
map_image = pygame.image.load("school.png")
map_image = pygame.transform.scale(map_image, (screen_width, screen_height))

# 創建學校的透明表面
school_surface = pygame.Surface((school_rect.width, school_rect.height))
school_surface.fill(GREEN) 
school_surface.set_alpha(0)

# 顯示歡迎畫面
def show_welcome_screen():
    screen.fill(WHITE)
    welcome_text = font.render('Welcome to your first day at UofT', True, BLACK)
    text_rect = welcome_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(welcome_text, text_rect)
    pygame.display.flip()
    time.sleep(3)

    screen.fill(WHITE)
    going_to_school_text = font.render("You're on your way to class...", True, BLACK)
    text_rect = going_to_school_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(going_to_school_text, text_rect)
    pygame.display.flip()
    time.sleep(3)

# 顯示結束提示畫面
def show_end_screen():
    screen.fill(WHITE)
    end_text = font.render('As soon as you walk into the classroom,', True, BLACK)
    text_rect1 = end_text.get_rect(center=(screen_width // 2, screen_height // 2 - 30))
    screen.blit(end_text, text_rect1)

    end_text2 = font.render('the earthquake struck...', True, BLACK)
    text_rect2 = end_text2.get_rect(center=(screen_width // 2, screen_height // 2 + 30))
    screen.blit(end_text2, text_rect2)

    pygame.display.flip()
    pygame.time.delay(3000)

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
        show_end_screen()
        os.system('python main.py')
        pygame.quit() 
        sys.exit()

    screen.fill(WHITE)
    screen.blit(map_image, (0, 0)) 
    screen.blit(school_surface, school_rect.topleft)

    # 畫玩家
    pygame.draw.rect(screen, RED, player_rect)

    # 更新畫面
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()
