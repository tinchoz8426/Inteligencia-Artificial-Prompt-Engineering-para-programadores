# Realizad con ChatGPT

def emojify_text(text):
    """
    Reemplaza palabras clave en el texto con emojis correspondientes.
    """
    emoji_dict = {
        "feliz": "😄",
        "triste": "😢",
        "amor": "❤️",
        "gato": "🐱",
        "perro": "🐶",
        "pizza": "🍕",
        "sol": "☀️",
        "luna": "🌙"
    }
    
    words = text.split()
    emojified_words = [emoji_dict.get(word, word) for word in words]
    
    return " ".join(emojified_words)


# Ejemplo de uso
mensaje = "Estoy muy feliz porque mi perro come pizza bajo el sol"
print(emojify_text(mensaje))


# Aquí tienes una función inventada en Python llamada emojify_text() 
# que convierte ciertas palabras clave en emojis correspondientes para hacer el texto más divertido.
# Puedes modificar o expandir el diccionario para agregar más palabras clave y emojis.