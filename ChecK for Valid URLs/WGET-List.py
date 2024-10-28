# This app will run a batch of wgets with a fixed string before and after a set of values that it gets from pagelist.txt
# The resulting return codes are listed in output.txt

import requests

# Ask the user for input strings to be used in the URL format
before_string = input("Enter the string to paste before the values in pagelist.txt: ")
after_string = input("Enter the string to paste after the values in pagelist.txt: ")

# Check if before_string starts with "http://" or "https://"
if not (before_string.startswith("http://") or before_string.startswith("https://")):
    print("Error: The string before the values must start with 'http://' or 'https://'.")
    exit(1)

# Function to check the status of each request
def check_status(page_value):
    url = f"{before_string}{page_value}{after_string}"
#    url = f"https://100robots.mohammadlotfi.com/{page_value}/flag.txt"
    response = requests.get(url)
    if response.status_code == 403:
        return "Forbidden"
    elif response.status_code == 404:
        return "Lost"
    elif response.status_code == 200:
        return "OK"
    else:
        return f"Statuscode {response.status_code}"

# Read the values from pagelist.txt
with open('pagelist.txt', 'r') as file:
    page_values = file.read().split()

# Open the output file to write the results
with open('output.txt', 'w') as output_file:
    for page_value in page_values:
        status = check_status(page_value)
        output_file.write(f"{page_value}: {status}\n")

print("Status check completed. Results are written to output.txt.")
