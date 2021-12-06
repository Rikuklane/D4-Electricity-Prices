import os
import pandas as pd


class IlmateenistusProcessor:

    def __init__(self, filename):
        self.__filename = filename

    def process_ilmateenistus_data(self):
        df = pd.read_excel(os.path.join("data", "raw", self.__filename), header=1)
        df.drop(columns=["Tunni miinimum õhutemperatuur °C", "Tunni maksimum õhutemperatuur °C",
                         "10 minuti keskmine tuule suund", "Tunni maksimum tuule kiirus m/s",
                         "Õhurõhk jaama kõrgusel hPa"], inplace=True)
        df = df[df["Aasta"] >= 2013]
        df.rename(columns={"Õhurõhk merepinna kõrgusel hPa": "AirPressure",
                           "10 minuti keskmine tuule kiirus m/s": "WindSpeed",
                           "Tunni sademete summa mm": "Precipitation",
                           "Suhteline õhuniiskus %": "AirHumidity",
                           "Õhutemperatuur °C": "Temperature",
                           "Kell (UTC)": "Time", "Aasta": "year", "Kuu": "month", "Päev": "day"}, inplace=True)

        df['Date'] = pd.to_datetime(df[["day", "month", "year"]])
        df.drop(columns=["year", "month", "day"], inplace=True)

        new_file_name = "ilmateenistus.csv"
        df.to_csv(os.path.join("data", "processed", new_file_name), index=False)
        print(f"Ilmateenistus data written to file: {new_file_name}")


if __name__ == '__main__':
    # changing the working directory to src
    os.chdir("..")
    IlmateenistusProcessor("Tartu-Toravere_2004-2020.xlsx").process_ilmateenistus_data()
