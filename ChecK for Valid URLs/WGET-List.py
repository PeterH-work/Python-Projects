# This script will read pagelist.txt and check if the value is a readable webpage on https://100robots.mohammadlotfi.com/
import requests

# Function to check the status of each request
def check_status(page_value):
    url = f"https://100robots.mohammadlotfi.com/{page_value}"
    response = requests.get(url)
    if response.status_code == 403:
        return "Forbidden"
    else:
        return "OK"

# Read the values from pagelist.txt
with open('pagelist.txt', 'r') as file:
    page_values = file.read().split()

# Open the output file to write the results
with open('output.txt', 'w') as output_file:
    for page_value in page_values:
        status = check_status(page_value)
        output_file.write(f"{page_value}: {status}\n")

print("Status check completed. Results are written to output.txt.")
