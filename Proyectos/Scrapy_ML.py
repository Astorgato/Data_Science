import re
import requests
from bs4 import BeautifulSoup
import pandas as pd


def limpiar_vendedor(vendedor): #Función buscada por GPT y adaptada al código
    # Utilizar una expresión regular para extraer la palabra entre "Por" y "["
    match = re.search(r'Por\s([a-zA-Z\s]+)', vendedor)
    if match:
        return match.group(1).strip()  # Devolver solo el nombre
    return ""  # Si está vacío o no coincide, devolver cadena vacía

url = 'https://listado.mercadolibre.cl/nintendo-switch#D[A:nintendo%20switch]'
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.content, 'html.parser')   
    #Plays = soup.find_all('span','andes-money-amount__fraction')
    Articulos = soup.find_all('li',class_ = 'ui-search-layout__item shops__layout-item')
    Nombre = []
    Precio = []
    Vendedores = []
    for Articulo in Articulos:
        Nombre.append(Articulo.find('h2',class_ = 'poly-box poly-component__title').text)
        Precio.append(Articulo.find('span',class_ = 'andes-money-amount__fraction').text)
        Vendedores.append(str(Articulo.find('span',class_ = 'poly-component__seller')))
else:
    print(f'hubo un error al hacer la petición, error: {respuesta.status_code}')


vendedores_limpios = [limpiar_vendedor(vendedor) for vendedor in Vendedores]

df = pd.DataFrame({'Nombre':Nombre, 'Precio':Precio, 'Vendedor':vendedores_limpios})

print(df)