# Rest API em Flask & MongoDB com teste de Métricas Prometheus (Counter & Histogram)

Instale os requirements:
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

- GET /users/:name - endpoint para obter um usuário

- POST /users -  endpoint para adicionar um novo usuário

- DELETE /users/:name - endpoint para deletar pelo nome

O banco foi feito em um Cluster no [MongoDB Clound](https://www.mongodb.com/cloud) para fins de teste. 

### Construído com

 - Linguagem: Python 3.7
 - Utilizado para chamada na API: Postman
 - Biblioteca: Flask & MongoDB
