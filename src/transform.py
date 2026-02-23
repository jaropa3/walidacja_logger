import pandas as pd
import logging
from logging_config import setup_logging

logger = logging.getLogger(__name__)

def validacja(df):
    
    required_columns = ["Data", "Opis", "Kwota"]
    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"Brak wymaganego nagłówka: {col}")
           # logger.info("Brak wymaganego nagłówka")
        if df['Data'].isnull().any():
            empty_dates = df[df['Data'].isnull()]
            print("ERROR: Puste daty w wierszach:")
            logger.error("Brak wymaganego nagłówka")
            print(empty_dates)
    
    # 3. Sprawdzenie ujemnych kwot
        if df['Kwota'].lt(0).any():
            negative_amounts = df[df['Kwota'] < 0]
            print("WARNING: Ujemne kwoty w wierszach:")
        print(negative_amounts)
    
