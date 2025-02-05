import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "sentimentanalysis"

list_of_files = [
    # Core project structure
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_preprocessing.py",  # Data cleaning and preprocessing
    f"src/{project_name}/components/feature_extraction.py",  # Feature extraction for sentiment analysis
    f"src/{project_name}/components/model_training.py",  # Model training for sentiment analysis
    f"src/{project_name}/components/evaluation.py",  # Model evaluation
    f"notebook/eda.ipynb",  # Exploratory data analysis
    f"notebook/sentiment_analysis.ipynb",  # Sentiment analysis notebook
    f"app/app.py",  # Application entry point
    f"app/index.html",  # Main webpage
    f"templates/index.html",  # HTML template for the app
    f"templates/result.html",  # Display sentiment analysis result
    f"templates/error.html",  # Error handling page

    # Unit test structure
    f"tests/test_data_preprocessing.py",  # Unit tests for preprocessing
    f"tests/test_feature_extraction.py",  # Unit tests for feature extraction
    f"tests/test_model_training.py",  # Unit tests for model training
    
    # DVC structure
    "dvc.yaml",  # Data version control configuration
    ".dvc/config",  # DVC configuration
    ".dvcignore",  # Files to be ignored by DVC
    "requirements.txt",  # List of project dependencies
    "setup.py",  # Setup script
    "logging.py",  # Logging configuration
    "custom_exception.py",  # Custom exception handling
    ".gitignore"  # Git ignore file
]

# Create the directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
