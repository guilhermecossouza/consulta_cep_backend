import requests
import json

def consulta_cep(event, context):
    str_cep = event["pathParameters"]["codCep"] if "codCep" in event["pathParameters"] else "31140190"
    cep = str_cep.replace("-", "")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url=url)
    if response.status_code == 200:
        serverless_response = {
            "statusCode": 200,
            "body": json.dumps(response.json(), ensure_ascii=False)
        }    
    else:
        serverless_response = {
            "statusCode": 400,
            "body": {"message": "URL not faud"}
        }        
    return serverless_response 

