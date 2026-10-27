import pygame


class Elipse:
    def __init__(self, screen, cor):
        self.screen = screen
        self.cor = cor
        self.area = (400, 250, 40, 80)
        self.width = 1

    def desenhar(self):
        pygame.draw.ellipse(self.screen, self.cor, self.area, self.width)
