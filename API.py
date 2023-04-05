import requests
import csv
import time

# Census API key
API_KEY = '48edb2e40ca9e42b1572c4bb4a46a18f8417fedf'

# ZIP codes and variable names
zip_codes = ['53211']
cbp_variable_names = ['ESTAB', 'EMP', 'PAYANN']
acs_variable_names = ['B19013_001E', 'B01002_001E']

# Build the API URLs
cbp_url = 'https://api.census.gov/data/2020/cbp?get=NAME,' + ','.join(cbp_variable_names) + '&for=zipcode:' + ','.join(zip_codes) + '&key=' + API_KEY
acs_url = 'https://api.census.gov/data/2020/acs/acs5?get=' + ','.join(acs_variable_names) + '&for=zip%20code%20tabulation%20area:' + ','.join(zip_codes) + '&key=' + API_KEY

# Start the timer
start_time = time.time()

# Fetch data from the CBP API
cbp_response = requests.get(cbp_url)

# Check for errors
if cbp_response.status_code != 200:
    print('Error fetching data from CBP API')
    exit()

# Fetch data from the ACS API
acs_response = requests.get(acs_url)

# Check for errors
if acs_response.status_code != 200:
    print('Error fetching data from ACS API')
    exit()

# Combine CBP and ACS data
cbp_data = cbp_response.json()
acs_data = acs_response.json()

combined_data = [cbp_data[0] + acs_data[0]]
for i in range(1, len(cbp_data)):
    combined_data.append(cbp_data[i] + acs_data[i])

# Save data in a CSV file
with open('combined_data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(combined_data)

# End the timer and print the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Data saved in combined_data.csv in {elapsed_time:.2f} seconds')
