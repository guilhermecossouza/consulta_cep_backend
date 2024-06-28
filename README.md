Consulta CEP Backend

Este projeto implementa uma função Lambda para consulta de CEP utilizando Python 3.10, Docker, Docker Compose, Serverless Framework e a biblioteca requests. A aplicação também inclui uma página HTML5 para separar o front-end do back-end. Nota: Este projeto é executado localmente, pois não possuo conta na AWS.


Estrutura do Projeto:

consulta_cep_backend/
├── docker-compose.yaml
├── Dockerfile
├── serverless.yaml
└── source/
    ├── cep.py
    └── requirements.txt

Pré-requisitos:

|--Python 3.10
|--Docker
|--Docker Compose
|--Serverless Framework

Instalação:
|--1° Clone este repositório:
   |--git clone https://github.com/seu_usuario/consulta_cep_backend.git
   |--cd consulta_cep_backend

|--2° Construa e inicie os containers Docker:
   |--docker-compose up --build

|--3° Construa e inicie os containers Docker:
   |--docker-compose exec app pip install -r source/requirements.txt

Execução Local:
|---Para executar o projeto localmente, utilize os seguintes comandos:
    |---1° Inicie o ambiente Serverless localmente:
        |---serverless offline 
            |--OBS: Instale o plugin RUN serverless plugin install -n serverless-offline
    |---2° Em um novo terminal, envie uma requisição para o endpoint local. Exemplo de uso com curl:
        |-- curl -X GET http://localhost:3000/dev/consulta-cep?cep=01001000

Exemplo de Resposta
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}

Página HTML:
A aplicação inclui uma página HTML5 para a interface do usuário. Certifique-se de que o servidor está em execução e acesse a página em seu navegador.

Contribuição
|---1° Se desejar contribuir com o projeto, por favor, siga os passos abaixo:
|---2° Faça um fork do projeto.
|---3° Crie uma branch para sua feature (git checkout -b feature/nova-feature).
|---4° Faça commit das suas alterações (git commit -am 'Adiciona nova feature').
|---5° Faça push para a branch (git push origin feature/nova-feature).
|---6° Abra um Pull Request.

Licença
Este projeto está licenciado sob a MIT License.







