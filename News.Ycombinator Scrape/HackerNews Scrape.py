from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

req = Request('https://news.ycombinator.com/', headers ={'User-Agent': 'Mozilla/5.0'})

raw_html = urlopen(req).read()
page_soup = soup(raw_html, "html.parser")

containers = page_soup.findAll("tr", {"class": "athing"})

out_filename = "HackerNews Scrape.csv"

headers = "Title\t Link \n"

f = open(out_filename, "w")
f.write(headers)
for container in containers:
        content = container.find("a", {"class": "storylink"})
        title = content.text

        link = content['href']
        print(f"{title} ---> {link}")

        f.write(title + "\t" + link + "\n")

f.close()
