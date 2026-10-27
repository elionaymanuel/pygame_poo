import math

import pygame

from cor import Cor
from figuras.arco import Arco
from figuras.circulo import Circulo
from figuras.elipse import Elipse
from figuras.line import Linha
from figuras.poligono import Poligono
from figuras.retangulo import Retangulo
from figuras.texto import Texto
import os


class AplicacaoFiguras:
    def __init__(self):
        pygame.init()
        self.cores = Cor()
        self.janela = pygame.display.set_mode((500, 400))
        pygame.display.set_caption("Figuras e Texto")
        self.texto = Texto(
            self.janela,
            "Olá, mundo!",
            self.cores.BRANCO,
            self.cores.AZUL,
            (30, 150),
            48,
        )
        self.figuras = [
            Linha(self.janela, self.cores.VERDE),
            Poligono(self.janela, self.cores.PRETO),
            Circulo(self.janela, self.cores.AZUL),
            Elipse(self.janela, self.cores.VERMELHO),
            Retangulo(self.janela, self.cores.VERDE),
            Arco(self.janela, self.cores.VERMELHO, math.pi / 2, 3 * math.pi / 2),
            Arco(self.janela, self.cores.PRETO, -math.pi / 2, math.pi / 2),
        ]

    def desenhar(self):
        self.janela.fill(self.cores.BRANCO)
        self.texto.desenhar()
        for figura in self.figuras:
            figura.desenhar()
        pygame.display.update()

    def executar(self):
        self.desenhar()
        deve_continuar = True
        while deve_continuar:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    deve_continuar = False
        os._exit(0)


if __name__ == "__main__":
    AplicacaoFiguras().executar()
