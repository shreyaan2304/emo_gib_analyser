from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from datetime import datetime
import sqlite3
import os
import pandas as pd

app = FastAPI()

# Load models
emotion_model = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")
gibberish_model = pipeline("text-classification", model="wajidlinux99/gibberish-text-detector")

# Use this to run locally
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DB_PATH = os.path.join(BASE_DIR, 'database', 'logs.db')

# Use this to run through docker
DB_PATH = '/app/logs.db'

# Pydantic Model for a text request
class TextRequest(BaseModel):
    text: str

# Post request for the server
@app.post("/analyze")
async def analyze_text(request: TextRequest):
    # calculating the scores using the Hugging Face model
    text = request.text
    emotion_scores = emotion_model(text)
    gibberish_scores = gibberish_model(text)

    print('Data sent to server')

    # Connect and save to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO logs (input_text, emotion_scores, gibberish_scores) VALUES (?, ?, ?)",
              (text, str(emotion_scores), str(gibberish_scores)))
    conn.commit()
    conn.close()

    # Returns the scores to the UI for the request
    return {"emotion": emotion_scores, "gibberish": gibberish_scores}

# Get request from the server database
@app.get("/fetch_records")
async def fetch_records():
    """Fetch all records from the logs database."""
    try:
        # Connect to the database and get the data
        conn = sqlite3.connect(DB_PATH)
        query = "SELECT id, input_text, emotion_scores, gibberish_scores, timestamp FROM logs"
        records = pd.read_sql_query(query, conn)
        conn.close()
        
        # Converting string to dictionaries
        emotion_data = records['emotion_scores'].apply(eval)  
        gibberish_data = records['gibberish_scores'].apply(eval)  

        # Extract the label and score from each list
        records['emotion_label'] = emotion_data.apply(lambda x: x[0]['label'] if x else None)
        records['emotion_score'] = emotion_data.apply(lambda x: x[0]['score'] if x else None)
        records['gibberish_label'] = gibberish_data.apply(lambda x: x[0]['label'] if x else None)
        records['gibberish_score'] = gibberish_data.apply(lambda x: x[0]['score'] if x else None)

        formatted_records = records[['input_text', 'emotion_label', 'emotion_score',
                                     'gibberish_label', 'gibberish_score', 'timestamp']]
        
        return formatted_records.to_dict(orient="records")  
    
    except Exception as e:
        print('Error in the GET request')
        return {"error": f"Error fetching database records: {e}"}