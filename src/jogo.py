
import pygame

from src.sprites import GerenciadorSprites
from src.dados import carregar_casos
from src.funcoes import carregar_imagem, desenhar_texto_centralizado

from src.config import (
    COR_FUNDO,
    COR_TEXTO,
    COR_ERRO,
    VIDAS_INICIAIS,
    PONTOS_POR_ACERTO,
    TAMANHO_IMAGEM,
    FONTE_TITULO_JOGO,
    FONTE_PUBLICACAO,
    FONTE_STATUS
)


def criar_bancada(largura, altura):

    gerenciador = GerenciadorSprites(largura, altura)

    casos = carregar_casos()
    indice_caso = 1
    caso_atual = casos[indice_caso]

    imagem = carregar_imagem(caso_atual["imagem"], TAMANHO_IMAGEM)

    estado = {
        "gerenciador": gerenciador,
        "casos": casos,
        "indice_caso": indice_caso,
        "caso_atual": caso_atual,
        "imagem": imagem,
        "pontuacao": 0,
        "vidas": VIDAS_INICIAIS,
        "mensagem": "",
        "fim_de_jogo": False,
        "fonte": pygame.font.SysFont(None, FONTE_TITULO_JOGO),
        "fonte_publicacao": pygame.font.SysFont(None, FONTE_PUBLICACAO),
        "fonte_status": pygame.font.SysFont(None, FONTE_STATUS)
    }

    return estado


def tratar_evento_bancada(evento, estado):

    if estado["fim_de_jogo"]:
        return

    resultado = estado["gerenciador"].tratar_evento_mouse(evento)

    classificacoes = {
        "HUMAN": "HUMAN",
        "AI_GENERATED": "GERADO POR IA",
        "INCONCLUSIVE": "INCONCLUSIVO"
    }

    if resultado == "CONSULTAR_PISTAS":
        estado["mensagem"] = "Consulta de pistas ainda nao disponivel."

    elif resultado in classificacoes:

        resposta = classificacoes[resultado]
        caso_atual = estado["caso_atual"]

        estado["mensagem"] = ""

        if resultado != "INCONCLUSIVE":

            if resposta == caso_atual["classificacao"]:
                estado["pontuacao"] += PONTOS_POR_ACERTO
            else:
                estado["vidas"] -= 1

        # Verificando se o jogador ainda tem vidas.
        if estado["vidas"] == 0:
            estado["fim_de_jogo"] = True

        else:
            # Avancando para o proximo caso.
            estado["indice_caso"] += 1

            if estado["indice_caso"] < len(estado["casos"]):

                indice = estado["indice_caso"]
                estado["caso_atual"] = estado["casos"][indice]

                estado["imagem"] = carregar_imagem(
                    estado["caso_atual"]["imagem"], TAMANHO_IMAGEM
                )

            else:
                estado["fim_de_jogo"] = True


def desenhar_bancada(tela, largura, altura, estado):

    tela.fill(COR_FUNDO)

    fonte = estado["fonte"]
    fonte_publicacao = estado["fonte_publicacao"]
    fonte_status = estado["fonte_status"]

    # Exibindo a pontuacao e as vidas.
    desenhar_texto_centralizado(
        tela, f"Pontos: {estado['pontuacao']}",
        fonte_status, COR_TEXTO, (100, 35)
    )

    desenhar_texto_centralizado(
        tela, f"Vidas: {estado['vidas']}",
        fonte_status, COR_TEXTO, (700, 35)
    )

    # Titulo da bancada.
    desenhar_texto_centralizado(
        tela, "Bancada de Investigacao",
        fonte, COR_TEXTO, (largura // 2, 75)
    )

    # Exibindo a imagem da publicacao.
    imagem = estado["imagem"]
    retangulo_imagem = imagem.get_rect(center=(largura // 2, 220))
    tela.blit(imagem, retangulo_imagem)

    # Exibindo a legenda da publicacao.
    desenhar_texto_centralizado(
        tela, estado["caso_atual"]["publicacao"],
        fonte_publicacao, COR_TEXTO, (largura // 2, 350)
    )

    estado["gerenciador"].desenhar_elementos(tela)

    if estado["fim_de_jogo"]:
        desenhar_texto_centralizado(
            tela, "fim de jogo", fonte,
            COR_ERRO, (largura // 2, 530)
        )
    else:
        desenhar_texto_centralizado(
            tela, estado["mensagem"], fonte_publicacao,
            COR_TEXTO, (largura // 2, 530)
        )
