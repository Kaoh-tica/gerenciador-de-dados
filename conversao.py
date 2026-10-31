import csv
import json

from backup import criar_backup
from tratamento_erros import tratar_erro


def converter_csv_para_json(arquivo_csv, arquivo_json):

    try:

        # Lendo o CSV
        with open(arquivo_csv, "r", encoding="utf-8") as arquivo:

            leitor = csv.DictReader(arquivo)

            dados = list(leitor)

        # Criando backup antes da escrita
        if not criar_backup(arquivo_json):
            return

        # Escrevendo o JSON
        with open(arquivo_json, "w", encoding="utf-8") as arquivo:

            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

        print("Conversão CSV para JSON realizada com sucesso!")

    except Exception as erro:

        tratar_erro(erro, arquivo_csv)


def converter_json_para_csv(arquivo_json, arquivo_csv):

    try:

        # Lendo o JSON
        with open(arquivo_json, "r", encoding="utf-8") as arquivo:

            dados = json.load(arquivo)

        if not dados:

            print("O arquivo JSON está vazio.")
            return

        campos = dados[0].keys()

        # Criando backup
        if not criar_backup(arquivo_csv):
            return

        # Escrevendo o csv
        with open(arquivo_csv, "w", encoding="utf-8", newline="") as arquivo:

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            escritor.writeheader()

            escritor.writerows(dados)

        print("Conversão JSON para CSV realizada com sucesso!")

    except Exception as erro:

        tratar_erro(erro, arquivo_json)