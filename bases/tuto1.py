import random
import pygame

from bases import settings

class Ball:
    def __init__(self, image, center):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = random.randint(1, 5)

    def display(self, window):
        window.blit(self.image, self.rect)

    def move(self):
        self.rect = self.rect.move(0, self.speed)

    def collide(self, other):
        return self.rect.colliderect(other)

class Hero:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (270, 380)
        self._speed = 10

    def display(self, window):
        window.blit(self.image, self.rect)

    def move_right(self):
        if self.rect.right <= 630:
            self.rect = self.rect.move(self._speed, 0)

    def move_left(self):
        if self.rect.left >= 10:
            self.rect = self.rect.move(-self._speed, 0)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

background = pygame.image.load(settings.ASSETS_PATH / 'background.jpg').convert()
screen.blit(background, (0, 0))

hero = Hero(settings.ASSETS_PATH / 'Perso.png')
balls = []

running = True
dt = 0 # Fort Delta_Time

while running:
    if len(balls) < 10 and random.randint(1, 500) <= 10:
        balls.append(Ball(settings.ASSETS_PATH / 'golfBall.png', (random.randint(25, 455), -25)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        hero.move_left()
    if keys[pygame.K_d]:
        hero.move_right()

    # flip() the display to put your work on screen
    screen.blit(background, (0, 0))
    for ball in balls:
        ball.move()
        if ball.rect.top >= 480:
            balls.remove(ball)

        else:
            if ball.collide(hero.rect):
                running = False
                print("hit !!!")

            ball.display(screen)

    hero.display(screen)
    
    pygame.display.flip()
    pygame.display.update()

    dt = clock.tick(60) / 1000  # limits FPS to 60


pygame.quit()