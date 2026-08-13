#Importando a biblioteca "resquests" e a chamando de "rq"
import requests as rq

#Função para descobrir a latitude e longitude da cidade
def localizacao(cidade):
    #Url da Api de geolocalização(Open mateo)
    api = "https://geocoding-api.open-meteo.com/v1/search"

    #Parametros base que vão ser enviados para api
    pb = {"name": cidade, "count": 1, "language": "pt-BR"}
    #Enviando os parametros para api
    rb = rq.get(api, params=pb)
    #Transformando a resposta em um dicionario
    db = rb.json()

    # Pega o primeiro item (posição 0) da lista 'results'
    r = db["results"][0]
    #Guarda os dados de latitude que está dentro do dicionario 
    lat = (r["latitude"])
    #Guarda os dados de longitude que está dentro do dicionario 
    lng = r["longitude"]
    #Guarda o nome certo da cidade( Caso a pessoa erre ou digite algo diferente) 
    name = r['name']
    #retorna os dados em lista 
    return lat, lng, name

def clima(latitude, longitude):
    #url da api de clima (Open mateo)
    apiclima = 'https://api.open-meteo.com/v1/forecast'
    #Parametros que vão ser enviados para api 
    pc = {"latitude": latitude, "longitude": longitude, "current": "temperature_2m,precipitation,precipitation_probability,relative_humidity_2m", "timezone": "auto"}
    #Enviando os parametros para api
    rp = rq.get(apiclima, params=pc)
    #Transformando a resposta em um dicionario
    dc = rp.json()
    #retorna os dados
    return dc

l = input("Digite o nome de sua cidade para saber o clima: ")

c = localizacao(l)[0]
c1 = localizacao(l)[1]
re = clima(c, c1)["current"]
print(f"temperatura em {localizacao(l)[2]}: {re["temperature_2m"]}°C")
print(f"probabilidade de precipitação: {re["precipitation_probability"]}%")
print(f"precipitação atual: {re["precipitation"]}mm")
print(f"umidade atual: {re["relative_humidity_2m"]}%")


