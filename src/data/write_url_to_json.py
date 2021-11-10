import json


def write_urls_to_json(start_year=2016, end_year=2021):
    # variables
    data = {"nordpooldata": []}
    elspot_prices = []
    consumption = []

    # creating file data
    for year in range(start_year, end_year + 1):
        elspot_prices.append({
            "url": f"https://www.nordpoolgroup.com/4ab6cc/globalassets/marketdata-excel-files/elspot-prices_{year}_hourly_eur.xls",
            "filename": f"elspot-prices_{year}_hourly_eur.xls"
        })
        consumption.append({
            "url": f"https://www.nordpoolgroup.com/4a742e/globalassets/marketdata-excel-files/consumption-per-country_{year}_hourly.xls",
            "filename": f"consumption-per-country_{year}_hourly.xls"
        })

    # appending file data to a feature
    data["nordpooldata"].append({
        'feature': "elspot_price",
        'files': elspot_prices
    })
    data["nordpooldata"].append({
        'feature': "consumption",
        'files': consumption
    })

    # writing to json
    with open('urls.json', 'w') as file:
        json_string = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=2)
        file.write(json_string)


if __name__ == '__main__':
    write_urls_to_json()
