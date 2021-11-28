import json
import requests
import os


class DataDownloader:

    @staticmethod
    def __download_file(url, filename):
        """
        A method that downloads the given file
        :param url: the url from where to download the file
        :param filename: the name the file is going to be saved as
        """
        print('Downloading from {} to {}'.format(url, filename))
        response = requests.get(url)
        if response.status_code == 200:
            print("Download successful")
        else:
            print(f"Something fishy! Status code: {response.status_code}")
            print(f"Failed file '{filename}' with url: {url}")
        with open(filename, 'wb') as file:
            file.write(response.content)

    def download_nordpool_data(self):
        """
        A method to download all the data from nordpool using urls.json
        """
        print("fetching data...")
        with open(os.path.join('data', 'urls.json')) as json_data:
            url_data = json.load(json_data)
            for nordpool_data in url_data["nordpool"]:
                for data_file in nordpool_data["files"]:
                    self.__download_file(data_file["url"], os.path.join("data", "raw", data_file["filename"]))


if __name__ == '__main__':
    os.chdir("../src")
    DataDownloader().download_nordpool_data()