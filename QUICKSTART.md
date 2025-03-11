# Quick Start Guide

This guide will help you get started with GoogleSheet2LinkedIn in just 15 minutes!

## 🚀 5-Minute Setup

### Step 1: Install Python
1. Go to [Python Downloads](https://www.python.org/downloads/)
2. Click big yellow "Download Python" button
3. Run the installer
   - On Windows: Check ✓ "Add Python to PATH"
   - Click "Install Now"

### Step 2: Download This Project
1. Click the green "Code" button above
2. Click "Download ZIP"
3. Extract the ZIP file to your Desktop

### Step 3: Get OpenAI API Key
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Click "Create new secret key"
3. Copy the key (save it somewhere safe!)

## 🔧 5-Minute Configuration

### Step 1: Create Google Sheet
1. Go to [Google Sheets](https://sheets.google.com)
2. Click "+ Blank"
3. Add these column headers:
   - A1: "Topic"
   - B1: "Status"
   - C1: "Generated Post"
4. Copy the Sheet ID from URL:
   ```
   https://docs.google.com/spreadsheets/d/THIS_LONG_ID_HERE/edit
   ```

### Step 2: Set Up Project
1. Open Terminal/Command Prompt:
   - Windows: Press Win+R, type `cmd`, press Enter
   - Mac: Press Cmd+Space, type `terminal`, press Enter

2. Navigate to project:
   ```bash
   # Windows (if on Desktop):
   cd %USERPROFILE%\Desktop\GoogleSheet2LinkedIn

   # Mac (if on Desktop):
   cd ~/Desktop/GoogleSheet2LinkedIn
   ```

3. Create virtual environment:
   ```bash
   # Windows:
   python -m venv venv
   venv\Scripts\activate

   # Mac:
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Add Your Keys
1. Create file named `.env` in project folder
2. Add these lines:
   ```
   OPENAI_API_KEY=your_key_here
   LLM_PROVIDER=openai
   LLM_MODEL=gpt-4
   ```

3. Open `src/config.py`
4. Replace `YOUR_SHEET_ID_HERE` with your Sheet ID

## 🎯 5-Minute Test Run

1. Make sure virtual environment is active (you see `(venv)` at start of line)

2. Run the program:
   ```bash
   python src/main.py
   ```

3. When browser opens:
   - Select your Google account
   - Click through warnings
   - Grant permissions
   - Close browser window

4. Add a test topic in your sheet:
   - Column A: "The benefits of AI in daily life"
   - Leave columns B and C empty

5. Watch the magic happen!

## ❓ Common Issues

### "Python not found"
- Make sure Python is in PATH
- Try using `python3` instead of `python`

### "Module not found"
- Make sure you're in the right directory
- Make sure virtual environment is activated
- Try running `pip install -r requirements.txt` again

### "Sheet not found"
- Double-check your Sheet ID
- Make sure sheet is not deleted
- Try copying ID again

### "Invalid API key"
- Check for spaces in `.env` file
- Make sure key is copied correctly
- Try generating a new key

Need more help? Check the full README.md for detailed instructions! 