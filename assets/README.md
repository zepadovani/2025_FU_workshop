# Assets - Arquivos de Áudio

Esta pasta contém arquivos de áudio de exemplo para o workshop.

## 📁 Como adicionar seus próprios arquivos

1. Adicione arquivos de áudio (`.wav`, `.mp3`, etc.) nesta pasta
2. Certifique-se de que o `.gitignore` permite o commit dos exemplos
3. Use arquivos pequenos (< 5MB) para facilitar o versionamento

## 🎵 Formatos Suportados

- WAV (recomendado para qualidade)
- MP3 (comprimido, menor tamanho)
- FLAC (lossless)
- OGG

## 📝 Exemplo de uso

```python
import librosa

# Carrega um arquivo de áudio
y, sr = librosa.load('assets/example.wav')
```

## 🌐 Fontes de Áudio Gratuitas

- [Freesound](https://freesound.org/)
- [Free Music Archive](https://freemusicarchive.org/)
- [BBC Sound Effects](https://sound-effects.bbcrewind.co.uk/)
