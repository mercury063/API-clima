## Documentação das APIs

> Esta documentação tem o objetivo de servir como dados de referência das APIs utilizadas no projeto.

### Sumário
- 1. [Base (Geolocalizador e Previsão do tempo)](#base-geolocalizador-e-previsão-do-tempo)
- 2. [Geolocalizador](#geolocalizador)
- 3. [Previsão do tempo](#previsão-do-tempo)
- 4. [API de obtenção e consulta de CEP (ViaCEP)](#api-de-obtenção-e-consulta-de-cep-viacep)
- 5. [Referências no Código](#referências-no-código)
  - 5.1 [Geolocalização e Clima (`script.py`)](#geolocalização-e-clima)
  - 5.2 [CEP (`cep.py`)](#cep)

---

## Base (Geolocalizador e Previsão do tempo)
A API do **Open-Meteo** é uma API pública aberta para uso em projetos de estudos e não comercial. Ela se caracteriza por usar a chamada **GET**, a mesma usada pelos **navegadores web**.

## Geolocalizador
A API de geolocalização do Open-Meteo utiliza a chamada **GET** e recebe 3 parâmetros obrigatórios: `name`, `count` e `language`. 

Exemplo: `https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=10&language=en&format=json` irá gerar a saída:

```json
{
  "results": [
    {
      "id": 2950159,
      "name": "Berlin",
      "latitude": 52.52437,
      "longitude": 13.41053,
      "elevation": 74,
      "feature_code": "PPLC",
      "country_code": "DE",
      "admin1_id": 2950157,
      "admin3_id": 6547383,
      "admin4_id": 6547539,
      "timezone": "Europe/Berlin",
      "population": 3426354,
      "postcodes": [
        "10967",
        "13347"
      ],
      "country_id": 2921044,
      "country": "Germany",
      "admin1": "State of Berlin",
      "admin3": "Berlin, Stadt",
      "admin4": "Berlin"
    },
    {
      "id": 5083330,
      "name": "Berlin",
      "latitude": 44.46867,
      "longitude": -71.18508,
      "elevation": 311,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 5090174,
      "admin2_id": 5084973,
      "admin3_id": 5083340,
      "timezone": "America/New_York",
      "population": 9367,
      "postcodes": [
        "03570"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "New Hampshire",
      "admin2": "Coos",
      "admin3": "City of Berlin"
    },
    {
      "id": 4500771,
      "name": "Berlin",
      "latitude": 39.79123,
      "longitude": -74.92905,
      "elevation": 50,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 5101760,
      "admin2_id": 4501019,
      "admin3_id": 4500776,
      "timezone": "America/New_York",
      "population": 7590,
      "postcodes": [
        "08009"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "New Jersey",
      "admin2": "Camden",
      "admin3": "Borough of Berlin"
    },
    {
      "id": 4349706,
      "name": "Brunswick",
      "latitude": 39.31427,
      "longitude": -77.62777,
      "elevation": 90,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 4361885,
      "admin2_id": 4355594,
      "timezone": "America/New_York",
      "population": 6116,
      "postcodes": [
        "21716"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "Maryland",
      "admin2": "Frederick County"
    },
    {
      "id": 5245497,
      "name": "Berlin",
      "latitude": 43.96804,
      "longitude": -88.94345,
      "elevation": 246,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 5279468,
      "admin2_id": 5255015,
      "admin3_id": 5245510,
      "timezone": "America/Chicago",
      "population": 5420,
      "postcodes": [
        "54923"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "Wisconsin",
      "admin2": "Green Lake",
      "admin3": "City of Berlin"
    },
    {
      "id": 4348460,
      "name": "Berlin",
      "latitude": 38.32262,
      "longitude": -75.21769,
      "elevation": 11,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 4361885,
      "admin2_id": 4374180,
      "timezone": "America/New_York",
      "population": 5065,
      "postcodes": [
        "21811"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "Maryland",
      "admin2": "Worcester"
    },
    {
      "id": 4930431,
      "name": "Berlin",
      "latitude": 42.3812,
      "longitude": -71.63701,
      "elevation": 100,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 6254926,
      "admin2_id": 4956199,
      "admin3_id": 4930436,
      "timezone": "America/New_York",
      "population": 2422,
      "postcodes": [
        "01503"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "Massachusetts",
      "admin2": "Worcester",
      "admin3": "Town of Berlin"
    },
    {
      "id": 4556518,
      "name": "Berlin",
      "latitude": 39.92064,
      "longitude": -78.9578,
      "elevation": 710,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 6254927,
      "admin2_id": 5212857,
      "admin3_id": 4556520,
      "timezone": "America/New_York",
      "population": 2019,
      "postcodes": [
        "15530"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "Pennsylvania",
      "admin2": "Somerset",
      "admin3": "Borough of Berlin"
    },
    {
      "id": 4557666,
      "name": "East Berlin",
      "latitude": 39.9376,
      "longitude": -76.97859,
      "elevation": 131,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 6254927,
      "admin2_id": 4556228,
      "admin3_id": 4557667,
      "timezone": "America/New_York",
      "population": 1534,
      "postcodes": [
        "17316"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "Pennsylvania",
      "admin2": "Adams County",
      "admin3": "Borough of East Berlin"
    },
    {
      "id": 5147132,
      "name": "Berlin",
      "latitude": 40.56117,
      "longitude": -81.7943,
      "elevation": 391,
      "feature_code": "PPL",
      "country_code": "US",
      "admin1_id": 5165418,
      "admin2_id": 5157783,
      "admin3_id": 5147154,
      "timezone": "America/New_York",
      "population": 898,
      "postcodes": [
        "44610"
      ],
      "country_id": 6252001,
      "country": "United States",
      "admin1": "Ohio",
      "admin2": "Holmes",
      "admin3": "Berlin Township"
    }
  ],
  "generationtime_ms": 0.5606413
}
```

> Essa base pode ser usada como exemplo para você entender o retorno do **GET** dessa API e adaptar para suas necessidades ou projetos pessoais.

## Previsão do tempo
A API de previsão do tempo do Open-Meteo utiliza obrigatoriamente dados de latitude e longitude para enviar dados em seu **GET** e retorna também o código 200 (HTTP OK). Exemplo de saída da API usando `https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m` de referência:

```json
{
  "latitude": 52.52,
  "longitude": 13.419998,
  "generationtime_ms": 99.4424819946289,
  "utc_offset_seconds": 0,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "elevation": 38,
  "hourly_units": {
    "time": "iso8601",
    "temperature_2m": "°C"
  },
  "hourly": {
    "time": [
      "2026-08-13T00:00",
      "2026-08-13T01:00",
      "2026-08-13T02:00",
      "2026-08-13T03:00",
      "2026-08-13T04:00",
      "2026-08-13T05:00",
      "2026-08-13T06:00",
      "2026-08-13T07:00",
      "2026-08-13T08:00",
      "2026-08-13T09:00",
      "2026-08-13T10:00",
      "2026-08-13T11:00",
      "2026-08-13T12:00",
      "2026-08-13T13:00",
      "2026-08-13T14:00",
      "2026-08-13T15:00",
      "2026-08-13T16:00",
      "2026-08-13T17:00",
      "2026-08-13T18:00",
      "2026-08-13T19:00",
      "2026-08-13T20:00",
      "2026-08-13T21:00",
      "2026-08-13T22:00",
      "2026-08-13T23:00",
      "2026-08-14T00:00",
      "2026-08-14T01:00",
      "2026-08-14T02:00",
      "2026-08-14T03:00",
      "2026-08-14T04:00",
      "2026-08-14T05:00",
      "2026-08-14T06:00",
      "2026-08-14T07:00",
      "2026-08-14T08:00",
      "2026-08-14T09:00",
      "2026-08-14T10:00",
      "2026-08-14T11:00",
      "2026-08-14T12:00",
      "2026-08-14T13:00",
      "2026-08-14T14:00",
      "2026-08-14T15:00",
      "2026-08-14T16:00",
      "2026-08-14T17:00",
      "2026-08-14T18:00",
      "2026-08-14T19:00",
      "2026-08-14T20:00",
      "2026-08-14T21:00",
      "2026-08-14T22:00",
      "2026-08-14T23:00",
      "2026-08-15T00:00",
      "2026-08-15T01:00",
      "2026-08-15T02:00",
      "2026-08-15T03:00",
      "2026-08-15T04:00",
      "2026-08-15T05:00",
      "2026-08-15T06:00",
      "2026-08-15T07:00",
      "2026-08-15T08:00",
      "2026-08-15T09:00",
      "2026-08-15T10:00",
      "2026-08-15T11:00",
      "2026-08-15T12:00",
      "2026-08-15T13:00",
      "2026-08-15T14:00",
      "2026-08-15T15:00",
      "2026-08-15T16:00",
      "2026-08-15T17:00",
      "2026-08-15T18:00",
      "2026-08-15T19:00",
      "2026-08-15T20:00",
      "2026-08-15T21:00",
      "2026-08-15T22:00",
      "2026-08-15T23:00",
      "2026-08-16T00:00",
      "2026-08-16T01:00",
      "2026-08-16T02:00",
      "2026-08-16T03:00",
      "2026-08-16T04:00",
      "2026-08-16T05:00",
      "2026-08-16T06:00",
      "2026-08-16T07:00",
      "2026-08-16T08:00",
      "2026-08-16T09:00",
      "2026-08-16T10:00",
      "2026-08-16T11:00",
      "2026-08-16T12:00",
      "2026-08-16T13:00",
      "2026-08-16T14:00",
      "2026-08-16T15:00",
      "2026-08-16T16:00",
      "2026-08-16T17:00",
      "2026-08-16T18:00",
      "2026-08-16T19:00",
      "2026-08-16T20:00",
      "2026-08-16T21:00",
      "2026-08-16T22:00",
      "2026-08-16T23:00",
      "2026-08-17T00:00",
      "2026-08-17T01:00",
      "2026-08-17T02:00",
      "2026-08-17T03:00",
      "2026-08-17T04:00",
      "2026-08-17T05:00",
      "2026-08-17T06:00",
      "2026-08-17T07:00",
      "2026-08-17T08:00",
      "2026-08-17T09:00",
      "2026-08-17T10:00",
      "2026-08-17T11:00",
      "2026-08-17T12:00",
      "2026-08-17T13:00",
      "2026-08-17T14:00",
      "2026-08-17T15:00",
      "2026-08-17T16:00",
      "2026-08-17T17:00",
      "2026-08-17T18:00",
      "2026-08-17T19:00",
      "2026-08-17T20:00",
      "2026-08-17T21:00",
      "2026-08-17T22:00",
      "2026-08-17T23:00",
      "2026-08-18T00:00",
      "2026-08-18T01:00",
      "2026-08-18T02:00",
      "2026-08-18T03:00",
      "2026-08-18T04:00",
      "2026-08-18T05:00",
      "2026-08-18T06:00",
      "2026-08-18T07:00",
      "2026-08-18T08:00",
      "2026-08-18T09:00",
      "2026-08-18T10:00",
      "2026-08-18T11:00",
      "2026-08-18T12:00",
      "2026-08-18T13:00",
      "2026-08-18T14:00",
      "2026-08-18T15:00",
      "2026-08-18T16:00",
      "2026-08-18T17:00",
      "2026-08-18T18:00",
      "2026-08-18T19:00",
      "2026-08-18T20:00",
      "2026-08-18T21:00",
      "2026-08-18T22:00",
      "2026-08-18T23:00",
      "2026-08-19T00:00",
      "2026-08-19T01:00",
      "2026-08-19T02:00",
      "2026-08-19T03:00",
      "2026-08-19T04:00",
      "2026-08-19T05:00",
      "2026-08-19T06:00",
      "2026-08-19T07:00",
      "2026-08-19T08:00",
      "2026-08-19T09:00",
      "2026-08-19T10:00",
      "2026-08-19T11:00",
      "2026-08-19T12:00",
      "2026-08-19T13:00",
      "2026-08-19T14:00",
      "2026-08-19T15:00",
      "2026-08-19T16:00",
      "2026-08-19T17:00",
      "2026-08-19T18:00",
      "2026-08-19T19:00",
      "2026-08-19T20:00",
      "2026-08-19T21:00",
      "2026-08-19T22:00",
      "2026-08-19T23:00"
    ],
    "temperature_2m": [17.7, 16.9, 16.4, 15.9, 15.4, 15.5, 16.5, 18, 20, 22.2, 23.7, 24.9, 25.9, 26.6, 27.2, 27.4, 27.4, 27.1, 26.3, 24.9, 23.3, 21.9, 20.7, 19.7, 18.9, 18.2, 17.6, 17, 16.5, 16.4, 17, 18.9, 21.3, 23.9, 26.2, 28, 29.2, 30.1, 30.8, 31, 31, 30.6, 29.4, 27.5, 25.6, 23.8, 22.1, 20.7, 19.8, 19, 18.4, 18, 17.5, 18, 20.1, 23.1, 26.2, 29, 31, 32.4, 33, 32.8, 32.4, 32, 31.8, 31.2, 29.4, 27.1, 24.8, 23.4, 22.2, 21.3, 20.7, 20.1, 19.6, 19.1, 18.5, 18, 17.9, 18.6, 19.7, 20.7, 21.5, 22, 22.1, 21.4, 20.2, 19.1, 18.4, 17.8, 17.2, 16.8, 16.5, 16.2, 15.8, 15.5, 15.2, 14.9, 14.7, 14.6, 14.5, 14.6, 15, 16, 17.3, 18.5, 19.3, 19.9, 20.4, 20.8, 20.9, 20.9, 20.7, 20.1, 19.6, 19.6, 18.7, 18, 17.4, 16.9, 16.6, 16.5, 16.6, 16.6, 16.4, 16.2, 16.2, 16.6, 17.3, 17.8, 17.9, 17.8, 18.1, 19.3, 21.1, 22.3, 22.6, 22.4, 22, 21.7, 21.2, 20.6, 19.8, 18.9, 18.1, 17.6, 17.2, 16.9, 16.9, 17, 17.3, 18.1, 19, 19.9, 20.5, 21.1, 21.5, 21.8, 22.1, 21.8, 20.7, 19.2, 17.8, 17, 16.4, 16, 15.5, 15.2]
  }
}
```

## API de obtenção e consulta de **CEP** (ViaCEP)

A API do ViaCEP é utilizada para realizar tanto consulta quanto a obtenção de **CEPs**. Ela retorna o código **200 (HTTP OK)** em consultas válidas e um dicionário com chave `'erro'` igual a `'true'` em caso de erro na consulta. Exemplo de saída de consulta de **CEP** utilizando `https://viacep.com.br/ws/RS/Porto%20Alegre/Domingos+Jos%C3%A9/json/`:

```json
[
  {
    "cep": "91790-072",
    "logradouro": "Rua Domingos José Poli",
    "complemento": "",
    "unidade": "",
    "bairro": "Restinga",
    "localidade": "Porto Alegre",
    "uf": "RS",
    "estado": "Rio Grande do Sul",
    "regiao": "Sul",
    "ibge": "4314902",
    "gia": "",
    "ddd": "51",
    "siafi": "8801"
  },
  {
    "cep": "91910-420",
    "logradouro": "Rua José Domingos Varella",
    "complemento": "",
    "unidade": "",
    "bairro": "Cavalhada",
    "localidade": "Porto Alegre",
    "uf": "RS",
    "estado": "Rio Grande do Sul",
    "regiao": "Sul",
    "ibge": "4314902",
    "gia": "",
    "ddd": "51",
    "siafi": "8801"
  },
  {
    "cep": "90420-200",
    "logradouro": "Rua Domingos José de Almeida",
    "complemento": "",
    "unidade": "",
    "bairro": "Rio Branco",
    "localidade": "Porto Alegre",
    "uf": "RS",
    "estado": "Rio Grande do Sul",
    "regiao": "Sul",
    "ibge": "4314902",
    "gia": "",
    "ddd": "51",
    "siafi": "8801"
  }
]
```

# Referências no código

> Como referência: no **`script.py`**, linhas **5 a 25** (geolocalização), linhas **27 a 37** (clima); e no **`cep.py`**, linhas **5 a 19** (consulta de CEP), linhas **21 a 30** (obtenção de CEP). Seguem as funções (`def`) como exemplos de utilização da API:

## Geolocalização e Clima:

`script.py`
```python
import requests as rq

"""Função de Geolocalização"""
def localizacao(cidade):
    # Url da API de geolocalização (Open-Meteo)
    api = "https://geocoding-api.open-meteo.com/v1/search"

    # Parâmetros base que vão ser enviados para a API
    pb = {"name": cidade, "count": 1, "language": "pt-BR"}
    # Enviando os parâmetros para a API
    rb = rq.get(api, params=pb)
    # Transformando a resposta em um dicionário
    db = rb.json()

    # Pega o primeiro item (posição 0) da lista 'results'
    r = db["results"][0]
    # Guarda os dados de latitude que estão dentro do dicionário 
    lat = (r["latitude"])
    # Guarda os dados de longitude que estão dentro do dicionário 
    lng = r["longitude"]
    # Guarda o nome correto da cidade (caso a pessoa erre ou digite algo diferente) 
    name = r['name']
    # Retorna os dados em tupla/lista
    return lat, lng, name
```

`script.py`
```python
import requests as rq

"""Função de Clima"""
def clima(latitude, longitude):
    # Url da API de clima (Open-Meteo)
    apiclima = 'https://api.open-meteo.com/v1/forecast'
    # Parâmetros que vão ser enviados para a API 
    pc = {"latitude": latitude, "longitude": longitude, "current": "temperature_2m,precipitation,precipitation_probability,relative_humidity_2m", "timezone": "auto"}
    # Enviando os parâmetros para a API
    rp = rq.get(apiclima, params=pc)
    # Transformando a resposta em um dicionário
    dc = rp.json()
    # Retorna os dados
    return dc
```

## CEP:

`cep.py`
```python 
import requests as rq

"""Função de busca de CEP com tratamento de erro"""
def descobrirCEP(estado, cidade, enderecp):
    api = f"https://viacep.com.br/ws/{estado}/{cidade}/{enderecp}/json/"
    resultado = rq.get(api)
    status = resultado.status_code
    if status == 200:
        formato = resultado.json()
        cep = formato['cep']
        return cep
    else:
        return "Erro! Verifique os dados e tente novamente"
```

`cep.py`
```python
import requests as rq

"""Função de consulta de CEP com tratamento de erro"""
def cepc(cep):
    api = f"https://viacep.com.br/ws/{cep}/json/"
    resultado = rq.get(api)
    formato = resultado.json()
    status = resultado.status_code
    cep1 = formato['cep']
    rua = formato['logradouro']
    bairro = formato['bairro']
    cidade = formato['localidade']
    estado = formato['estado']
    if status == 200 and formato != {"erro": "true"}:
        return cep1, cidade, rua, bairro, estado
    else:
        return "Erro! Verifique os dados e tente novamente"
```
