from django.contrib import admin
from django.urls import path, include
from calapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('entry/add', views.add, name='add'),
    path('calendar', views.calendar, name='calendar'),
    path('schedule/', include('schedule.urls'))
]
