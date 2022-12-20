import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get('https://wordcounter.net/')

# Parse the content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the data
title = soup.title.string
links = soup.find_all('a')

# Print the data
print(title)
print(links)
