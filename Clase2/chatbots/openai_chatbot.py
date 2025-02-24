from openai import OpenAI

client = OpenAI(api_key="API_KEY_OPENAI")

prompt = ""

while True:
    prompt = input("Tu: ")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content": prompt
            }
        ],
        model="gpt-4o-mini",
        
    )
    
    # si el usuario ingresa 'exit' se sale del bucle
    if prompt == "exit":
        print("Gracias por utilizar a nuestro Bot Pedrito 🤖")
        break
    
    # imprimimos la respuesta
    response_message = chat_completion.choices[0].message.content
    print("Pedrito el Bot 🤖: ", response_message)
