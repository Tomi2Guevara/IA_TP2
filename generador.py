import json

csv_data = """
20.0;20.5;21.0;21.5;22.0;22.5;23.0;23.5;24.0;24.5;25.0;25.5;22;21.6;20;20.5
19.5;20.0;20.5;21.0;21.5;22.0;22.5;23.0;23.5;24.0;24.5;25.0;27;30;29;31.0
30.5;29;28.5;27.5;26.8;26;26.5;27;26;24;25;26;27.6;26;25.0;24
26;28;30;31;30;27;25;22;18;15;12;15;13;14;10;5
"""

# Split the CSV data into rows
rows = csv_data.strip().split("\n")

# Process each row and convert to a JSON array
json_data = [list(map(float, row.split(";"))) for row in rows]

# Output the JSON data
output_file_path = 't2f1.json'
with open(output_file_path, 'w') as json_file:
    json.dump(json_data, json_file)

print(f"Data successfully converted and saved to '{output_file_path}'.")
