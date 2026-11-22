import pygame


def executar_menu(tela):

    largura = 800
    altura = 600

    fonte_titulo = pygame.font.SysFont(None, 72)
    fonte_botao = pygame.font.SysFont(None, 36)

    botao_jogar = pygame.Rect(325, 400, 150, 50)

    rodando = True

    while rodando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_jogar.collidepoint(evento.pos):
                    return True

        tela.fill((25, 25, 35))

        texto = fonte_titulo.render("AI, Please!", False, (255, 255, 255))
        retangulo_texto = texto.get_rect(center=(largura // 2, altura // 3))
        tela.blit(texto, retangulo_texto)

        pygame.draw.rect(tela, (70, 130, 180), botao_jogar, border_radius=8)

        texto_botao = fonte_botao.render("JOGAR", False, (255, 255, 255))
        retangulo_botao = texto_botao.get_rect(center=botao_jogar.center)
        tela.blit(texto_botao, retangulo_botao)

        pygame.display.flip()