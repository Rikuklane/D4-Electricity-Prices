import os
import json
import locale
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from functools import reduce


class NordpoolDataProcessor:

    def combine_nordpool_data(self):
        """
        Method that combines all nordpool data files in urls.json into one csv file
        """
        locale.setlocale(locale.LC_NUMERIC, '')
        # variables
        raw_dataframes = {}
        features = []
        json_path = os.path.join("data", "urls.json")

        # getting data from files
        with open(json_path) as json_data:
            # opening json
            url_data = json.load(json_data)
            # looking through each feature in nordpool data in the json
            for feature_data in url_data["nordpool"]:
                # Appending all feature names into a list of features to later search them in the dictionary
                feature_name = feature_data["feature"]
                raw_dataframes[feature_name] = []
                features.append(feature_name)
                for data_file in feature_data["files"]:
                    # Looking through a file in the feature and appending to the feature dataframe list
                    df = self.__process_files_nordpool(data_file["filename"], feature_name)
                    raw_dataframes[feature_name].append(df)
                print(f"Feature {feature_name} factored!")

        # concatenating dataframes with same column names
        combined_dataframes = []
        for i in range(len(features)):
            feature_df = pd.concat(raw_dataframes[features[i]])
            if feature_df[features[i]].dtype == object:
                # making sure the decimal is "."
                feature_df[features[i]] = feature_df[features[i]].str.replace(',', '.')
            combined_dataframes.append(feature_df)
            print(f"All dataframes with feature {features[i]} combined!")

        # merging dataframes with different column names
        final_df = reduce(lambda df_left, df_right: pd.merge(df_left, df_right, on=["Date", "Hours"], how='outer'),
                          combined_dataframes).fillna(np.nan)
        final_df.Hours = final_df.Hours.map(lambda x: str(x)[0:2] + ":00:00")  # replacing Hour format
        final_df['Date'] = pd.to_datetime(final_df['Date'])
        final_df.rename(columns={"Hours": "Time"}, inplace=True)
        # writing to file
        file_name = "nordpool_estonia.csv"
        final_df.to_csv(os.path.join("data", "processed", file_name), index=False)
        print(f"Nordpool data written to file: {file_name}")

    @staticmethod
    def __process_files_nordpool(file_name, feature_name) -> pd.DataFrame:
        """
        A method that processes a nordpool data file in data/raw/ into a dataframe
        :param file_name: the file name in data/raw/
        :param feature_name: the feature we are currently working on
        :return: pandas DataFrame of formatted data
        """
        data = []

        # getting the correct path of the file and opening it open
        path = os.path.join("data", "raw", file_name)
        soup = BeautifulSoup(open(path), 'html.parser')

        # for getting the header (row of column names) from the HTML file
        list_header = []
        header = soup.find("table").find("thead").find("tr").findNextSibling().findNextSibling()

        # getting each column name
        for items in header:
            try:
                list_header.append(items.get_text())
            except AttributeError:
                continue

        # finding the data part
        html_data = soup.find("table").find("tbody").find_all("tr")

        # extracting the data from each html row
        for html_data_row in html_data:
            row = []
            # getting each column in each row
            for html_data_column in html_data_row:
                try:
                    row.append(html_data_column.get_text())
                except AttributeError:
                    continue
            data.append(row)  # appending the row to the data list

        # Storing the data into Pandas DataFrame and filtering out unnecessary columns
        list_header[1] = "Date"
        df = pd.DataFrame(data=data, columns=list_header)
        df = df[["Date", "Hours", "EE"]]
        df.rename(columns={"EE": feature_name}, inplace=True)
        if len(df.columns) > 3:
            # Because some columns have the same names and part of data is in one column and other part in the other
            return df.groupby(df.columns, axis=1).sum()
        return df


if __name__ == '__main__':
    # changing the working directory to src
    os.chdir("..")
    # running the code
    NordpoolDataProcessor().combine_nordpool_data()
