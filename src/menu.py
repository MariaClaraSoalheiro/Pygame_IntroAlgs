import pygame

pygame.init()

largura = 800
altura = 600

# criando a janela e definindo seu título.
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("AI, Please!")

# fonte para o título.
fonte_titulo = pygame.font.SysFont(None, 72)

rodando = True

while rodando:

    ''' 1 - verificação de eventos '''

    # neste for, a ideia principal é ficar conferindo
    # se o jogador pediu para fechar a janela.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    ''' 2 - desenho dos elementos '''

    # o fill() preenche uma superfície com uma cor.
    tela.fill((25, 25, 35))

    ''' TÍTULO '''
    
    # o render() transforma texto em superfície.
    texto = fonte_titulo.render("AI, Please!", False, (255, 255, 255))

    # para ajudar a manter o título no centro da tela, é usado o get_rect(),
    # que retorna uma referência geométrica da superfície de texto.
    # ele recebe center=(x, y), fazendo o centro dele aparecer nessa posição.
    retangulo_texto = texto.get_rect(center=(largura // 2, altura // 3))

    # desenhando o título na tela.
    tela.blit(texto, retangulo_texto)

    # atualização da tela.
    pygame.display.flip()

pygame.quit()