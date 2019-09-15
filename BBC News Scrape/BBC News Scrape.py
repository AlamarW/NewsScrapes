from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

page_url = 'https://www.bbc.com/news/world/us_and_canada'

uClient = uReq(page_url)

page_soup = soup(uClient.read(), "html.parser")
uClient.close()

containers = page_soup.findAll("div", {"class": "gs-c-promo gs-t-News nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline gs-c-promo--stacked@m gs-c-promo--flex"})

out_filename = "BBC_USA_news.csv"

headers = "title,promo_sum,link,time_since_posted \n"

f = open(out_filename, "w")
f.write(headers)
for container in containers:
    title = container.h3.text
    try:
        promo_sum = container.p.text
    except:
        promo_sum = "Null"
    link = "https://www.bbc.com"+ container.a["href"]
    try:
        time_since_posted = container.span.time.find('span', attrs={'class':'gs-u-vh'}).text
    except:
        time_since_posted = "Null"
        
    print("title: " + title + "\n")
    print("promo_sum: " + promo_sum + "\n")
    print("link: " + link + "\n")
    print("time_since_posted: " + time_since_posted + "\n")

    f.write(title.replace(",",";") + ", " + promo_sum.replace(",",";") +", " + link + ", " + time_since_posted + "\n")

f.close()
    


