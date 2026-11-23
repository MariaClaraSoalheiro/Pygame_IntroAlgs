# AI, Please!

**AI, Please!** é um jogo desenvolvido em Python com Pygame, no qual o jogador analisa publicações e tenta identificar se suas imagens foram criadas por seres humanos ou por inteligência artificial.

> **Versão inicial:** esta é uma versão parcial e simplificada do jogo, desenvolvida para demonstrar sua mecânica principal. Novas funcionalidades e melhorias serão adicionadas durante o desenvolvimento.

## Como executar

Instale o Pygame:

```bash
pip install pygame
```

Execute:

```bash
python main.py
```

## Organização dos módulos

- **`main.py`**: inicializa o jogo, cria a janela e controla o loop principal.
- **`config.py`**: centraliza as configurações do jogo.
- **`funcoes.py`**: reúne funções auxiliares reutilizáveis.
- **`menu.py`**: controla a apresentação e interação do menu inicial.
- **`jogo.py`**: controla a mecânica da partida, pontuação, vidas e publicações.
- **`sprites.py`**: gerencia os botões e suas interações.
- **`dados.py`**: armazena os casos e as funções de recorde.

## Recursos atuais

- Menu inicial.
- Classificação de publicações em HUMAN, AI GENERATED e INCONCLUSIVE.
- Sistema básico de pontuação e vidas.
- Progressão entre publicações.