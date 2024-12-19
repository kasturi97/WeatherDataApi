# weatherData
A Python project to fetch and save weather data.

This Python project fetches weather data for specified locations and saves it in JSON and CSV formats.

- Fetches weather data from OpenWeatherMap API.
- Saves data in both JSON and CSV formats in output folder(master branch)

# Setup Instructions

1. Clone the repository:

   git clone https://github.com/kasturi97/WeatherDataApi.git

   Two folders in Master branch:  main, output
 

   main 

    ─ weatherData.py         # Your main weather data processing script

    ─ parseJsonToCsv.py      # Script for parsing JSON to CSV

    ─ config.py              # Configuration file

    ─ runalll.py             # Script for running the application

   output                   # Output folder for results

    ─ weatherdata.csv        # output file (CSV format)

    ─ weatherdata.json       # output file (json format)


                                  
2. Install required packages:
 
   pip install requests pandas
 
3. Update `config.json` with your OpenWeatherMap API key

4. Run the main script:
   python3 runAll.py
