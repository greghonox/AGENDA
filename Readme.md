# Praticando conceitos de *Django Framework com Python 3.10*.


## O desafio será realizar:
1. O usuário pode marcar uma consulta
    1.1. Não deve ser possível marcar consultas para um dia e horário não disponível
    1.2. Não deve ser possível marcar consultas para dia e horário passados
2. O usuário pode desmarcar uma consulta
    2.1. Não deve ser possível desmarcar uma consulta que já aconteceu
3. O usuário pode visualizar as todas as consultas marcadas que ainda não aconteceram
4. O gestor da clínica pode cadastrar um médico
5. O gestor da clínica pode criar a agenda do médico para cada dia

___

## Antes do desafio, __caso queira rodar o projeto faço os passos abaixos:__
---
1. Faça build do docker compose para ter o projeto rodando. __(Lembrando que não vou explicar os conceitos basicos de instalar o docker e coisas mais basicas)__


```python
docker-compose up
```

Ele deve aparecer no seu terminal alguns sinais semelhantes a esses:
![build](https://github.com/greghonox/AGENDA/blob/main/docs/build.png)

2. Após isso deve se __migragar os dados__ para poder ter a base no postgres.


```python
docker exec -it id bash 
```
2.1 Caso não tenha o __id__:


```python
docker ps
```
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/docker_ps.png)

2.2 Observe o nome da imagem que deve ser __agenda_web__. Você deve copiar o numero da coluna __CONTAINER_ID__. Depois voltar no passo **2** para conectar.

3. Migração dos dados:

```python
cd agenda/ 
python manage.py migrate
python manage.py createsuperuser 
```    

![migrate_and_createsuperuser](https://github.com/greghonox/AGENDA/blob/main/docs/migrate_and_createsuperuser.png)

## Agora estamos pronto...

### Autorização
---
#### Foi adicionado autorização com token em todas as rotas como *plus*. Então deve se solicitar o token confome requisição abaixo para utilizar.

```python
POST {{server_base}}/token/
Content-Type: application/json

{
    "username": "greg",
    "password": "123"
}
```
#### _Detalhe:_ O campo *username* e *password* são informações de login que criou no comando de *createsuperuser*.

#### Antes de mais nada existe um arquivo de testes dentro de __agenda/playground__ chamado *test.http*. Ele é os verbos de __GET POST PUT e DELETE__ para todas entidades desse projeto. Mas ainda sim vamos comentar algumas coisas.
[test.http](https://github.com/greghonox/AGENDA/blob/main/agenda/playground/test.http)

#### O test.http é usado junto com __vs code__ assim consegue ter um cliente __rest__ no ambiente de desenvolvimento. Veja abaixo o icone da extenção
![test.http](https://github.com/greghonox/AGENDA/blob/main/docs/http.png)

#### Veja também como fica no vs code os test.http aberto para uso
![test.http](https://github.com/greghonox/AGENDA/blob/main/docs/test_http_aberto.png)

### 1. O usuário pode marcar uma consulta
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/cadastrar_agenda.png)

### 1.1. Não deve ser possível marcar consultas para um dia e horário não disponível
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/error_data_anterior.png)
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/error_consulta_agendada_admin.png)


### 1.2. Não deve ser possível marcar consultas para dia e horário passados
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/error_consulta_agendada.png)

#### Como ficou as validações anteriores em codigo:
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/codigo_validacao.png)

### 2. O usuário pode desmarcar uma consulta
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/ecluir_consulta.png)

### 2.1. Não deve ser possível desmarcar uma consulta que já aconteceu
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/error_excluir_consulta_agendada.png)
#### Veja também o codigo de validação
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/codigo_validacao2.png)

### 3. O usuário pode visualizar as todas as consultas marcadas que ainda não aconteceram(__Isso usando o filtro, caso quiera__)
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/consulta_agenda.png)

#### 4. O gestor da clínica pode cadastrar um médico
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/cadastro_doutor.png)

#### 4.1 Caso exista um __CRM__ já registrado ele vai apresentar erro
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/cadastro_doutor_erro_crm.png)

### 5. O gestor da clínica pode criar a agenda do médico para cada dia
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/cadastrar_agenda.png)

# ***Um pouco mais...***

### O que vamos ver aqui?
#### 1. Criação de cadastro simples.
#### 2. Consulta de cadastro simples.
#### 3. Conexão com banco de dados.
#### 4. Migração de modelos de tabelas. (__Veja o histórico do github__)
#### 5. Esboço de testes unitários.

### Requisito para rodar projeto
#### docker e docker-compose


### Historico de desenvolvimento:
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/github_history.png)

### Admin do django
#### Primeiro faça o login para entrar no admin django
[admin django](http://127.0.0.1:8000/admin)

### Tela de login no adm:
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/login.png)

### Testes unitários(não implementado):
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/tests.png)