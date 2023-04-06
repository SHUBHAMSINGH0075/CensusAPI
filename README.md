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
2020 ACS (America Community Survey-5 year) are here: https://api.census.gov/data/2020/acs/acs5/variables.html
Current target:
Write a wrapper program to access the Census API
The progam can:
Take in a list of ZIP code
Take in optional API variable names (0 or more variable names)
Get 2020 CBP and ACS outputs on a ZIP level
Print out the collected data in a CSV file for checking.
