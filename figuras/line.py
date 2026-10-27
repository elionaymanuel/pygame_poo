
import pygame


class Linha:
    def __init__(self, screen, cor):
        self.screen = screen
        self.start_pos = (60, 260)
        self.end_pos = (420, 260)
        self.width = 5
        self.cor = cor

    def desenhar(self):
        pygame.draw.line(
            self.screen, self.cor, self.start_pos, self.end_pos, self.width
        )