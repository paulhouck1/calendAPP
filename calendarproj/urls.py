from django.contrib import admin
from django.urls import path
from calapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('entry/add', views.add, name='add')
]
