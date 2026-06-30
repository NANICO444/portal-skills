# kimi_chat.py
import os
import requests
import json

# Defina sua chave aqui ou use a variável de ambiente OPENROUTER_API_KEY
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "SUA_CHAVE_AQUI")

def chat_com_kimi(mensagem):
    print("Enviando mensagem para o Kimi...")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "moonshotai/kimi-k2.6:free",
        "messages": [
            {"role": "system", "content": "Você é um assistente útil e amigável."},
            {"role": "user", "content": mensagem}
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status() # Lança um erro se o status não for 200 OK
        
        resultado = response.json()
        print("\n================ Resposta do Kimi ================\n")
        print(resultado["choices"][0]["message"]["content"])
        print("\n==================================================\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Falha ao comunicar com o Kimi: {e}")
        if response is not None:
            print("Detalhes do erro:", response.text)

if __name__ == "__main__":
    chat_com_kimi("Olá! Qual é o seu nome e que modelo de inteligência artificial você é?")
