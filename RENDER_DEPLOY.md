# Deploy to Render.com

This guide will help you deploy your Pandas QA Bot to Render.com (FREE tier available).

## Prerequisites

1. A Render account (sign up at https://render.com)
2. Your GitHub repository with this code
3. A Google Gemini API key (get it from https://makersuite.google.com/app/apikey)

## Deployment Steps

### Option 1: One-Click Deploy (Easiest)

1. **Click the Deploy Button** (or follow manual steps below)
   
   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

2. **Connect Your Repository**
   - Sign in to Render
   - Click "New +" → "Web Service"
   - Connect your GitHub account
   - Select this repository: `vanshkhandelwa/rag_qa_bot`

3. **Configure Your Service**
   - **Name**: `pandas-qa-bot` (or your choice)
   - **Region**: Choose closest to you (Oregon for US West)
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Instance Type**: Select **Free**

4. **Add Environment Variables**
   - Click "Advanced" → "Add Environment Variable"
   - Add these variables:
     
     | Key | Value |
     |-----|-------|
     | `GEMINI_API_KEY` | Your Google Gemini API key |
     | `PYTHON_VERSION` | `3.10.0` |
     | `GRADIO_SERVER_NAME` | `0.0.0.0` |
     | `GRADIO_SERVER_PORT` | `10000` |

5. **Deploy**
   - Click "Create Web Service"
   - Wait for the build to complete (5-10 minutes)
   - Your app will be live at: `https://pandas-qa-bot.onrender.com`

### Option 2: Using render.yaml (Automated)

Your repository already has a `render.yaml` file configured!

1. **Go to Render Dashboard**: https://dashboard.render.com

2. **Click "New +" → "Blueprint"**

3. **Connect Repository**
   - Select your GitHub repository
   - Render will automatically detect the `render.yaml` file

4. **Add Environment Variable**
   - During setup, you'll be prompted to add `GEMINI_API_KEY`
   - Paste your Google Gemini API key

5. **Deploy**
   - Click "Apply"
   - Render will automatically deploy your app

### Option 3: Using Render CLI

```bash
# Install Render CLI
npm install -g render-cli

# Login to Render
render login

# Deploy
render deploy
```

## After Deployment

### Your App URL
Your app will be available at: `https://YOUR-APP-NAME.onrender.com`

### Free Tier Limitations
- App will spin down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds
- 750 hours/month of free runtime

### Upgrade to Keep Always On
- If you need the app to always be running, upgrade to paid plan ($7/month)

## Troubleshooting

### Build Fails
- Check the logs in Render dashboard
- Verify all dependencies are in `requirements.txt`
- Make sure Python version is compatible (3.10)

### App Not Responding
- Check if the app has spun down (free tier)
- View logs: Dashboard → Your Service → Logs
- Verify environment variables are set correctly

### Port/Connection Issues
- Render requires apps to bind to `0.0.0.0` on port `10000`
- This is already configured in `app.py`

### API Key Not Working
- Go to Dashboard → Your Service → Environment
- Verify `GEMINI_API_KEY` is set correctly
- No quotes needed in the value

## Updating Your App

Render automatically redeploys when you push to your `main` branch:

```bash
git add .
git commit -m "Update app"
git push origin main
```

Your app will automatically rebuild and redeploy!

## Monitoring

- **Logs**: Dashboard → Your Service → Logs
- **Metrics**: Dashboard → Your Service → Metrics
- **Health**: Render pings your app to keep it alive

## Cost

- **Free Tier**: Perfect for demos and testing
- **Starter ($7/month)**: Always on, better performance
- **Standard ($25/month)**: More resources, better for production

## Get Help

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- Status Page: https://status.render.com

---

**That's it!** Your Pandas QA Bot should now be live on Render! 🚀
