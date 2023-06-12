import pygame
import Apple
import Bowl
import threading
import Data
import Timer
import math
import Results


def get_score():
    return Data.score


class Main:
    def __init__(self):
        self.spawn_timer = Timer.Timer()
        self.spawn_timer.reset()
        self.bowl = Bowl.Bowl()
        self.bowl_timer = Timer.Timer()
        self.bowl_timer.reset()
        self.apples = []
        self.backdrop = pygame.image.load("Images\\Blue Sky.png")
        self.apple_image = pygame.image.load("Images\\apple.png")
        self.bowl_image = pygame.image.load("Images\\bowl.png")
        pygame.init()
        pygame.display.set_caption("Apple Catching Game")
        self.screen = pygame.display.set_mode((480, 360))
        self.clock = pygame.time.Clock()
        self.gameRun = True
        self.score = 0
        self.right = False
        self.left = False
        self.font = pygame.font.SysFont("Times New Roman", 24)
        self.start_move()
        self.timer = Timer.Timer()
        self.timer.reset()
        while self.gameRun:
            self.clock.tick(12)
            if math.floor(self.spawn_timer.get_time()) >= 1:
                self.spawn()
                self.spawn_timer.reset()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameRun = False
                    for i in self.apples:
                        i.display = False
                    continue
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.right = True
                    if event.key == pygame.K_LEFT:
                        self.left = True
                if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    self.right = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    self.left = False
            for i in range(0, len(self.apples)):
                try:
                    if self.apples[i].display:
                        self.apples[i].move()
                        self.apples[i].collision_check()
                    else:
                        self.apples.pop(i)
                except IndexError:
                    pass
            self.score = get_score()
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.backdrop, (0, 0))
            for i in self.apples:
                if i.display:
                    self.screen.blit(self.apple_image, (i.pos_x, i.pos_y))
            self.screen.blit(self.bowl_image, (self.bowl.pos_x, self.bowl.pos_y))
            self.screen.blit(self.font.render("Score: " + str(self.score) + " , Timer: " + str(math.floor(61 - self.timer.get_time())), False, (0, 0, 0)), (0, 0))
            pygame.display.update()
            if self.timer.get_time() > 60:
                self.gameRun = False
                for i in self.apples:
                    i.display = False
                continue
        pygame.quit()
        Results.Results(self.score)

    def spawn(self):
        self.apples.append(Apple.Apple(self.bowl))

    def move(self):
        while self.gameRun:
            if self.right:
                if self.bowl_timer.get_time() > 0.04:
                    self.bowl.right()
                    self.bowl_timer.reset()
            elif self.left:
                if self.bowl_timer.get_time() > 0.04:
                    self.bowl.left()
                    self.bowl_timer.reset()

    def start_move(self):
        self.thread = threading.Thread(target=self.move)
        self.thread.start()
