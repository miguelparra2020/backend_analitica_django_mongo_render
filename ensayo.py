import requests
import json

urlpost = "https://us-east-1.aws.data.mongodb-api.com/app/data-jocyn/endpoint/data/v1/action/insertOne"

urlget = "https://us-east-1.aws.data.mongodb-api.com/app/data-jocyn/endpoint/data/v1/action/find"

objectUsuario = {
    "usuario": "NuevoUsuario1234",
    "fecha_ingreso": "8/25/2023",
    "hora_ingreso": "09:30:00",
    "pais": "Colombia",
    "ciudad": "Pereira",
    "tiempo": "00:03:45",
    "ruta": "/nueva-pagina",
    "dispositivo": "Celular"
    }



payload = json.dumps({
    "collection": "Usuarios",
    "document": objectUsuario,
    "database": "Estadistica",
    "dataSource": "estadistica",
})

payload2 = json.dumps({
    "collection": "Usuarios",
    "database": "Estadistica",
    "dataSource": "estadistica",
})

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'LInXiCwRYyJIrl5I3Lsfc76iyQMSoxDx5FYhThbHexGwMepzzdYVmxETgp3hgXxw',
    'Accept': 'application/ejson'
}

response = requests.request("POST", urlpost, headers=headers, data=payload)
response2 = requests.request("POST", urlget, headers=headers, data=payload2)

# Procesar la respuesta JSON
data = json.loads(response.text)
data2 = json.loads(response2.text)

print(data)
print(data2)