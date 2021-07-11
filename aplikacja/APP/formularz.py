from django.forms import ModelForm
from .models import Bronie, Amunicja, Aktualizacja

class BronForm(ModelForm):
    class Meta:
        model = Bronie
        fields = ['Nazwa', 'Rodzaj', 'Typ_amunicji', 'Cena_broni', 'image']


class AmunicjaForm(ModelForm):
    class Meta:
        model = Amunicja
        fields = ['Nazwa', 'Typ_amunicji', 'Cena_amunicji', 'image']


class AktualizacjaForm(ModelForm):
    class Meta:
        model = Aktualizacja
        fields = ['Nazwa', 'Opis']