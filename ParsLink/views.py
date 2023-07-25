from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

import requests
from bs4 import BeautifulSoup
from .models import *
from .forms import *

menu = ['Главная','История']

def index(request):
    links = []
    if request.method == 'POST':
        form = AddUrlForm(request.POST)
        if form.is_valid():
            try:
                links = pars(form.cleaned_data['content'])
            except:
                form.add_error(None, 'Ошибка обработки ссылки')
    else:
        form = AddUrlForm()
    return render(request,'ParsLink/index.html', {'menu': menu,'title': 'Парсинатор-3000','form':form, 'posts': links}) 

def history(request):
    history_posts = History.objects.all()
    return render(request,'ParsLink/history.html', {'posts': history_posts,'menu': menu,'title': 'History'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def pars (pars_url):
    new_links=[] # Этот список выводится в таблицу, заняться выводом, потом уже интерфейс и преколы
    page = requests.get(pars_url)
    soup = BeautifulSoup(page.content, "html.parser")
    all_links = soup.find_all("a")
    for link in all_links:
        temp_link=link.get("href")
        if temp_link.startswith("/"):
            new_links.append(pars_url + temp_link)
            add_history = History.objects.create(title = pars_url, content = pars_url + temp_link)
        else:
            new_links.append(temp_link)
            add_history = History.objects.create(title = pars_url, content = temp_link)
    return new_links


