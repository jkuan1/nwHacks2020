import requests
import json
import textwrap
from bs4 import BeautifulSoup

CHARACTER_LIMIT = 5000

# Website url and requsting the html
URL = url
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

    final_article = final_article.replace(u'\xa0', u' ')
    final_article = final_article.replace(u'\n', u'.')

print(len(final_article))



def prepare_key_phrases(article):
    article_size = len(article)
    if (article_size / CHARACTER_LIMIT > 0):
        document = [article[i:i + CHARACTER_LIMIT] for i in range(0, article_size, CHARACTER_LIMIT)]
    else:
        document = [article]
    return document

print(prepare_key_phrases(final_article))