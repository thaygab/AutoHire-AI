import json
from pathlib import Path


def carregar_tecnologias() -> list:
    """
    Carrega a lista de tecnologias utilizadas pelo sistema.

    Retorno:
        list: Lista de tecnologias.
    """

    caminho = (
        Path(__file__)
        .parent.parent
        / "knowledge"
        / "tecnologias.json"
    )

    with open(
        caminho,
        "r",
        encoding="utf-8"
    ) as arquivo:
         
         tecnologias = json.load(arquivo)

    return tecnologias