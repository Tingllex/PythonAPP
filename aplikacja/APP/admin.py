from django.contrib import admin

from .models import Kategoria, Bronie, Amunicja, Aktualizacja
admin.site.register(Kategoria)
admin.site.register(Bronie)
admin.site.register(Amunicja)
admin.site.register(Aktualizacja)