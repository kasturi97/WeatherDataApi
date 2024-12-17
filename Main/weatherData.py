import json
import requests
import os

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Function to fetch weather data
def fetch_weather_data(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units={config['units']}&appid={config['api_key']}"
    response = requests.get(url)
    return response.json()

# Collect weather data for all locations
weather_data = []
for location in config['locations']:
    data = fetch_weather_data(location)
    weather_data.append(data)

#Output path for Json file
output_dir = os.path.join(os.path.dirname(__file__), '../output')

# Create Output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)


# Save the initial response in JSON format in the Output directory
output_file_path = os.path.join(output_dir, 'weather_data.json')

#output file path
with open(output_file_path, 'w') as json_file:
    json.dump(weather_data, json_file, indent=4)

