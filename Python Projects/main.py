import streamlit as st

# Set page title and icon
st.set_page_config(page_title="📖 KnowledgeGPT", layout="wide")

st.sidebar.markdown("### Company name")
st.sidebar.image("images/company.png", use_container_width=True)

st.sidebar.title("Main Menu")
# Navigation Buttons
if st.sidebar.button("Home"):
    st.session_state.page = "Home"
if st.sidebar.button("Settings"):
    st.session_state.page = "Settings"

# Sidebar for API Key and Navigation
st.sidebar.title("How to use")
st.sidebar.markdown("1. Enter your OpenAI API key below 🔑\n2. Upload a pdf, docx, or txt file 📄\n3. Ask a question about the document 💬")
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Ensure session state is initialized
if "page" not in st.session_state:
    st.session_state.page = "Home"

# About section
st.sidebar.markdown("### About")
st.sidebar.info("📖 KnowledgeGPT allows you to ask questions about your documents and get accurate answers with instant citations.")
st.sidebar.markdown("This tool is a work in progress. You can contribute to the project on [GitHub](https://github.com/) with your feedback and suggestions 💡")

# Main UI
st.title("📖 KnowledgeGPT")
st.markdown("Enter your OpenAI API key in the sidebar. You can get a key at [OpenAI API Keys](https://platform.openai.com/account/api-keys).")

if st.session_state.page == "Home":
    # File uploader
    uploaded_file = st.file_uploader("Upload a pdf, docx, or txt file", type=["pdf", "docx", "txt"], help="Limit 25MB per file")

    # Model selection
    model = st.selectbox("Model", ["gpt-3.5-turbo", "gpt-4"])

    # Advanced Options
    with st.expander("Advanced Options"):
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

    if uploaded_file and openai_key:
        st.success("File uploaded successfully!")
        st.info("Processing document...")
        # Here you would add the logic to process the file and interact with OpenAI API.
    else:
        st.warning("Please upload a file and enter an API key to proceed.")

elif st.session_state.page == "Settings":
    st.subheader("Settings Page")
    st.write("Here you can configure additional settings.")
