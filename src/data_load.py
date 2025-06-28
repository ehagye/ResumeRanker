import zipfile
import pandas as pd

def extract_zip(zip_path, extract_to):
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

def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

        