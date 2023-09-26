# https://platform.openai.com/   # login openai
import os
import openai
import spacy

api_key = os.getenv("API_KEY")
print('api key',api_key)
openai.api_key = api_key

# verificar conexion
# modelos = openai.Model.list()
# print(f"Modelos disponibles: {modelos}")

modelo = 'text-davinci-002'
# prompt = 'cual es la capital de francia?'
# prompt = 'inventa un poema de 10 palabras de python'
prompt = 'de que se trata la pelicula el padrino?'

respuesta = openai.Completion.create(
    engine= modelo, # obligatorio
    prompt= prompt, # obligatorio
    n = 1, # numero de respuestas por recibir
    temperature=0.1, # lo menos creativo = va de 0.1 a 1
    max_tokens= 100, # lo largo de la respuesta
    # cantidad de las respuestas
)

# 1 respuesta
textoGenerado = respuesta.choices[0].text.strip() # strip elimina espacios en blanco
print("respuesta",textoGenerado)

# varias respuesta
for idx, option in enumerate(respuesta.choices):
    texto_generado = option.text.strip()
    print(f"Respuesta {idx + 1}: {texto_generado}\n")


# spacy
modelo_spacy = spacy.load("es_core_news_md")
# se instala el modelo a usar
# python -m spacy download es_core_news_md

analisis = modelo_spacy(texto_generado)

for token in analisis:
    print(
        token.text, 
        token.pos, # categoria gramatical
        token.dep_, # relacion de dependencia
        token.head.text, # relacion 
    ) 

for ent in analisis.ents:
    print(
        ent.text, # persona
        ent.label_, # etiqueta que lo categoriza
    )

ubicacion = None

for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break

if ubicacion:
    prompt2 = f"Dime más acerca de {ubicacion}"
    respuesta2 = openai.Completion.create(
        engine=modelo,
        prompt=prompt2,
        n=1,
        max_tokens=100
    )
    print(respuesta2.choices[0].text.strip())


