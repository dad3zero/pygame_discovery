import random
import pygame

from bases import settings

class Scene:
    def __init__(self, bg_img_path=None):
        self._background = pygame.image.load(bg_img_path).convert()

        self._ball_img_path = settings.ASSETS_PATH / 'golfBall.png'
        self._balls = []
        self._hero = Hero(settings.ASSETS_PATH / 'Perso.png')


    def display(self, screen):
        screen.blit(self._background, (0, 0))
        if len(self._balls) < 10 and random.randint(1, 500) <= 10:
            self._balls.append(Ball(self._ball_img_path, (random.randint(25, 455), -25)))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self._hero.move_left()
        if keys[pygame.K_d]:
            self._hero.move_right()

        self._hero.display(screen)
        for ball in self._balls:
            ball.move()
            if ball.rect.top >= 480:
                self._balls.remove(ball)

            else:
                if ball.collide(self._hero.rect):
                    print("hit !!!")

                ball.display(screen)


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


class App:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0.0

        self.scene = None

    def add_scene(self, scene):
        self.scene = scene

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.scene.display(self.screen)

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000  # Limit FPS to 60

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.add_scene(Scene(settings.ASSETS_PATH / 'background.jpg'))

    app.run()
