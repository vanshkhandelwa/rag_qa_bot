---
title: Pandas QA Bot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# Pandas_QA_Bot
Using Langchain, Gradio and Google Gemini for creating an interactive question answering bot.

## Features

- 📊 Upload CSV files and ask questions about your data
- 💬 Natural language interface powered by Google Gemini
- 🎯 Smart feedback system to improve responses
- 🔍 RAG-based query enhancement using historical feedback

## How to Use

1. **Upload Tab**: Upload your CSV file (and optionally a text file describing your columns)
2. **Chat Tab**: Ask questions about your dataset in plain English
3. **Feedback**: Rate responses to help improve the bot

## Example Questions

- "What are the column names in the dataset?"
- "Show me the first 5 rows"
- "What is the average of numerical columns?"
- "How many rows are in the dataset?"

# Steps to run locally:
1. cd to the project directory
2. Run the command 'pip install -r requirements.txt'
3. Create a .env file with your API key: `GEMINI_API_KEY=your_key_here`
4. Run the command 'python app.py'

# Environment variables
For deployment, set these in your Hugging Face Space settings:
- GEMINI_API_KEY (required)
- LANGCHAIN_ENDPOINT (optional)
- LANGCHAIN_API_KEY (optional)
- LANGCHAIN_PROJECT (optional)