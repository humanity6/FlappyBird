import pygame
import sys
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
floor_x = 0
gravity = 0.25
jump_force = -4.5
bird_movement = 0
PIPE_GAP = 152
pipe_vel = 1

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 24)

pygame.display.set_caption("Flappy Bird")

background = pygame.image.load("images/bg.png")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

floor = pygame.image.load("images/base.png")
floor = pygame.transform.scale(floor, (WINDOW_WIDTH * 2, floor.get_height()))

bird = pygame.image.load("images/bird1.png")
bird = pygame.transform.scale(bird, (int(bird.get_width() * 1.5), int(bird.get_height() * 1.5)))
bird_y = WINDOW_HEIGHT // 2

pipe = pygame.image.load("images/pipe.png")
pipe = pygame.transform.scale(pipe, (pipe.get_width(), pipe.get_height() + 180))
pipe2 = pygame.transform.rotate(pipe, 180)
pipe2 = pygame.transform.scale(pipe2, (pipe2.get_width(), pipe2.get_height() + 180))

pipe_X = WINDOW_WIDTH

pipe2_height = pipe2.get_rect().size[1]
floor_height = floor.get_rect().size[1]

clock = pygame.time.Clock()


# bird class
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 0.25
        self.jump_force = -4.5
        self.bird_movement = 0

    def jump(self):
        self.bird_movement = self.jump_force

    def update(self):
        self.bird_movement += self.gravity
        self.y += self.bird_movement

    def draw(self):
        screen.blit(bird, (self.x, self.y))


# pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.pipe_vel = 1
        self.PIPE_GAP = 152
        self.pipe2_bottom = random.randrange(50, WINDOW_HEIGHT - 300)
        self.pipe_top = self.pipe2_bottom + self.PIPE_GAP
        self.pipe2_height = pipe2.get_rect().size[1]

    def update(self):
        self.x -= self.pipe_vel

    def draw(self):
        screen.blit(pipe, (self.x, self.pipe_top))
        screen.blit(pipe2, (self.x, self.pipe2_bottom - self.pipe2_height))


# floor class
class Floor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.floor_x = 0
        self.floor_height = floor.get_rect().size[1]

    def update(self):
        self.floor_x -= 1
        if self.floor_x <= -WINDOW_WIDTH:
            self.floor_x = 0

    def draw(self):
        screen.blit(floor, (self.floor_x, WINDOW_HEIGHT - self.floor_height))


bird_obj = Bird(WINDOW_WIDTH // 3, bird_y)
# pipe_obj = Pipe(pipe_X)
floor_obj = Floor(floor_x, WINDOW_HEIGHT - floor_height)

pipes = [Pipe(pipe_X)]
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_obj.jump()

    bird_obj.update()
    floor_obj.update()

    if pipes[-1].x < WINDOW_WIDTH - 300:
        pipes.append(Pipe(pipe_X))

    if pipes[0].x < -pipe.get_width():
        pipes.pop(0)

    # collisions
    for pipe_objs in pipes:
        if bird_obj.x + bird.get_width() > pipe_objs.x and bird_obj.x < pipe_objs.x + pipe.get_width():
            if bird_obj.y < pipe_objs.pipe2_bottom or bird_obj.y + bird.get_height() > pipe_objs.pipe2_bottom + PIPE_GAP:
                print("collision")
                pygame.quit()
                sys.exit()


        if bird_obj.y + bird.get_height() > WINDOW_HEIGHT - floor_height:
            print("collision")
            pygame.quit()
            sys.exit()
    
    # scoring 
    for pipe_objs in pipes:
        if pipe_objs.x == bird_obj.x:
            score += 1

    # Update screen
    screen.blit(background, (0, 0))
    bird_obj.draw()
    for pipe_objs in pipes:
        pipe_objs.update()
        pipe_objs.draw()
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    floor_obj.draw()

    pygame.display.update()

    clock.tick(60)
