from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

req = Request('https://www.propublica.org/', headers ={'User-Agent': 'Mozilla/5.0'})

raw_html = urlopen(req).read()
soup = soup(raw_html, "html.parser")

containers = soup.findAll("div",{"class" : "description"})

out_filename = "Propublica.com_Scrape.csv"
headers = "title%excerpt%save_url%date_published \n"

f = open(out_filename, "w")
f.write(headers) 

for container in containers:
    title = container.h1.text
    excerpt = container.h2.text
    save_url = container.h1.a["href"]
    date_published = container.time.text
    
    print(title, excerpt, save_url, date_published,"\n")
    #Replacing commas with semi colons to stop it from being counted as a comma deliminator
    f.write(title.replace(",",";") + "% " + excerpt.replace(",",";") + "% " + save_url + "% " + date_published.replace(","," ") + "\n")

f.close()
