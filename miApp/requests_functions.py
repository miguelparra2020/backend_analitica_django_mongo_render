import requests
import json

def insertar_usuario(datos_usuario):
    urlpost = "https://us-east-1.aws.data.mongodb-api.com/app/data-jocyn/endpoint/data/v1/action/insertOne"

    # Utiliza los datos proporcionados en el parámetro 'datos_usuario'
    payload = {
        "collection": "Usuarios",
        "document": datos_usuario,  # Utiliza los datos del usuario proporcionados
        "database": "Estadistica",
        "dataSource": "estadistica",
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'LInXiCwRYyJIrl5I3Lsfc76iyQMSoxDx5FYhThbHexGwMepzzdYVmxETgp3hgXxw',
        'Accept': 'application/ejson'
    }

    response = requests.post(urlpost, headers=headers, json=payload)

    # Procesar la respuesta JSON
    data = response.json()
    return data

def obtener_usuarios():
    urlget = "https://us-east-1.aws.data.mongodb-api.com/app/data-jocyn/endpoint/data/v1/action/find"

    payload = {
        "collection": "Usuarios",
        "database": "Estadistica",
        "dataSource": "estadistica",
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
