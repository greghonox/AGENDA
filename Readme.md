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
### 1. O usuário pode marcar uma consulta([Cadastro de consultas](http://127.0.0.1:8000/register_scheduler/))
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/cadastrar_agenda.png)

### 1.1. Não deve ser possível marcar consultas para um dia e horário não disponível
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/error_data_anterior.png)
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/error_consulta_agendada_admin.png)


### 1.2. Não deve ser possível marcar consultas para dia e horário passados
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/error_consulta_agendada.png)

#### Como ficou as validações anteriores em codigo:
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/codigo_validacao.png)

### 2. O usuário pode desmarcar uma consulta([Cadastro de consultas](http://127.0.0.1:8000/query_scheduler/))
#### Pode ser feito através do botão de excluir na consulta.
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/consulta_agenda.png)

### 2.1. Não deve ser possível desmarcar uma consulta que já aconteceu
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/error_excluir_consulta_agendada.png)
#### Veja também o codigo de validação
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/codigo_validacao2.png)

### 3. O usuário pode visualizar as todas as consultas marcadas que ainda não aconteceram
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/consulta_agenda.png)

#### 4. O gestor da clínica pode cadastrar um médico([Cadastro de consultas](http://127.0.0.1:8000/register_doctor/))
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/cadastro_doutor.png)

### 5. O gestor da clínica pode criar a agenda do médico para cada dia
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/cadastrar_agenda.png)

# ***Um pouco mais...***

### O que vamos ver aqui?
#### 1. Criação de cadastro simples.
#### 2. Consulta de cadastro simples.
#### 3. Conexão com banco de dados.
#### 4. Migração de modelos de tabelas. (__Veja o histórico do github__)
#### 5. Criação de __graficos com bootstrap__.
#### 6. Esboço de testes unitários.

### Requisito para rodar projeto
#### 1. Ter python <= 3.10
#### 2. Instalar o *requirements.txt*.
#### 3. Noção de __Makefile__ e comandos linux.

### Para começar, __Comandos abaixo funcionan apenas em sistema unix__.

```python
make create-venv
make install-requirements
make run
```

### Acessando o sistema:
[Cadastro de consultas](http://127.0.0.1:8000/register_scheduler/)
[Consulta da agenda](http://127.0.0.1:8000/query_scheduler/)
[Cadastro de Pacientes](http://127.0.0.1:8000/register_patient/)
[Consulta de Pacientes](http://127.0.0.1:8000/query_patient/)
[Cadastro de Doutores](http://127.0.0.1:8000/register_doctor/)
[Consulta de Doutores](http://127.0.0.1:8000/query_doctor/)
[Admin](http://127.0.0.1:8000/admin/)

### Historico de desenvolvimento:
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/github_history.png)

### Admin do django
#### Primeiro faça o login para entrar no admin django
[admin django](http://127.0.0.1:8000/admin)

### Credenciais para acesso:
```python
usuario: greg
senha: 123
```
### Tela de login no adm:
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/login.png)

### Tela de login no template:
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/login2.png)

### Testes unitários(não implementado):
![Grafico](https://github.com/greghonox/AGENDA/blob/main/docs/tests.png)