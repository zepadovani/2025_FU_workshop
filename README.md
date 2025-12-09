# 🎵 Listening with machines, crafting transductions: technodiversity, creative tools, and critical perspectives in research-creation practices

This is the repository for the practical/hands-on part of the workshop "Listening with machines, crafting transductions: technodiversity, creative tools, and critical perspectives in research-creation practices" held at Freie Universität Berlin in March 2025.

In this session, we will explore Audio Processing and AI using Python.

## 🚀 How to Run

You can run the workshop materials in two ways: **Google Colab** (recommended for beginners) or **Locally** (for users familiar with Python and Jupyter notebooks).

### Option 1: Google Colab (Recommended)

No installation required. Choose a notebook below to start:

| Notebook | Description | Link |
| :--- | :--- | :--- |
| **01. Workshop Demo** | Introduction and environment test. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zepadovani/2025_FU_workshop/blob/main/notebooks/01_test_pixi_gradio_colab.ipynb) |
| **02. Audio Descriptors** | Explore audio features (Centroid, MFCCs, etc.) interactively. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zepadovani/2025_FU_workshop/blob/main/notebooks/02_audio_descriptors_explorer.ipynb) |
| **03. CQT Analyzer** | Upload and analyze audio using Constant-Q Transform. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zepadovani/2025_FU_workshop/blob/main/notebooks/03_cqt_analyzer.ipynb) |

1.  Click the badge for the notebook you want to run.
2.  Sign in with your Google account if asked.
3.  Run the first cell to set up the environment automatically.
4.  Have fun!

### Option 2: Running Locally

If you prefer to run on your own machine, we use **Pixi** for environment management.

1.  **Install Pixi**: [https://pixi.sh](https://pixi.sh)
2.  **Clone the repository**:
    ```bash
    git clone https://github.com/zepadovani/2025_FU_workshop.git
    cd 2025_FU_workshop
    ```
3.  **Install dependencies**:
    ```bash
    pixi install
    ```
4.  **Run the Notebook**:
    ```bash
    pixi run jupyter lab
    ```

## 📂 Project Structure

- `notebooks/`: Contains the interactive lessons (`.ipynb`).
- `assets/`: Example audio files.
- `scripts/`: Python scripts for standalone apps.

## 🛠️ Tools We Will Use

- **Librosa**: For audio analysis.
- **Gradio**: For creating interactive web demos.
- **Matplotlib**: For visualization.

---

**Happy Coding! 🎧**
