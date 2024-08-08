import requests

# URL base de la API
url_base = "https://66b4e4f09f9169621ea4c19d.mockapi.io/api/v1/contactos"

# Datos del nuevo registro a agregar
nuevo_registro = {
    "nombre": "Ana Lopez",
    "email": "ana.lopez@example.com",
    "telefono": "+9876543210"
}


# Función para agregar un nuevo registro
def agregar_registro(datos):
    # Realizar la solicitud POST para agregar los datos
    response = requests.post(url_base, json=datos)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 201:
        # Convertir los datos JSON de la respuesta en un diccionario de Python
        data = response.json()

        print("Registro agregado con éxito. Datos del nuevo registro:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"Error al agregar el registro. Código de estado: {response.status_code}")


# Llamar a la función para agregar el nuevo registro
agregar_registro(nuevo_registro)
