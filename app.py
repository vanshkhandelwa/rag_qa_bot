import gradio as gr
import os
import shutil
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent))

from backend.main import PandasGptAgent, setup_logging
from vector_db.vector_db import FeedbackDB
import logging

logger = logging.getLogger("Pandas_agent")

setup_logging()

agent_class = PandasGptAgent()
feedback_db = FeedbackDB(positive_feedback_file='positive_feedback.db', negative_feedback_file='negative_feedback.db')
agent = None
last_prompt = None
last_response = None

def on_submit(csv_file, desc_file):
    global agent, csv_path, desc_path
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    if csv_file is not None:
        csv_path = os.path.join("data", os.path.basename(csv_file.name))
        shutil.copy(csv_file.name, csv_path)

    if desc_file is not None:
        desc_path = os.path.join("data", os.path.basename(desc_file.name))
        shutil.copy(desc_file.name, desc_path)
    
    try:
        agent = agent_class.create_agent(csv_path, desc_path, "")
        return "Files uploaded successfully! You can now go to the Chat tab."
    except Exception as e:
        logger.error(f"Error creating agent: {e}")
        return f"Error: {str(e)}"

def on_feedback(feedback_type):
    global last_prompt, last_response
    if last_prompt and last_response:
        query = last_prompt
        chain_of_thought = ""
        feedback_db.add_feedback(query, last_response, chain_of_thought, feedback_type)
        logger.info("Feedback added")
        return "Feedback recorded! Thank you."
    return "No feedback to record"

def chat_prompt_new(prompt, history):
    global last_prompt, last_response, agent
    
    if agent is None:
        return "Please upload a CSV file first in the Upload tab!"
    
    try:
        pos_results, neg_results = feedback_db.search_similar_queries(prompt)
        last_prompt = prompt
        extended_prompt = (
            f"{agent_class.create_prompt_RAG_samples(pos_results, neg_results)}\n Query: {prompt}"
        )
        response = agent_class.chat_prompt(extended_prompt, agent)
        last_response = response
        return response
    except Exception as e:
        logger.error(f"Error in chat: {e}")
        return f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 Pandas QA Bot")
    gr.Markdown("Upload your CSV dataset and ask questions about it using natural language!")
    
    with gr.Tab("📤 Upload"):
        gr.Markdown("### Upload your dataset")
        csv_upload = gr.File(label="Upload CSV File", file_types=[".csv"])
        desc_upload = gr.File(label="Upload Column Descriptions (Text File - Optional)", file_types=[".txt"])
        submit_btn = gr.Button("Submit", variant="primary")
        upload_status = gr.Textbox(label="Status", interactive=False)
        
        submit_btn.click(on_submit, [csv_upload, desc_upload], upload_status)

    with gr.Tab("💬 Chat"):
        gr.Markdown("### Ask questions about your dataset")
        chat_interface = gr.ChatInterface(
            fn=chat_prompt_new,
            examples=[
                "What are the column names in the dataset?",
                "Show me the first 5 rows",
                "What is the average of numerical columns?",
                "How many rows are in the dataset?"
            ],
            title="",
            description="Type your question below"
        )
        
        with gr.Row():
            feedback_good = gr.Button("👍 Good Response", variant="secondary")
            feedback_bad = gr.Button("👎 Bad Response", variant="secondary")
        
        feedback_output = gr.Textbox(label="Feedback Status", interactive=False)
        
        feedback_good.click(lambda: on_feedback("positive"), outputs=feedback_output)
        feedback_bad.click(lambda: on_feedback("negative"), outputs=feedback_output)

if __name__ == "__main__":
    # Get port from environment variable (for Render deployment)
    port = int(os.environ.get("GRADIO_SERVER_PORT", 7860))
    server_name = os.environ.get("GRADIO_SERVER_NAME", "127.0.0.1")
    
    demo.launch(
        server_name=server_name,
        server_port=port,
        share=False
    )
