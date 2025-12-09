# 🎵 Machine Listening Workshop

Workshop de **Machine Listening** (Processamento de Áudio e IA) com suporte híbrido para execução local (Pixi) e Google Colab.

## 📋 Sobre o Projeto

Este repositório contém materiais e código para um workshop hands-on de processamento de áudio usando bibliotecas modernas de Python e IA. O projeto é estruturado para máxima acessibilidade:

- 💻 **Execução Local**: Rápida e eficiente usando [Pixi](https://pixi.sh)
- 🌐 **Google Colab**: Acesso via navegador, sem instalação local
- 🎨 **Interface Gradio**: UIs web interativas para demonstrações

## 🚀 Como Rodar no Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SEU_USUARIO/SEU_REPO/blob/main/notebooks/workshop_demo.ipynb)

1. Clique no badge acima para abrir o notebook no Colab
2. Execute as células sequencialmente
3. O ambiente será configurado automaticamente!

> **Nota**: Substitua `SEU_USUARIO/SEU_REPO` pela URL real do seu repositório GitHub.

## 💻 Como Rodar Localmente

### Pré-requisitos

- [Pixi](https://pixi.sh) instalado no sistema
- Git para clonar o repositório

### Instalação

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPO.git
cd SEU_REPO

# Instale as dependências com Pixi
pixi install

# (Opcional) Gere o requirements.txt para compatibilidade com Colab
pixi run export-reqs
```

### Executando a Aplicação Template

```bash
# Execute o script principal
pixi run python scripts/template_app.py
```

A interface Gradio será aberta automaticamente no navegador em `http://localhost:7860`.

### Executando Notebooks Localmente

```bash
# Inicie o Jupyter Lab
pixi run jupyter lab

# Ou Jupyter Notebook
pixi run jupyter notebook
```

## 📦 Gerenciando Dependências

Para adicionar novas bibliotecas ao projeto:

1. **Adicione via Pixi** (Local):
   ```bash
   # Para pacotes Conda (preferencial - ex: scikit-learn)
   pixi add scikit-learn

   # Para pacotes PyPI (pip - ex: openai)
   pixi add --pypi openai
   ```

2. **Atualize o requirements.txt** (Para Colab):
   Sempre que adicionar um pacote, regenere o arquivo de requisitos para garantir que funcione no Colab:
   ```bash
   pixi run export-reqs
   ```

3. **Commit**: Envie as alterações do `pixi.toml`, `pixi.lock` e `requirements.txt` para o GitHub.

## 📁 Estrutura do Projeto

```
.
├── notebooks/           # Jupyter notebooks para o workshop
│   └── workshop_demo.ipynb
├── scripts/            # Scripts Python standalone
│   └── template_app.py # Aplicação template com Gradio
├── assets/             # Arquivos de áudio de exemplo
├── pixi.toml           # Configuração de dependências Pixi
├── requirements.txt    # Gerado automaticamente para Colab
├── .gitignore
└── README.md
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.10**: Linguagem base
- **Librosa**: Análise e processamento de áudio
- **Gradio**: Interfaces web interativas
- **NumPy/Pandas**: Manipulação de dados
- **Matplotlib**: Visualizações
- **Pixi**: Gerenciamento de ambiente e dependências

## 📚 Conteúdo do Workshop

### Módulos Principais

1. **Fundamentos de Áudio Digital**
   - Taxa de amostragem, formato de arquivos
   - Representação de sinais

2. **Análise Espectral**
   - STFT (Short-Time Fourier Transform)
   - Espectrogramas e mel-spectrogramas
   - MFCCs (Mel-Frequency Cepstral Coefficients)

3. **Detecção de Características**
   - Tempo (BPM)
   - Onset detection
   - Pitch tracking

4. **Interface com Gradio**
   - Criação de UIs para demos
   - Deploy e compartilhamento

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:

- Abrir issues para bugs ou sugestões
- Enviar pull requests com melhorias
- Compartilhar exemplos de uso

## 📄 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📧 Contato

Para dúvidas ou sugestões sobre o workshop, abra uma issue neste repositório.

---

**Happy Audio Processing! 🎧🎶**
