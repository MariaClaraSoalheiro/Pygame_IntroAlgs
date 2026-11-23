
import pygame

from src.config import (
    COR_FUNDO,
    COR_TEXTO,
    COR_BOTAO_JOGAR,
    FONTE_TITULO_MENU,
    FONTE_BOTAO_MENU,
    TAMANHO_BOTAO_MENU
)

from src.funcoes import desenhar_texto_centralizado


def criar_menu(largura, altura):

    fonte_titulo = pygame.font.SysFont(None, FONTE_TITULO_MENU)
    fonte_botao = pygame.font.SysFont(None, FONTE_BOTAO_MENU)

    botao_jogar = pygame.Rect(0, 0, *TAMANHO_BOTAO_MENU)
    botao_jogar.center = (largura // 2, int(altura * 2 / 3))

    return fonte_titulo, fonte_botao, botao_jogar


def tratar_evento_menu(evento, botao_jogar):

    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if botao_jogar.collidepoint(evento.pos):
            return True

    return False


def desenhar_menu(tela, largura, altura, fonte_titulo, fonte_botao, botao_jogar):

    tela.fill(COR_FUNDO)

    desenhar_texto_centralizado(
        tela, "AI, Please!", fonte_titulo,
        COR_TEXTO, (largura // 2, altura // 3)
    )

    pygame.draw.rect(
        tela, COR_BOTAO_JOGAR, botao_jogar, border_radius=8
    )

    desenhar_texto_centralizado(
        tela, "JOGAR", fonte_botao,
        COR_TEXTO, botao_jogar.center
    )
