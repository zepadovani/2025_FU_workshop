# Audio Descriptors for Musicians & Creative Coding
**Libraries:** `audiofile`, `librosa`, `numpy`

This guide bridges the gap between digital signal processing and musical perception. It describes the most common features used in Machine Listening and how to extract them using Python.

## 0. The Basics (Loading Audio)
We use the **`audiofile`** library to load the audio because it is faster and preserves the **original sample rate** of the file (unlike `librosa.load`, which resamples to 22kHz by default).

*   **y (Signal):** The raw waveform (sequence of numbers).
*   **sr (Sample Rate):** How many samples per second (e.g., 44100 Hz, 48000 Hz).

```python
import audiofile
import librosa
import numpy as np

# Load audio maintaining the original Sample Rate
y, sr = audiofile.read('audio_file.wav')

# Note: audiofile might return stereo audio. 
# For basic analysis, it is often easier to convert to Mono first:
if y.ndim > 1:
    y = librosa.to_mono(y)
```

---

## 1. Timbre (Tone Color & Texture)
These features describe the "quality" of a sound—what makes a guitar sound different from a piano, even if they play the same note.

### Spectral Centroid (Brightness)
*   **What is it?** It calculates the "center of gravity" of the frequency spectrum.
*   **Musician's Perspective:** Think of this as a measure of **Brightness**.
    *   **High value:** Bright, sharp, treble-heavy sounds (e.g., Hi-hat, Violin, Distorted Synth).
    *   **Low value:** Dark, deep, bass-heavy sounds (e.g., Kick drum, Sub-bass).
*   **Common Applications:**
    *   **Visual Arts:** Mapping brightness to the color or intensity of a visual (Bright sound = White color; Dark sound = Blue color).
    *   **Smart Sorting:** Automatically organizing a sample library from "Darkest" to "Brightest" snares.
*   **Code:**
    ```python
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    ```

### Spectral Rolloff (The Shape)
*   **What is it?** The frequency below which most (usually 85%) of the energy resides.
*   **Musician's Perspective:** This defines the **limit of the high frequencies**. It helps distinguish sounds that are "airy" or "hissy" from sounds that are "muffled."
*   **Common Applications:**
    *   Distinguishing voiced sounds (vowels like "Aaa") from unvoiced sounds (fricatives like "Sss" or "Shh").
    *   Discriminating between a Kick drum (low rolloff) and a Snare drum (high rolloff).
*   **Code:**
    ```python
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    ```

### MFCCs (The Fingerprint)
*   **What is it?** Mel-Frequency Cepstral Coefficients. A set of numbers (usually 13 or 20) that summarize the shape of the spectrum.
*   **Musician's Perspective:** This is the **Timbral Fingerprint** or "ID Card" of the sound. It mimics how the human ear identifies specific instruments or voices.
*   **Common Applications:**
    *   **Genre Classification:** Teaching a computer to identify Jazz vs. Techno.
    *   **Instrument Recognition:** Identifying if an audio file contains a Piano or a Trumpet.
    *   **Voice commands:** Used in speech recognition.
*   **Code:**
    ```python
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    ```

### Spectral Flatness (Noisiness)
*   **What is it?** A measure of how "flat" (uniform) the spectrum is.
*   **Musician's Perspective:** **Tone vs. Noise**.
    *   **Value ~ 1:** Pure Noise (White noise, wind, heavy cymbal crash).
    *   **Value ~ 0:** Pure Tone (Sine wave, whistling, clean bell).
*   **Common Applications:**
    *   Classifying sound FX (identifying explosions or wind).
    *   Filtering out noisy/low-quality recordings from a collection.
*   **Code:**
    ```python
    flatness = librosa.feature.spectral_flatness(y=y)
    ```

---

## 2. Dynamics & Time
Features based on amplitude (loudness) or changes over time.

### RMS (Loudness)
*   **What is it?** Root Mean Square.
*   **Musician's Perspective:** This represents the average **Volume** or energy of the track over time.
*   **Common Applications:**
    *   **Silence Detection:** Automatically trimming the silence at the start/end of a recording.
    *   **Adaptive Effects:** Triggering a reverb or delay only when the volume exceeds a certain threshold.
*   **Code:**
    ```python
    rms = librosa.feature.rms(y=y)
    ```

### Zero Crossing Rate (Roughness/Percussion)
*   **What is it?** How frequently the waveform crosses the center (zero) line.
*   **Musician's Perspective:** Highly correlated with **percussive** or **noisy** textures.
    *   **Low ZCR:** Smooth, pitched sounds (Bass, Cello).
    *   **High ZCR:** Noisy, rough sounds (Snare, Metal scraping, Distortion).
*   **Common Applications:**
    *   Detecting the onset (start) of a drum hit.
    *   Distinguishing speech (high variation) from music (more stable).
*   **Code:**
    ```python
    zcr = librosa.feature.zero_crossing_rate(y)
    ```

---

## 3. Rhythm (Tempo)

### Beat Tracker
*   **What is it?** An algorithm that finds the recurring rhythmic pulse.
*   **Musician's Perspective:** It finds the **BPM** (Tempo) and the location of every beat (the metronome click).
*   **Common Applications:**
    *   **Auto-Sync:** Syncing two tracks in DJ software.
    *   **Looping:** Automatically cutting a sample to make a perfect loop.
*   **Code:**
    ```python
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print(f"Estimated BPM: {tempo}")
    ```

---

## 4. Harmony & Pitch

### Chroma (Notes & Chords)
*   **What is it?** It collapses the entire spectrum into 12 bins corresponding to the 12 semitones.
*   **Musician's Perspective:** It ignores octaves and tells you the **harmonic content** (C, C#, D, D#...) active at any moment.
*   **Common Applications:**
    *   **Chord Recognition:** Identifying if the band is playing C Major or F Minor.
    *   **Cover Song ID:** Recognizing a melody regardless of the instrument playing it.
*   **Code:**
    ```python
    chromagram = librosa.feature.chroma_stft(y=y, sr=sr)
    ```

---

## 5. Advanced Time-Frequency Representations

### CQT (Constant-Q Transform)
*   **What is it?** Unlike the STFT (which has linear frequency resolution), the CQT uses a **logarithmic frequency scale**.
*   **Musician's Perspective:** It matches the **musical scale** (piano keys) much better than a standard spectrogram. Low frequencies have better resolution, just like our ears.
*   **Common Applications:**
    *   **Music Transcription:** Converting audio to MIDI.
    *   **Instrument Analysis:** Analyzing the harmonic series of instruments in a musically relevant way.
*   **Code:**
    ```python
    C = librosa.cqt(y=y, sr=sr)
    C_db = librosa.amplitude_to_db(np.abs(C), ref=np.max)
    ```

---

## 6. Spectral Dynamics & Flux

### Spectral Flux
*   **What is it?** It measures how quickly the power spectrum is changing. It calculates the difference between the current frame and the previous one.
*   **Musician's Perspective:** It indicates **"How much is the sound changing right now?"**.
    *   **High Flux:** Note onsets, percussive hits, drastic timbre changes.
    *   **Low Flux:** Sustained notes, drones, silence.
*   **Common Applications:**
    *   **Onset Detection:** Finding exactly when a note starts.
    *   **Novelty Detection:** Identifying new sections in a song.
*   **Code:**
    ```python
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    ```

---

## 7. Psychoacoustics & Perception

### Loudness (Perceptual)
*   **What is it?** While RMS measures physical energy, Perceptual Loudness (often measured in LUFS or Phons) accounts for the fact that human ears are more sensitive to certain frequencies (2kHz-5kHz) than others (bass/treble).
*   **Musician's Perspective:** **"How loud does it actually feel?"**. A sub-bass sine wave at -10dB sounds much quieter than a chainsaw sound at -10dB.
*   **Common Applications:**
    *   **Mastering:** Ensuring consistent volume across tracks.
    *   **ReplayGain:** Normalizing audio for playback.
*   **Note:** Librosa has basic weighting (`librosa.A_weighting`), but for strict LUFS compliance, libraries like `pyloudnorm` are preferred.

---

## 8. Segmentation & Structure

### Onset Detection & Segmentation
*   **What is it?** The process of dividing audio into meaningful chunks (notes, bars, or sections).
*   **Musician's Perspective:** **"Slicing the sample"**.
*   **Common Applications:**
    *   **Sampler Slicing:** Automatically chopping a drum break into individual hits (Kick, Snare, Hat).
    *   **Structure Analysis:** Identifying Verse vs. Chorus.
*   **Code:**
    ```python
    # Detect onset frames (where notes start)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    # Convert frames to time (seconds)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    ```