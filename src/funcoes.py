import pygame


def carregar_imagem(caminho, tamanho, manter_proporcao=False):
    imagem = pygame.image.load(caminho).convert_alpha()
    if manter_proporcao:
        area = pygame.Rect((0, 0), tamanho)
        tamanho = imagem.get_rect().fit(area).size

    return pygame.transform.smoothscale(imagem, tamanho)


def carregar_cenario_bancada(largura, altura):
    fundo = pygame.image.load("assets/imagens/hud_normal.png").convert()
    area_disponivel = pygame.Rect(0, 44, largura, altura - 44)
    area_fundo = fundo.get_rect().fit(area_disponivel)
    escala_x = area_fundo.width / fundo.get_width()
    escala_y = area_fundo.height / fundo.get_height()

    # Coordenadas da tela e dos controles na arte original.
    areas_originais = {
        "monitor": (527, 142, 607, 422),
        "HUMAN": (1203, 691, 110, 100),
        "AI_GENERATED": (1335, 691, 115, 100),
        "INCONCLUSIVE": (1472, 691, 116, 100),
        "CONSULTAR_PISTAS": (24, 630, 447, 253),
    }
    areas = {}
    for nome, (x, y, largura_area, altura_area) in areas_originais.items():
        areas[nome] = pygame.Rect(
            area_fundo.x + round(x * escala_x),
            area_fundo.y + round(y * escala_y),
            round(largura_area * escala_x),
            round(altura_area * escala_y),
        )

    area_monitor = areas.pop("monitor")
    moldura = pygame.image.load("assets/imagens/computadortransparente.png").convert_alpha()
    contorno_interno = moldura.subsurface((243, 101, 957, 693))

    arquivos_hover = {
        "HUMAN": "hud_hover_verde.png",
        "AI_GENERATED": "hud_hover_vermelho.png",
        "INCONCLUSIVE": "hud_hover_amarelo.png",
        "CONSULTAR_PISTAS": "hud_hover_pasta.png",
    }
    fundos_hover = {}
    for acao, arquivo in arquivos_hover.items():
        fundo_hover = pygame.image.load(f"assets/imagens/{arquivo}").convert()
        fundos_hover[acao] = pygame.transform.smoothscale(fundo_hover, area_fundo.size)

    return {
        "fundo": pygame.transform.smoothscale(fundo, area_fundo.size),
        "area_fundo": area_fundo,
        "contorno_monitor": pygame.transform.smoothscale(contorno_interno, area_monitor.size),
        "area_monitor": area_monitor,
        "areas_controles": areas,
        "fundos_hover": fundos_hover,
    }


def obter_controle(areas_controles, posicao_mouse):
    for acao, area in areas_controles.items():
        if area.collidepoint(posicao_mouse):
            return acao

    return None


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
        area_monitor = estado["cenario"]["area_monitor"]
        imagem = carregar_imagem(proximo_caso["imagem"], area_monitor.size, manter_proporcao=True)
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
