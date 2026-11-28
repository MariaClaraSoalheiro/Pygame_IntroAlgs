import pygame


def carregar_imagem(caminho, tamanho):
    imagem = pygame.image.load(caminho).convert_alpha()
    imagem = pygame.transform.smoothscale(imagem, tamanho)

    return imagem


def desenhar_texto_centralizado(tela, texto, fonte, cor, posicao):
    superficie = fonte.render(texto, False, cor)
    retangulo = superficie.get_rect(center=posicao)

    tela.blit(superficie, retangulo)

def verificar_vitoria(acertos, vidas, total_casos):   #macla
    """Verifica se o jogador venceu a partida."""

    if total_casos == 5 and acertos >= 4 and vidas > 0:
        return True

    return False

def verificar_derrota(acertos, vidas, total_casos):   #macla
    """Verifica se o jogador perdeu a partida."""

    if vidas <= 0:
        return True

    if total_casos == 5 and acertos < 4:
        return True

    return False
