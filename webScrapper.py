import requests
from bs4 import BeautifulSoup

# Webiste url and requsting the html
URL = "https://www.cbc.ca/news/canada/ottawa/shelley-kettles-skating-1.5401235"
page = requests.get(URL)

# Setup BeatifulSoup web scrapper
soup = BeautifulSoup(page.content, 'html.parser')
headline = soup.find("h1", class_="detailHeadline")

story = soup.find(class_='story')
lines = story.find_all("p")

# Recombine html paragraphs into one string
list_lines = [headline.get_text() + "\n"]
for p in range(len(lines)):
    paragraph = lines[p].get_text()
    list_lines.append(paragraph)
    final_article = " ".join(list_lines)

print(final_article)