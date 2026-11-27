import pygame

from src.config import COR_BOTAO_JOGAR, COR_FUNDO, COR_TEXTO


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


def quebrar_linhas(texto, fonte, largura_maxima):
    linhas = []
    linha = ""
    for palavra in texto.split():
        candidata = f"{linha} {palavra}".strip()
        if linha and fonte.size(candidata)[0] > largura_maxima:
            linhas.append(linha)
            linha = palavra
        else:
            linha = candidata

    if linha:
        linhas.append(linha)
    return linhas


def criar_tutorial(largura, altura):
    lado = min(largura, altura) - 64
    painel = pygame.Rect(0, 0, lado, lado)
    painel.center = (largura // 2, altura // 2)
    botao = pygame.Rect(0, 0, 212, 54)
    botao.midbottom = (painel.centerx, painel.bottom - 42)
    fundo = pygame.Surface((largura, altura), pygame.SRCALPHA)
    fundo.fill((4, 8, 16, 176))
    fonte_texto = pygame.font.Font(None, 36)

    conteudo = [
        (
            "Você é um investigador, seu trabalho é definir se as imagens "
            "selecionadas são feitas por Inteligência Artificial ou não.",
            None,
        ),
        ("Use o botão verde se a imagem for real", "botao_verde.png"),
        ("Caso a imagem seja feita por IA, aperte o botão vermelho", "botao_vermelho.png"),
        ("Em caso de dúvida, aperte o botão amarelo", "botao_amarelo.png"),
        (
            "Você tem acesso a uma pasta, com informações sobre a imagem. "
            "Analise essas pistas e tire suas conclusões sobre a imagem.",
            "pasta.png",
        ),
    ]
    quadros = []
    for texto, arquivo in conteudo:
        imagem = None
        if arquivo is not None:
            imagem = carregar_imagem(
                f"assets/imagens/{arquivo}", (210, 140), manter_proporcao=True
            )
        linhas = quebrar_linhas(texto, fonte_texto, painel.width - 108)
        quadros.append((linhas, imagem))

    return {
        "painel": painel,
        "botao": botao,
        "fundo": fundo,
        "quadros": quadros,
        "indice": 0,
        "fonte_texto": fonte_texto,
        "fonte_controles": pygame.font.Font(None, 28),
    }


def tratar_evento_tutorial(evento, estado):
    if evento.type != pygame.MOUSEBUTTONDOWN or evento.button != 1:
        return False
    if not estado["botao"].collidepoint(evento.pos):
        return False
    if estado["indice"] == len(estado["quadros"]) - 1:
        return True

    estado["indice"] += 1
    return False


def desenhar_tutorial(tela, estado):
    painel = estado["painel"]
    botao = estado["botao"]
    fonte_texto = estado["fonte_texto"]
    fonte_controles = estado["fonte_controles"]
    indice = estado["indice"]
    total_quadros = len(estado["quadros"])
    linhas, imagem = estado["quadros"][indice]

    tela.blit(estado["fundo"], (0, 0))
    pygame.draw.rect(tela, COR_FUNDO, painel, border_radius=10)
    pygame.draw.rect(tela, (67, 98, 119), painel, width=2, border_radius=10)
    desenhar_texto_centralizado(
        tela, f"{indice + 1} de {total_quadros}", fonte_controles,
        (143, 197, 226), (painel.centerx, painel.top + 54)
    )

    centro_texto = painel.centery - 26
    if imagem is not None:
        centro_texto = painel.top + painel.height * 2 // 5
        centro_imagem = (painel.centerx, painel.top + painel.height * 2 // 3)
        tela.blit(imagem, imagem.get_rect(center=centro_imagem))

    espaco_linhas = fonte_texto.get_linesize() + 6
    linha_y = centro_texto - (len(linhas) - 1) * espaco_linhas // 2
    for linha in linhas:
        desenhar_texto_centralizado(
            tela, linha, fonte_texto, COR_TEXTO, (painel.centerx, linha_y)
        )
        linha_y += espaco_linhas

    rotulo = "Começar" if indice == total_quadros - 1 else "Avançar"
    pygame.draw.rect(tela, COR_BOTAO_JOGAR, botao, border_radius=6)
    desenhar_texto_centralizado(tela, rotulo, fonte_controles, COR_TEXTO, botao.center)


def desenhar_pistas(tela, area_monitor, caso, fonte):
    painel = area_monitor.inflate(-34, -34)
    pygame.draw.rect(tela, COR_FUNDO, painel, border_radius=6)
    desenhar_texto_centralizado(
        tela, "Pistas da publicação", fonte, COR_TEXTO,
        (painel.centerx, painel.top + 36)
    )

    linhas = [f"Fonte: {caso['fonte']}", f"Autoria: {caso['autoria']}", f"Data: {caso['data']}"]
    linhas.append("")
    linhas.extend(quebrar_linhas(caso["pista"], fonte, painel.width - 36))
    linha_y = painel.top + 80
    for linha in linhas:
        desenhar_texto_centralizado(tela, linha, fonte, COR_TEXTO, (painel.centerx, linha_y))
        linha_y += fonte.get_linesize() + 5

    desenhar_texto_centralizado(
        tela, "Clique na pasta para voltar", fonte, (143, 197, 226),
        (painel.centerx, painel.bottom - 30)
    )


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
