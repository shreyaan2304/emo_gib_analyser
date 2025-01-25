import plotly.express as px
import streamlit as st
import pandas as pd

def emotion_ts(records):
    if not records.empty:
        # Convert timestamp to datetime
        records['timestamp'] = pd.to_datetime(records['timestamp'])
        unique_emotions = records['emotion_label'].unique()
        
        selected_emotions = st.multiselect(
            "Select Emotion Labels to Display", 
            options=unique_emotions, 
            default=unique_emotions
        )
        filtered_records = records[records['emotion_label'].isin(selected_emotions)]
        
        if not filtered_records.empty:
            fig = px.line(
                filtered_records, 
                x='timestamp', 
                y='emotion_score', 
                color='emotion_label', 
                title='Emotion Scores Over Time',
                markers=True,
                labels={
                    'timestamp': 'Timestamp', 
                    'emotion_score': 'Emotion Score', 
                    'emotion_label': 'Emotion Label'
                }
            )
            st.plotly_chart(fig)
        else:
            st.warning("No data available for the selected emotions.")
    else:
        st.info("No data available to display.")

def gibberish_ts(records):
    if not records.empty:
        records['timestamp'] = pd.to_datetime(records['timestamp'])
        unique_gibberish_labels = records['gibberish_label'].unique()
        
        selected_gibberish_labels = st.multiselect(
            "Select Gibberish Labels to Display", 
            options=unique_gibberish_labels, 
            default=unique_gibberish_labels
        )
        filtered_records = records[records['gibberish_label'].isin(selected_gibberish_labels)]
        
        if not filtered_records.empty:
            fig = px.line(
                filtered_records, 
                x='timestamp', 
                y='gibberish_score', 
                color='gibberish_label',
                title='Gibberish Scores Over Time',
                markers=True,
                labels={
                    'timestamp': 'Timestamp', 
                    'gibberish_score': 'Gibberish Score', 
                    'gibberish_label': 'Gibberish Label'
                }
            )
            st.plotly_chart(fig)
        else:
            st.warning("No data available for the selected gibberish labels.")
    else:
        st.info("No data available to display.")

def emotional_ld_bar(records):
    if not records.empty:
        label_counts = records['emotion_label'].value_counts()
        fig = px.pie(values=label_counts.values, names=label_counts.index,
                     title='Emotion Label Distribution')
        st.plotly_chart(fig)
    else:
        st.info("No data available to display.")

def gibberish_ld_pie(records):
    if not records.empty:
        label_counts = records['gibberish_label'].value_counts()
        fig = px.pie(values=label_counts.values, names=label_counts.index,
                     title='Gibberish Label Distribution')
        st.plotly_chart(fig)
    else:
        st.info("No data available to display.")
