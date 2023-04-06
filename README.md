# CensusAPI
The Census Bureau's Application Programming Interface (API) is a tool that you can use to access
American Community Survey (ACS) data more efficiently.  
It reduces the need for data storage and provides users with a set of standard commands to easily 
access statistics that can be incorporated into their programs and applications.
Instead of making a web browser query request we are going develop a python program to fetch data from census API because:
Automation: A wrapper program allows you to automate the process of fetching data from the Census API, which can be useful
if you need to fetch data for many different ZIP codes or variables.
Flexibility: A wrapper program allows you to customize the data you fetch from the Census API by specifying which variables
to fetch and how to format the data. This gives you more flexibility than a web query, which may have limitations on what data
you can fetch and how you can format it.
Efficiency: A wrapper program can be more efficient than a web query because it can fetch data for multiple ZIP codes and
variables in a single API call. This can save you time and reduce the load on the Census API servers.
Reproducibility: A wrapper program makes it easy to reproduce your data fetching process,
which can be useful if you need to update your data regularly or share your data with others.
Overall, a wrapper program gives you more control over the data you fetch from the Census API and allows
you to automate the process of fetching data, making it a more efficient and reproducible approach to data collection.
All API endpoints: https://api.census.gov/data/
All 2020 API endpoints: https://api.census.gov/data/2020/
Target cesnsus variable APIs (on ZIP data):
2020 County Business Patterns (CBP) https://api.census.gov/data/2020/cbp/variables.html
2020 ACS (America Community Survey-5 year) are here: https://api.census.gov/data/2020/acs/acs5/variables.htmlKe
Program Description:
API_KEY:
Request a Secret Key from the United States Census Bureau: https://www.census.gov/data/developers.html
In order to make API calls (just a fancy name for a web request asking for specific data), you will need to request a secret key from the US Census Bureau. Navigate to the census developers page and you should see “Request a Key”.
Replace your_api_key_here with your actual Census API key. The code fetches data for the ZIP codes 53211 and 53154 and the variable names ESTAB, EMP, and PAYANN from the 2020 CBP data, and the variable names B19013_001E and B01002_001E from the 2020 ACS 5-year estimates. You can modify the zip_codes, cbp_variable_names, and acs_variable_names lists to fetch data for different ZIP codes and variable names.
The program measures the elapsed time using the time module in Python and prints it to the console in seconds with two decimal places.
