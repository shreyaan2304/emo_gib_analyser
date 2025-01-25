Setup Instructions
==================

Prerequisites
-------------
- **Python 3.8 or higher**: Ensure you have Python installed. You can download it from the `official Python website <https://www.python.org/>`_.
- **Virtual environment (optional, but recommended)**: Using a virtual environment helps manage dependencies and avoid conflicts. You can create one using `venv` or `virtualenv`.

Docker Run
----------

Follow these steps to set up and run the application using Docker:

Step 1: Build and Start the Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use Docker Compose to build and start the application:

.. code-block:: bash

    docker-compose build
    docker-compose up

This will build the Docker images and start the containers for the backend and frontend services.

Step 2: Access the Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- The FastAPI backend will be available at ``http://0.0.0.0:8000``.
- The Streamlit frontend will be available at ``http://0.0.0.0:8501``.

Step 3: Stop the Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To stop the application and remove the containers, run:

.. code-block:: bash

    docker-compose down


Run Locally
-----------

Follow these steps to set up and run the application locally:

Step 1: Clone the Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clone the project repository to your local machine and navigate into the project directory:

.. code-block:: bash

    git clone <repository_url>
    cd <repository_directory>

Replace ``<repository_url>`` with the actual URL of the repository and ``<repository_directory>`` with the name of the directory created by cloning the repository.

Step 2: Install Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Install all the required Python packages listed in the ``requirements.txt`` file using ``pip``:

.. code-block:: bash

    cd api
    pip install -r requirements.txt
    cd ..
    cd ui
    pip install -r requirements.txt
    cd ..

This command will install all the necessary libraries and dependencies needed for the project.

Step 3: Set Up the Database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Run the database setup script to create the SQLite database. If you want to create you own new database.
.. code-block:: bash

    cd database
    rm logs.db
    python db_setup.py

This script will create a ``logs.db`` file with the required schema in the ``database`` directory. This database will store user inputs and analysis results. The rm logs.db will remove the already present database file.

Step 4: Start the Backend API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Navigate to the ``api`` folder and start the FastAPI application using ``uvicorn``:

.. code-block:: bash

    cd ../api
    uvicorn main:app --reload --host 0.0.0.0 --port 8000

The ``--reload`` flag enables auto-reloading of the server on code changes. The API will be accessible at ``http://localhost:8000``.

Step 5: Start the Frontend UI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Navigate to the ``ui`` folder and run the Streamlit application:

.. code-block:: bash

    cd ../ui
    streamlit run app.py

This command will start the Streamlit server, and the UI will open in your default web browser. You can interact with the application through this interface.

