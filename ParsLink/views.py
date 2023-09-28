from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, FormView, CreateView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import *
from .forms import *
from .services import parse, clean_history
from .utils import *

menu = [{'title':"История", 'url_name': 'history'}
]  # Список меню в хэдэре

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


class ParsLinkHistory(ListView, FormView, DataMixin):
    """
    Класс представления страницы истории.

    Наследован от:
    ListView -  базовый класс Django отображение содержимого БД,
    FormView -  базовый класс Django отображение и валидация формы,
    DataMixin - формирование контекста

    """
    model = History
    template_name = 'ParsLink/history.html'
    context_object_name = 'posts'
    form_class = HistoryForm
    success_url = '/history/'


    def clean_history(self, form):
        clean_history.clean_history()

    def form_valid(self, form):
        self.clean_history(form)
        return super().form_valid(form)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='История')
        return dict(list(context.items()) + list(c_def.items()))

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

class RegisterUser(DataMixin, CreateView):
    """
    Класс представления страницы регистрации.

    Наследован от:
    CreateView - базовый класс Django создание объекта,
    DataMixin - формирование контекста

    """

    form_class = RegisterUserForm
    template_name = 'ParsLink/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    """
    Класс представления страницы аутентификации.

    Наследован от:
    LoginView - базовый класс Django отображения формы входа и соответствующие действия,
    DataMixin - формирование контекста

    """

    form_class = LoginUserForm
    template_name = 'ParsLink/login.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


