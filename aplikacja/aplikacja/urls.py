"""aplikacja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from APP.views import wypisBroni, wypisAmunicji
from APP.views import dodanieBroni, edycjaBroni, usuniecieBroni
from APP.views import dodanieAmunicji, edycjaAmunicji, usuniecieAmunicji
from APP.views import DanaBron, DanaAmunicja
from APP.views import SearchPage
from APP.views import Update
from APP.views import dodanieAktualizacji, edycjaAktualizacji, usuniecieAktualizacji

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('APP/', include('APP.urls')),
    path('APP/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('Bronie/', wypisBroni),
    path('Amunicja/', wypisAmunicji),
    path('', include('start.urls')),
    path('dodanieBroni/', dodanieBroni, name="dodajB"),
    path('edycjaBroni/<int:id>', edycjaBroni, name="edycjaB"),
    path('usunBron/<int:id>', usuniecieBroni, name="usunB"),
    path('dodanieAmunicji/', dodanieAmunicji, name="dodajA"),
    path('edycjaAmunicji/<int:id>', edycjaAmunicji, name="edycjaA"),
    path('usunAmunicje/<int:id>', usuniecieAmunicji, name="usunA"),
    path('DanaBron/<int:id>', DanaBron, name="danaB"),
    path('DanaAmunicja/<int:id>', DanaAmunicja, name="danaA"),
    path('search/', SearchPage, name="search_result"),
    path('aktualizacje', Update, name="update"),
    path('dodanieAktualizacji/', dodanieAktualizacji, name="dodajAk"),
    path('edycjaAktualizacji/<int:id>', edycjaAktualizacji, name="edycjaAk"),
    path('usuniecieAktualizacji/<int:id>', usuniecieAktualizacji, name="usunAk"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

