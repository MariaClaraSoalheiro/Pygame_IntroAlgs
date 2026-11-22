def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0


def carregar_casos():
    """Retorna os casos que serão analisados pelo jogador."""

    casos = [
        {
            "id": 1,
            "publicacao": "Texto sem autoria identificada.",
            "fonte": "Desconhecida",
            "autoria": "Não informada",
            "data": "Não informada",
            "pista": "Não existem evidências suficientes para determinar a origem.",
            "classificacao": "INCONCLUSIVO"
        },
        {
            "id": 2,
            "imagem": "assets/imagens/caso1.png",
            "publicacao": "Foto do meu gato hoje de manhã.",
            "fonte": "Arquivo de demonstração",
            "autoria": "Sistema de IA",
            "data": "20/11/2026",
            "pista": "O registro de criação confirma o uso de um gerador de IA.",
            "classificacao": "GERADO POR IA"
        },
        {
            "id": 3,
            "imagem": "assets/imagens/caso2.png",
            "publicacao": "Encontrei esse gato no corredor hoje.",
            "fonte": "Wikimedia Commons",
            "autoria": "DogeGamer2015MZT",
            "data": "31/01/2022",
            "pista": "A fotografia foi disponibilizada pelo autor sob licença CC0.",
            "classificacao": "HUMAN"
        },
        {
            "id": 4,
            "imagem": "assets/imagens/caso3.png",
            "publicacao": "Finalmente conheci esse castelo na Alemanha!",
            "fonte": "Arquivo de demonstração",
            "autoria": "Sistema de IA",
            "data": "22/11/2026",
            "pista": "A imagem foi criada por um gerador de imagens de inteligência artificial.",
            "classificacao": "GERADO POR IA"
        },
        {
            "id": 5,
            "imagem": "assets/imagens/caso4.png",
            "publicacao": "Não sabia que o farol era tão bonito à noite.",
            "fonte": "Wikimedia Commons",
            "autoria": "Janus Y",
            "data": "04/12/2014",
            "pista": "A fotografia original foi publicada pelo autor e dedicada ao domínio público.",
            "classificacao": "HUMAN"
        }
    ]

    return casos