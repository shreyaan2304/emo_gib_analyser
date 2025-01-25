Features
========

Text Analysis
-------------
- Detects emotions in text using a pre-trained RoBERTa model (`SamLowe/roberta-base-go_emotions <https://huggingface.co/SamLowe/roberta-base-go_emotions>`_).
  - The model is fine-tuned for emotion detection and can identify a wide range of emotions in the input text.
- Identifies gibberish using a custom gibberish text detection model (`wajidlinux99/gibberish-text-detector <https://huggingface.co/wajidlinux99/gibberish-text-detector>`_).
  - The gibberish detection model is trained to distinguish between meaningful text and nonsensical or random sequences of characters.

Data Storage
------------
- Logs user inputs and analysis results into an SQLite database.
  - The database stores raw text inputs, processed results, and timestamp for efficient retrieval and analysis.

Visualization
-------------
- Displays trends and distributions of analysis results using interactive charts (Plotly).
  - Interactive line charts show how emotion and gibberish scores change over time.
  - Pie charts visualize the distribution of different emotion labels and gibberish detection results.

Web UI
------
- A user-friendly interface built with Streamlit for submitting text and exploring logged data.
  - The UI provides an input box for users to submit text for analysis.
  - Analysis results are displayed dynamically, allowing users to see the emotional tone and gibberish content of their inputs.
  - Users can explore logged data and visualize trends using interactive charts.