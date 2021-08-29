from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # it is nothing
    path('about', views.about, name='about'),

]
