# Streamlit Project

A Streamlit application template with OpenAI API key management.

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

Start the Streamlit app with:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## OpenAI API Key Setup

You can configure your OpenAI API key in two ways:

### Option 1: Using env.local file (Recommended)

1. Create a file named `env.local` in the project root directory
2. Add your OpenAI API key to the file:
```
OPENAI_API_KEY=your_key_here
```
3. The app will automatically load the key from this file when it starts
4. The key will be displayed in masked format (first 4 and last 4 characters) in the sidebar

**Note:** The `env.local` file is excluded from git (via `.gitignore`) to keep your API key private.

### Option 2: Using the App Interface

1. Run the app
2. Enter your OpenAI API key in the sidebar input field
3. The key will be stored in session state for the current session

## Project Structure

```
poles/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .gitignore         # Git ignore rules
├── .streamlit/        # Streamlit configuration
│   └── config.toml
└── env.local          # Your API keys (not tracked by git)
```

## Development

- Edit `app.py` to customize your application
- Add new dependencies to `requirements.txt`
- Configure Streamlit settings in `.streamlit/config.toml`

