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

### Goals
 - Analyse Covid-19 impact on electricity prices and consumption
 - Find correlation between different external parameters (CO2, gas price, solar, wind, rain intensity) and electricity prices
 - How much money could be saved by applying smart consumption theory

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
