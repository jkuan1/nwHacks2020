import requests
from bs4 import BeautifulSoup

URL = "https://www.cbc.ca/news/canada/ottawa/shelley-kettles-skating-1.5401235"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='story')
lines = results.find_all("p")

list_lines = []
for p in range(len(lines)):
    paragraph = lines[p].get_text()
    list_lines.append(paragraph)
    final_article = " ".join(list_lines)

print(final_article)

# for i in range(len(lines)):
    # print(lines[i])


# print(results.prettify())



# print(results.prettify())