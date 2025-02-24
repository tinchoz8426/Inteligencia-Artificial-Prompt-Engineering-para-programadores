
import datetime
import openai


def generar_contenido_blog(tema):
    """
    Genera 5 ideas de blogs sobre el tema indicado, 
    incluyendo un resumen de 3 líneas para cada idea.
    """
    prompt = f"Genera 5 ideas de blogs sobre: {tema}. Incluye un resumen de 3 líneas para cada una."
    
    try:
        client = openai.OpenAI(api_key="API_KEY_OPENAI")
        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # Puedes ajustar la creatividad de la respuesta
            max_tokens=500    # Ajusta el límite de tokens según lo necesites
        )
        contenido_generado = respuesta.choices[0].message.content.strip()
        return contenido_generado
    except Exception as e:
        print("Error al generar contenido:", e)
        return None

def guardar_en_archivo(contenido):
    """
    Guarda el contenido en un archivo .txt cuyo nombre incluye la fecha y hora actual para asegurar
    que cada respuesta se almacene en un archivo diferente.
    """
    # Genera un nombre de archivo único usando la fecha y hora actual
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"blog_ideas_{timestamp}.txt"
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
        print(f"\nContenido guardado en el archivo: {nombre_archivo}")
    except Exception as e:
        print("Error al guardar el archivo:", e)

def main():
    tema = input("Introduce el tema para el blog: ")
    contenido = generar_contenido_blog(tema)
    
    if contenido:
        print("\nContenido generado:\n")
        print(contenido)
        guardar_en_archivo(contenido)
    else:
        print("No se pudo generar el contenido.")

if __name__ == "__main__":
    main()


# EXPLICACIÓN
# Requisitos previos:
# * Tener una cuenta en OpenAI.
# * Instalar la librería openai (puedes hacerlo con pip install openai).
# * Obtener y configurar tu API key de OpenAI.

# Importación del módulo datetime:
# * Se utiliza para generar un timestamp que ayudará a crear un nombre único para cada archivo.

# Función generar_contenido_blog:
# * Se define un prompt que incluye la instrucción de generar 5 ideas de blogs con un resumen de 3 líneas para cada una, basado en el tema proporcionado.
# * Se utiliza la función client.chat.completions.create para obtener la respuesta del modelo gpt-4o-mini.
# * Se devuelve el contenido generado.

# Función main:
# * Solicita al usuario que ingrese un tema.
# * Llama a generar_contenido_blog y muestra el resultado.

# Función guardar_en_archivo:
# * Se genera un nombre de archivo basado en la fecha y hora actual (blog_ideas_YYYYMMDD_HHMMSS.txt).
# * Se abre el archivo en modo escritura con codificación UTF-8 y se guarda el contenido generado.
# * Se notifica al usuario que el contenido se ha guardado correctamente.

# Llamada a guardar_en_archivo:
# * Después de generar el contenido, se llama a esta función para guardar la respuesta en un archivo .txt diferente cada vez.