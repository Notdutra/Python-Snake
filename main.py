import asyncio
import pygame
import random
import threading

<<<<<<< Updated upstream
async def game_loop():
    global direction, change_to, score, snake_speed, fruit_spawn, fruit_position
=======
# Constants
SNAKE_SPEED = 15
WINDOW_X = 720
WINDOW_Y = 480
GRID_SIZE = 10
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 69, 58)
GREEN = pygame.Color(50, 215, 75)

# Initialize Pygame
pygame.init()
print("Pygame initialized")

# Load sound effects with error handling
pygame.mixer.init()
print("Pygame mixer initialized")
try:
    EAT_SOUND = pygame.mixer.Sound('assets/eat.wav')
    GAME_START_SOUND = pygame.mixer.Sound('assets/game_start.wav')
    GAME_OVER_SOUND = pygame.mixer.Sound('assets/game_over.wav')
    DIRECTION_CHANGE_SOUND = pygame.mixer.Sound('assets/direction_change.wav')
    print("Sound effects loaded successfully")
except pygame.error as e:
    print(f"Error loading sound effects: {e}")
    EAT_SOUND = None
    GAME_START_SOUND = None
    GAME_OVER_SOUND = None
    DIRECTION_CHANGE_SOUND = None

# Load background music with error handling
try:
    pygame.mixer.music.load('assets/background_music.wav')
    print("Background music loaded successfully")
except pygame.error as e:
    print(f"Error loading background music: {e}")
>>>>>>> Stashed changes

# Adjust the volume of sounds
if EAT_SOUND and GAME_START_SOUND and GAME_OVER_SOUND and DIRECTION_CHANGE_SOUND:
    EAT_SOUND.set_volume(0.3)
    GAME_START_SOUND.set_volume(0.5)
    GAME_OVER_SOUND.set_volume(0.5)
    DIRECTION_CHANGE_SOUND.set_volume(0.2)
    pygame.mixer.music.set_volume(0.4)
    print("Sound volumes set successfully")
else:
    print("Sound objects not initialized, skipping volume settings")

class SnakeGame:
    def __init__(self):
        print("Initializing SnakeGame")
        self.snake_speed = SNAKE_SPEED
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.fruit_position = self.random_fruit_position()
        self.fruit_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.high_score = 0
        self.game_over_flag = False
        self.pause_flag = False
        self.mute_flag = False

        # Initialize Pygame and game window
        pygame.display.set_caption('Snake')
        self.game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
        self.fps = pygame.time.Clock()
        print("SnakeGame initialized")

        # Direction mappings
        self.opposite_directions = {
            'UP': 'DOWN',
            'DOWN': 'UP',
            'LEFT': 'RIGHT',
            'RIGHT': 'LEFT'
        }
        self.direction_movements = {
            'UP': (0, -GRID_SIZE),
            'DOWN': (0, GRID_SIZE),
            'LEFT': (-GRID_SIZE, 0),
            'RIGHT': (GRID_SIZE, 0)
        }

    def random_fruit_position(self):
        while True:
            position = [random.randrange(1, (WINDOW_X // GRID_SIZE)) * GRID_SIZE, random.randrange(1, (WINDOW_Y // GRID_SIZE)) * GRID_SIZE]
            if position not in self.snake_body:
                return position

    def play_sound(self, sound):
        if sound and not self.mute_flag:
            threading.Thread(target=sound.play).start()

    def show_score(self):
        score_font = pygame.font.SysFont(None, 20)
        score_surface = score_font.render('Score : ' + str(self.score), True, WHITE)
        score_rect = score_surface.get_rect(topleft=(10, 10))
        self.game_window.blit(score_surface, score_rect)

        high_score_surface = score_font.render('High Score : ' + str(self.high_score), True, WHITE)
        high_score_rect = high_score_surface.get_rect(topleft=(10, 30))
        self.game_window.blit(high_score_surface, high_score_rect)

<<<<<<< Updated upstream
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

    # game over function
    async def game_over():
        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)

        # creating a text surface on which text
        # will be drawn
        game_over_surface = my_font.render('Your Score is : ' + str(score) + " | Press SPACE to play again", True, red)

        # create a rectangular object for the text surface object
        game_over_rect = game_over_surface.get_rect()

        # setting position of the text
        game_over_rect.midtop = (window_x / 2, window_y / 4)

        # blit will draw the text on screen
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Exit the loop to restart the game

        await asyncio.sleep(0)
=======
    def show_game_over(self):
        my_font = pygame.font.SysFont('times new roman', 50)
        
        if self.score > self.high_score:
            self.high_score = self.score

        if self.high_score != 0:
            high_score_surface = my_font.render(f'High score is : {self.high_score}', True, RED)
            high_score_rect = high_score_surface.get_rect(center=(WINDOW_X/2, WINDOW_Y/3))
            self.game_window.blit(high_score_surface, high_score_rect)
            
        game_over_surface = my_font.render(f'Your score is : {self.score}', True, RED)
        game_over_rect = game_over_surface.get_rect(center=(WINDOW_X/2, WINDOW_Y/2))
        self.game_window.blit(game_over_surface, game_over_rect)

        restart_surface = my_font.render('Press SPACE to restart', True, RED)
        restart_rect = restart_surface.get_rect(center=(WINDOW_X/2, WINDOW_Y/1.5))
        self.game_window.blit(restart_surface, restart_rect)
>>>>>>> Stashed changes

    def show_pause(self):
        my_font = pygame.font.SysFont('times new roman', 50)
        pause_surface = my_font.render('Game Paused', True, RED)
        pause_rect = pause_surface.get_rect(center=(WINDOW_X/2, WINDOW_Y/2))
        self.game_window.blit(pause_surface, pause_rect)

    def restart_game(self):
        self.__init__()
        self.play_sound(GAME_START_SOUND)
        pygame.mixer.music.play(-1)

    async def main(self):
        self.play_sound(GAME_START_SOUND)
        pygame.mixer.music.play(-1)
        print("Game started")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            pygame.quit()
                            return
                        case pygame.K_UP | pygame.K_w:
                            if not self.pause_flag and self.direction != 'DOWN' and self.direction != 'UP':
                                self.change_to = 'UP'
                                self.play_sound(DIRECTION_CHANGE_SOUND)
                        case pygame.K_DOWN | pygame.K_s:
                            if not self.pause_flag and self.direction != 'UP' and self.direction != 'DOWN':
                                self.change_to = 'DOWN'
                                self.play_sound(DIRECTION_CHANGE_SOUND)
                        case pygame.K_LEFT | pygame.K_a:
                            if not self.pause_flag and self.direction != 'RIGHT' and self.direction != 'LEFT':
                                self.change_to = 'LEFT'
                                self.play_sound(DIRECTION_CHANGE_SOUND)
                        case pygame.K_RIGHT | pygame.K_d:
                            if not self.pause_flag and self.direction != 'LEFT' and self.direction != 'RIGHT':
                                self.change_to = 'RIGHT'
                                self.play_sound(DIRECTION_CHANGE_SOUND)
                        case pygame.K_SPACE if self.game_over_flag:
                            self.restart_game()
                        case pygame.K_p if not self.game_over_flag:
                            self.pause_flag = not self.pause_flag
                        case pygame.K_m:
                            self.mute_flag = not self.mute_flag
                            if self.mute_flag:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()

            if self.pause_flag:
                self.show_pause()
                pygame.display.update()
                await asyncio.sleep(0)
                continue

            if self.game_over_flag:
                self.show_game_over()
                pygame.display.update()
                await asyncio.sleep(0)
                continue

            if self.change_to != self.opposite_directions[self.direction] and self.change_to != self.direction:
                self.direction = self.change_to

            self.snake_position[0] += self.direction_movements[self.direction][0]
            self.snake_position[1] += self.direction_movements[self.direction][1]

            self.snake_body.insert(0, list(self.snake_position))
            if self.snake_position == self.fruit_position:
                self.score += 10
                self.fruit_spawn = False
                self.play_sound(EAT_SOUND)
                if self.score % 50 == 0:
                    self.snake_speed += 1
            else:
                self.snake_body.pop()

            if not self.fruit_spawn:
                self.fruit_position = self.random_fruit_position()

            self.fruit_spawn = True
            self.game_window.fill(BLACK)

            for pos in self.snake_body:
                pygame.draw.rect(self.game_window, GREEN, pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE))

            pygame.draw.rect(self.game_window, WHITE, pygame.Rect(self.fruit_position[0], self.fruit_position[1], GRID_SIZE, GRID_SIZE))

            if self.snake_position[0] < 0 or self.snake_position[0] > WINDOW_X - GRID_SIZE:
                self.game_over_flag = True
                self.play_sound(GAME_OVER_SOUND)
                pygame.mixer.music.stop()
            if self.snake_position[1] < 0 or self.snake_position[1] > WINDOW_Y - GRID_SIZE:
                self.game_over_flag = True
                self.play_sound(GAME_OVER_SOUND)
                pygame.mixer.music.stop()

            for block in self.snake_body[1:]:
                if self.snake_position == block:
                    self.game_over_flag = True
                    self.play_sound(GAME_OVER_SOUND)
                    pygame.mixer.music.stop()

            self.show_score()
            pygame.display.update()
            await asyncio.sleep(0)
            self.fps.tick(self.snake_speed)

# This is the program entry point:
if __name__ == "__main__":
    print("Starting SnakeGame")
    game = SnakeGame()
    asyncio.run(game.main())
    print("SnakeGame ended")

# Do not add anything from here, especially sys.exit/pygame.quit
# asyncio.run is non-blocking on pygame-wasm and code would be executed right before program start main()