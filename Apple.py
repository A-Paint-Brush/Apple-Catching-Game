import random
import Data
import pygame.mixer


def increase_score():
    Data.score = Data.score + 1


class Apple:
    def __init__(self, bowl):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("Sounds\\pop.wav")
        self.r = random.Random()
        self.bowl = bowl
        self.pos_x = self.r.randint(0, 417)
        self.pos_y = -64
        self.score = 0
        self.display = True

    def move(self):
        self.pos_y = self.pos_y + 10

    def collision_check(self):
        if self.pos_y >= 360:
            self.display = False
        elif (
                self.bowl.pos_x < self.pos_x + 63 < self.bowl.pos_x + 60 or self.bowl.pos_x < self.pos_x < self.bowl.pos_x + 60 or self.bowl.pos_x < self.pos_x + 31.5 < self.bowl.pos_x + 60) and (
                self.bowl.pos_y < self.pos_y + 64 < self.bowl.pos_y + 37 or self.bowl.pos_y < self.pos_y < self.bowl.pos_y + 37 or self.bowl.pos_y < self.pos_y + 32 < self.bowl.pos_y + 37):
            increase_score()
            self.display = False
            try:
                self.sound.play()
            except:
                pass
