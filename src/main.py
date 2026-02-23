import pandas as pd
import logging
from config import FILE_PATH
from extract import open_file, read_input
from transform import validacja
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger()
logger.critical("Uruchomienie programu")

#df_data_path = open_file()
data = read_input(FILE_PATH)

data = validacja(data)
print(data)