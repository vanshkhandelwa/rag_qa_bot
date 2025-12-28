# Deployment Guide for Hugging Face Spaces

## Quick Deploy to Hugging Face Spaces

### Option 1: Using the Web Interface (Easiest)

1. **Create a new Space**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Name it (e.g., `pandas-qa-bot`)
   - Select SDK: **Gradio**
   - Choose visibility (Public/Private)
   - Click "Create Space"

2. **Upload your code**
   - Click "Files" tab in your new Space
   - Click "Add file" → "Upload files"
   - Upload all files from this project (or use git method below)

3. **Set up your API key**
   - Go to your Space's "Settings" tab
   - Scroll to "Repository secrets"
   - Click "New secret"
   - Name: `GEMINI_API_KEY`
   - Value: Your Google Gemini API key
   - Click "Add"

4. **Your app will automatically build and deploy!**
   - Check the "Logs" tab to see the build progress
   - Once complete, your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/pandas-qa-bot`

### Option 2: Using Git (Recommended for developers)

1. **Create a new Space on Hugging Face**
   - Follow step 1 from Option 1 above

2. **Add Hugging Face as a remote**
   ```bash
   git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/pandas-qa-bot
   ```

3. **Push your code**
   ```bash
   git push hf main
   ```

4. **Set up your API key**
   - Follow step 3 from Option 1 above

### Get Your Gemini API Key

1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API key"
3. Copy the key and add it to your Hugging Face Space secrets

### Optional: Enable LangSmith Tracing

If you want to debug and trace your LangChain calls:

1. Sign up at https://smith.langchain.com
2. Get your API key
3. Add these secrets to your Hugging Face Space:
   - `LANGCHAIN_TRACING_V2=true`
   - `LANGCHAIN_API_KEY=your_langsmith_key`
   - `LANGCHAIN_PROJECT=pandas-qa-bot`

### Troubleshooting

- **Build fails**: Check the "Logs" tab in your Space for error messages
- **Import errors**: Make sure all dependencies are in `requirements.txt`
- **API key not working**: Verify the secret name is exactly `GEMINI_API_KEY`
- **App not responding**: Check if your Space has enough resources (may need to restart)

### Testing Locally Before Deploy

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
cp .env.template .env
# Edit .env and add your GEMINI_API_KEY

# Run the app
python app.py
```

The app will open at http://localhost:7860

---

**Need help?** Check out the [Hugging Face Spaces documentation](https://huggingface.co/docs/hub/spaces-overview)
