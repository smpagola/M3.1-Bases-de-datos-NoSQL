import requests
import pandas as pd

# URL de la API
url = "https://66b4e4f09f9169621ea4c19d.mockapi.io/api/v1/contactos"

# Realizar la solicitud GET para obtener los datos
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir los datos JSON de la respuesta en un diccionario de Python
    data = response.json()

    # Mostrar los datos en formato JSON formateado
    print("Datos en formato JSON formateado:")
    print(pd.json_normalize(data).to_json(orient="records", indent=4))

    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(data)

    # Mostrar los datos en formato DataFrame
    print("\nDatos en formato DataFrame:")
    print(df)

    # Exportar los datos a un archivo CSV
    df.to_csv('contactos.csv', index=False)
    print("\nDatos exportados a 'contactos.csv'")
else:
    print(f"Error al obtener los datos. Código de estado: {response.status_code}")
