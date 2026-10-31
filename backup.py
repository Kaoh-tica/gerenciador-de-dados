import shutil
import os
from datetime import datetime

from tratamento_erros import tratar_erro


def criar_backup(caminho):

    try:

        # Verifica se o arquivo existe
        if not os.path.exists(caminho):

            print("Arquivo ainda não existe. Backup não necessário.")
            return True

        # Cria a pasta de backups, caso não exista
        os.makedirs("backups", exist_ok=True)

        # Cria um nome único para o backup
        nome_arquivo = os.path.basename(caminho)

        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

        destino = f"backups/{nome_arquivo}_{data_hora}.bak"

        # Copia o arquivo original
        shutil.copy2(caminho, destino)

        print(f"Backup criado com sucesso: {destino}")

        return True

    except Exception as erro:

        tratar_erro(erro, caminho)

        return False