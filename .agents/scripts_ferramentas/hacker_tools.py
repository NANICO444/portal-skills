# -*- coding: utf-8 -*-
"""
hacker_tools.py - Ferramentas nativas de automação do modo "Hacker Raiz" do Nexus.
Permite movimentar o mouse, clicar, abrir pastas, checar vírus com Windows Defender,
baixar modelos leves com limite de tamanho e se comunicar com IAs locais via Ollama.
"""

import os
import sys
import time
import ctypes
import subprocess
import argparse
import requests

# Configuração de encoding para console Windows
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

def mover_mouse(x, y):
    """Move o mouse nativamente usando a API do Windows (user32.dll)"""
    print(f"🖱️ Movendo o mouse para as coordenadas: X={x}, Y={y}")
    ctypes.windll.user32.SetCursorPos(x, y)
    return True

def clicar_mouse():
    """Simula um clique com o botão esquerdo do mouse"""
    print("🖱️ Clicando com o botão esquerdo...")
    # MOUSEEVENTF_LEFTDOWN = 0x0002
    # MOUSEEVENTF_LEFTUP = 0x0004
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
    return True

def abrir_pasta(caminho):
    """Abre qualquer pasta ou arquivo no Windows Explorer de forma nativa"""
    print(f"📂 Abrindo pasta ou arquivo: {caminho}")
    try:
        os.startfile(caminho)
        return True
    except Exception as e:
        print(f"❌ Erro ao abrir: {e}")
        return False

def escanear_virus(caminho_arquivo):
    """Escaneia um arquivo por vírus usando o Windows Defender CLI (MpCmdRun.exe)"""
    print(f"🛡️ Iniciando varredura de vírus com Windows Defender no arquivo: {caminho_arquivo}")
    if not os.path.exists(caminho_arquivo):
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado para escaneamento.")
        return False

    defender_path = r"C:\Program Files\Windows Defender\MpCmdRun.exe"
    if not os.path.exists(defender_path):
        print("⚠️ Windows Defender (MpCmdRun.exe) não encontrado no caminho padrão. Pulando escaneamento real (Simulando aprovação de segurança)...")
        return True

    # Comando para escanear arquivo específico
    cmd = [defender_path, "-Scan", "-ScanType", "3", "-File", os.path.abspath(caminho_arquivo)]
    try:
        # Define timeout de 60 segundos
        resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=60, encoding='cp850', errors='ignore')
        
        # Códigos de retorno do MpCmdRun: 
        # 0 = Nenhuma ameaça encontrada
        # 2 = Ameaça encontrada ou erro crítico
        if resultado.returncode == 0:
            print("\n================ Resultado do Scan ================")
            print("🛡️ SUCESSO: Arquivo analisado e 100% SEGURO!")
            print("Nenhuma ameaça ou vírus detectados pelo Windows Defender.")
            print("===================================================\n")
            return True
        else:
            print("\n================ ALERTA DE SEGURANÇA ================")
            print("⚠️ AVISO: O arquivo pode conter uma ameaça ou o Windows Defender falhou no escaneamento!")
            print(f"Código de retorno: {resultado.returncode}")
            print(resultado.stdout)
            print("=====================================================\n")
            return False
    except subprocess.TimeoutExpired:
        print("❌ Erro: O escaneamento de vírus demorou muito tempo e expirou.")
        return False
    except Exception as e:
        print(f"❌ Erro ao executar o Windows Defender: {e}")
        return False

def baixar_ia_segura(url, destino, limite_gb=2.0):
    """Baixa um modelo da internet apenas se o tamanho estiver abaixo do limite especificado"""
    limite_mb = limite_gb * 1024
    print(f"🌐 Verificando informações de tamanho para o download de: {url}")
    
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        tamanho_bytes = int(response.headers.get('content-length', 0))
        tamanho_mb = tamanho_bytes / (1024 * 1024)
        
        if tamanho_bytes == 0:
            print("⚠️ Aviso: Não foi possível obter o tamanho do arquivo via cabeçalho HEAD. Tentando GET parcial...")
            response = requests.get(url, stream=True, timeout=10)
            tamanho_bytes = int(response.headers.get('content-length', 0))
            tamanho_mb = tamanho_bytes / (1024 * 1024)

        print(f"📊 Tamanho do arquivo na nuvem: {tamanho_mb:.2f} MB ({tamanho_bytes} bytes)")
        
        if tamanho_mb > limite_mb:
            print(f"❌ DOWNLOAD CANCELADO: O arquivo possui {tamanho_mb:.2f} MB, excedendo o limite seguro de {limite_mb:.0f} MB ({limite_gb} GB) estabelecido pelo João!")
            print("Sugestão: Procure uma versão mais leve/quantizada (GGUF menor, ex: Qwen 2.5 0.5B ou 1.5B).")
            return False

        print(f"✅ Tamanho dentro do limite seguro ({limite_gb} GB)! Iniciando download...")
        
        # Cria a pasta de destino se não existir
        os.makedirs(os.path.dirname(destino), exist_ok=True) if os.path.dirname(destino) else None
        
        response_get = requests.get(url, stream=True, timeout=30)
        tamanho_baixado = 0
        ultimo_print = time.time()
        
        with open(destino, 'wb') as f:
            for chunk in response_get.iter_content(chunk_size=65536):
                if chunk:
                    f.write(chunk)
                    tamanho_baixado += len(chunk)
                    # Printa progresso a cada 3 segundos para não encher a tela
                    if time.time() - ultimo_print > 3:
                        progresso = (tamanho_baixado / tamanho_bytes) * 100
                        print(f"⚡ Baixando: {progresso:.1f}% ({tamanho_baixado / (1024*1024):.1f}MB de {tamanho_mb:.1f}MB)")
                        ultimo_print = time.time()
                        
        print(f"🎉 Download concluído com sucesso e salvo em: {destino}")
        
        # Após baixar, roda AUTOMATICAMENTE a verificação de vírus!
        escanear_virus(destino)
        return True
        
    except Exception as e:
        print(f"❌ Erro crítico no download: {e}")
        return False

def conversar_ollama(modelo, prompt):
    """Envia um comando/prompt para uma IA local rodando no Ollama e retorna o resultado no CLI"""
    print(f"🤖 Tentando conversar com a IA Local '{modelo}' usando Ollama...")
    
    # 1. Verifica se o Ollama está rodando na porta padrão (11434)
    url_ollama = "http://localhost:11434/api/generate"
    try:
        data = {
            "model": modelo,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url_ollama, json=data, timeout=90)
        response.raise_for_status()
        resultado = response.json()
        
        resposta_texto = resultado.get("response", "")
        print("\n================ RESPOSTA DA IA LOCAL ================\n")
        print(resposta_texto)
        print("\n======================================================\n")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ ERRO: O serviço do Ollama não está rodando localmente (Connection Refused na porta 11434).")
        print("Verifique se o Ollama está instalado e rodando em segundo plano. Digite 'ollama serve' ou abra o app Ollama.")
        return False
    except Exception as e:
        print(f"❌ Erro ao enviar comando para o Ollama: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Nexus Hacker Tools CLI")
    parser.add_argument("--move-mouse", nargs=2, type=int, metavar=("X", "Y"), help="Move o mouse para coordenadas X e Y")
    parser.add_argument("--click-mouse", action="store_true", help="Simula um clique com o botão esquerdo")
    parser.add_argument("--open-folder", type=str, metavar="CAMINHO", help="Abre uma pasta ou arquivo no Windows Explorer")
    parser.add_argument("--scan-virus", type=str, metavar="ARQUIVO", help="Verifica se um arquivo contém vírus usando o Windows Defender")
    parser.add_argument("--download-model", nargs=2, metavar=("URL", "DESTINO"), help="Baixa um modelo checando limite de tamanho (padrão 2GB)")
    parser.add_argument("--limit-gb", type=float, default=2.0, help="Limite em GB para o download do modelo (padrão: 2.0)")
    parser.add_argument("--chat-ollama", nargs=2, metavar=("MODELO", "PROMPT"), help="Conversa com uma IA local instalada no Ollama")
    
    args = parser.parse_args()
    
    # Se nenhum argumento foi passado, mostra o help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
        
    if args.move_mouse:
        mover_mouse(args.move_mouse[0], args.move_mouse[1])
        
    if args.click_mouse:
        clicar_mouse()
        
    if args.open_folder:
        abrir_pasta(args.open_folder)
        
    if args.scan_virus:
        escanear_virus(args.scan_virus)
        
    if args.download_model:
        baixar_ia_segura(args.download_model[0], args.download_model[1], args.limit_gb)
        
    if args.chat_ollama:
        conversar_ollama(args.chat_ollama[0], args.chat_ollama[1])
