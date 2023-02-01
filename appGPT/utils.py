import openai
from TestGPT.config import *

def getCHAT(prompt,temperature):
    model = 'text-davinci-003'
    openai.api_key = API_KEY
    response = openai.Completion.create(
        prompt=prompt,
        max_tokens=3000,
        model=model,
        temperature=int(temperature) / 10,
    )
    return response.choices[0].text.replace('BOT:', '').replace('AARON:', '')