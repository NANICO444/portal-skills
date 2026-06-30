# -*- coding: utf-8 -*-
"""
instalar_ollama.py - Automação de download e instalação silenciosa do Ollama no Windows
e download do modelo ultra-leve Qwen 2.5 0.5B.
"""

import os
import sys
import time
import requests
import subprocess

# Configuração de encoding para console Windows
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

def baixar_arquivo(url, destino):
    print(f"📥 Baixando instalador do Ollama de: {url}")
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        tamanho_total = int(response.headers.get('content-length', 0))
        tamanho_mb = tamanho_total / (1024 * 1024)
        print(f"📊 Tamanho do instalador: {tamanho_mb:.2f} MB")
        
        tamanho_baixado = 0
        ultimo_print = time.time()
        
        with open(destino, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):  # 1MB chunks
                if chunk:
                    f.write(chunk)
                    tamanho_baixado += len(chunk)
                    if time.time() - ultimo_print > 2:
                        progresso = (tamanho_baixado / tamanho_total) * 100
                        print(f"⚡ Download: {progresso:.1f}% ({tamanho_baixado / (1024*1024):.1f}MB de {tamanho_mb:.1f}MB)")
                        ultimo_print = time.time()
                        
        print("🎉 Download concluído!")
        return True
    except Exception as e:
        print(f"❌ Erro ao baixar o instalador: {e}")
        return False

def instalar_silencioso(installer_path):
    print("⚙️ Iniciando instalação silenciosa do Ollama (aguarde alguns segundos)...")
    try:
        # O instalador do Ollama suporta /silent para instalação silenciosa
        process = subprocess.Popen([installer_path, '/silent'], shell=True)
        print("⏳ Aguardando conclusão da instalação (instalando em segundo plano)...")
        
        # Vamos verificar se o executável do Ollama aparece no diretório padrão do Windows
        ollama_path = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Ollama\ollama.exe")
        
        tentativas = 30
        for i in range(tentativas):
            time.sleep(2)
            if os.path.exists(ollama_path):
                print(f"✅ Executável detectado em: {ollama_path}")
                print("🎉 Ollama instalado com SUCESSO no sistema!")
                return True
            print(f"⌛ Verificando instalação... tentativa {i+1}/{tentativas}")
            
        print("⚠️ Aviso: O tempo limite expirou, mas a instalação pode estar concluindo. Vamos verificar novamente.")
        return os.path.exists(ollama_path)
    except Exception as e:
        print(f"❌ Erro durante a instalação: {e}")
        return False

def iniciar_e_pull():
    ollama_path = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Ollama\ollama.exe")
    if not os.path.exists(ollama_path):
        print("❌ Erro: Não foi possível localizar o executável do Ollama.")
        return False
        
    print("🔌 Iniciando o serviço do Ollama...")
    try:
        # Inicia o servidor em segundo plano
        subprocess.Popen([ollama_path, "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)  # Aguarda 5 segundos para o servidor ligar
        
        print("🤖 Baixando o modelo ultra-leve Qwen 2.5 0.5B (apenas 397MB!)...")
        print("Isso pode levar de 1 a 3 minutos dependendo da sua internet.")
        
        # Executa o comando de pull
        process = subprocess.run([ollama_path, "pull", "qwen2.5:0.5b"], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        
        if process.returncode == 0:
            print("\n================ INSTALAÇÃO CONCLUÍDA ================")
            print("🚀 A segunda IA local (Qwen 2.5) foi instalada com sucesso!")
            print("Você agora pode conversar com ela via CLI usando:")
            print("python scripts_ferramentas\\hacker_tools.py --chat-ollama qwen2.5:0.5b \"Sua mensagem\"")
            print("======================================================\n")
            return True
        else:
            print(f"⚠️ Erro ao puxar o modelo: {process.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao iniciar ou puxar modelo: {e}")
        return False

def main():
    installer_url = "https://ollama.com/download/OllamaSetup.exe"
    temp_dir = os.path.join(os.getcwd(), "temp")
    os.makedirs(temp_dir, exist_ok=True)
    installer_dest = os.path.join(temp_dir, "OllamaSetup.exe")
    
    # Passo 1: Baixar
    if baixar_arquivo(installer_url, installer_dest):
        # Passo 2: Instalar
        if instalar_silencioso(installer_dest):
            # Passo 3: Iniciar e baixar modelo
            iniciar_e_pull()
            
        # Limpeza
        try:
            os.remove(installer_dest)
            os.rmdir(temp_dir)
            print("🧹 Arquivos temporários de instalação limpos.")
        except Exception:
            pass

if __name__ == "__main__":
    main()
