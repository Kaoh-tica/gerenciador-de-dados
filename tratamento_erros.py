import json
def tratar_erro(erro, caminho):

    if isinstance(erro, FileNotFoundError):

        print(f"Erro: arquivo não encontrado: {caminho}")

    elif isinstance(erro, PermissionError):

        print(f"Erro: sem permissão para acessar: {caminho}")

    elif isinstance(erro, UnicodeDecodeError):

        print("Erro: problema na codificação dos caracteres.")

    elif isinstance(erro, json.JSONDecodeError):

        print("Erro: o arquivo JSON possui formato inválido.")

    else:

        print(f"Erro inesperado: {erro}")