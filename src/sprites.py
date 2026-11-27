import pygame

from src.funcoes import obter_controle


class GerenciadorSprites:
    """Traduz cliques nas áreas interativas da bancada em ações do jogo."""

    def __init__(self, areas_controles):
        self.areas_controles = areas_controles

    def tratar_evento_mouse(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            return obter_controle(self.areas_controles, evento.pos)

        return None
