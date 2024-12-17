import subprocess
import os

# Run weatherData.py to fetch and save weather data
subprocess.run(["python3", os.path.join(os.path.dirname(__file__), 'weatherData.py')], check=True)

# Run parseJsonToCsv.py to convert JSON to CSV
subprocess.run(["python3", os.path.join(os.path.dirname(__file__), 'parseJsonToCsv.py')], check=True)


