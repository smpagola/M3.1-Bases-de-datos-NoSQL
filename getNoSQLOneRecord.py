import requests

# URL base de la API
url_base = "https://66b4e4f09f9169621ea4c19d.mockapi.io/api/v1/contactos"


# Función para obtener un registro específico por ID
def obtener_registro_por_id(registro_id):
    # Construir la URL para el registro específico
    url = f"{url_base}/{registro_id}"

    # Realizar la solicitud GET para obtener los datos del registro
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir los datos JSON de la respuesta en un diccionario de Python
        data = response.json()

        # Mostrar los datos en formato plano
        print(f"Datos del registro con ID {registro_id}:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"Error al obtener el registro. Código de estado: {response.status_code}")


# ID del registro que deseas consultar
registro_id = 1  # Cambia este valor por el ID que deseas consultar

# Llamar a la función para mostrar el registro
obtener_registro_por_id(registro_id)
