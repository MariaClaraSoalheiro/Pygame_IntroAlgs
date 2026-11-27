
import pygame

from src.sprites import GerenciadorSprites
from src.dados import carregar_casos
from src.funcoes import (
    avancar_caso,
    carregar_cenario_bancada,
    carregar_imagem,
    classificacao_valida,
    desenhar_texto_centralizado,
    obter_controle,
    registrar_escolha,
    resumir_partida,
    verificar_resposta,
)

from src.config import (
    COR_FUNDO,
    COR_TEXTO,
    COR_ERRO,
    VIDAS_INICIAIS,
    PONTOS_POR_ACERTO,
    FONTE_TITULO_JOGO,
    FONTE_PUBLICACAO,
    FONTE_STATUS,
    FONTE_ROTULOS,
    FONTE_RESUMO,
)


def criar_bancada(largura, altura):

    casos = carregar_casos()
    indice_caso = 1
    caso_atual = casos[indice_caso]

    cenario = carregar_cenario_bancada(largura, altura)
    gerenciador = GerenciadorSprites(cenario["areas_controles"])
    tamanho_monitor = cenario["area_monitor"].size
    imagem = carregar_imagem(caso_atual["imagem"], tamanho_monitor, manter_proporcao=True)

    estado = {
        "gerenciador": gerenciador,
        "casos": casos,
        "indice_caso": indice_caso,
        "caso_atual": caso_atual,
        "escolhas": {},
        "imagem": imagem,
        "cenario": cenario,
        "pontuacao": 0,
        "vidas": VIDAS_INICIAIS,
        "mensagem": "",
        "fim_de_jogo": False,
        "fonte": pygame.font.SysFont(None, FONTE_TITULO_JOGO),
        "fonte_publicacao": pygame.font.SysFont(None, FONTE_PUBLICACAO),
        "fonte_status": pygame.font.SysFont(None, FONTE_STATUS),
        "fonte_rotulos": pygame.font.Font(None, FONTE_ROTULOS),
        "fonte_resumo": pygame.font.Font(None, FONTE_RESUMO),
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

    elif classificacao_valida(resultado, classificacoes):

        resposta = classificacoes[resultado]
        registrar_escolha(estado, resposta)
        caso_atual = estado["caso_atual"]

        estado["mensagem"] = ""

        avaliacao = verificar_resposta(resposta, caso_atual["classificacao"])
        if avaliacao == "ACERTO":
            estado["pontuacao"] += PONTOS_POR_ACERTO
        elif avaliacao == "ERRO":
            estado["vidas"] -= 1

        avancar_caso(estado)


def desenhar_bancada(tela, largura, altura, estado):

    tela.fill(COR_FUNDO)
    cenario = estado["cenario"]
    area_fundo = cenario["area_fundo"]
    area_monitor = cenario["area_monitor"]
    areas_controles = cenario["areas_controles"]

    fundo = cenario["fundo"]
    if not estado["fim_de_jogo"] and pygame.mouse.get_focused():
        controle = obter_controle(areas_controles, pygame.mouse.get_pos())
        fundo = cenario["fundos_hover"].get(controle, fundo)
    tela.blit(fundo, area_fundo)

    fonte = estado["fonte"]
    fonte_publicacao = estado["fonte_publicacao"]
    fonte_status = estado["fonte_status"]

    # Exibindo a pontuacao e as vidas.
    desenhar_texto_centralizado(
        tela, f"Pontos: {estado['pontuacao']}",
        fonte_status, COR_TEXTO, (100, 22)
    )

    desenhar_texto_centralizado(
        tela, f"Vidas: {estado['vidas']}",
        fonte_status, COR_TEXTO, (largura - 100, 22)
    )

    # Titulo da bancada.
    desenhar_texto_centralizado(
        tela, "Bancada de Investigação",
        fonte, COR_TEXTO, (largura // 2, 22)
    )

    # Exibindo a imagem da publicacao.
    imagem = estado["imagem"]
    retangulo_imagem = imagem.get_rect(center=area_monitor.center)
    tela.blit(imagem, retangulo_imagem)
    tela.blit(cenario["contorno_monitor"], area_monitor)

    # A legenda e o aviso de pistas usam a mesma posição na arte.
    legenda = estado["mensagem"] or estado["caso_atual"]["publicacao"]
    desenhar_texto_centralizado(
        tela, legenda, fonte_publicacao, COR_TEXTO,
        (area_fundo.centerx, area_fundo.bottom - 13)
    )

    if estado["fim_de_jogo"]:
        painel = area_monitor.inflate(-14, -118)
        pygame.draw.rect(tela, COR_FUNDO, painel, border_radius=6)
        desenhar_texto_centralizado(
            tela, "fim de jogo", fonte,
            COR_ERRO, (painel.centerx, painel.centery - 20)
        )

        resumo = resumir_partida(estado)
        texto_resumo = (
            f"Acertos: {resumo['ACERTO']}  "
            f"Erros: {resumo['ERRO']}  "
            f"Inconclusivas: {resumo['INCONCLUSIVO']}"
        )
        desenhar_texto_centralizado(
            tela, texto_resumo, estado["fonte_resumo"],
            COR_TEXTO, (painel.centerx, painel.centery + 20)
        )
    else:
        fonte_rotulos = estado["fonte_rotulos"]
        rotulos = {
            "HUMAN": "Human",
            "AI_GENERATED": "AI-generated",
            "INCONCLUSIVE": "Inconclusive",
        }
        for acao, texto in rotulos.items():
            area = areas_controles[acao]
            desenhar_texto_centralizado(
                tela, texto, fonte_rotulos, COR_TEXTO,
                (area.centerx, area.bottom + 13)
            )

        pasta = areas_controles["CONSULTAR_PISTAS"]
        desenhar_texto_centralizado(
            tela, "Consultar pistas e informações", fonte_rotulos, COR_FUNDO,
            (pasta.centerx, pasta.centery - 5)
        )
