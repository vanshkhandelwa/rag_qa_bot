---
title: Pandas QA Bot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# Pandas QA Bot 🤖

An interactive question-answering bot powered by LangChain and Google Gemini that allows you to chat with your CSV datasets using natural language!

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
- "Who is the highest paying customer?"

## Setup for Local Development

1. Clone this repository
2. Create a `.env` file with your API keys:
   ```
   GEMINI_API_KEY=your_key_here
   LANGCHAIN_API_KEY=your_key_here (optional)
   LANGCHAIN_PROJECT=your_project_name (optional)
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Tech Stack

- **LangChain**: For building the conversational agent
- **Google Gemini**: For natural language understanding
- **Gradio**: For the web interface
- **Pandas**: For data manipulation
- **SQLite**: For storing user feedback

## Environment Variables

Set these in your Hugging Face Space settings:

- `GEMINI_API_KEY` (required): Your Google Gemini API key
- `LANGCHAIN_API_KEY` (optional): For LangSmith tracing
- `LANGCHAIN_PROJECT` (optional): Your LangSmith project name
- `LANGCHAIN_ENDPOINT` (optional): LangSmith endpoint URL

---

Built with ❤️ using LangChain and Gradio
