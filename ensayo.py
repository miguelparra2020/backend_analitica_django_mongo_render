import requests
import json
def obtener_usuarios():
    urlget = "https://us-east-1.aws.data.mongodb-api.com/app/data-jocyn/endpoint/data/v1/action/find"

    payload = {
        "collection": "Usuarios",
        "database": "Estadistica",
        "dataSource": "estadistica",
        "filter": {},
        "limit": 1000000,
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'LInXiCwRYyJIrl5I3Lsfc76iyQMSoxDx5FYhThbHexGwMepzzdYVmxETgp3hgXxw',
        'Accept': 'application/ejson'
    }

    response = requests.post(urlget, headers=headers, json=payload)

    # Procesar la respuesta JSON
    data = response.json()
    return data

print(obtener_usuarios())