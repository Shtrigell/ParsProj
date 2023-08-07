from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
from .forms import *
from .services import parse, clean_history

menu = ['Главная','История']  # Список меню в хэдэре

def index(request):
    """
    Функция представления главной страницы.

    Возвращает рендер главной страницы, передавая список меню в хэдэр,
    заголовок страницы, форму для работы с URL, 
    список спаршенных ссылок.

    """
    links = []  # Пустой список для заполнения функцией parse()
    if request.method == 'POST':
        form = AddUrlForm(request.POST)
        if form.is_valid():
            try:
                links = parse.parse(form.cleaned_data['content'])
            except:
                form.add_error(None, 'Ошибка обработки ссылки')
    else:
        form = AddUrlForm()

    return render(request,'ParsLink/index.html', {'menu': menu, 'title': 'Main page', 'form':form, 'posts': links}) 

def history(request):
    """
    Функция представления страницы с историей обращений.

    Возвращает рендер страницы с историей, передавая список меню в хэдэр,
    заголовок страницы, форму связанную с моделью History, 
    список истории парсинга.
    
    """
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            try:
                clean_history.clean_history()
            except:
                form.add_error(None, 'Ошибка очистка истории')
    else:
        form = HistoryForm()

    history_posts = History.objects.all()
    return render(request,'ParsLink/history.html', {'menu': menu, 'title': 'History', 'form':form, 'posts': history_posts})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
