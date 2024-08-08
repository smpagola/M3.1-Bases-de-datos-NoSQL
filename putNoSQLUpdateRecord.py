import requests

# URL base de la API
url_base = "https://66b4e4f09f9169621ea4c19d.mockapi.io/api/v1/contactos"

# ID del registro que deseas modificar
registro_id = 1  # Cambia este valor al ID del registro que deseas actualizar

# Datos que deseas modificar en el registro
datos_modificados = {
    "nombre": "Carlos Gomez",
    "email": "carlos.gomez@example.com"
}


# Función para modificar un registro existente
def modificar_registro(registro_id, datos):
    # Construir la URL para el registro específico
    url = f"{url_base}/{registro_id}"

    # Realizar la solicitud PATCH para actualizar los datos
    response = requests.patch(url, json=datos)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir los datos JSON de la respuesta en un diccionario de Python
        data = response.json()

        print("Registro modificado con éxito. Datos actualizados:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"Error al modificar el registro. Código de estado: {response.status_code}")


# Llamar a la función para modificar el registro
modificar_registro(registro_id, datos_modificados)
