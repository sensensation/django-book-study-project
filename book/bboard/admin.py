from django.contrib import admin

#Регистрация приложения явно в django admin на сайте отладки
from .models import Bb 
admin.site.register(Bb)

from .models import Rubric
admin.site.register(Rubric)

