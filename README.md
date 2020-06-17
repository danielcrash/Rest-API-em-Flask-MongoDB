# Rest API em Flask & MongoDB

Entre no shell python dentro da pasta do seu projeto e adicione as variáveis de ambiente:
```sh
$ export MONGO_URI="SUA_URI"
$ export MONGO_DBNAME="SEU_DB_NAME"
```
Em seguida instale os requirements:
```sh
$ pip install -r requirements.txt
```
Após isso, para rodar a aplicação execute o comando no diretório 'resources'
```sh
$ python app.py 
```
Use o Postman com a url (http://localhost:5000), com os endpoints para fazer a chamada na API

### Endpoints
- GET /users - endpoint para obter todos os usuários

- GET /users/:name - endpoints para obter um usuário

- POST /users -  endpoint para adicionar um novo usuário

- DELETE /users/:name - endpoint para deletar pelo nome

### Construído com

 - Linguagem: Python 3.7
 - Utilizado para chamada na API: Postman
 - Biblioteca: Flask & MongoDB
