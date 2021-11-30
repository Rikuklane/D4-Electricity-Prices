import os
import json


class UrlWriter:

    def __init__(self, start_year, end_year):
        self.__start_year = start_year
        self.__end_year = end_year

    def __collect_nordpool_urls(self) -> list:
        """
        Method to collect all the used datafile urls from www.nordpoolgroup.com into urls.json
        :return: formated data for urls.json
        """
        # variables
        data = []
        elspot_prices = []
        consumption = []

        # creating file data
        for year in range(self.__start_year, self.__end_year + 1):
            elspot_prices.append({
                "url": f"https://www.nordpoolgroup.com/4ab6cc/globalassets/marketdata-excel-files/elspot-prices_{year}_hourly_eur.xls",
                "filename": f"elspot-prices_{year}_hourly_eur.xls"
            })
            consumption.append({
                "url": f"https://www.nordpoolgroup.com/4a742e/globalassets/marketdata-excel-files/consumption-per-country_{year}_hourly.xls",
                "filename": f"consumption-per-country_{year}_hourly.xls"
            })

        # appending file data to a feature
        data.append({
            'feature': "elspot_price",
            'files': elspot_prices
        })
        data.append({
            'feature': "consumption",
            'files': consumption
        })
        return data

    @staticmethod
    def __collect_ilmateenistus_url() -> dict:
        url = "https://www.ilmateenistus.ee/wp-content/uploads/2021/05/Tartu-Toravere_2004-2020.xlsx"
        return {"url": url, "filename": "Tartu-Toravere_2004-2020.xlsx"}

    def write_urls_to_json(self):
        """
        Method to get all the necessary datafile urls for every needed source
        """
        # getting different url data
        url_data = {"nordpool": self.__collect_nordpool_urls(),
                    "ilmateenistus": self.__collect_ilmateenistus_url()}

        # writing to json
        with open(os.path.join("data", "urls.json"), 'w') as file:
            json_string = json.dumps(url_data, default=lambda o: o.__dict__, sort_keys=True, indent=2)
            file.write(json_string)


if __name__ == '__main__':
    os.chdir("..")
    UrlWriter(2016, 2021).write_urls_to_json()
