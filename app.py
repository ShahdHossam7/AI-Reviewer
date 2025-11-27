import streamlit as st
import pandas as pd
import json
import torch
from transformers import pipeline

# ======================================================
# Page Config + Custom CSS
# ======================================================
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.markdown("""
<style>
    .app-title {
        font-size: 42px !important;
        font-weight: 800 !important;
        text-align: center;
        color: #4A90E2;
    }
    .section-title {
        font-size: 20px !important;
        font-weight: 600 !important;
        margin-top: 25px;
        color: #333;
    }
    .stButton>button {
        background: #4A90E2;
        color: white;
        border-radius: 10px;
        padding: 10px 22px;
        font-size: 17px;
    }
    .stButton>button:hover {
        background: #3c75b8;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-title'>AI Code Review System</div>", unsafe_allow_html=True)
st.write("Upload or paste your code, and the AI model will analyze it and return structured issues in JSON format.")

# ======================================================
# Load Model (Cached)
# ======================================================
@st.cache_resource
def load_model():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-Coder-1.5B-Instruct",
        device=device,
        max_new_tokens=512,
        temperature=0.2
    )

reviewer = load_model()

# ======================================================
# Prompt Builder
# ======================================================
def build_prompt(code):
    return f"""
You are a strict senior Python code reviewer.
Return ONLY a valid JSON array containing issues in the following format:

{{
    "issue": "description",
    "line_start": 0,
    "line_end": 0,
    "suggestion": "fix",
    "severity": "Critical"
}}

Rules:
- Do not include text outside JSON.
- No explanations.
- Maximum clarity.
- JSON array only.

Review this code:
--- CODE START ---
{code}
--- CODE END ---
"""

# ======================================================
# JSON Parser
# ======================================================
def parse_json(output):
    try:
        start = output.find("[")
        end = output.rfind("]") + 1
        return json.loads(output[start:end])
    except:
        return [{
            "issue": "Invalid JSON returned",
            "line_start": 0,
            "line_end": 0,
            "suggestion": "Model did not follow JSON rules",
            "severity": "Error"
        }]

# ======================================================
# UI – Code Input Section
# ======================================================
st.markdown("<div class='section-title'>Upload or Paste Your Code</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a Python or text file", type=["py", "txt"])
code_text = uploaded_file.read().decode("utf-8") if uploaded_file else ""

code_input = st.text_area("Paste your code here:", value=code_text, height=300)

# ======================================================
# Review Button
# ======================================================
if st.button("Review Code"):
    if not code_input.strip():
        st.warning("Please upload or paste code first.")
    else:
        with st.spinner("Analyzing your code..."):
            prompt = build_prompt(code_input)
            raw_output = reviewer(prompt)[0]["generated_text"]
            issues = parse_json(raw_output)

        st.success("Review completed.")

        st.markdown("<div class='section-title'>Detected Issues</div>", unsafe_allow_html=True)
        df = pd.DataFrame(issues)
        st.dataframe(df, use_container_width=True)

        st.markdown("<div class='section-title'>Raw Model Output</div>", unsafe_allow_html=True)
        st.code(raw_output)
