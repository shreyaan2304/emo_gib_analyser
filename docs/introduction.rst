Introduction
============

This project is a full-stack application designed to analyze the emotional tone and gibberish content of text inputs. The backend is built using FastAPI, a high-performance web framework for building APIs with Python. FastAPI handles the core logic for text analysis, utilizing huggingface open source models to determine emotional tone and detect gibberish. The frontend is developed with Streamlit, an open-source app framework that allows for the creation of interactive web applications. Streamlit provides a user-friendly interface for text input and displays the analysis results dynamically. Data is stored in SQLite, a lightweight, disk-based database that efficiently manages and retrieves user inputs and analysis results. The workflow involves users entering text into the Streamlit interface, which sends the input to the FastAPI backend for processing. The results are then stored in SQLite and displayed back to the user through the Streamlit frontend, ensuring a seamless and interactive user experience.

Project Structure
-----------------
.. code-block:: text

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