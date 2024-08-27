import asyncio
import pygame
import random




async def game_loop():
    global direction, change_to, score, snake_speed, fruit_spawn, fruit_position

    # Setting snake speed variable
    snake_speed = 15

    # Window size
    window_x = 720
    window_y = 480


    # Defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 69, 58)
    green = pygame.Color(50, 215, 75)
    blue = pygame.Color(10, 132, 255)

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS or frames per second controller
    fps = pygame.time.Clock()

    # Defining snake default position
    snake_position = [100, 50]

    # Defining first 4 blocks of the snake body
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

    # Fruit position
    fruit_position = [
        random.randrange(1, (window_x // 10)) * 10,
        random.randrange(1, (window_y // 10)) * 10
    ]

    fruit_spawn = True

    # Setting default snake direction towards right
    direction = 'RIGHT'
    change_to = direction

    # Initial score
    score = 0

    # Displaying score function
    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    # Game over function
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # This should be awaited when called from an async function
        async def wait_then_quit():
            await asyncio.sleep(2)  # Asynchronous sleep
            pygame.quit()
            quit()

        # Schedule the wait_then_quit task
        asyncio.create_task(wait_then_quit())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            snake_speed += 0.3
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [
                random.randrange(1, (window_x // 10)) * 10,
                random.randrange(1, (window_y // 10)) * 10
            ]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        show_score(1, white, 'times new roman', 20)
        pygame.display.update()

        # Regulate the speed of the game
        await asyncio.sleep(1 / snake_speed)


async def main():
    await game_loop()


# Running the game
asyncio.run(main())