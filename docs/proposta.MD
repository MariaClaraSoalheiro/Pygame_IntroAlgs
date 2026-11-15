# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Informe o nome provisório do jogo.

**Nome:**

> AI, Please!.

## 2. Integrantes do grupo

- Nome 1: Maria Clara Soalheiro Bessa
- Nome 2: Mateus Evaristo Melo
- Nome 3: Priscilla Louzada Nesio
- Nome 4: Ian Souza Maciel

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

>  Inteligência Artificial e identificação de conteúdos gerados por IA.

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> O jogador deverá investigar publicações digitais para identificar se os conteúdos foram produzidos por seres humanos ou gerados por inteligência artificial, considerando pistas como autoria, fontes, datas e outras informações disponíveis. O jogo mostrará que nem sempre é possível determinar com segurança a origem de um conteúdo, incentivando a análise crítica, o uso responsável da IA e o reconhecimento da falta de evidências.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Jogo de investigação e classificação de conteúdos digitais, inspirado em mecânicas de inspeção de documentos.

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> *AI, Please!* é um jogo inspirado na dinâmica de inspeção de *Papers, Please*, no qual o jogador atua em um departamento responsável por verificar a origem de conteúdos digitais. A cada rodada, será apresentada uma publicação contendo informações complementares, como fonte, data, horário, autoria e outros elementos que auxiliem na investigação. O jogador utilizará ferramentas simples disponíveis em sua bancada para consultar pistas e escolher uma das três classificações: HUMANO, GERADO POR IA ou INCONCLUSIVO. Serão apresentados cinco casos previamente preparados. As respostas serão registradas sem revelar se estão corretas durante as rodadas, e o resultado será mostrado somente ao final da partida.

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> Investigar as evidências disponíveis e classificar corretamente pelo menos quatro das cinco publicações, distinguindo conteúdos produzidos por seres humanos, conteúdos gerados por inteligência artificial e situações em que as informações disponíveis são insuficientes para uma conclusão segura.

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

- Regra 1: O jogador começa a partida com três vidas e zero pontos.
- Regra 2: Cada rodada apresenta uma publicação digital com informações complementares e ferramentas para consultar pistas.
- Regra 3: Para cada publicação, o jogador escolhe uma das classificações: HUMANO, GERADO POR IA ou INCONCLUSIVO.
- Regra 4: Uma classificação correta vale 10 pontos; uma incorreta resulta na perda de uma vida. Os acertos e erros não são revelados durante a partida.
- Regra 5: A partida termina após os cinco casos ou quando as três vidas forem perdidas. Somente na tela final são exibidos acertos, erros, pontuação e percentual de aproveitamento.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> O jogador vencerá ao concluir corretamente pelo menos quatro dos cinco casos apresentados, mantendo pelo menos uma vida ao final da partida. Ao alcançar esse objetivo, será exibida uma tela de vitória com a pontuação obtida.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> A partida terminará com derrota caso o jogador perca todas as três vidas ou conclua os cinco casos sem atingir o mínimo de quatro classificações corretas. Ao final, será apresentada uma tela com a pontuação total, o número de acertos e erros, o percentual de aproveitamento e a possibilidade de iniciar uma nova partida.

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal:** Bancada digital de um funcionário responsável por analisar a origem de publicações digitais.
- **Obstáculos ou desafios:** Publicações com diferentes origens e evidências incompletas, contraditórias ou que exigem atenção aos detalhes.
- **Itens ou objetos de interação:** Cartões com conteúdos digitais e informações complementares, ferramentas de consulta de pistas e três botões de classificação: HUMANO, GERADO POR IA e INCONCLUSIVO.
- **Pontuação, vidas, tempo ou progresso:** Três vidas iniciais, 10 pontos por acerto e progresso de até cinco casos. A pontuação, os acertos, os erros e a quantidade de vidas perdidas serão apresentados somente ao final da partida, para não revelar os resultados durante as rodadas.

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

> O jogador utilizará o mouse para consultar as informações e ferramentas da bancada, selecionar uma das classificações: HUMANO, GERADO POR IA ou INCONCLUSIVO, e avançar para a próxima publicação..

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: Organizar a interface no Pygame para exibir as imagens, os textos e os botões de forma legível.
- Dificuldade 2: Desenvolver a lógica de investigação e classificação dos conteúdos digitais, garantindo que as ferramentas de consulta e as opções de resposta funcionem corretamente.
- Dificuldade 3: Implementar corretamente o sistema de pontuação, controle de vidas e condições de vitória e derrota, garantindo que os resultados sejam calculados e apresentados apenas ao final da partida.

## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> A versão mínima terá uma tela inicial, uma tela de investigação e uma tela final. Serão cadastrados cinco casos, cada um contendo uma publicação digital, informações complementares, pistas previamente definidas e uma classificação correta (HUMANO, GERADO POR IA ou INCONCLUSIVO). O jogador poderá consultar pistas e registrar sua escolha utilizando o mouse. O jogo controlará internamente três vidas, a pontuação e o número de casos analisados. Cada acerto renderá 10 pontos e cada erro reduzirá uma vida, sem informar imediatamente o resultado. A partida terminará ao concluir os cinco casos ou perder todas as vidas. Na tela final, serão apresentados a vitória ou derrota, a pontuação, os acertos, os erros, o percentual de aproveitamento e a opção de reiniciar.

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: Adicionar novas ferramentas de investigação, permitindo que o jogador consulte mais informações sobre a origem e a confiabilidade das publicações
- Melhoria 2: Implementar diferentes níveis de dificuldade, com casos mais complexos e pistas menos evidentes.
- Melhoria 3: Adicionar efeitos sonoros, animações simples e melhorias visuais para tornar o jogo mais dinâmico e interativo.
