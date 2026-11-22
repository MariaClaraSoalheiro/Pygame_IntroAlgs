
import pygame
from src.sprites import GerenciadorSprites
from src.dados import carregar_casos


def executar_bancada(tela):

    largura = 800
    altura = 600

    gerenciador = GerenciadorSprites(largura, altura)

    casos = carregar_casos()
    indice_caso = 1
    caso_atual = casos[indice_caso]

    imagem = pygame.image.load(caso_atual["imagem"]).convert_alpha()
    imagem = pygame.transform.smoothscale(imagem, (300, 200))

    fonte = pygame.font.SysFont(None, 48)
    fonte_publicacao = pygame.font.SysFont(None, 28)
    fonte_status = pygame.font.SysFont(None, 32)

    pontuacao = 0
    vidas = 3
    mensagem = ""
    fim_de_jogo = False

    classificacoes = {
        "HUMAN": "HUMAN",
        "AI_GENERATED": "GERADO POR IA",
        "INCONCLUSIVE": "INCONCLUSIVO"
    }

    rodando = True

    while rodando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            resultado = gerenciador.tratar_evento_mouse(evento)

            if resultado is not None and not fim_de_jogo:

                if resultado == "CONSULTAR_PISTAS":
                    mensagem = "Consulta de pistas ainda nao disponivel."

                elif resultado in classificacoes:

                    resposta = classificacoes[resultado]

                    mensagem = ""

                    if resultado != "INCONCLUSIVE":

                        if resposta == caso_atual["classificacao"]:
                            pontuacao += 10
                        else:
                            vidas -= 1

                    # Verificando se o jogador ainda tem vidas.
                    if vidas == 0:
                        fim_de_jogo = True

                    else:
                        # Avancando para o proximo caso.
                        indice_caso += 1

                        if indice_caso < len(casos):

                            caso_atual = casos[indice_caso]

                            imagem = pygame.image.load(
                                caso_atual["imagem"]
                            ).convert_alpha()

                            imagem = pygame.transform.smoothscale(
                                imagem, (300, 200)
                            )

                        else:
                            fim_de_jogo = True

        tela.fill((25, 25, 35))

        # Exibindo a pontuacao e as vidas.
        texto_pontos = fonte_status.render(
            f"Pontos: {pontuacao}", False, (255, 255, 255)
        )
        tela.blit(texto_pontos, texto_pontos.get_rect(center=(100, 35)))

        texto_vidas = fonte_status.render(
            f"Vidas: {vidas}", False, (255, 255, 255)
        )
        tela.blit(texto_vidas, texto_vidas.get_rect(center=(700, 35)))

        # Titulo da bancada.
        texto = fonte.render(
            "Bancada de Investigação", False, (255, 255, 255)
        )
        retangulo_texto = texto.get_rect(center=(largura // 2, 75))
        tela.blit(texto, retangulo_texto)

        # Exibindo a imagem da publicacao.
        retangulo_imagem = imagem.get_rect(center=(largura // 2, 220))
        tela.blit(imagem, retangulo_imagem)

        # Exibindo a legenda da publicacao.
        texto_publicacao = fonte_publicacao.render(
            caso_atual["publicacao"], False, (255, 255, 255)
        )
        retangulo_publicacao = texto_publicacao.get_rect(
            center=(largura // 2, 350)
        )
        tela.blit(texto_publicacao, retangulo_publicacao)

        gerenciador.desenhar_elementos(tela)

        if fim_de_jogo:
            texto_mensagem = fonte.render(
                "fim de jogo", False, (255, 100, 100)
            )
        else:
            texto_mensagem = fonte_publicacao.render(
                mensagem, False, (255, 255, 255)
            )

        retangulo_mensagem = texto_mensagem.get_rect(
            center=(largura // 2, 530)
        )
        tela.blit(texto_mensagem, retangulo_mensagem)

        pygame.display.flip()
