import os
import pandas as pd
import numpy as np
from datetime import datetime


class IlmateenistusProcessor:

    def __init__(self, filename):
        self.__filename = filename

    def process_ilmateenistus_data(self):
        df = pd.read_excel(os.path.join("data", "raw", self.__filename), header=1)
        df.drop(columns=["Tunni miinimum õhutemperatuur °C", "Tunni maksimum õhutemperatuur °C",
                         "10 minuti keskmine tuule suund", "Tunni maksimum tuule kiirus m/s",
                         "Õhurõhk jaama kõrgusel hPa"], inplace=True)
        df = df[df["Aasta"] >= 2013]
        df.rename(columns={"Õhurõhk merepinna kõrgusel hPa": "Õhurõhk (hPa)",
                           "10 minuti keskmine tuule kiirus m/s": "Tuule kiirus (m/s)",
                           "Tunni sademete summa mm": "Sademed (mm)", "Kell (UTC)": "UTC"}, inplace=True)

        # TODO
        #  - think what to do with nan values ("Õhurõhk" and "Tuule kiirus")
        #  - combine Aasta, Kuu, Päev into "Date" in format dd-MM-yyyy
        #       something that i tried but did not work:
        #           df["Date"] = df.Aasta + "-" + df.Kuu + "-" + df.Päev + " " + df.UTC
        #           df.Date = datetime.strptime(df.Date, "%Y-%m-%d %I:%M:%S")
        print(df)  # remove this when done
        new_file_name = "ilmateenistus.csv"
        df.to_csv(os.path.join("data", "processed", new_file_name), index=False)
        print(f"Ilmateenistus data written to file: {new_file_name}")


if __name__ == '__main__':
    # changing the working directory to src
    os.chdir("..")
    IlmateenistusProcessor("Tartu-Toravere_2004-2020.xlsx").process_ilmateenistus_data()
