Usage
=====

1. Open the Streamlit UI in your browser.
2. Enter text into the input box and click the "Analyze" button.
3. View the emotion and gibberish analysis results.
4. Explore the logged data and visualize trends using the provided charts.

Tabs
----

The application consists of three main tabs:

1. **Text Analysis Tab**:
   - This tab provides a user interface to input text for analysis.
   - Users can enter text into the input box and click the "Analyze" button.
   - The text is sent to the server using a POST request, and the analysis results are retrieved using a GET request.
   - The results include emotion scores and gibberish detection, which are displayed on the UI.

2. **Database Tab**:
   - This tab displays the database contents with various filters to facilitate convenient analysis.
   - Users can view the complete log of inputs and outputs of the model.
   - Filters allow users to narrow down the data based on specific criteria, making it easier to analyze trends and patterns.

3. **Graphical Analysis Tab**:
   - This tab provides graphical visualizations of the analysis results.
   - Users can navigate between different graphs using navigation buttons.
   - The available graphs include:
     - **Emotion Scores Over Time**: A line chart showing how emotion scores change over time. Users can filter by a particular emotion to analyze its score over time, helping to identify when certain emotions peak.
     - **Gibberish Scores Over Time**: A line chart tracking gibberish scores over time, allowing users to observe trends in gibberish content.
     - **Emotion Label Distribution**: A pie chart displaying the distribution of different emotion labels found in the text inputs.
     - **Gibberish Label Distribution**: A pie chart showing the distribution of gibberish detection results.

Visualization Options
---------------------
- **Emotion Scores Over Time**: Line chart showing how emotion scores change over time. Users can filter by a particular emotion to analyze its score over time, helping to identify when certain emotions peak.
- **Gibberish Scores Over Time**: Line chart tracking gibberish scores over time, allowing users to observe trends in gibberish content.
- **Emotion Label Distribution**: Pie chart displaying the distribution of different emotion labels found in the text inputs.
- **Gibberish Label Distribution**: Pie chart showing the distribution of gibberish detection results.