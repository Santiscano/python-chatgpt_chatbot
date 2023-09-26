import openai
import os

api_key = os.getenv("API_KEY")
print('api key',api_key)
openai.api_key = api_key


def traducir_texto(texto, idioma):
    prompt=f"traduce el texto '{texto}' al {idioma}"
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=texto.length() + 30,
        tempetarute=0.5
    )
    return respuesta.choices[0].text.strip()

mi_texto = input("Escribe el texto que quieres traducir: ")
mi_idioma = input("A que idioma quieres traducirlo? ")
traduccion = traducir_texto(mi_texto, mi_idioma)
print(traduccion)


