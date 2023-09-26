import openai
import os

api_key = os.getenv("API_KEY")
print('api key',api_key)
openai.api_key = api_key

def clasiticar_texto(texto):
    categorias = [
        "arte",
        "ciencia",
        "deportes",
        "economia",
        "educacion",
        "entretenimiento",
        "medio ambiente",
        "politica",
        "salud",
        "tecnologia",
    ]
    prompt = f"Por favor clasifica el siguiente texto '{texto}' en una de estas categorias: {','.join(categorias)}. la categoria es: "
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=50,
        tempetarute=0.5
    )
    return respuesta.choices[0].text.strip()

texto_para_clasificar = input("Ingrese un texto: ")
clasificacion = clasiticar_texto(texto_para_clasificar)
print(clasificacion)



