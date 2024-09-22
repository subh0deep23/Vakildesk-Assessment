import requests
from bs4 import BeautifulSoup

# URL of CNN's World section
url = "https://edition.cnn.com/world"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags with href attributes
    articles = soup.find_all('a', href=True)

    # Loop through the articles and filter valid news URLs
    for article in articles:
        link = article['href']
        title = article.get_text(strip=True)

        # Filter links that lead to valid news articles
        if '/2024/' in link or '/2023/' in link or '/articles/' in link:
            # Append base URL if the link is relative
            if not link.startswith('http'):
                link = "https://edition.cnn.com" + link
            print(f"Title: {title}")
            print(f"URL: {link}\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
