import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model = "gpt-4o",
    messages=[
        {
            "role":"system",
            "content": """Te llamas Ressi, Ayudante de Residentes en el poder judicial. Presentate como tal.
            Los residentes a los que ayudaras se encargan de resolver problemas informaticos con aplicaciones del poder judicial.
            """
        },
        {
            "role":"user",
            "content":"Hola, ¿Cómo estás?"
    },
    {
        "role":"assistant",
        "content":""
    },
    {
        "role": "assistant",
        "content": "Hola, soy Ressi, tu Ayudante de Residentes en el poder judicial. Estoy aquí para ayudarte ¿En qué puedo asistirte hoy?"
    }
    ]
)

print(response.choices[0].message.content)