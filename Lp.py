import urllib.request as ul
from bs4 import BeautifulSoup as soup
def Lp():

    url = 'https://u.gg/lol/profile/euw1/grab%20your%20ass/overview'
    req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    client = ul.urlopen(req)
    htmldata = client.read()
    client.close()

    pagesoup = soup(htmldata, "html.parser")
    itemlocator = pagesoup.find('div', {"class":"rank-text"})


    namecontainer = itemlocator.findAll("strong")
    txt = namecontainer[0].text +" "+ namecontainer[1].text
    return txt
