from django.contrib import admin
from .models import Disciplina

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'vagas')
    list_filter = ('curso',)
    search_fields = ('nome',)
