# GoogleSheet2LinkedIn

An automated tool that reads topics from Google Sheets and generates professional LinkedIn posts using various AI language models (LLMs). Supports multiple providers including OpenAI, Anthropic, Google AI, and Cohere.

## Prerequisites

Before you begin, make sure you have:
1. Python 3.8 or higher installed on your computer
   - To check, open terminal/command prompt and run: `python --version`
   - If not installed, download from [Python's official website](https://www.python.org/downloads/)
2. A Google account
3. At least one API key from a supported LLM provider:
   - [OpenAI](https://platform.openai.com/api-keys)
   - [Anthropic](https://console.anthropic.com/account/keys)
   - [Google AI](https://makersuite.google.com/app/apikey)
   - [Cohere](https://dashboard.cohere.com/api-keys)
4. Basic familiarity with terminal/command prompt

## Detailed Setup Guide

### 1. Project Setup
```bash
# Clone or download this repository
# Navigate to the project directory
cd GoogleSheet2LinkedIn

# Create a virtual environment (recommended)
# For Windows:
python -m venv venv
venv\Scripts\activate

# For macOS/Linux:
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Google Sheets API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project:
   - Click on the project dropdown at the top
   - Click "New Project"
   - Name it (e.g., "GoogleSheet2LinkedIn")
   - Click "Create"

3. Enable Google Sheets API:
   - Select your project
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

4. Create credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth 2.0 Client ID"
   - If prompted, configure the OAuth consent screen:
     - User Type: External
     - App name: GoogleSheet2LinkedIn
     - User support email: Your email
     - Developer contact email: Your email
     - Save and continue
   - For application type, select "Desktop app"
   - Name it "GoogleSheet2LinkedIn Client"
   - Click "Create"
   - Download the JSON file
   - Rename it to `credentials.json` and place it in the project root directory

### 3. LLM Provider Setup

1. Choose your preferred LLM provider (OpenAI, Anthropic, Google AI, or Cohere)
2. Get your API key from the chosen provider's website
3. Create a file named `.env` in the project root directory
4. Add your API key(s) and provider preference:
   ```
   # Required: At least one API key
   OPENAI_API_KEY=your_openai_key_here
   ANTHROPIC_API_KEY=your_anthropic_key_here
   GOOGLE_AI_API_KEY=your_google_key_here
   COHERE_API_KEY=your_cohere_key_here

   # Optional: Choose your provider and model
   LLM_PROVIDER=openai  # Options: openai, anthropic, google, cohere
   LLM_MODEL=gpt-4     # See available models below
   ```

### Available Models by Provider

1. OpenAI Models:
   - gpt-4 (default)
   - gpt-4-turbo
   - gpt-3.5-turbo

2. Anthropic Models:
   - claude-3-opus (default)
   - claude-3-sonnet
   - claude-2

3. Google AI Models:
   - gemini-pro (default)

4. Cohere Models:
   - command (default)
   - command-light

If not specified, the application will use OpenAI's GPT-4 as the default model.

### 4. Google Sheet Setup

1. Create a new Google Sheet
2. Set up the following columns:
   - Column A: Title = "Topic"
   - Column B: Title = "Status"
   - Column C: Title = "Generated Post"

3. Get your Sheet ID:
   - Open your Google Sheet
   - Look at the URL: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID_HERE/edit
   - Copy the YOUR_SHEET_ID_HERE part

4. Update config.py:
   - Open `src/config.py`
   - Replace "YOUR_SHEET_ID_HERE" with your actual Sheet ID

### 5. Running the Application

1. Make sure your virtual environment is activated
2. Run the script:
   ```bash
   python src/main.py
   ```
3. On first run:
   - A browser window will open
   - Select your Google account
   - Grant the requested permissions
   - The application will start running using your chosen LLM provider

## Usage Guide

### Adding Topics for Generation

1. Open your Google Sheet
2. In column A (Topic), add the topics you want posts about
3. Leave columns B (Status) and C (Generated Post) empty
4. The application will:
   - Check for new topics every 5 minutes
   - Generate posts for topics without "Generated" status
   - Update the Status to "Generated"
   - Place the generated post in the Generated Post column

### Example Topic Format

Good topic examples:
- "The impact of AI on healthcare in 2024"
- "5 best practices for cloud security"
- "Why DevOps is crucial for modern software development"

### Monitoring the Process

The application will show:
- When it starts checking for new topics
- Which topic is currently being processed
- Success or failure messages for each generation
- Any errors that occur

## Troubleshooting

### Common Issues and Solutions

1. "Invalid credentials":
   - Delete the `token.pickle` file
   - Restart the application
   - Re-authenticate through the browser

2. "API key not found":
   - Check if `.env` file exists
   - Verify the OPENAI_API_KEY format
   - Make sure there are no spaces around the API key

3. "Sheet not found":
   - Verify your Sheet ID in `config.py`
   - Make sure the sheet is shared with your Google account
   - Check if the sheet URL is accessible

4. "Permission denied":
   - Go to Google Cloud Console
   - Check if the API is enabled
   - Verify OAuth consent screen configuration
   - Delete `token.pickle` and re-authenticate

Additional LLM-specific issues:

1. "Provider not available":
   - Check if LLM_PROVIDER in .env matches available options
   - Verify API key for chosen provider exists
   - Install required dependencies

2. "Model not available":
   - Check if LLM_MODEL matches available models for your provider
   - Some models may require special access or higher API tiers

3. "Rate limit exceeded":
   - Different providers have different rate limits
   - Consider switching to a provider with higher limits
   - Adjust the wait time between requests

### Provider-Specific Notes

1. OpenAI:
   - Most stable and widely used
   - Good balance of quality and speed
   - Higher cost for GPT-4 models

2. Anthropic:
   - Claude models excel at longer content
   - Good at technical accuracy
   - May have different rate limits

3. Google AI:
   - Gemini offers good performance
   - Competitive pricing
   - May have regional restrictions

4. Cohere:
   - Good for specific use cases
   - May have different output styles
   - Consider for cost-effective solutions

## Best Practices

1. Keep your API keys secure:
   - Never commit `.env` or `credentials.json` to version control
   - Don't share these files with others

2. Monitor API usage:
   - Check your OpenAI dashboard for API usage
   - Be aware of rate limits and costs

3. Regular maintenance:
   - Keep Python packages updated
   - Monitor the Google Sheet for any issues
   - Backup important generated content

Additional LLM best practices:

1. Choose the right provider:
   - Consider your needs (quality, speed, cost)
   - Test different providers for your use case
   - Monitor usage and costs

2. Model selection:
   - Start with default models
   - Upgrade to more powerful models if needed
   - Balance cost vs. quality

3. API key security:
   - Keep separate keys for development/production
   - Regularly rotate API keys
   - Never share or expose keys

## Contributing

Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests

## License

This project is open source and available under the MIT License.
