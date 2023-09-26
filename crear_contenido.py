import openai
import os

api_key = os.getenv("API_KEY")
print('api key',api_key)
openai.api_key = api_key

def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por facor escribe un articulo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        temperature=temperatura,
        n=1,
        max_tokens=tokens
    )

    return respuesta.choices[0].text.strip()

def resumir_texto(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt= f"Por favor resume el siguiente texto: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=temperatura,
        max_tokens=tokens
    )

    return respuesta.choices[0].text.strip()

tema = input("elije un tema para tu articulo: ")
tokens = int(input("cuantos tokens maximos tendra tu articulo:"))
temperatura = int(input("Del 1 al 10, que tan creativo quieres que sea tu articulo")) / 10
articulo_creado = crear_contenido(tema, tokens, temperatura)
print(articulo_creado)


