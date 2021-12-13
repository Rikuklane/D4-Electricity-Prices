from data.delete_data import DataDeleter
from data.url_writer import UrlWriter
from data.download_data import DataDownloader
from features.process_nordpool import NordpoolDataProcessor
from features.process_ilmateenistus import IlmateenistusProcessor


def user_interaction(question: str, command):
    """
    Leaving the input fields empty is also counted as a yes
    :param question: the question to ask the user
    :param command: the command that should be ran if the answer is "yes"
    """
    while True:
        print(f"{question} ( Y / N )")
        answer = input().lower()
        if answer == "y" or answer == "":
            command()
            break
        elif answer == "n":
            break


# This method is not ready to be used yet (can only delete data currently)
if __name__ == '__main__':
    """
    This is the CLI for the project setup
    """
    # deleting data
    user_interaction("Clear all data?",
                     DataDeleter().clean_data)
    # writing urls into json
    user_interaction("Write to be fetched urls to json file?",
                     UrlWriter(2016, 2021).write_urls_to_json)
    # downloading raw data
    user_interaction("Download the data files located in urls.json?",
                     DataDownloader().download_nordpool_data)
    # processing nordpool data
    user_interaction("Factor the nordpool data into usable format for data engineering?",
                     NordpoolDataProcessor().combine_nordpool_data)
    # processing ilmateenistus data
    user_interaction("Factor the ilmateenistus data into usable format for data engineering?",
                     IlmateenistusProcessor("Tartu-Toravere_2004-2020.xlsx").process_ilmateenistus_data)

    print("All actions finished! Program will shutdown.")
