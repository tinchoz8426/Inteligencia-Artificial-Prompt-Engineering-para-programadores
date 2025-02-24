import openai
import json
import os
from datetime import datetime

def resumir_texto(texto, modelo="gpt-4o-mini", temperatura=0.5):
    """
    Genera un resumen del texto dado utilizando la API de OpenAI.
    """
    try:
        client = openai.OpenAI(api_key="API_KEY_OPENAI")  
        respuesta = client.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "system", "content": "Eres un asistente que resume textos de manera concisa."},
                {"role": "user", "content": f"Resume el siguiente texto: {texto}"}
            ],
            temperature=temperatura,
        )
        return respuesta.choices[0].message.content
    except Exception as e:
        return f"Error al generar el resumen: {e}"

def cargar_texto_desde_archivo(nombre_archivo):
    """
    Carga el contenido de un archivo de texto.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except Exception as e:
        return f"Error al leer el archivo: {e}"

def guardar_resumen_en_archivo(resumen):
    """
    Guarda el resumen en un archivo único basado en la fecha y hora.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"resumen_{timestamp}.txt"
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(resumen)
        print(f"Resumen guardado en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el resumen: {e}")

def guardar_resumen_en_json(resumen, nombre_archivo="resumenes.json"):
    """
    Guarda el resumen generado en un archivo JSON acumulativo.
    """
    datos = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
            except json.JSONDecodeError:
                datos = []
    
    datos.append({"resumen": resumen})
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print(f"Resumen guardado en {nombre_archivo}")

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    texto_largo = cargar_texto_desde_archivo(nombre_archivo)
    
    if "Error" not in texto_largo:
        resumen = resumir_texto(texto_largo)
        print("Resumen generado:")
        print(resumen)
        guardar_resumen_en_archivo(resumen)
        guardar_resumen_en_json(resumen)
    else:
        print(texto_largo)
