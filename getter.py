import sys
import re
import os
import requests
import zipfile
import shutil
import pandas as pd

# Expresión regular para validar una URL
URL_REGEX = re.compile(
    r'^(https?://)'                 # http:// o https:// (obligatorio)
    r'(www\.)?'                     # www. (opcional)
    r'([\w.-]*indec[\w.-]*)'        # Dominio que contenga "indec"
    r'(\.[a-z]{2,})'                # Dominio de nivel superior (.com, .ar, etc.)
    r'(/[\w./-]*)*',                 # Rutas y subrutas (opcional)
    re.IGNORECASE
)

def descargar_y_procesar(url):
    # Obtener el nombre del archivo
    zip_filename = url.split("/eph/")[1]
    zip_filename = f'./tmp/{zip_filename}'
    trimestre = zip_filename.split('_')[2]
    anio = zip_filename.split('_')[4]
    # Crear carpeta ./tmp si no existe
    os.makedirs("./tmp", exist_ok=True)

    # Descargar el archivo ZIP
    response = requests.get(url)
    if response.status_code == 200:
        with open(zip_filename, "wb") as file:
            file.write(response.content)
        print(f"Archivo descargado: {zip_filename}")
    else:
        print(f"Error al descargar el archivo: {response.status_code}")
        return

    # Extraer el ZIP
    with zipfile.ZipFile(zip_filename, "r") as zip_ref:
        zip_ref.extractall('tmp')
    print(f"Archivos extraídos en la carpeta 'tmp'")

    # Selecciona la primera carpeta 
    folders = [folder for folder in os.listdir("tmp") if os.path.isdir(os.path.join('tmp', folder))]
    folder = os.path.join('tmp', folders[0])
    archivos_txt = [file for file in os.listdir(folder) if file.endswith(".txt")]
    for txt_file in archivos_txt:
        txt_path = os.path.join(folder, txt_file)
        if os.path.exists(txt_path):
            # Convertir TXT a DataFrame
            df = pd.read_csv(txt_path, sep=";", low_memory=False)

            # Crear nombre para el CSV
            base_name = "hogar" if "hogar" in txt_file else "individual"
            csv_output = f"base_{base_name}_{anio}T{trimestre}.csv"
            zip_output = csv_output.replace(".csv", ".zip")

            # Guardar CSV
            df.to_csv(f'./tmp/{csv_output}', index=False)
            print(f"Archivo CSV generado: {csv_output}")

            # Comprimir el CSV en un ZIP
            with zipfile.ZipFile(f'{base_name}/{zip_output}', "w", zipfile.ZIP_DEFLATED) as zip_out:
                zip_out.write(f'./tmp/{csv_output}', arcname=csv_output)
            print(f"Archivo ZIP generado: {zip_output}")

        else:
            print(f"Archivo {txt_file} no encontrado en el ZIP.")

    # Limpiar la carpeta temporal
    try:
        shutil.rmtree("./tmp")
    except:
        print("No se pudo eliminar carpeta tmp")


if len(sys.argv) > 1:
    URI = sys.argv[1]
    if URL_REGEX.match(URI):
        descargar_y_procesar(URI)
        print("Procesado con éxito")
    else:
        print(f"La URI proporcionada no es válida: {URI}")
else:
    print("No se proporcionó URI.")
