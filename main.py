import pygame
from src.menu import executar_menu
from src.jogo import executar_bancada


def main():

    pygame.init()

    largura = 800
    altura = 600

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("AI, Please!")

    # Exibindo o menu inicial.
    if executar_menu(tela):

        executar_bancada(tela)

    pygame.quit()


if __name__ == "__main__":
    main()