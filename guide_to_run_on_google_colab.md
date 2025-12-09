# ☁️ Guide to Run on Google Colab

Google Colab is a free cloud service that lets you run Python code in your browser without installing anything on your computer. It is the easiest way to participate in the workshop if you don't want to set up a local environment.

---

## 1. Opening the Notebook

The easiest way to start is by clicking the **"Open in Colab"** badge found in the main `README.md` of this repository.

Alternatively, you can use this direct link:
[**Click here to open the Workshop Demo in Colab**](https://colab.research.google.com/github/zepadovani/2025_FU_workshop/blob/main/notebooks/workshop_demo.ipynb)

---

## 2. First Steps

When you open the notebook, you will see the code cells. Follow these steps to get started:

### A. Sign In
If you are not already logged in, click the **"Sign in"** button in the top right corner and use your Google account.

### B. Connect to a Runtime
Click the **"Connect"** button in the top right corner. This assigns a cloud computer to your session.
*   *Note: For this workshop, the standard CPU runtime is sufficient. You don't need a GPU.*

---

## 3. Running the Code

### A. The "Warning" Message
When you try to run the first cell, Google Colab might show a warning:
> *Warning: This notebook was not authored by Google.*

This is normal because the notebook comes from our GitHub repository. Click **"Run anyway"**.

### B. Environment Setup (Crucial Step!)
The first code cell in the notebook is designed to set up the environment.
1.  Locate the cell under **"Environment Setup"**.
2.  Click the **Play icon (▶️)** on the left side of the cell.
3.  Wait for it to finish. You will see messages like `Installing dependencies...` and finally `✅ Installation complete`.

*This step installs libraries like `librosa`, `gradio`, and `soundfile` that are not pre-installed in Colab.*

---

## 4. Using the Interactive App

Once the setup is done and libraries are imported:
1.  Run the cell containing the **Gradio** app code.
2.  Colab will display the interface directly inside the notebook.
3.  If the interface doesn't appear or is too small, look for a link that says **"Running on public URL: https://....gradio.live"**. Clicking this link opens the app in a full browser tab (great for sharing!).

---

## 5. Saving Your Work

**Important:** Google Colab sessions are temporary. If you close the tab, you might lose your changes.

To save your work:
1.  Go to **File > Save a copy in Drive**.
2.  This creates a copy of the notebook in your personal Google Drive.
3.  You can open this copy later from [drive.google.com](https://drive.google.com).

---

## 6. Troubleshooting

*   **"ModuleNotFoundError"**: If you see an error saying a module is missing, make sure you actually ran the **Environment Setup** cell at the top.
*   **Audio not playing**: Ensure your computer's volume is up. Sometimes browsers block auto-playing audio; check your browser's permission settings.
*   **Old version of the notebook**: If the notebook looks outdated, try adding `?v=2` to the end of the URL to force a refresh.
