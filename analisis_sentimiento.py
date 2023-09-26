import openai
import os

api_key = os.getenv("API_KEY")
print('api key',api_key)
openai.api_key = api_key

def analizar_sentimiento(texto):
    prompt = f"Por favor, analiza el sentimiento predominante en el siguiente texto: '{texto}'"
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=100,
        temperature=0.5
    )
    return respuesta.choices[0].text.strip()

texto_para_analizar = input("Ingresa un texto: ")
sentimiento = analizar_sentimiento(texto_para_analizar)
print(sentimiento)