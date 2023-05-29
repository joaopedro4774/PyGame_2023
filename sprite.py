import pygame
import pygame, random
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED = 10
GRAVITY = 1
GAME_SPEED = 10

GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100

PIPE_WIDTH = 80
PIPE_HEIGHT = 500

PIPE_GAP = 200

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('bird_up.png').convert_alpha(),
                       pygame.image.load('bird_mid.png').convert_alpha(),
                       pygame.image.load('bird_down.png').convert_alpha()]

        self.speed = SPEED

        self.current_image = 0

        self.image = pygame.image.load('bird_up.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2