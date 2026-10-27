import pygame


class Retangulo:
    def __init__(self, screen, cor):
        self.screen = screen
        self.cor = cor
        self.posicao = (20, 20)
        self.largura = 60
        self.altura = 40
        self.width = 0

    def desenhar(self):
        pygame.draw.rect(
            self.screen,
            self.cor,
            (*self.posicao, self.largura, self.altura),
            self.width,
        )
