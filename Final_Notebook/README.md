# Diabetes Risk Prediction (TensorFlow + Streamlit)

This project contains a trained TensorFlow/Keras model (`diabetes_model.keras`) and a Streamlit app (`app.py`) for diabetes risk prediction using the Pima Indians Diabetes dataset.

## Project structure

- `app.py` - Streamlit UI for predictions
- `Model/diabetes_model.keras` - trained Keras model
- `requirements.txt` - Python dependencies
- `.gitignore` - local environment/cache exclusions

## Prerequisites

- Windows
- Python 3.11 (recommended)
- VS Code (optional)

## Setup and run

Open terminal in this folder:

```powershell
cd "d:\Coding_Work\Tensorflow event\Final_Notebook"
```

Create virtual environment:

```powershell
py -3.11 -m venv .venv
```

Activate virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run Streamlit app:

```powershell
streamlit run app.py
```

Then open the URL shown in terminal (usually `http://localhost:8501`).

## Notes

- The app expects the model at `Model/diabetes_model.keras`.
- If model loading fails, confirm the file path and filename exactly match.
- This app is for educational/demo use, not medical diagnosis.
