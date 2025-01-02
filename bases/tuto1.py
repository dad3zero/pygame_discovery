# Example file showing a basic pygame "game loop"
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

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

background = pygame.image.load(settings.ASSETS_PATH / 'background.jpg').convert()
screen.blit(background, (0, 0))

hero = pygame.image.load(settings.ASSETS_PATH / 'Perso.png').convert_alpha()
hero_rect = hero.get_rect()
hero_rect.topleft = (270, 380)
balls = []

running = True
dt = 0 # Fort Delta_Time

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    if len(balls) < 10 and random.randint(1, 500) <= 10:
        balls.append(Ball(settings.ASSETS_PATH / 'golfBall.png', (random.randint(25, 455), -25)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_q]:
        if hero_rect.left >= 10:
            hero_rect = hero_rect.move(-10, 0)
    if keys[pygame.K_d]:
        if hero_rect.right <= 630:
            hero_rect = hero_rect.move(10, 0)

    # flip() the display to put your work on screen
    screen.blit(background, (0, 0))
    for ball in balls:
        ball.move()
        if ball.rect.top >= 480:
            balls.remove(ball)

        else:
            if ball.collide(hero_rect):
                running = False
                print("hit !!!")

            ball.display(screen)

    screen.blit(hero, hero_rect)
    pygame.display.flip()
    pygame.display.update()

    dt = clock.tick(60) / 1000  # limits FPS to 60


pygame.quit()