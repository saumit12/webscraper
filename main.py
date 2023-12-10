
import requests
from bs4 import BeautifulSoup

# URL of the target webpage
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information based on HTML structure
    # Example: Extracting all text from paragraph (p) tags
    paragraphs = soup.find_all('p')

    # Display the extracted information
    for paragraph in paragraphs:
        print(paragraph.text)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
