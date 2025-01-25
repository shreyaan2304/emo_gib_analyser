import streamlit as st
import requests
import pandas as pd
import sqlite3
import os
from plots import emotion_ts, gibberish_ts, emotional_ld_bar, gibberish_ld_pie
import time
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)


st.set_page_config(page_title='Emotion and Gibberish Analyser', layout='wide')
# Path for the server
API_URL_POST = "http://api:8000/analyze"
API_URL_GET = "http://api:8000/fetch_records"

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    modify = st.checkbox("Add filters")

    if not modify:
        return df
    df = df.copy()
    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            # Treat columns with < 20 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 20:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    return df

def fetch_database_records():
    # Fetch records from the FastAPI server using a GET request.
    try:
        response = requests.get(API_URL_GET)
        # st.write(response.status_code)
        if response.status_code == 200:
            # st.write(response.json())
            records = pd.DataFrame(response.json())
            return records
        else:
            st.error(f"Error fetching records: {response.status_code}")
            return pd.DataFrame()
    
    except Exception as e:
        st.error(f"Error fetching records: {e}")
        return pd.DataFrame()

def main():
    sections = [
        'Input Section',
        'Data Repository',
        'Visual Insights'
    ]
    st.title("Emotion and Gibberish Analyser")
    tab1, tab2, tab3 = st.tabs(sections)
    # User Input Section
    with tab1:
        text = st.text_area("Enter text here", height=150)
        
        if st.button("Analyze"):
            if text:
                response = requests.post(API_URL_POST, json={"text": text})
                # st.write(response.json())
                if response.status_code == 200:
                    result = response.json()
                    # st.write(result['emotion'])
                    st.subheader("Results:")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader('Emotion Analysis')
                        emotion_scores = result['emotion']
                        cols_e1, cols_e2 = st.columns(2)
                        cols_e1.metric('Score', round(emotion_scores[0]['score'], 2))
                        cols_e2.metric('Label', emotion_scores[0]['label'])

                    with col2:
                        st.subheader("Gibberish Analysis:")
                        gibberish_scores = result['gibberish']
                        cols_g1, cols_g2 = st.columns(2)
                        cols_g1.metric('Score', round(gibberish_scores[0]['score'], 2))
                        cols_g2.metric('Label', gibberish_scores[0]['label'])

                    with st.expander('JSON Output'):
                        st.json(result)
                else:
                    st.error("Error: Unable to analyze the text.")
            else:
                st.warning("Please enter some text to analyze.")

    # Fetching the Database using the GET Request
    records = fetch_database_records()

    # Data Repository Section
    with tab2:
        st.subheader("Logged Database Records:")
        if not records.empty:
            st.dataframe(filter_dataframe(records), width=2000)
        else:
            st.info("No records found in the database.")
    
    # Visualization Section
    with tab3:
        graph_type = st.selectbox("Select a graph to display", 
                            ["Emotion Scores Over Time", 
                            "Gibberish Scores Over Time", 
                            "Emotion Label Distribution", 
                            "Gibberish Label Distribution"])

        if graph_type == "Emotion Scores Over Time":
            emotion_ts(records)
        elif graph_type == "Gibberish Scores Over Time":
            gibberish_ts(records)
        elif graph_type == "Emotion Label Distribution":
            emotional_ld_bar(records)
        elif graph_type == "Gibberish Label Distribution":
            gibberish_ld_pie(records)

if __name__ == "__main__":
    main()
