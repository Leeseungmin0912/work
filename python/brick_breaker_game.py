import pygame
import sys
from pygame.locals import *
import time

# 파이게임 초기화
pygame.init()

# 파이게임 캡틴 설정
pygame.display.set_caption('Brick Breaker Game')

# 게임 화면 설정
screen = pygame.display.set_mode((800, 600))

# 패들 설정
paddle = pygame.Rect(400, 500, 60, 10)

# 공 리스트 초기화
balls = []
ball_speeds = []
ball_count = 0

# 벽돌 설정
bricks = []

# 난이도 증가 타이머
start_time = pygame.time.get_ticks()
difficult_interval = 5000  # 밀리초
increase_speeds_factor = 0.1

# 점수 관련 변수
game_start_time = None
elapsed_time = 0

def draw_text(text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def show_end_buttons():
    button_width = 200
    button_height = 50
    button_x = screen.get_width() / 2 - button_width / 2
    main_button_y = screen.get_height() / 2 + 50
    restart_button_y = screen.get_height() / 2 + 110

    # 메인 메뉴 버튼
    pygame.draw.rect(screen, (255, 255, 255), (button_x, main_button_y, button_width, button_height))
    draw_text('Main Menu', 36, screen.get_width() / 2, main_button_y + 10, (0, 0, 0))

    # 다시 시작 버튼
    pygame.draw.rect(screen, (255, 255, 255), (button_x, restart_button_y, button_width, button_height))
    draw_text('Restart', 36, screen.get_width() / 2, restart_button_y + 10, (0, 0, 0))

    pygame.display.flip()

    # 버튼 클릭 이벤트 처리
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_x <= mouse_pos[0] <= button_x + button_width:
                    if main_button_y <= mouse_pos[1] <= main_button_y + button_height:
                        main_menu()  # 메인 메뉴로 이동
                    elif restart_button_y <= mouse_pos[1] <= restart_button_y + button_height:
                        start_game()  # 다시 시작

#게임 패배 함수
def game_over():
    global elapsed_time
    elapsed_time = time.time() - game_start_time
    draw_text('Player Lose!', 48, screen.get_width() / 2, screen.get_height() / 2 - 50)
    draw_text(f'Time: {int(elapsed_time)}s', 36, screen.get_width() / 2, screen.get_height() / 2)
    pygame.display.flip()
    pygame.time.wait(1000)
    show_end_buttons()

#게임 승리 함수
def victory():
    global elapsed_time
    elapsed_time = time.time() - game_start_time
    draw_text('Player Win!', 48, screen.get_width() / 2, screen.get_height() / 2 - 50)
    draw_text(f'Time: {int(elapsed_time)}s', 36, screen.get_width() / 2, screen.get_height() / 2)
    pygame.display.flip()
    pygame.time.wait(1000)
    show_end_buttons()

#메인 메뉴 함수
def main_menu():
    button_width = 200
    button_height = 50
    button_x = screen.get_width() / 2 - button_width / 2
    button_y = screen.get_height() / 2 - button_height / 2

    while True:
        screen.fill((0, 0, 0))  # 배경 색상
        draw_text('Brick Breaker Game', 48, screen.get_width() / 2, screen.get_height() / 4)

        # 게임 설명 텍스트 추가
        game_description = "Smash all the bricks to send the ball sending them away!"
        draw_text(game_description, 24, screen.get_width() / 2, screen.get_height() / 3)

        # 버튼 배경 그리기 (흰색 바)
        pygame.draw.rect(screen, (255, 255, 255), (button_x, button_y, button_width, button_height))

        # 검정색 글씨로 '게임 시작하기' 텍스트
        draw_text('Start', 36, screen.get_width() / 2, button_y + 10, (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                    start_game()

        pygame.display.flip()

def start_game():
    global balls, ball_speeds, ball_count, bricks, start_time, game_start_time

    # 게임 초기화
    paddle.x = 400
    paddle.y = 500
    balls = [pygame.Rect(400, 300, 10, 10)]
    ball_speeds = [(1, 1)]
    ball_count = 1
    bricks = [pygame.Rect(50 + 100 * i, 50 + 20 * j, 80, 10) for i in range(7) for j in range(3)]
    start_time = pygame.time.get_ticks()

    # 게임 시작 시간 기록
    game_start_time = time.time()

    # 게임 루프
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 패들 움직임
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= 4
        if keys[K_RIGHT] and paddle.right < 800:
            paddle.right += 4

        # 난이도 올리기
        current_time = pygame.time.get_ticks()
        if current_time - start_time > difficult_interval:
            ball_count += 1
            new_ball = pygame.Rect(400, 300, 10, 10)
            balls.append(new_ball)
            new_speed = (1 + increase_speeds_factor * (ball_count - 1), 1 + increase_speeds_factor * (ball_count - 1))
            ball_speeds.append(new_speed)
            start_time = current_time

        # 공 움직임
        for i in range(ball_count):
            balls[i].left += ball_speeds[i][0]
            balls[i].top += ball_speeds[i][1]

            # 공이 출돌할 때
            if balls[i].left <= 0 or balls[i].right >= 800:
                ball_speeds[i] = (-ball_speeds[i][0], ball_speeds[i][1])
            if balls[i].top <= 0:
                ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])

            # 게임 종료 (패들 아래)
            if balls[i].top >= paddle.bottom:
                game_over()

            # 패들과 공 충돌
            if balls[i].colliderect(paddle) and ball_speeds[i][1] > 0:
                ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])

            # 벽돌과 공의 충돌
            hit_index = balls[i].collidelist(bricks)
            if hit_index != -1:
                hit_brick = bricks.pop(hit_index)
                ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])

        # 승리 조건
        if len(bricks) == 0:
            victory()

        # 화면 그리기
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), paddle)
        for ball in balls:  # 각 공을 개별적으로 그리기
            pygame.draw.rect(screen, (255, 255, 255), ball)
        for brick in bricks:
            pygame.draw.rect(screen, (255, 0, 0), brick)

        # 화면 업데이트
        pygame.display.flip()

        # 프레임 속도 설정
        pygame.time.delay(10)

# 메인 메뉴 실행
main_menu()
