import pygame


class Circulo:
    def __init__(self, screen, cor):
        self.screen = screen
        self.cor = cor
        self.centro = (300, 50)
        self.raio = 20
        self.width = 0

    def desenhar(self):
        pygame.draw.circle(
            self.screen, self.cor, self.centro, self.raio, self.width
        )
