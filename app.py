import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from env.local if it exists
load_dotenv('env.local')

# Page configuration
st.set_page_config(
    page_title="Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Initialize session state for API key
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = None

# Sidebar for API key management
with st.sidebar:
    st.header("🔑 API Key Configuration")
    
    # Check if key exists in env.local
    env_key = os.getenv('OPENAI_API_KEY')
    
    if env_key:
        # Display masked version: first 4 and last 4 characters
        masked_key = f"{env_key[:4]}...{env_key[-4:]}"
        st.info(f"Key found in env.local: `{masked_key}`")
        
        # Set session state from environment
        st.session_state.openai_api_key = env_key
    else:
        st.info("No key found in env.local. Enter your key below or add it to env.local file.")
    
    # Input field for API key
    api_key_input = st.text_input(
        "OpenAI API Key",
        type="password",
        value="" if not env_key else env_key,
        help="Enter your OpenAI API key or add it to env.local file"
    )
    
    if api_key_input:
        st.session_state.openai_api_key = api_key_input
        st.success("API key set!")
    elif not env_key:
        st.warning("Please enter an API key to continue")

# Main content area
st.title("🚀 Welcome to Streamlit!")
st.write("This is a basic Streamlit application template.")

# Example: Display API key status
st.header("API Key Status")
if st.session_state.openai_api_key:
    masked_display = f"{st.session_state.openai_api_key[:4]}...{st.session_state.openai_api_key[-4:]}"
    st.success(f"✅ API key is configured: `{masked_display}`")
else:
    st.error("❌ No API key configured. Please set it in the sidebar.")

# Add your app content here
st.header("Your Content Here")
st.write("Start building your Streamlit app below!")

