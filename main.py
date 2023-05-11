import re
import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    'https://www.example.com',
    'https://www.example.net',
    'https://www.example.org'
]

# Regular expression pattern to match email addresses
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Dictionary to store email addresses for each URL
email_dict = {}

# Loop through each URL
for url in urls:
    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all text in the HTML document
    text = soup.get_text()

    # Find all email addresses using regular expressions
    email_addresses = re.findall(email_regex, text)

    # Add the email addresses to the dictionary
    email_dict[url] = email_addresses

# Print the dictionary of email addresses for each URL
print(email_dict)
