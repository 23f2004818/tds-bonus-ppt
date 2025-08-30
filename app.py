import streamlit as st
from utils.llm_providers import LLMClient
from utils.text_parser import parse_text_to_slides
from utils.pptx_builder import build_pptx_from_template

st.title("📊 Text → Deck Generator")

text_input = st.text_area("Paste your text or markdown here:")
guidance = st.text_input("Optional guidance (e.g., 'Investor pitch deck')")
api_key = st.text_input("Enter your API Key (never stored)", type="password")
provider = st.selectbox("Choose LLM provider", ["OpenAI", "Anthropic", "Gemini"])
template_file = st.file_uploader("Upload PowerPoint template (.pptx/.potx)", type=["pptx", "potx"])

if st.button("Generate Presentation"):
    if not text_input or not api_key or not template_file:
        st.error("Please provide text, API key, and template file.")
    else:
        client = LLMClient(provider, api_key)

        # (Optional: refine with LLM)
        slides = parse_text_to_slides(text_input, guidance)

        output_path = "generated.pptx"
        with open("uploaded_template.pptx", "wb") as f:
            f.write(template_file.read())

        build_pptx_from_template("uploaded_template.pptx", slides, output_path)

        with open(output_path, "rb") as f:
            st.download_button("Download Presentation", f, file_name="presentation.pptx")
