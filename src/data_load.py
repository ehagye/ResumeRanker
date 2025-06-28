from pathlib import Path
import zipfile
import pandas as pd

# getting root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Defining relative paths
RAW_DATA_PATH = PROJECT_ROOT / 'data' / 'raw' / 'ResumeData.zip'
INTERIM_PATH = PROJECT_ROOT / 'data' / 'interim'
CSV_PATH = INTERIM_PATH / 'AI_Resume_Screening.csv'

# Extracting the raw data zip file to a csv in interim file
def extract_zip(zip_path=RAW_DATA_PATH, extract_to=INTERIM_PATH):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Extracted '{zip_path}' to '{extract_to}'")
    except FileNotFoundError:
        print(f"File not found: '{zip_path}'. Make sure the path is correct.")
    except zipfile.BadZipFile:
        print(f"Bad zip file: '{zip_path}' is not a valid zip file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# loads csv file and returns a pandas DataFrame
def load_csv(file_path=CSV_PATH):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

        