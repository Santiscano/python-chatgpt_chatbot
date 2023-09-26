import openai
import os
import spacy
import numpy as np

api_key = os.getenv("API_KEY")
print('api key',api_key)
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []
modelo_spacy = spacy.load("es_core_news_md")
palabras_prohibidas = ["madrid", "palabra2"]

# funcion que cambia las palabras prohibidas
def filtrar_lista_negra(text, lista_negra):
    token = modelo_spacy(text)
    resultado = []

    for t in token:
        if t.text.lower() not in lista_negra:
            resultado.append(t.text)
        else:
            resultado.append("[xxx]")
    
    return "".join(resultado)

# calcular similitud coseno
def similitud_coseno(vec1, vec2):
    superposicion = np.doy(vec1, vec2)
    magnitud1 = np.linalg.norm(vec1)
    magnitud2 = np.linalg.norm(vec2)

    sim_cos = superposicion / (magnitud1 * magnitud2)
    return sim_cos


def es_relevante(respuesta, entrada, umbral=0.5):
    entrada_ventorizada = modelo_spacy(entrada).vector
    respuesta_vetorizada = modelo_spacy(respuesta).vector
    similitud = similitud_coseno(entrada_ventorizada, respuesta_vetorizada)
    return similitud >= umbral

# funcion que se llamara para el chatbot
def preguntar_chat_gpt(prompt, modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=1.5
    )
    respuesta_sin_controlar = respuesta.choices[0].text.strip()
    respuesta_controlada = filtrar_lista_negra(respuesta_sin_controlar, palabras_prohibidas)
    return respuesta_controlada


print("bienvenido a nuestro chatbot basico, escribe salir cuando quieras terminar")

while True:
    conversacion_historica = ""
    ingreso_usuario = input('\nTu:')
    if ingreso_usuario.lower == 'salir':
        break

    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica + f"El usuario pregunta: {pregunta}\n"
        conversacion_historica + f"ChatGPT responde: {respuesta}\n"

    prompt = f"El usuario pregunta: {ingreso_usuario}\n"
    conversacion_historica += prompt
    respuesta_gpt = preguntar_chat_gpt(conversacion_historica)
    
    relevante = es_relevante(respuesta_gpt, ingreso_usuario)
    if relevante:
        print(f"{respuesta_gpt}")
        preguntas_anteriores.append(ingreso_usuario)
        respuestas_anteriores.append(respuesta_gpt)
    else: 
        print('la respuestsa no es relevante')
    
    print(f"{respuesta_gpt}")

    preguntas_anteriores.append(ingreso_usuario)
    respuestas_anteriores.append(respuesta_gpt)


# mantener el contexto de la conversación

