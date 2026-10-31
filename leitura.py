import csv
import json

from tratamento_erros import tratar_erro


def ler_csv(caminho):

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:

            leitor = csv.DictReader(arquivo)

            dados = list(leitor)

        return dados

    except Exception as erro:

        tratar_erro(erro, caminho)

        return None


def ler_json(caminho):

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:

            dados = json.load(arquivo)

        return dados

    except Exception as erro:

        tratar_erro(erro, caminho)

        return None