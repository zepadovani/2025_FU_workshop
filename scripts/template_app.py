#!/usr/bin/env python3
"""
Template App - Machine Listening Workshop
Aplicação híbrida para rodar localmente (Pixi) ou no Google Colab
"""

import os
import sys
import subprocess
from pathlib import Path


def setup_environment():
    """
    Detecta o ambiente e configura dependências automaticamente.
    - Google Colab: Baixa requirements.txt e instala via pip
    - Local: Usa o ambiente atual (gerenciado pelo Pixi)
    """
    try:
        # Detecta se está rodando no Google Colab
        import google.colab
        IN_COLAB = True
        print("🌐 Ambiente detectado: Google Colab")
    except ImportError:
        IN_COLAB = False
        print("💻 Ambiente detectado: Local")
    
    if IN_COLAB:
        print("\n📦 Instalando dependências no Colab...")
        
        # URL do repositório (ajuste para o seu repo)
        # Assumindo que o requirements.txt está na raiz
        REPO_URL = "https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPO/main"
        REQUIREMENTS_URL = f"{REPO_URL}/requirements.txt"
        
        try:
            # Baixa o requirements.txt
            subprocess.run(
                ["wget", "-q", REQUIREMENTS_URL, "-O", "requirements.txt"],
                check=True
            )
            print("✓ requirements.txt baixado com sucesso")
            
            # Instala as dependências
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"],
                check=True
            )
            print("✓ Dependências instaladas com sucesso")
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Erro ao instalar dependências: {e}")
            print("Tentando instalação manual das principais bibliotecas...")
            
            # Fallback: instala manualmente as bibliotecas essenciais
            packages = ["librosa", "soundfile", "gradio", "numpy", "pandas", "matplotlib"]
            for pkg in packages:
                try:
                    subprocess.run(
                        [sys.executable, "-m", "pip", "install", "-q", pkg],
                        check=True
                    )
                    print(f"✓ {pkg} instalado")
                except:
                    print(f"✗ Falha ao instalar {pkg}")
    else:
        print("✓ Usando ambiente local (gerenciado pelo Pixi)")
        print("  Execute 'pixi install' se ainda não instalou as dependências\n")
    
    return IN_COLAB


def process_audio(audio_file):
    """
    Processa um arquivo de áudio usando Librosa.
    
    Args:
        audio_file: Caminho do arquivo de áudio ou tupla (sample_rate, numpy_array)
    
    Returns:
        tuple: (mensagem de resultado, imagem do espectrograma)
    """
    import librosa
    import librosa.display
    import numpy as np
    import matplotlib.pyplot as plt
    
    try:
        # Caso o input seja uma tupla (Gradio Audio format)
        if isinstance(audio_file, tuple):
            sample_rate, audio_data = audio_file
            # Converte para mono se for estéreo
            if len(audio_data.shape) > 1:
                audio_data = np.mean(audio_data, axis=1)
            # Normaliza para float32
            audio_data = audio_data.astype(np.float32)
            if audio_data.max() > 1.0:
                audio_data = audio_data / np.iinfo(np.int16).max
            y = audio_data
            sr = sample_rate
        else:
            # Carrega o arquivo de áudio
            y, sr = librosa.load(audio_file, sr=None)
        
        # Análise do áudio
        duration = librosa.get_duration(y=y, sr=sr)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        
        # Gera espectrograma
        D = librosa.stft(y)
        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
        
        # Cria a visualização
        fig, ax = plt.subplots(figsize=(10, 4))
        img = librosa.display.specshow(
            S_db, 
            x_axis='time', 
            y_axis='hz', 
            sr=sr, 
            ax=ax,
            cmap='viridis'
        )
        ax.set_title('Espectrograma')
        fig.colorbar(img, ax=ax, format='%+2.0f dB')
        plt.tight_layout()
        
        # Resultado textual
        result = f"""
        ✅ **Análise Completa!**
        
        📊 **Informações do Áudio:**
        - Duração: {duration:.2f} segundos
        - Taxa de Amostragem: {sr} Hz
        - Tempo Estimado: {tempo:.2f} BPM
        - Forma do Array: {y.shape}
        """
        
        return result, fig
        
    except Exception as e:
        error_msg = f"❌ **Erro ao processar áudio:** {str(e)}"
        return error_msg, None


def create_interface(share=False):
    """
    Cria e lança a interface Gradio.
    
    Args:
        share (bool): Se True, cria link público (útil para Colab)
    """
    import gradio as gr
    
    # Define a interface usando gr.Blocks para maior controle
    with gr.Blocks(title="Machine Listening Workshop") as demo:
        gr.Markdown("""
        # 🎵 Machine Listening Workshop
        ### Processamento de Áudio com IA
        
        Faça upload de um arquivo de áudio ou grave usando o microfone para análise automática.
        """)
        
        with gr.Row():
            with gr.Column():
                audio_input = gr.Audio(
                    label="📁 Upload de Áudio ou 🎤 Gravação",
                    type="filepath",
                    sources=["upload", "microphone"]
                )
                process_btn = gr.Button("🔍 Analisar Áudio", variant="primary")
            
            with gr.Column():
                text_output = gr.Markdown(label="Resultados")
        
        plot_output = gr.Plot(label="Espectrograma")
        
        # Conecta o botão à função de processamento
        process_btn.click(
            fn=process_audio,
            inputs=audio_input,
            outputs=[text_output, plot_output]
        )
        
        gr.Markdown("""
        ---
        ### 📖 Como usar:
        1. Faça upload de um arquivo de áudio (.wav, .mp3, etc.) ou grave usando o microfone
        2. Clique em "Analisar Áudio"
        3. Veja os resultados da análise e o espectrograma
        
        ### 🔧 Tecnologias:
        - **Librosa**: Análise de áudio
        - **Gradio**: Interface web
        - **Matplotlib**: Visualização
        """)
    
    # Lança a aplicação
    demo.launch(share=share, server_name="0.0.0.0")


def main():
    """Função principal"""
    print("=" * 60)
    print("🎵 Machine Listening Workshop - Template App")
    print("=" * 60)
    
    # Configura o ambiente
    in_colab = setup_environment()
    
    print("\n🚀 Iniciando interface Gradio...\n")
    
    # Cria e lança a interface
    # share=True no Colab para gerar link público
    create_interface(share=in_colab)


if __name__ == "__main__":
    main()
