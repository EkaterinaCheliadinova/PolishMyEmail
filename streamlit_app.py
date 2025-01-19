import streamlit as st
from emailcraft.email_processor import EmailWorkflow
from emailcraft.ai_integration import AIModel
from emailcraft.streamlit_utils import StreamlitInterface
from emailcraft.config import OPEN_AI_KEY

# Initialize components
ai_model = AIModel(api_key=OPEN_AI_KEY)
workflow = EmailWorkflow(model=ai_model).get_workflow()
interface = StreamlitInterface(workflow=workflow)

# Set Streamlit page configuration
st.set_page_config(
    page_title="PolishMyMail - Email Assistant",
    page_icon="📨",
    layout="wide"
)

# Sidebar: Application Information
st.sidebar.title("📋 About PolishMyMail")
st.sidebar.write(
    """
    **PolishMyMail** helps you craft structured, polished, and professional emails.
    Whether you need a formal tone, a friendly style, or a concise summary, we’ve got you covered!
    """
)
st.sidebar.write("**Features:**")
st.sidebar.write("- Tone adjustment (Formal/Informal)\n- Grammar and style improvements\n- Email summarization")

# Main App Layout
st.title("📨 PolishMyMail - Smart Email Assistant")

# Input Section
st.subheader("Write or Paste Your Email")
email_input = st.text_area("Email Content", height=120, placeholder="Type your email here...")

# Options for Processing
st.subheader("Choose Options")
tone_option = st.selectbox(
    "Select Email Tone",
    options=["Original", "Formal", "Informal"],
    index=0
)

summarize_option = st.checkbox("Summarize Email (Shortened Version)")

if st.button("Polish My Email",use_container_width=True):
    if not email_input.strip():
        st.warning("Please enter some email content before processing!")
    else:
        # Core Processing
        st.subheader("Improved Email")
        placeholder = st.empty()
        interface.stream_response(email_input, tone_option, summarize_option, placeholder)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("💡 **Created by:** Ekaterina Cheliadinova | Powered by Streamlit and LangGraph")

