import types

from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse

from .models import *

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import EmailAuthenticationForm
menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Туры', 'url_name': 'tour_categories'},
    {'title': 'Типы экосистем', 'url_name': 'Ecosystem_categories'},  # Исправил 'тахси' на 'такси'
    {'title': 'Войти', 'url_name': 'login'},
]


# def Ecosystem_types(request, slug):
#     Ecosystem_type = get_object_or_404(EcosystemCategory, slug=slug)
#
#     return render(request, 'shopp/Ecosystem_types.html', {'Ecosystem_type': Ecosystem_type})
#
# def Ecosystem_types_list(request):
#     types = EcosystemCategory.objects.all()  # Запрос на получение всех типов экосистем из базы данных
#     return render(request, 'shopp/Ecosystem_types_list.html', {'types': types})


def Ecosystem_by_category(request, slug):
    ecosystem_type = get_object_or_404(EcosystemCategory, slug=slug)
    ecosystems = Ecosystem.objects.filter(category=ecosystem_type)
    return render(request, 'shopp/Ecosystem_by_category.html', {
        'ecosystem_type': ecosystem_type,
        'ecosystems': ecosystems,
    })

def Ecosystem_categories(request):
    categories = EcosystemCategory.objects.all()  # Получаем все категории
    return render(request, 'shopp/Ecosystem_categories.html', {'categories': categories,
                                                                                   'menu': menu})

# Представление для отображения экосистем по выбранной категории


# def tours_by_category(request, category_id):
#     tours = Tour.objects.filter(category_id=category_id)
#     category = TourCategory.objects.get(id=category_id)
#     return render(request, 'shopp/tours_by_category.html', {'tours': tours, 'category': category})
#
# def tour_categories(request):
#     categories = TourCategory.objects.all()
#     return render(request, 'shopp/tour_categories.html', {'categories': categories, 'menu': menu})

def about(request):
    return render(request, 'shopp/about.html', {'menu': menu,
                                                                     'title': 'О нас'})
def taxi(request):
    return render(request, 'shopp/taxi.html', {'menu': menu, 'title': 'about texit'})

def index(request):
    posts = Product.objects.all()
    return render(request, 'shopp/index.html', {'posts': posts, 'menu': menu, 'title': 'Главный страница'})

def car(request, catid):

    return HttpResponse(f'i love{catid} you')







def login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему!')
                return redirect('index')  # Замените 'home' на имя URL, куда вы хотите перенаправить после входа
            else:
                messages.error(request, 'Неверный email или пароль.')
    else:
        form = EmailAuthenticationForm()

    return render(request, 'shopp/login.html', {'form': form})
#
# def Ecosystem_by_category(request, slug):
#     ecosystem_type = get_object_or_404(EcosystemCategory, slug=slug)
#     ecosystems = Ecosystem.objects.filter(category=ecosystem_type)
#     return render(request, 'shopp/Ecosystem_by_category.html', {
#         'ecosystem_type': ecosystem_type,
#         'ecosystems': ecosystems,
#     })
#
# def Ecosystem_categories(request):
#     categories = EcosystemCategory.objects.all()  # Получаем все категории
#     return render(request, 'shopp/Ecosystem_categories.html', {'categories': categories})

#
# def tours_by_category(request, slug):
#     category = get_object_or_404(TourCategory, slug=slug)
#     tours = Tour.objects.filter(category=category)
#     return render(request, 'shopp/tours_by_category.html', {'tours': tours, 'category': category})
#
# def tour_categories(request):
#     categories = TourCategory.objects.all()
#     return render(request, 'shopp/tour_categories.html', {'categories': categories, 'menu': menu})


def tours_by_category(request, category_id):
    tours = Tour.objects.filter(category_id=category_id)
    category = TourCategory.objects.get(id=category_id)
    return render(request, 'shopp/tours_by_category.html', {'tours': tours, 'category': category})

def tour_categories(request):
    categories = TourCategory.objects.all()
    return render(request, 'shopp/tour_categories.html', {'categories': categories, 'menu': menu})


