from django.contrib import admin
from django.urls import path

from Courses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('Yonalish/', spes),
    path('ustozlar/', ustozlar),
    path('fanlar/', fanlar),
    path('ustozlar/<int:pk>/', ustoz_ochir),
    path('Yonalish/<int:son>/', spes_ochir),
    path('edit_book/<int:son>/', edit_book),
]
