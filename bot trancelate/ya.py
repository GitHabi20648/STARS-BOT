import requests
import config


memory = [
    {
        'role':'system',
        'text': '''
    ты - робот переводчик, если тебе пишет на русском языке - спроси на какой язык человек хочет перевести фразу, после этого переведи начальную фразу на ответ пользователя
''' # ты Дженни, ты интерисуешься openai и компьютерными технологиями
    }
]

def gpt(text):

    memory.append(
        {
            "role": "user",
            "text": text
        }
    )

    prompt = {
        "modelUri": f"gpt://{config.id_ya}/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": memory
    }
    
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {config.key_ya}"
    }
    
    response = requests.post(url, headers=headers, json=prompt)
    result = response.json().get('result')
    memory.append(
        {
            'role':'assistant',
            'text': result['alternatives'][0]['message']['text']
        }
    )
    return result['alternatives'][0]['message']['text']
