import pygame


class Arco:
    def __init__(self, screen, cor, start_angle, stop_angle):
        self.screen = screen
        self.cor = cor
        self.rect = (250, 75, 150, 125)
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.width = 2

    def desenhar(self):
        pygame.draw.arc(
            self.screen,
            self.cor,
            self.rect,
            self.start_angle,
            self.stop_angle,
            self.width,
        )
