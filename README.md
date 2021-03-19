# CODAY - FastAPI - Conta Corrente
Api responsável por:
- Cadastrar contas e correntistas
- Realizar lançamentos de crédito e débito
- Exibir o saldo das contas

## Executar em ambiente de desenvolvimento
### Python
 - Version 3.8
  
### PyCharm
#### Configurando o Virtual Environment
1. Abra o menu File -> Open e navegue até a pasta raiz do projeto
2. Abra o menu File -> Settings, na tela a seguir, navegue até Project: backend -> Python Interpreter
3. Na tela a seguir clique na engrenagem na frente do campo "Python Interpreter" e clique em "add" 
4. Selecione a opção "New Environment" e em seguida clique em "OK"

#### Baixando as dependencias
1. Abra o terminal do PyCharm e digite `pip install -r requirements.txt`
2. Certifique-se que todas as dependencias foram instaladas corretamente

#### Executando o projeto
1. Clique com o botão direito no arquivo `main.py` e selecione a opção `Run main`
2. Para certificar-se que está tudo certo, abra o navegador e digite o endereço `http://localhost:8000/docs`
2.1 Uma pagina com a visualização dos endpoints deverá ficar visível

## Dependências
- fastapi==0.63.0 (API Framework)
- uvicorn==0.13.4 (Servidor de desenvolvimento)
