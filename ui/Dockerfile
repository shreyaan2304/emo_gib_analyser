FROM python:3.12
WORKDIR /app
COPY . /app
#Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
# Command to run streamlit app
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]