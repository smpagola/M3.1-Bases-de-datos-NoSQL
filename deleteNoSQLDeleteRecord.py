import requests

# URL base de la API
url_base = "https://66b4e4f09f9169621ea4c19d.mockapi.io/api/v1/contactos"

# ID del registro que deseas eliminar
registro_id = 1  # Cambia este valor al ID del registro que deseas eliminar


# Función para eliminar un registro existente
def eliminar_registro(registro_id):
    # Construir la URL para el registro específico
    url = f"{url_base}/{registro_id}"

    # Realizar la solicitud DELETE para eliminar el registro
    response = requests.delete(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print(f"Registro con ID {registro_id} eliminado con éxito.")
    else:
        print(f"Error al eliminar el registro. Código de estado: {response.status_code}")


# Llamar a la función para eliminar el registro
eliminar_registro(registro_id)
