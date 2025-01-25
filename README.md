# emo_gib_analyser
Emotion and Gibberish Analyzer is a Python-based tool designed to analyze text for emotional sentiment and detect gibberish content.

# Text Analysis Application

## Introduction
This project is a full-stack application designed to analyze the emotional tone and gibberish content of text inputs. The backend is built using FastAPI, a high-performance web framework for building APIs with Python. FastAPI handles the core logic for text analysis, utilizing Hugging Face open-source models to determine emotional tone and detect gibberish. The frontend is developed with Streamlit, an open-source app framework that allows for the creation of interactive web applications. Streamlit provides a user-friendly interface for text input and displays the analysis results dynamically. Data is stored in SQLite, a lightweight, disk-based database that efficiently manages and retrieves user inputs and analysis results. The workflow involves users entering text into the Streamlit interface, which sends the input to the FastAPI backend for processing. The results are then stored in SQLite and displayed back to the user through the Streamlit frontend, ensuring a seamless and interactive user experience.

## Project Structure
.
├── api
│   ├── main.py         # Backend API using FastAPI
├── database
│   ├── db_setup.py     # SQLite database setup script
│   ├── logs.db         # SQLite database file
├── ui
│   ├── app.py          # Streamlit application for the UI
│   ├── plots.py        # Visualization functions using Plotly
├── requirements.txt    # Dependencies management file
├── docs                # Documentation using sphinx
└── README.md           # Project documentation


## Setup Instructions

### Prerequisites
- **Python 3.8 or higher**: Ensure you have Python installed. You can download it from the official Python website.
- **Virtual environment (optional, but recommended)**: Using a virtual environment helps manage dependencies and avoid conflicts. You can create one using `venv` or `virtualenv`.

### Docker Run
Follow these steps to set up and run the application using Docker:

#### Step 1: Build and Start the Application
Use Docker Compose to build and start the application:
```bash
docker-compose build
docker-compose up
This will build the Docker images and start the containers for the backend and frontend services.

Step 2: Access the Application
The FastAPI backend will be available at http://0.0.0.0:8000.
The Streamlit frontend will be available at http://0.0.0.0:8501.
Step 3: Stop the Application
To stop the application and remove the containers, run:

docker-compose down
Run Locally
Follow these steps to set up and run the application locally:

Step 1: Clone the Repository
Clone the project repository to your local machine and navigate into the project directory:

git clone <repository_url>
cd <repository_directory>
Replace <repository_url> with the actual URL of the repository and <repository_directory> with the name of the directory created by cloning the repository.

Step 2: Install Dependencies
Install all the required Python packages listed in the requirements.txt file using pip:

cd api
pip install -r requirements.txt
cd ..
cd ui
pip install -r requirements.txt
cd ..
This command will install all the necessary libraries and dependencies needed for the project.

Step 3: Set Up the Database
Run the database setup script to create the SQLite database. If you want to create your own new database:

cd database
rm logs.db
python db_setup.py
This script will create a logs.db file with the required schema in the database directory. This database will store user inputs and analysis results. The rm logs.db will remove the already present database file.

Step 4: Start the Backend API
Navigate to the api folder and start the FastAPI application using uvicorn:

cd ../api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
The --reload flag enables auto-reloading of the server on code changes. The API will be accessible at http://localhost:8000.

Step 5: Start the Frontend UI
Navigate to the ui folder and run the Streamlit application:

cd ../ui
streamlit run app.py
This command will start the Streamlit server, and the UI will open in your default web browser. You can interact with the application through this interface.

Usage
Open the Streamlit UI in your browser.
Enter text into the input box and click the “Analyze” button.
View the emotion and gibberish analysis results.
Explore the logged data and visualize trends using the provided charts.
Tabs
The application consists of three main tabs:

Text Analysis Tab
Provides a user interface to input text for analysis.
Users can enter text into the input box and click the “Analyze” button.
The text is sent to the server using a POST request, and the analysis results are retrieved using a GET request.
The results include emotion scores and gibberish detection, which are displayed on the UI.
Database Tab
Displays the database contents with various filters to facilitate convenient analysis.
Users can view the complete log of inputs and outputs of the model.
Filters allow users to narrow down the data based on specific criteria, making it easier to analyze trends and patterns.
Graphical Analysis Tab
Provides graphical visualizations of the analysis results.
Users can navigate between different graphs using navigation buttons.
The available graphs include:
Emotion Scores Over Time: A line chart showing how emotion scores change over time. Users can filter by a particular emotion to analyze its score over time, helping to identify when certain emotions peak.
Gibberish Scores Over Time: A line chart tracking gibberish scores over time, allowing users to observe trends in gibberish content.
Emotion Label Distribution: A pie chart displaying the distribution of different emotion labels found in the text inputs.
Gibberish Label Distribution: A pie chart showing the distribution of gibberish detection results.
Features
Text Analysis
Detects emotions in text using a pre-trained RoBERTa model (SamLowe/roberta-base-go_emotions).
The model is fine-tuned for emotion detection and can identify a wide range of emotions in the input text.
Identifies gibberish using a custom gibberish text detection model (wajidlinux99/gibberish-text-detector).
The gibberish detection model is trained to distinguish between meaningful text and nonsensical or random sequences of characters.
Data Storage
Logs user inputs and analysis results into an SQLite database.
The database stores raw text inputs, processed results, and timestamps for efficient retrieval and analysis.
Visualization
Displays trends and distributions of analysis results using interactive charts (Plotly).
Interactive line charts show how emotion and gibberish scores change over time.
Pie charts visualize the distribution of different emotion labels and gibberish detection results.
Web UI
A user-friendly interface built with Streamlit for submitting text and exploring logged data.
The UI provides an input box for users to submit text for analysis.
Analysis results are displayed dynamically, allowing users to see the emotional tone and gibberish content of their inputs.
Users can explore logged data and visualize trends using interactive charts.
