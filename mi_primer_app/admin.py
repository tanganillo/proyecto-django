from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso, Estudiante

regiter_models = [Familiar, Curso, Estudiante]

admin.site.register(regiter_models)