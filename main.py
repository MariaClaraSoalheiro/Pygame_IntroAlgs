
import pygame

from src.config import LARGURA_TELA, ALTURA_TELA, TITULO_JOGO, FPS
from src.menu import criar_menu, tratar_evento_menu, desenhar_menu
from src.jogo import criar_bancada, tratar_evento_bancada, desenhar_bancada
from src.funcoes import criar_tutorial, desenhar_tutorial, tratar_evento_tutorial


def main():

    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    # Preparando o menu inicial.
    fonte_titulo, fonte_botao, botao_jogar = criar_menu(
        LARGURA_TELA, ALTURA_TELA
    )

    tela_atual = "menu"
    estado_bancada = None
    estado_tutorial = None

    rodando = True

    # Loop principal da aplicacao.
    while rodando:

        # Verificando os eventos.
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            elif tela_atual == "menu":

                iniciar_jogo = tratar_evento_menu(evento, botao_jogar)

                if iniciar_jogo:
                    estado_bancada = criar_bancada(
                        LARGURA_TELA, ALTURA_TELA
                    )
                    estado_tutorial = criar_tutorial(LARGURA_TELA, ALTURA_TELA)
                    tela_atual = "tutorial"

            elif tela_atual == "tutorial":
                if tratar_evento_tutorial(evento, estado_tutorial):
                    estado_tutorial = None
                    tela_atual = "bancada"

            elif tela_atual == "bancada":
                tratar_evento_bancada(evento, estado_bancada)

        if not rodando:
            break

        # Desenhando a tela atual.
        if tela_atual == "menu":

            desenhar_menu(
                tela, LARGURA_TELA, ALTURA_TELA,
                fonte_titulo, fonte_botao, botao_jogar
            )

        else:
            desenhar_bancada(
                tela, LARGURA_TELA, ALTURA_TELA, estado_bancada,
                interativa=tela_atual == "bancada"
            )
            if tela_atual == "tutorial":
                desenhar_tutorial(tela, estado_tutorial)

        pygame.display.flip()

        # Controlando a quantidade de atualizacoes por segundo.
        relogio.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
