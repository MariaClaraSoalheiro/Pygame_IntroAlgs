def carregar_casos():
    """Retorna os casos que serão analisados pelo jogador."""

    # Lista que armazena as publicações do jogo
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
            "publicacao": "Descrição de um jardim futurista.",
            "fonte": "Arquivo de demonstração",
            "autoria": "Sistema de IA",
            "data": "20/11/2026",
            "pista": "O registro de criação confirma o uso de um gerador de IA.",
            "classificacao": "GERADO POR IA"
        }
    ]

    # Retorna os casos cadastrados
    return casos