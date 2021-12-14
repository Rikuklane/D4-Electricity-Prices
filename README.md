# D4-Electricity-Prices
## Project Description
This project is made for the "Introduction to Data Science" subject as a mandatory project to finish the class successfully.

Subject: Why is electricity so expensive? NORDPOOL  
Reason: The electricity prices have tripled in recent months.

### Team members
 - Richard Kuklane
 - Georg Šumailov
 - Jakob Tamm

### Data
Data is fetched from
 - https://www.nordpoolgroup.com/historical-market-data/
 - https://www.ilmateenistus.ee/
 - https://finance.yahoo.com/

##### Ilmateenistus
 - AirPressure (hPa)
 - Temperature (°C)
 - Precipitation (mm)
 - WindSpeed (m/s)
 - AirHumidity (%)
 - DateTime (UTC)

##### Nordpool
 - DateTime (UTC+1)
 - Consumption (MWh for whole country)
 - Elspot price (€/MWh)

##### Yahoo finance
 - Date
 - Dutch Natural Gas Open price (€/MMBTU)
 - Dutch Natural Gas Close price (€/MMBTU)

##### Personal house energy consumption data
 - Electricity transfer during day (€/kWh)
 - Electricity transfer during night (€/kWh)
 - Renewable electricity tax (€/kWh)
 - Electricity tax (€/kWh)

### Goals
 - Analyse Covid-19 impact on electricity prices and consumption
 - Find correlation between different external parameters (gas price, wind and rain intensity, temperature, etc.) and electricity prices
 - How much money could be saved by applying smart consumption theory

## Files
```
/
├── data                                                 # data files, fetching data, deleting data
│   ├── processed                                        # contains processed data files
│   ├── raw                                              # contains raw fetched data files
│   ├── delete_data.py                                   # deletes data from raw and processed directories
│   ├── download_data.py                                 # downloads data from urls.json sources
│   ├── url_writer                                       # writes sources urls to urls.json
│   └── urls.json                                        # sources urls
├── features                                             # contains files for processing raw data
│   ├── process_ilmateenistus.py                         # processes ilmateenistus dataset
│   └── process_nordpool.py                              # processes nordpool dataset
├── visualization                                        # contains reports in jupyter notebooks
│   ├── covid_impact_on_electricity.ipynb                # Covid-19 impact on electricity report      
│   ├── data_exploration.ipynb                           # initial data exploration notebook
│   ├── electricity_prices_vs_external_parameters.ipynb  # electricity prices and external parameters report
│   └── smart_consumption_theory.ipynb                   # smart consumption theory report
├──  D4_report.pdf                                       # CRISP-DM process report
├──  environment.yml                                     # dependencies
├──  index.py                                            # command line interface of the project
```
## How To Run The Project
### Before you can run the project
 - install Anaconda
 - make sure you can use `conda` to create an environment
### Running the project
First time run (If the environment does not already exist)
1. Create the virtual env `conda env create -f environment.yml -n D4-Electricity-Prices`
2. Activate the virtual env `conda activate D4-Electricity-Prices`
3. Run index.py (step by step setup)

If environment already exists
1. Update the dependencies `conda env update -f environment.yml -n D4-Electricity-Prices`
2. Run index.py
