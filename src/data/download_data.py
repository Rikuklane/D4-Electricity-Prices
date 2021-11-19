import json
import requests
import os


class DataDownloader:

    @staticmethod
    def __download_file(url, filename):
        print('Downloading from {} to {}'.format(url, filename))
        response = requests.get(url)
        if response.status_code == 200:
            print("Download successful")
        else:
            print(f"Something fishy! Status code: {response.status_code}")
        with open(filename, 'wb') as file:
            file.write(response.content)

    @staticmethod
    def download_nordpool_data():
        print("fetching data...")
        with open('urls.json') as json_data:
            url_data = json.load(json_data)
            for nordpool_data in url_data["nordpooldata"]:
                for data_file in nordpool_data["files"]:
                    DataDownloader.__download_file(data_file["url"], os.path.join("raw", data_file["filename"]))


if __name__ == '__main__':
    DataDownloader.download_nordpool_data()
