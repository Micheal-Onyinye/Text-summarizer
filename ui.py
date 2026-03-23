import streamlit as st
import requests
from file_utils import extract_text  # Import file extractor

st.set_page_config(page_title="Summarizer", layout="wide")

st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1E1E1E;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .sub-title {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }

   
    .summary-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin-top: 20px;
    }
    
   
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.markdown('<h1 class="main-title">Text Summarizer</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Transform long articles into clear, concise summaries instantly.</p>', unsafe_allow_html=True)

left_spacer, main_content, right_spacer = st.columns([1, 3, 1])

with main_content:
    # Input Section
    with st.expander("Upload Document", expanded=True):
        # 1. File Uploader
      uploaded_file = st.file_uploader("Upload a file (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
    
    text_input = st.text_area("OR Paste text here:", height=250, placeholder="type or paste your content here")

 
    col1, col2 = st.columns(2)
    with col1:
        max_len = st.slider("Max Summary Length", 50, 500, 130)
    with col2:
        min_len = st.slider("Min Summary Length", 10, 100, 30)


    if st.button("Generate Summary"):
        final_text = ""

        if uploaded_file is not None:
            with st.spinner("Reading file"):
                final_text = extract_text(uploaded_file)
        elif text_input.strip() != "":
            final_text = text_input
        else:
            st.warning("Please provide some text or upload a file.")

        if final_text:
            with st.spinner("Summarizing"):
                try:
                    payload = {"text": final_text, "max_len": max_len, "min_len": min_len}
                    response = requests.post("http://127.0.0.1:8000/summarize", json=payload)
                    
                    if response.status_code == 200:
                        summary = response.json()['summary']
                        
                        st.markdown("Summary")
                        st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)
                        
                        # Download Button
                        st.write("") 
                        st.download_button(
                            label="Download Summary as TXT",
                            data=summary,
                            file_name="summary.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error("Backend error. Is your API running?")
                except Exception as e:
                    st.error("Could not connect to the Backend server.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Created with Python, FastAPI & HuggingFace</p>", unsafe_allow_html=True)







