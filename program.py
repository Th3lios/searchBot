import glob
import os
import json
from bs4 import BeautifulSoup
import requests

src_path = r"/Users/macbook/Desktop"


def ocr_space_file(filename, overlay=False, api_key='af599d01d888957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def search():

    # Variables
    str_api = []
    query_str = []
    flag = False
    cont_aux = 0

    # Contadores de palabras claves
    cont = 0
    cont2 = 0
    cont3 = 0

    # Devuelve una lista de path's del desktop
    list_of_files = glob.glob('/Users/macbook/Desktop/*')

    # Devuelve el path del último archivo del desktop
    latest_file = max(list_of_files, key=os.path.getctime)

    # Devuelve un string con el texto de la imagen
    dict_file = ocr_space_file(filename=latest_file, language='eng')

    # Devuelve un diccionario con el contenido de la imagen
    data = json.loads(dict_file)

    # Retorna el contenido exacto requerido como un array
    filter = (data['ParsedResults'][0]['ParsedText']).split(' ')

    # Loop utilizado para filtrar palabras clave
    for i in filter:

        # Si el flag sea False, almecenará cada string en query_str
        if not flag:
            query_str.append(i.replace('\r\n', ''))

        # Si se llega al signo de interrogación, se salta el loop
        if '?' in i:
            flag = True
            continue

        # Si ya se paso el signo de interrogación, empieza a guardar en str_api
        if flag:

            # Si encuentra que un elemento de la lista es igual a \r\n se sale del loop
            if i == '\r\n':
                break

            # Si encuentra un \r\n en algún elemento de la lista lo reemplaza y lo añade
            if '\r\n' in i:
                str_api.append(i.replace('\r\n', ' '))
            # En caso contrario contatena el elemento actual con el anterior
            else:
                str_api[cont_aux - 1] += " " + i
            cont += 1

    # Une q_string en una sola linea
    q_string = " ".join(query_str)

    # Pregunta
    query = q_string
    print(query)

    # Si el array string no llega a tener 4 valores, arroja una excepcion
    try:

        # Respuestas sin contar el primer caracter
        key = str_api[0][1:]
        key2 = str_api[1][1:]
        key3 = str_api[2][1:]
    except IndexError:
        print("No se cargaron las palabras clave")
        exit(1)

    search = query.replace(" ", "+")

    # Se carga el enlace con la pregunta y palabras claves
    google_search = "https://www.google.cl/search?q=" + search + " " + key + " " + key2 + " " + key3

    # Se realiza el request al enlace, retorna informacion de la pagina
    r = requests.get(google_search)

    # Devuelve el texto de la pagina con tag's
    soup = BeautifulSoup(r.text, "html.parser")

    # Se buscan todos los contenidos de la pagina que estan entre <span "class"="st"><span>
    url = soup.findAll('span', {"class": "st"})

    # Se analiza linea por linea el string url
    for i in url:

        # Entrega una linea obviando los tag's intermedios
        value = i.get_text()

        # Se contabilizan concurrencias de palabras claves en una linea
        if key in value:
            cont += 1
        if key2 in value:
            cont2 += 1
        if key3 in value:
            cont3 += 1

    # Suma total de ocurrencias
    contf = cont + cont2 + cont3

    # Evitar problema de division por 0
    if contf == 0:
        contf = 1

    # Muestra los resultados en porcentajes
    print(str(cont / contf * 100) + "% - " + key)
    print(str(cont2 / contf * 100) + "% - " + key2)
    print(str(cont3 / contf * 100) + "% - " + key3)


print('--- Start recognize text from image ---')
search()
print("------ Done -------")
