import os
import argparse
import requests
import json
import sys
import time

def delegar_para_ia(prompt, file_path=None, output_path=None, modelo_primario=None):
    api_key = os.environ.get("OPENROUTER_API_KEY", "SUA_CHAVE_AQUI")
    
    conteudo_arquivo = ""
    if file_path:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                conteudo_arquivo = f.read()
            prompt = f"{prompt}\n\nConteúdo do arquivo base ({file_path}):\n```\n{conteudo_arquivo}\n```"
        else:
            print(f"Aviso: Arquivo de contexto '{file_path}' não encontrado.")
            sys.exit(1)
            
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "messages": [
            {
                "role": "system", 
                "content": "Você é um assistente especialista operando via orquestrador. Siga as instruções do usuário. Se pedirem código, forneça código limpo."
            },
            {"role": "user", "content": prompt}
        ]
    }
    
    # Rotação Dinâmica com Modelos Injetados pelo João (O Arquiteto)
    modelos_fallback = []
    if modelo_primario:
        modelos_fallback.append(modelo_primario)
        
    modelos_fallback.extend([
        "moonshotai/kimi-k2.6:free",
        "qwen/qwen-2.5-coder-32b-instruct:free",
        "deepseek/deepseek-chat:free",
        "google/gemini-2.0-flash-exp:free",
        "meta-llama/llama-3.3-70b-instruct:free",
        "microsoft/phi-3-medium-128k-instruct:free"
    ])
    
    # Remove duplicatas mantendo a ordem
    modelos_fallback = list(dict.fromkeys(modelos_fallback))
    
    tempos_espera = [5, 12, 30]
    
    for modelo in modelos_fallback:
        data["model"] = modelo
        print(f"Tentando rota de modelo: {modelo}...")
        
        for tentativa, tempo in enumerate(tempos_espera + [0]):
            try:
                response = requests.post(url, headers=headers, data=json.dumps(data))
                
                if response.status_code == 429:
                    if tentativa < 3:
                        print(f"Erro 429. Aguardando {tempos_espera[tentativa]}s...")
                        time.sleep(tempos_espera[tentativa])
                        continue
                    else:
                        print(f"Modelo {modelo} rate-limited 3x seguidas.")
                        break
                        
                response.raise_for_status()
                resultado = response.json()
                resposta_ai = resultado["choices"][0]["message"]["content"]
                
                if output_path:
                    with open(output_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(resposta_ai)
                    print(f"Sucesso: Salvo em '{output_path}'.")
                else:
                    print(resposta_ai)
                return 
                
            except requests.exceptions.RequestException as e:
                print(f"Erro na requisição ({modelo}): {e}")
                if 'response' in locals() and hasattr(response, 'text'):
                    print(response.text)
                break 

    print("\nFALHA CRÍTICA: Todos os modelos do pool falharam.")
    sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=str, help="A instrução")
    parser.add_argument("--file", "-f", type=str, default=None)
    parser.add_argument("--out", "-o", type=str, default=None)
    parser.add_argument("--model", "-m", type=str, help="Modelo primário", default=None)
    
    args = parser.parse_args()
    delegar_para_ia(args.prompt, args.file, args.out, args.model)
