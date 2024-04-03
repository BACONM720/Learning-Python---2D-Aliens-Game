import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships curr pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color     

        # create a bullet rect at (0, 0) then set correct pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
