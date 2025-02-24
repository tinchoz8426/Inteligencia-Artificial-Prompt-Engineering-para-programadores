import google.generativeai as genai

genai.configure(api_key="API_KEY_GEMINI")
model = genai.GenerativeModel("gemini-1.5-flash")

# Configuración inicial
historial = []
print("\n🤖 ¡Hola! Soy un chatbot básico. Escribe 'salir' para terminar la conversación\n")

# Bucle de conversación
while True:
    # Obtener entrada del usuario
    try:
        user_input = input("👤 Tú: ")
    except KeyboardInterrupt:
        print("\n\n Conversación interrumpida. Hasta luego!")
        break

    # Verificar si quiere salir
    if user_input.lower() in ["salir", "exit", "adiós"]:
        print("\n🤖 ¡Hasta luego! Fue un gusto conversar contigo 👋\n")
        break

    # Generar respuesta
    try:
        respuesta = model.generate_content(user_input)
        if respuesta.text:
            print(f"\n🤖 Bot: {respuesta.text}\n")
            historial.append({"role": "user", "parts": [user_input]})
            historial.append({"role": "model", "parts": [respuesta.text]})
        else:
            print("\n🤖 No entendí tu mensaje. ¿Podrías reformularlo?\n")
            
    except Exception as e:
        print(f"\n Error generando respuesta: {str(e)}\n")




