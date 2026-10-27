import pygame


class Poligono:
    def __init__(self, screen, cor):
        self.screen = screen
        self.cor = cor
        self.vertices = ((191, 206), (236, 277), (156, 277))
        self.width = 0

    def desenhar(self):
        pygame.draw.polygon(self.screen, self.cor, self.vertices, self.width)