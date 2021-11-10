import os
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from functools import reduce


def combine_nordpool_data():
    # combine all dataframes here
    # can use concat with list of dataframes with same columns
    # and then merge when two dataframes need to be combined with different columns
    raw_dataframes = {}
    features = []
    json_path = get_data_file_location("urls.json", folder="")

    # getting data from files
    with open(json_path) as json_data:
        url_data = json.load(json_data)
        for nordpool_data in url_data["nordpooldata"]:
            feature = nordpool_data["feature"]
            raw_dataframes[feature] = []
            features.append(feature)
            for data_file in nordpool_data["files"]:
                df = process_files_nordpool(data_file["filename"], feature)
                raw_dataframes[nordpool_data["feature"]].append(df)

    combined_dataframes = []
    for i in range(len(features)):
        combined_dataframes.append(pd.concat(raw_dataframes[features[i]]))

    final_df = reduce(lambda df_left, df_right: pd.merge(df_left, df_right, on=["Date", "Hours"], how='outer'),
                      combined_dataframes).fillna(np.nan)
    final_df.to_csv(get_data_file_location("nordpool_estonia.csv", folder="processed"), index=False)


def process_files_nordpool(file_name, feature_name):
    path = get_data_file_location(file_name)

    data = []

    # for getting the header from the HTML file
    list_header = []
    soup = BeautifulSoup(open(path), 'html.parser')
    header = soup.find("table").find("thead").find("tr").findNextSibling().findNextSibling()

    for items in header:
        try:
            list_header.append(items.get_text())
        except AttributeError:
            continue

    html_data = soup.find("table").find("tbody").find_all("tr")

    for element in html_data:
        sub_data = []
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except AttributeError:
                continue
        data.append(sub_data)

    # Storing the data into Pandas DataFrame
    list_header[0] = "Date"
    df = pd.DataFrame(data=data, columns=list_header)
    df.Hours = df.Hours.str.replace("\\xa0", " ")
    df = df[["Date", "Hours", "EE"]]
    df.rename(columns={"EE": feature_name}, inplace=True)
    if len(df.columns) > 3:
        # because some columns are multiplied in some datasets
        return df.groupby(df.columns, axis=1).sum()
    return df


def get_data_file_location(file_name, folder="raw"):
    if folder != "":
        return os.path.join(os.getcwd(), "data", folder, file_name)
    return os.path.join(os.getcwd(), "data", file_name)


if __name__ == '__main__':
    # changing the working directory to src
    os.chdir("..")
    # running the code
    combine_nordpool_data()

    # THIS BELOW IS HOW DATA FROM NORDPOOL SHOULD BE READ
    # processed_df = pd.read_csv(get_data_file_location("nordpool_estonia.csv", folder="processed"), decimal=",")
