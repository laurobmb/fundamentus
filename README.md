![alt text](imagens/investimento.jpg "Title")

# Fundamentus
Esta é uma pequena API feita em python3 para análise de ações da BOVESPA utilizando o site fundamentus (www.fundamentus.com.br), que retorna os principais indicadores fundamentalistas em formato JSON. A API utiliza o microframework Flask. Também é possível utilizar via linha de comando.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


[![Docker Repository on Quay](https://quay.io/repository/lagomes/fundamentus/status "Docker Repository on Quay")](https://quay.io/repository/lagomes/fundamentus)

## Etapas

### Ações
0. [X] Efetuar web scrapingg na página da fundamentus para obter ações da bolsa brasileira
1. [X] Excluir empresas com EBIT negativo
2. [X] Excluir empresas com EBITDA negativo
3. [X] Excluir empresas com crescimento negativo nos ultimos 5 anos
4. [ ] Excluir empresas em recuperação judicial
5. [X] Criar ranking por Dividend yield, P/VP, P/L
6. [X] Gerar csv a partir dos dados processados
7. [X] Mostra Dividend yield maior que 6%
8. [X] Evita Earning Yield negativo e maior que 10%
9. [X] Evita PL negativo e maior que 5
10. [X] Evita VP negativo e maior que 5
11. [X] Evita ROE negativo e maior que 80%
12. [x] selecao de segmento

### Fundos imobiliarios
0. [X] excluindo fundos com liquidez baixa
1. [x] seleciona fundos que pagam Dividend yield maior que 6%
2. [x] Evita fundos do Rendimento da Operação negativos (FFO Yield)
3. [x] Evita PL negativo e maior que 5
4. [X] Evita VP negativo e maior que 5
5. [x] Evita fundos com liqueidez menor que 5000
6. [X] Criar ranking por Dividend yield, P/VP, FFOYield e Liquidez 

## instalação:
* pip3 install -r app/requirements.txt

## Executando na linha de comando
### Ações 
* python3 app/fundamentus.py
### FII
* python3 app/fundamentusfii.py

## Iniciando a API
Execute o _python3 app/app.py_ e conecte no endereço a baixo com seu browser

* http://127.0.0.1:8080/


## Acessando as melhores ações e fundos imobiliários
Aqui voce pode colocar um valor menor ou igual a 100, como segue o exemplo

* http://127.0.0.1:8080/acoes/10
* http://127.0.0.1:8080/fii/10

## Acessando as APIs
* http://127.0.0.1:8080/api/acoes/fundamentus.json
* http://127.0.0.1:8080/api/fii/fundamentus.json

## Health check
* http://127.0.0.1:8080/health

## Docker app
* podman build -t fundamentus:v1 .
* podman run -it --rm --name fundamentus_app -p 8080:8080 fundamentus:v1

## Deploy openshift
[Comandos openshift](https://github.com/laurobmb/fundamentus/blob/master/openshift.comandos.md)

## Sites para consulta 
[Investidor10](https://investidor10.com.br/)

[Fundamentus](https://fundamentus.com.br/)

[StatusInvest](https://statusinvest.com.br/)

![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)
