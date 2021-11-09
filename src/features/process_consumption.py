import pandas as pd
import os
from pathlib import Path


df = pd.read_excel("../../src/data/raw/consumption-per-country_2021_hourly.xls")
df.drop(df.columns.difference(['Hours', 'EE']), 1, inplace=True)
writer = pd.ExcelWriter('output.xls')

df.to_excel(writer, "../../src/data/processed/consumption-per-country_2021_processed.xls")
writer.save()
