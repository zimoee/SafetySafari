import pygame
import sys

# 初始化 Pygame
pygame.init()

# 設定窗口大小
screen = pygame.display.set_mode((900, 450))

# 設定顏色
WHITE = (255, 255, 255)
FONT_COLOR = (0, 0, 0)

# 載入圖片
program_image = pygame.image.load('program.png')
open_space_image = pygame.image.load('open_space.png')

# 顯示提示的函數
def show_message(message):
    font = pygame.font.Font(None, 30)
    text = font.render(message, True, FONT_COLOR)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    screen.fill(WHITE)
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)

# 繪製圖片的函數
def draw_images():
    screen.fill(WHITE)
    screen.blit(program_image, (0, 0))
    screen.blit(open_space_image, (450, 0))
    pygame.display.flip()

# 顯示結果的函數
def show_result(result):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 30)
    result_text = font.render(result, True, FONT_COLOR)
    text_rect = result_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    
    # 按鈕的文字
    continue_text = font.render("Continue", True, FONT_COLOR)
    continue_rect = continue_text.get_rect(center=(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50))
    
    exit_text = font.render("Exit", True, FONT_COLOR)
    exit_rect = exit_text.get_rect(center=(screen.get_width() // 2 + 100, screen.get_height() // 2 + 50))

    screen.blit(result_text, text_rect)
    screen.blit(continue_text, continue_rect)
    screen.blit(exit_text, exit_rect)

    pygame.display.flip()

    return continue_rect, exit_rect

# 顯示開始提示
show_message("You're on your way home and another earthquake hits")
show_message("You have to choose the safer path...")

# 主循環
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            # 檢查點擊的位置
            if 0 <= mouse_x <= 450: 
                result_message = "You lost!"
            elif 450 <= mouse_x <= 900:
                result_message = "You won!"
            else:
                continue 

            # 顯示結果和按鈕
            continue_button_rect, exit_button_rect = show_result(result_message)

            # 等待用戶點擊按鈕
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        if continue_button_rect.collidepoint(mouse_x, mouse_y):
                            draw_images()
                            break
                        elif exit_button_rect.collidepoint(mouse_x, mouse_y):
                            pygame.quit()
                            sys.exit()

    draw_images()
