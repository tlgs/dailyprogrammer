# 24/06/2017
from lxml import html
import requests
import re

if __name__ == "__main__":
    visited = []
    current_page = input()
    
    while((current_page != "Philosophy" and current_page != None) and current_page not in visited):
        visited.append(current_page)
        page = requests.get("https://en.wikipedia.org/wiki/" + current_page)

        if not page.ok:
            print("Invalid URL")
            break

        page_text = re.sub(r"\([^\)]*\<[^\>]*\>[^\)]*\)", "", page.text)
        tree = html.fromstring(page_text)
        raw_links = tree.xpath("//p/a[@href]")
        links = [x.get("href")[6:] for x in raw_links]
        current_page = links[0] if len(links) > 0 else None
        print(current_page)