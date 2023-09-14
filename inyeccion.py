import httpx
import asyncio

# Lista de objetos a enviar por POST
objetos = [
   

{"usuario":"Usuario519231123456B56","fecha_ingreso":"9/14/2023","pais":"	 República Dominicana","hora_ingreso":"20:41:38","ciudad":"La Altagracia","ruta":"/losplanosdelapaz","tiempo":"	0:04:16	","dispositivo":"celular"}






    # Agrega más objetos aquí si los tienes
]

# URL de la endpoint donde enviar los objetos
url = "https://sistemas-backend-analitica-django-mongo.onrender.com/insertar_usuario/"

# Función asincrónica para enviar objetos
async def enviar_objetos():
    async with httpx.AsyncClient() as client:
        for objeto in objetos:
            try:
                response = await client.post(url, json=objeto)
                response.raise_for_status()  # Verifica si hay errores en la solicitud
                print(f"Objeto enviado con éxito: {objeto}")
            except httpx.HTTPError as e:
                print(f"Error al enviar objeto: {e}")

# Ejecutar la función asincrónica
if __name__ == "__main__":
    asyncio.run(enviar_objetos())
