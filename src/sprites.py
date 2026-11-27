import pygame

class Botao:
    """Classe base para criação de botões interativos na bancada."""
    def __init__(self, x, y, largura, altura, cor, texto, cor_texto):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor
        self.texto = texto
        self.cor_texto = cor_texto
        self.fonte = pygame.font.Font(None, 24)

    def desenhar(self, tela):
        # Desenha o retângulo do botão na bancada
        pygame.draw.rect(tela, self.cor, self.rect, border_radius=6)
        # Renderiza e centraliza o texto
        txt_surface = self.fonte.render(self.texto, True, self.cor_texto)
        txt_rect = txt_surface.get_rect(center=self.rect.center)
        tela.blit(txt_surface, txt_rect)

    def verificar_clique(self, posicao_mouse):
        """Retorna True se o mouse clicou em cima do botão."""
        return self.rect.collidepoint(posicao_mouse)


class GerenciadorSprites:
    """Responsável por criar, organizar e gerenciar os elementos visuais da bancada de trabalho."""
    def __init__(self, largura_tela, altura_tela):
        inicio_botoes = (largura_tela - 736) // 2
        altura_botoes = altura_tela - 70

        # 1. Criar os três botões de classificação (HUMAN, AI GENERATED, INCONCLUSIVE)
        self.botao_human = Botao(
            inicio_botoes, altura_botoes, 150, 40, (70, 130, 180), "HUMAN", (255, 255, 255)
        )
        self.botao_ai = Botao(
            inicio_botoes + 160, altura_botoes, 150, 40, (205, 92, 92), "AI GENERATED", (255, 255, 255)
        )
        self.botao_inconclusive = Botao(
            inicio_botoes + 320, altura_botoes, 150, 40, (112, 128, 144), "INCONCLUSIVE", (255, 255, 255)
        )

        # 2. Criar o botão de consultar pistas (ferramenta de investigação na bancada)
        self.botao_consultar_pistas = Botao(
            inicio_botoes + 480, altura_botoes, 256, 40, (46, 139, 87),
            "Consultar Pistas e Informações", (255, 255, 255)
        )

        # Agrupando os elementos para facilitar a organização visual e loops de renderização
        self.botoes = [
            self.botao_human,
            self.botao_ai,
            self.botao_inconclusive,
            self.botao_consultar_pistas
        ]

    def desenhar_elementos(self, tela):
        """Organiza e desenha todos os botões e elementos visuais na bancada."""
        for botao in self.botoes:
            botao.desenhar(tela)

    def tratar_evento_mouse(self, evento):
        """Implementa a interação com o mouse, comunicando a escolha com o módulo principal."""
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos_mouse = evento.pos
            
            if self.botao_human.verificar_clique(pos_mouse):
                return "HUMAN"
            elif self.botao_ai.verificar_clique(pos_mouse):
                return "AI_GENERATED"
            elif self.botao_inconclusive.verificar_clique(pos_mouse):
                return "INCONCLUSIVE"
            elif self.botao_consultar_pistas.verificar_clique(pos_mouse):
                return "CONSULTAR_PISTAS"
                
        return None
