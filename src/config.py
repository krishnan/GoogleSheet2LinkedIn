import os
from dotenv import load_dotenv

# Load environment variables from .env file
# Make sure you have created a .env file in the project root with your OpenAI API key
load_dotenv()

# Google Sheets Configuration
# To find your Sheet ID:
# 1. Open your Google Sheet
# 2. Look at the URL: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID_HERE/edit
# 3. Copy the YOUR_SHEET_ID_HERE part
SHEET_ID = "YOUR_SHEET_ID_HERE"

# The range in A1 notation that contains your data
# Format: "StartColumn StartRow : EndColumn EndRow"
# Example: "A2:C" means from column A row 2 to column C last row
# A = Topic column
# B = Status column
# C = Generated Post column
SHEET_RANGE = "A2:C"

# The path to your Google OAuth 2.0 credentials file
# This file should be downloaded from Google Cloud Console
# and renamed to 'credentials.json'
CREDENTIALS_FILE = "credentials.json"

# LLM Provider Configuration
# Available providers: 'openai', 'anthropic', 'google', 'cohere'
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")

# LLM Model Configuration
LLM_CONFIG = {
    "openai": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "available_models": {
            "gpt-4": {"max_tokens": 3000, "temperature": 0.7},
            "gpt-4-turbo": {"max_tokens": 4000, "temperature": 0.7},
            "gpt-3.5-turbo": {"max_tokens": 2000, "temperature": 0.7}
        },
        "default_model": "gpt-4"
    },
    "anthropic": {
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "available_models": {
            "claude-3-opus": {"max_tokens": 4000, "temperature": 0.7},
            "claude-3-sonnet": {"max_tokens": 3000, "temperature": 0.7},
            "claude-2": {"max_tokens": 3000, "temperature": 0.7}
        },
        "default_model": "claude-3-opus"
    },
    "google": {
        "api_key": os.getenv("GOOGLE_AI_API_KEY"),
        "available_models": {
            "gemini-pro": {"max_tokens": 2048, "temperature": 0.7}
        },
        "default_model": "gemini-pro"
    },
    "cohere": {
        "api_key": os.getenv("COHERE_API_KEY"),
        "available_models": {
            "command": {"max_tokens": 2048, "temperature": 0.7},
            "command-light": {"max_tokens": 2048, "temperature": 0.7}
        },
        "default_model": "command"
    }
}

# Get the selected model from environment or use provider's default
SELECTED_MODEL = os.getenv("LLM_MODEL", LLM_CONFIG[LLM_PROVIDER]["default_model"])

# Validate configuration
if LLM_PROVIDER not in LLM_CONFIG:
    raise ValueError(f"Invalid LLM provider: {LLM_PROVIDER}. Available providers: {list(LLM_CONFIG.keys())}")

if SELECTED_MODEL not in LLM_CONFIG[LLM_PROVIDER]["available_models"]:
    raise ValueError(
        f"Invalid model '{SELECTED_MODEL}' for provider '{LLM_PROVIDER}'. "
        f"Available models: {list(LLM_CONFIG[LLM_PROVIDER]['available_models'].keys())}"
    )

if not LLM_CONFIG[LLM_PROVIDER]["api_key"]:
    raise ValueError(f"API key not found for {LLM_PROVIDER}. Please check your .env file.")

# LinkedIn Post Configuration
MAX_POST_LENGTH = LLM_CONFIG[LLM_PROVIDER]["available_models"][SELECTED_MODEL]["max_tokens"]

# Template for generating LinkedIn posts
# This prompt template guides the AI in creating engaging posts
# You can modify this template to change the style of generated posts
PROMPT_TEMPLATE = """
Generate a LinkedIn post about {topic}. The post should be:
1. Professional and engaging
2. Technically accurate
3. Include relevant industry insights
4. End with 3-5 relevant hashtags

The post should be unique and written in a conversational yet professional tone.
Ensure the content is factual and provides value to the reader.

Additional guidelines:
- Start with a hook to grab attention
- Include specific examples or data points when possible
- Break up text into readable paragraphs
- Use emojis sparingly and professionally
- Keep the overall length suitable for LinkedIn
"""
