# AI, Please!

Projeto da disciplina de Introdução a Algoritmos, desenvolvido em Python utilizando Pygame.

Esta é uma versão inicial e parcial do jogo, desenvolvida para apresentar sua mecânica principal e permitir a execução e o acompanhamento do projeto durante as aulas.

## Integrantes do grupo

- Maria Clara Soalheiro Bessa
- Mateus Evaristo
- Priscilla Louzada Nesio
- Ian Souza Maciel

## Estrutura do projeto

- `main.py`: ponto de entrada e controlador principal da aplicação.
- `src/`: contém os módulos principais do jogo.
- `assets/`: armazena os recursos visuais utilizados nas publicações.
- `docs/`: documentação do projeto e proposta inicial.

## Descrição do jogo

AI, Please! é um jogo de investigação no qual o jogador analisa publicações digitais e tenta identificar se suas imagens foram criadas por seres humanos ou por inteligência artificial.

As publicações apresentam imagens acompanhadas de legendas, simulando conteúdos encontrados em redes sociais.

## Objetivo do jogador

Analisar as publicações e classificá-las corretamente como HUMAN, AI GENERATED ou INCONCLUSIVE, acumulando pontos e tentando manter suas vidas até o final da partida.

## Regras do jogo

- O jogador começa com 3 vidas.
- Uma classificação correta entre HUMAN e AI GENERATED concede 10 pontos.
- Uma classificação incorreta entre essas duas opções reduz uma vida.
- A opção INCONCLUSIVE permite avançar sem ganhar pontos ou perder vidas.
- Após cada classificação, uma nova publicação é apresentada.
- A partida termina quando o jogador perde todas as vidas ou quando todos os casos são analisados.

## Controles

- **Mouse:** selecionar as opções de classificação.
- **HUMAN:** classificar a publicação como conteúdo humano.
- **AI GENERATED:** classificar a publicação como gerada por inteligência artificial.
- **INCONCLUSIVE:** indicar que não existem evidências suficientes.
- **Consultar Pistas e Informações:** recurso ainda em desenvolvimento.
- **Fechar janela:** encerrar o jogo.

## Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/MariaClaraSoalheiro/Pygame_IntroAlgs.git
cd Pygame_IntroAlgs
```

Instale o Pygame:

```bash
pip install pygame
```

Execute o jogo:

```bash
python main.py
```

## Testes

Os testes automatizados ainda não foram implementados nesta versão inicial. A execução e as interações do jogo são verificadas manualmente.

## Observações

- Esta versão possui uma mecânica básica e recursos visuais simplificados.
- Novas publicações, funcionalidades e melhorias serão adicionadas ao longo do desenvolvimento.
- O código está organizado em módulos, separados conforme suas responsabilidades.