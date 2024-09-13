import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://dockerlabs.es/'
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.content, 'html.parser')
    
    maquinas = soup.find_all('div',onclick = True)
    
    nombre_maquina = []
    autor = []
    Dificultad = []
    Fecha_Creacion = []
    for maquina in maquinas:
        onclick_text = maquina['onclick']
        nombre_maquina.append(onclick_text.split("'")[1])
        autor.append(onclick_text.split("'")[7])
        Dificultad.append(onclick_text.split("'")[3])
        Fecha_Creacion.append(onclick_text.split("'")[11])
else:
    print(f'hubo un error al hacer la petición, el error fue: {respuesta.status_code}')
    
df = pd.DataFrame({'Autor':autor, 'Nombre_Maquina':nombre_maquina, 'Fecha_Creacion':Fecha_Creacion,'Dificultad':Dificultad})

print(df)