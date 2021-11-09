
import json
import requests

def download_file(url, filename):
   print('Downloading from {} to {}'.format(url, filename))
   response = requests.get(url)
   print(response)
   with open(filename,  'wb') as ofile:
       ofile.write(response.content)
       ofile.close()


if __name__ == '__main__':
   print("fetching data...")
   with open('urls.json') as data_file:
      data = json.load(data_file)
      for nordpool_data in data["nordpooldata"]:
         download_file(nordpool_data["url"], nordpool_data["filename"])

