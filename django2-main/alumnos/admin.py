from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Genero, Alumno, Ramo, Escuela

# Register your models here.
admin.site.register(Genero)
admin.site.register(Alumno)
admin.site.register(Ramo)
admin.site.register(Escuela)
