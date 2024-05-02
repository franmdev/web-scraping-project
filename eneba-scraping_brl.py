import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.eneba.com/es/apple-apple-itunes-gift-card-20-brl-itunes-key-brazil"

# Request
response = requests.get(url)
data = response.text

# uso de bs
soup = BeautifulSoup(data, 'html.parser')

# Buscamos en el codigo HTML los elementos que pertenecen a la clase "vo4RsO"
# clase que contiene los valores de nuestro interes
items = soup.find_all('li', class_='vo4RsO')

# Inicializamos listas vacias para almacenar valores
saldo = []
usd = []
ratio = []

# Extraccion de datos
for item in items:
    # Encontrar los elementos necesarios
    span_saldo = item.find('span', class_='MKITZF')
    span_usd = item.find('span', class_='L5ErLT w7tD3i')
    span_ratio = item.find('span', class_='ANNnf5')

    # Verificar que ninguno de los elementos es nulo antes de añadirlos a las listas
    if span_saldo and span_usd and span_ratio:
        saldo.append(span_saldo.text.strip())
        usd.append(span_usd.text.strip())
        ratio.append(span_ratio.text.strip())

# Creacion de dataframe com los valores de interes
df = pd.DataFrame({
    'Saldo': saldo,
    'USD': usd,
    'Ratio USD': ratio
})


# Columna auxiliar que permite ordenar los registros
df['Ratio_Num'] = df['Ratio USD'].str.extract('(\d+\.\d+)').astype(float)

# dataframe con valores ordenados de forma descendente
df_sorted = df.sort_values(by='Ratio_Num', ascending=False)

df_sorted


