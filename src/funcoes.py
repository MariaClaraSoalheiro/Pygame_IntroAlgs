import pygame


def carregar_imagem(caminho, tamanho, manter_proporcao=False):
    imagem = pygame.image.load(caminho).convert_alpha()
    if manter_proporcao:
        area = pygame.Rect((0, 0), tamanho)
        tamanho = imagem.get_rect().fit(area).size

    return pygame.transform.smoothscale(imagem, tamanho)


def carregar_cenario_bancada(largura, altura):
    fundo = pygame.image.load("assets/imagens/hud.png").convert()
    area_disponivel = pygame.Rect(0, 44, largura, altura - 150)
    area_fundo = fundo.get_rect().fit(area_disponivel)
    escala_x = area_fundo.width / fundo.get_width()
    escala_y = area_fundo.height / fundo.get_height()

    # As coordenadas correspondem à abertura do monitor nos dois PNGs.
    area_monitor = pygame.Rect(
        area_fundo.x + round(527 * escala_x),
        area_fundo.y + round(142 * escala_y),
        round(607 * escala_x),
        round(422 * escala_y),
    )
    moldura = pygame.image.load("assets/imagens/computadortransparente.png").convert_alpha()
    contorno_interno = moldura.subsurface((243, 101, 957, 693))

    return {
        "fundo": pygame.transform.smoothscale(fundo, area_fundo.size),
        "area_fundo": area_fundo,
        "contorno_monitor": pygame.transform.smoothscale(contorno_interno, area_monitor.size),
        "area_monitor": area_monitor,
    }


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
