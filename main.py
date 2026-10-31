from leitura import ler_csv, ler_json

from conversao import (
    converter_csv_para_json,
    converter_json_para_csv
)


def executar_testes():

    print("===== GERENCIADOR DE DADOS =====")

    # TESTE 1: Leitura CSV
    print("\n--- TESTE 1: LEITURA CSV ---")

    dados_csv = ler_csv("testes/teste.csv")

    print(dados_csv)

    # TESTE 2: Leitura JSON
    print("\n--- TESTE 2: LEITURA JSON ---")

    dados_json = ler_json("testes/teste.json")

    print(dados_json)

    # TESTE 3: Conversão CSV para JSON
    print("\n--- TESTE 3: CSV PARA JSON ---")

    converter_csv_para_json(
        "testes/teste.csv",
        "testes/convertido.json"
    )

    # TESTE 4: Conversão JSON para CSV
    print("\n--- TESTE 4: JSON PARA CSV ---")

    converter_json_para_csv(
        "testes/teste.json",
        "testes/convertido.csv"
    )

    # TESTE 5: Verificação dos arquivos convertidos
    print("\n--- TESTE 5: CONFERINDO CONVERSÕES ---")

    resultado_json = ler_json("testes/convertido.json")

    resultado_csv = ler_csv("testes/convertido.csv")

    print("JSON convertido:", resultado_json)

    print("CSV convertido:", resultado_csv)

    # TESTE 6: Backup
    print("\n--- TESTE 6: BACKUP AUTOMÁTICO ---")

    converter_csv_para_json(
        "testes/teste.csv",
        "testes/convertido.json"
    )

    # TESTE 7: Tratamento de erro
    print("\n--- TESTE 7: TRATAMENTO DE ERRO ---")

    ler_csv("testes/arquivo_inexistente.csv")

    print("\n===== TESTES FINALIZADOS =====")


if __name__ == "__main__":
    executar_testes()

