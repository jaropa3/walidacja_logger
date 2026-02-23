import pandas as pd
from pathlib import Path
from config import FILE_PATH

def open_file():
    return Path(FILE_PATH)

def read_input(file_path: Path):
    
    df = pd.read_csv(file_path)
    return df