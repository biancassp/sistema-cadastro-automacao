# Automação de Lançamentos Contábeis

Esse projeto foi desenvolvido para resolver um problema de produtividade: 
o processo maçante e manual de lançamentos em sistemas contábeis.

## Solução
Desenvolvi uma base composta por:
1. **Sistema de Cadastro**: Uma interface para recebimento de dados de produtos;
2. **Bot de Automação**: Um assistente que lê uma planilha Excel e realiza os lançamentos automaticamente no sistema.

## Demonstração
![Demonstracao da Automação]
(Demonstracao.gif.gif)

## Tecnologias Utilizadas
* **Python** para a lógica principal;
* **PyAutoGUI** para a automação da interface;
* **FreeSimpleGUI** para a criação da interface do sistema;
* **Openpyxl** para a manipulação dos dados em Excel.

## Estrutura do Repositório
* `/sistema`: Contém o código da interface de cadastro;
* `app.py`: Bot assistente (executor da automação);
* `vendas_de_produtos.xlsx`: Base de dados de exemplo.
