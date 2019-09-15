from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url = "https://getpocket.com/explore/trending?src=ff_ios&cdn=0"

uClient = urlopen(url)
page_html = uClient.read()
soup = soup(page_html, "html.parser")

containers = soup.findAll("div",{"class" : "item_content"})

out_filename = "Pocket.com_Scrape.csv"
headers = "title,excerpt,website,url,date_published \n"
f = open(out_filename, "w")
f.write(headers) 
##container = containers[0]
##print(container.h3.a["data-saveurl"])

for container in containers:
    title = container.h3.a.text
    excerpt = container.p.text
    website = container.cite.a.text
    save_url = container.h3.a["data-saveurl"]
    date_published = container.cite.span.text
    print(title, excerpt, website, date_published,"\n")
    f.write(title.replace(",",";") + ", " + excerpt.replace(",",";") +", " + website + ", " + save_url +", " +date_published.replace(","," ") + "\n")

f.close()
