import requests
import json

def obtener_urls_gifs(api_key, consulta, cantidad=20, random=False):
    base_url = "https://tenor.googleapis.com/v2/search"
    
    parametros = {
        'key': api_key,
        'q': consulta,
        'limit': cantidad,
        'random': random
    }

    try:
        respuesta = requests.get(base_url, params=parametros)
        respuesta.raise_for_status()  

        datos_json = respuesta.json()

   
        urls_gifs = [
            item['media_formats']['gif']['url']
            for item in datos_json.get('results', [])
        ]

        return urls_gifs

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a la API de Tenor: {e}")
        return []


tenor_api_key = "TuClaveDeAPI"

while True:

    consulta = input("Ingresa la consulta (por ejemplo, 'anime angry'): ")
    cantidad = int(input("Ingresa la cantidad de GIFs que deseas (valor máximo 50): "))
    random_order = input("¿Ordenar los resultados de forma aleatoria? (True/False): ").capitalize() == "True"


    urls_gifs = obtener_urls_gifs(tenor_api_key, consulta, cantidad, random_order)


    print("\nURLs de los GIFs:")
    print(',\n'.join([f"'{url}'" for url in urls_gifs]))

    seguir_buscando = input("\n¿Quieres buscar más GIFs? (Sí/No): ").capitalize()
    if seguir_buscando != "Si":
        break
