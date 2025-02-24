from groq import Groq


def generar_tareas(prompt_usuario, num_tareas=5):
    prompt = f"""
    Actúa como un asistente de productividad experto. Genera una lista de {num_tareas} tareas pendientes 
    basadas en la siguiente descripción. Las tareas deben ser específicas, accionables y estar en español.
    
    Descripción: {prompt_usuario}
    
    Formato requerido:
    1. [Tarea 1]
    2. [Tarea 2]
    ...
    """

    try:
        client = Groq(
            api_key="API_KEY_GROQ"
        )

        respuesta = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        tareas = respuesta.choices[0].message.content

        # tareas = respuesta.choices[0].message.content.strip()
        return tareas

    except Exception as e:
        return f"Error al generar tareas: {str(e)}"


def main():
    print("¡Generador de Lista de Tareas Pendientes!")
    descripcion = input(
        "\nDescribe lo que necesitas organizar (ej. 'organizar una boda', 'preparar examen final'): "
    )

    tareas = generar_tareas(descripcion)

    print("\n📝 Lista de tareas generada:")
    print(tareas)


if __name__ == "__main__":
    main()
