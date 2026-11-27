import pygame


def carregar_imagem(caminho, tamanho):
    imagem = pygame.image.load(caminho).convert_alpha()
    imagem = pygame.transform.smoothscale(imagem, tamanho)

    return imagem


def desenhar_texto_centralizado(tela, texto, fonte, cor, posicao):
    superficie = fonte.render(texto, False, cor)
    retangulo = superficie.get_rect(center=posicao)

    tela.blit(superficie, retangulo)


def registrar_escolha(estado, resposta):
    caso_atual = estado["caso_atual"]
    id_caso = caso_atual["id"]
    escolhas = estado["escolhas"]

    escolhas[id_caso] = resposta
