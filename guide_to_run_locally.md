# 🛠️ Guide to Run Locally

This guide will help you set up your local environment to run the workshop materials on your own computer. We will use **VS Code** as our editor and **Pixi** to manage dependencies (libraries) automatically.

---

## 1. Install Visual Studio Code (VS Code)

VS Code is a popular code editor that supports Jupyter Notebooks natively.

*   **Windows:**
    1.  Download the installer from [code.visualstudio.com](https://code.visualstudio.com/).
    2.  Run the installer and follow the instructions.
    3.  (Optional) During installation, check the box "Add to PATH".

*   **macOS:**
    1.  Download the `.zip` file from [code.visualstudio.com](https://code.visualstudio.com/).
    2.  Unzip it and drag the **Visual Studio Code** app to your `Applications` folder.

*   **Linux:**
    *   **Ubuntu/Debian:** `sudo snap install --classic code` or download the `.deb` file.
    *   **Arch:** `sudo pacman -S code`

---

## 2. Install Python

While **Pixi** (step 3) will handle the specific Python version for this workshop, it is good practice to have a base Python installation on your system.

*   **Windows:**
    *   Download Python from [python.org](https://www.python.org/downloads/).
    *   **Important:** During installation, check the box **"Add Python to PATH"**.

*   **macOS:**
    *   macOS comes with Python, but it's often outdated. We recommend installing via [python.org](https://www.python.org/downloads/) or using Homebrew: `brew install python`.

*   **Linux:**
    *   Python is usually pre-installed. You can verify by typing `python3 --version` in your terminal.

---

## 3. Install Pixi

Pixi is the tool we use to ensure everyone has the exact same libraries and versions. It works on Windows, macOS, and Linux.

*   **Windows (PowerShell):**
    ```powershell
    iwr -useb https://pixi.sh/install.ps1 | iex
    ```

*   **macOS & Linux (Terminal):**
    ```bash
    curl -fsSL https://pixi.sh/install.sh | bash
    ```

*After installation, you might need to restart your terminal or computer.*

---

## 4. Download the Repository

You need to get the workshop files onto your computer. You can do this via **Git** (recommended) or by downloading a **ZIP** file.

### Option A: Via Git (Recommended)
If you have Git installed:

1.  Open your terminal (or PowerShell on Windows).
2.  Navigate to the folder where you want to save the project.
3.  Run:
    ```bash
    git clone https://github.com/zepadovani/2025_FU_workshop.git
    cd 2025_FU_workshop
    ```

### Option B: Download ZIP (No Git required)
1.  Go to the repository page: [https://github.com/zepadovani/2025_FU_workshop](https://github.com/zepadovani/2025_FU_workshop)
2.  Click on the green **<> Code** button.
3.  Select **Download ZIP**.
4.  Extract the ZIP file to a folder on your computer.

---

## 5. Running the Workshop

Now that you have the files and the tools:

1.  Open **VS Code**.
2.  Go to **File > Open Folder...** and select the `2025_FU_workshop` folder you just downloaded.
3.  Open the terminal inside VS Code (`Ctrl + '` or `View > Terminal`).
4.  Initialize the environment by running:
    ```bash
    pixi install
    ```
    *(This may take a few minutes as it downloads all necessary libraries).*

5.  Once finished, you can open any notebook in the `notebooks/` folder.
6.  When asked to select a **Kernel** (top right of the notebook), look for **"Python (2025_FU_workshop)"** or select the python environment created by Pixi (usually inside `.pixi/envs/default`).

### Alternative: Running Jupyter Lab
If you prefer the classic Jupyter interface, run this in the terminal:
```bash
pixi run jupyter lab
```
