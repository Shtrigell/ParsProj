import requests
from bs4 import BeautifulSoup
from ParsLink.models import *

def parse (pars_url):
    """
    Функция парсинга

    Получает URL, парсит содержимое по указанному тегу, возвращает список ссылок.

    new_links - список, который заполняется ссылками, которые парсятся с указанного URL.
    page - строка, содержащая извлечённые данные со страницы.
    all_links - список, содержащий найденные ссылки по указаному тегу.
    temp_link - строка, содержащая спаршенную ссылку. Нужна для проверки и дополнения относительных ссылок.
    
    """
    new_links = []
    try:
        page = requests.get(pars_url)
    except:
        print('Error')
        new_links.append('Ошибка обработки ссылки')
        return new_links
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
