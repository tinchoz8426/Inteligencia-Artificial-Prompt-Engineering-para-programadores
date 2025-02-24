import openai
import json
import os

def generar_tareas(prompt_usuario):
    # Prompt del sistema para guiar a la IA
    sistema_prompt = """
    Genera una lista de tareas pendientes en formato JSON válido basado en la descripción del usuario.
    El JSON debe tener la siguiente estructura:
    {
        "tareas": [
            {
                "id": número único consecutivo,
                "titulo": string,
                "descripcion": string,
                "fecha_limite": string en formato YYYY-MM-DD,
                "prioridad": "alta", "media" o "baja"
            }
        ]
    }
    Asegúrate de que el JSON sea válido y no incluyas ningún texto adicional o markdown.
    """
    
    try:
        # Llamada a la API
        client = openai.OpenAI(api_key="API_KEY_OPENAI")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": sistema_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.7
        )
        
        # Extraer y limpiar la respuesta
        contenido = response.choices[0].message.content
        contenido = contenido.strip("` \n")  # Remover posibles markdown
        
        # Convertir a JSON y validar
        tareas_json = json.loads(contenido)
        return tareas_json
        
    except json.JSONDecodeError as e:
        print(f"Error decodificando JSON: {str(e)}")
        return None
    except KeyError as e:
        print(f"Error en la estructura del JSON: Falta clave {str(e)}")
        return None
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return None

def main():
    print("Generador de Lista de Tareas Pendientes")
    user_input = input("Describe tus tareas (ej. 'Necesito estudiar para el examen de matemáticas, comprar víveres y llamar a mi abuela mañana'):\n")
    
    resultado = generar_tareas(user_input)
    
    if resultado:
        nombre_archivo = "tareas.json"
        
        # Cargar contenido existente si el archivo existe
        try:
            with open(nombre_archivo, "r") as f:
                existente = json.load(f)
                # Fusionar las nuevas tareas manteniendo los IDs consecutivos
                ultimo_id = max(tarea["id"] for tarea in existente["tareas"]) if existente["tareas"] else 0
                for tarea in resultado["tareas"]:
                    ultimo_id += 1
                    tarea["id"] = ultimo_id
                existente["tareas"].extend(resultado["tareas"])
        except FileNotFoundError:
            existente = resultado
        
        # Escribir todo el contenido actualizado
        with open(nombre_archivo, "w") as f:
            json.dump(existente, f, indent=4)
            
        print(f"\nLista de tareas generada exitosamente! Guardada en {nombre_archivo}")
    else:
        print("No se pudo generar la lista de tareas")

if __name__ == "__main__":
    main()