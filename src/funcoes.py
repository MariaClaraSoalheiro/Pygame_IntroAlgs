import pygame


def carregar_imagem(caminho, tamanho):
    imagem = pygame.image.load(caminho).convert_alpha()
    imagem = pygame.transform.smoothscale(imagem, tamanho)

    return imagem


def desenhar_texto_centralizado(tela, texto, fonte, cor, posicao):
    superficie = fonte.render(texto, False, cor)
    retangulo = superficie.get_rect(center=posicao)

    tela.blit(superficie, retangulo)