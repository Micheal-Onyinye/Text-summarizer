#  Text Summarizer

An intelligent web application that transforms long articles and dense documents into clear, human-like summaries. Built with **Python**, **FastAPI**, and **HuggingFace Transformers**.


## Overview
Most basic summarizers use "extractive" methods (copy-pasting sentences). This project uses **Abstractive Summarization** via the **DistilBART** model. It "reads" the context and "rewrites" the summary in its own words, much like a human would.

## Key Features
*   **Multi-Format Upload:** Process `.pdf`, `.docx`, and `.txt` files directly.
*   **Adjustable Length:** Fine-tune your summary using interactive sliders for Min/Max length.
*   **Modern UI:** A centered, clean, and responsive interface with custom CSS.
*   **Async Backend:** Powered by FastAPI for high-performance, non-blocking requests.
*   **Downloadable Results:** Export your generated summaries as text files instantly.



##  Tech Stack
*   **AI Engine:** HuggingFace Transformers (`sshleifer/distilbart-cnn-12-6`)
*   **Backend:** FastAPI (Python)
*   **Frontend:** Streamlit
*   **Data Validation:** Pydantic
*   **Document Parsing:** PyPDF2 & python-docx


##  Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer
```
### 2. Create Virtual Environment
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
```
## How to Run
This application runs in two parts. You will need two terminal windows.
### Step 1: Start the Backend (API)
The backend handles the AI processing.
```bash
python main.py
```
### Step 2: Start the Frontend (UI)
The frontend provides the interactive interface.
```bash
streamlit run ui.py
```
## Project Structure
```
├── main.py          # FastAPI routes & API configuration
├── logic.py         # AI Model loading & tokenization logic
├── schema.py        # Pydantic data models for validation
├── file_utils.py    # PDF and DOCX text extraction helpers
├── ui.py            # Streamlit frontend with custom CSS styling
└── requirements.txt # Project dependencies
```
