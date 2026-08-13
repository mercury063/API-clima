
import requests as rq

interruptor = True
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
        return "Erro! verifique os dados e tente novamente"

def descobrirCEP(estado, cidade, enderecp):
    api = f"https://viacep.com.br/ws/{estado}/{cidade}/{enderecp}/json/"
    resultado = rq.get(api)
    status = resultado.status_code
    if status == 200:
        formato = resultado.json()
        cep = formato['cep']
        return cep
    else:
        return "Erro! verifique os dados e tente novamente"
while interruptor:
    selecto = int(input("digite 1 para consultar cep ou 2 para descobrir cep: "))

    if selecto == 1:
        cep = input("digite o cep: ")
        interruptor = False
        formato = cepc(cep)
        print(f"CEP: {formato[0]}\n CIDADE:{formato[1]}\n ENDEREÇO: {formato[2]}\n BAIRRO: {formato[3]}\n ESTADO: {formato[4]}")
    elif selecto == 2:
        estado = input("Digite o estado: ")
        cidade = input("Digite a cidade: ")
        enderecp = input("Digite o endereço: ")
        print(descobrirCEP(estado, cidade, enderecp))
        interruptor = False
        
    else:
        print("Opção inválida!")
        continue