from django.urls import path, include

from .views import *
from . import views
urlpatterns = [
    path('car/<slug:catid>/', views.car, name='car'),
    path('', views.index, name='index'),

    path('Ecosystems/', views.Ecosystem_categories, name='Ecosystem_categories'),
    path('Ecosystems/<slug:slug>/', views.Ecosystem_by_category, name='Ecosystem_by_category'),




    path('taxi', views.taxi, name='taxi'),
    path('about/', views.about, name='about'),
    path('login', views.login ,name='login'),
    path('accounts/', include('allauth.urls')),
    path('tours/', views.tour_categories, name='tour_categories'),
    path('tours/<str:category_id>/', views.tours_by_category, name='tours_by_category'),

    # Другие маршруты

]