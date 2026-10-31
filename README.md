Gerenciador de Dados

1. Descrição do Projeto

O Gerenciador de Dados é um projeto desenvolvido em Python com o objetivo de realizar o gerenciamento e a persistência de informações em arquivos externos nos formatos CSV e JSON.

O sistema permite realizar a leitura, conversão e manipulação de dados, além de utilizar mecanismos de backup automático e tratamento de exceções para garantir maior segurança durante as operações.

2. Funcionalidades

- Leitura de arquivos CSV.
- Leitura de arquivos JSON.
- Conversão de CSV para JSON.
- Conversão de JSON para CSV.
- Backup automático antes das alterações.
- Tratamento de exceções durante as operações com arquivos.
- Preservação dos dados durante as conversões.

3. Tecnologias Utilizadas

- Python 3.
- Biblioteca csv.
- Biblioteca json.
- Gerenciador de contexto "with open()".
- PyCharm como ambiente de desenvolvimento.

4. Organização dos Arquivos

- "main.py": arquivo principal responsável pela execução e testes.
- "leitura.py": responsável pela leitura dos arquivos CSV e JSON.
- "conversao.py": responsável pelas conversões entre os formatos.
- "backup.py": responsável pela criação de cópias de segurança.
- "tratamento_erros.py": responsável pelo tratamento de exceções.
- "testes/": diretório com arquivos utilizados nos testes.
- "backups/": diretório destinado às cópias de segurança.

5. Como Executar o Projeto

1. Baixe ou clone o repositório.
2. Abra a pasta do projeto no PyCharm ou em outro ambiente Python.
3. Verifique se os arquivos e diretórios necessários estão presentes.
4. Execute o arquivo "main.py".
5. Confira os resultados apresentados no terminal.

6. Testes Realizados

Foram realizados testes para verificar:

- Leitura de arquivos CSV.
- Leitura de arquivos JSON.
- Conversão de CSV para JSON.
- Conversão de JSON para CSV.
- Conferência dos dados convertidos.
- Criação de backups automáticos.
- Tratamento de erros para arquivos inexistentes.

Os testes demonstraram o funcionamento das funcionalidades implementadas.

7. Integrante

- Tatila França de Sousa (26.1.20352)

8. Instituição

Centro Universitário UNIBALSAS.