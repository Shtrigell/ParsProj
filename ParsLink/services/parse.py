import requests
from bs4 import BeautifulSoup
from ParsLink.models import *

def parse (pars_url):
    new_links = [] 
    page = requests.get(pars_url)
    soup = BeautifulSoup(page.content, "html.parser")
    all_links = soup.find_all("a")
    for link in all_links:
        temp_link = link.get("href")
        if temp_link.startswith("/"):
            new_links.append(pars_url + temp_link)
            add_history = History.objects.create(title = pars_url, content = pars_url + temp_link)
        else:
            new_links.append(temp_link)
            add_history = History.objects.create(title = pars_url, content = temp_link)
    return new_links
