import pygame


class Texto:
    def __init__(self, screen, conteudo, cor, cor_fundo, posicao, tamanho_fonte):
        self.screen = screen
        self.conteudo = conteudo
        self.cor = cor
        self.cor_fundo = cor_fundo
        self.posicao = posicao
        self.fonte = pygame.font.Font(None, tamanho_fonte)

    def desenhar(self):
        superficie_texto = self.fonte.render(
            self.conteudo, True, self.cor, self.cor_fundo
        )
        self.screen.blit(superficie_texto, self.posicao)
