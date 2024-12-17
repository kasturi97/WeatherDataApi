import json
import pandas as pd
import os

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

#Load the JSON data from Output folder specified in config file
json_input_path = os.path.join(os.path.dirname(__file__), config['output_file'])

# Load the JSON data from Output folder specified in config.json
with open(json_input_path) as json_file:
    weather_data = json.load(json_file)

# Prepare data for CSV
csv_data = []
for entry in weather_data:
    csv_entry = {
        "Location": entry["name"],
        "Temperature": entry["main"]["temp"],
        "Humidity": entry["main"]["humidity"],
        "Weather": entry["weather"][0]["description"]
    }
    csv_data.append(csv_entry)

# Save CSV file in Output directory specified in config file
csv_output_path = os.path.join(os.path.dirname(__file__), config['csv_file'])

# Create DataFrame and save as CSV
df = pd.DataFrame(csv_data)
df.to_csv(csv_output_path, index=False)


