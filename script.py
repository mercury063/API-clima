import requests as rq

def localizacao(cidade):
    api = "https://geocoding-api.open-meteo.com/v1/search"


    pb = {"name": cidade, "count": 1, "language": "pt-BR"}
    rb = rq.get(api, params=pb)
    db = rb.json()

    r = db["results"][0]
    lat = (r["latitude"])
    lng = r["longitude"]
    name = {r['name']}
    return lat, lng, name

def clima(latitude, longitude):
    apiclima = 'https://api.open-meteo.com/v1/forecast'
    pc = {"latitude": latitude, "longitude": longitude, "current": "temperature_2m,precipitation,precipitation_probability", "timezone": "auto"}
    rp = rq.get(apiclima, params=pc)
    dc = rp.json()
    return dc

l = input("Digite o nome de sua cidade para saber o clima: ")
c = localizacao(l)[0]
c1 = localizacao(l)[1]
re = clima(c, c1)["current"]
print(f"temperatura em {localizacao(l)[2]}: {re["temperature_2m"]}°C")
print(f"probabilidade de precipitação: {re["precipitation_probability"]}%")
print(f"precipitação atual: {re["precipitation"]}mm")



