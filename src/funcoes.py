import pygame

from src.config import TAMANHO_IMAGEM


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


def classificacao_valida(resultado, classificacoes):
    return resultado in classificacoes


def verificar_resposta(resposta, classificacao_correta):
    if resposta == "INCONCLUSIVO":
        return "INCONCLUSIVO"

    if resposta == classificacao_correta:
        return "ACERTO"

    return "ERRO"


def avancar_caso(estado):
    if estado["vidas"] == 0:
        estado["fim_de_jogo"] = True
        return

    proximo_indice = estado["indice_caso"] + 1
    casos = estado["casos"]

    if proximo_indice < len(casos):
        proximo_caso = casos[proximo_indice]
        imagem = carregar_imagem(proximo_caso["imagem"], TAMANHO_IMAGEM)
        estado["caso_atual"] = proximo_caso
        estado["imagem"] = imagem
    else:
        estado["fim_de_jogo"] = True

    estado["indice_caso"] = proximo_indice


def resumir_partida(estado):
    resumo = {
        "ACERTO": 0,
        "ERRO": 0,
        "INCONCLUSIVO": 0,
    }
    escolhas = estado["escolhas"]

    for caso in estado["casos"]:
        id_caso = caso["id"]
        if id_caso not in escolhas:
            continue

        resposta = escolhas[id_caso]
        classificacao_correta = caso["classificacao"]
        avaliacao = verificar_resposta(resposta, classificacao_correta)
        resumo[avaliacao] += 1

    return resumo
