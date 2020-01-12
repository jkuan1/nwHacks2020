import requests
from bs4 import BeautifulSoup

# Webiste url and requsting the html
URL = "https://www.cbc.ca/news/canada/ottawa/shelley-kettles-skating-1.5401235"
page = requests.get(URL)

# Setup BeatifulSoup web scrapper
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='story')
lines = results.find_all("p")

# Recombine html paragraphs into one string
list_lines = []
for p in range(len(lines)):
    paragraph = lines[p].get_text()
    list_lines.append(paragraph)
    final_article = " ".join(list_lines)

print(final_article)