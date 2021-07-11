from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Bronie, Amunicja
from django.shortcuts import render, get_object_or_404, redirect
from .formularz import BronForm, AmunicjaForm, AktualizacjaForm
from .models import Aktualizacja

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def wypisBroni(request):
    wszystkie = Bronie.objects.all()
    ilosc = len(wszystkie)
    return render(request, 'Bronie.html', {'ilosc_broni': ilosc,
                                           'bronie': wszystkie})


def wypisAmunicji(request):
    wszystkie = Amunicja.objects.all()
    ilosc = len(wszystkie)
    return render(request, 'Amunicja.html', {'ilosc_amunicji': ilosc,
                                             'amunicja': wszystkie})


def dodanieBroni(request):
    if request.user.is_superuser:
        formularz = BronForm(request.POST or None, request.FILES or None)
        if formularz.is_valid():
            formularz.save()
            return redirect(wypisBroni)
        return render(request, 'dodanieBroni.html', {'form': formularz})
    else:
        return render(request, 'NotSuperUser.html')


def edycjaBroni(request, id):
    if request.user.is_superuser:
        bron = get_object_or_404(Bronie, pk=id)
        formularz = BronForm(request.POST or None, request.FILES or None, instance=bron)
        if formularz.is_valid():
            formularz.save()
            return redirect(wypisBroni)
        return render(request, 'edycjaBroni.html', {'form': formularz})
    else:
        return render(request, 'NotSuperUser.html')


def usuniecieBroni(request, id):
    if request.user.is_superuser:
        bron = get_object_or_404(Bronie, pk=id)
        if request.method == 'POST':
            bron.delete()
            return redirect(wypisBroni)
        return render(request, 'usuniecieBroni.html', {'id_broni': bron})
    else:
        return render(request, 'NotSuperUser.html')


def dodanieAmunicji(request):
    if request.user.is_superuser:
        formularz = AmunicjaForm(request.POST or None, request.FILES or None)
        if formularz.is_valid():
            formularz.save()
            return redirect(wypisAmunicji)
        return render(request, 'dodanieAmunicji.html', {'form': formularz})
    else:
        return render(request, 'NotSuperUser.html')


def edycjaAmunicji(request, id):
    if request.user.is_superuser:
        ammo = get_object_or_404(Amunicja, pk=id)
        formularz = BronForm(request.POST or None, request.FILES or None, instance=ammo)
        if formularz.is_valid():
            formularz.save()
            return redirect(wypisAmunicji)
        return render(request, 'edycjaAmunicji.html', {'form': formularz})
    else:
        return render(request, 'NotSuperUser.html')


def usuniecieAmunicji(request, id):
    if request.user.is_superuser:
        ammo = get_object_or_404(Amunicja, pk=id)
        if request.method == 'POST':
            ammo.delete()
            return redirect(wypisAmunicji)
        return render(request, 'usuniecieAmunicji.html', {'id_amunicji': ammo})
    else:
        return render(request, 'NotSuperUser.html')


def DanaBron(request, id):
    bron = get_object_or_404(Bronie, pk=id)
    return render(request, "DanaBron.html", {'JednaBron': bron})


def DanaAmunicja(request, id):
    ammo = get_object_or_404(Amunicja, pk=id)
    return render(request, "DanaAmunicja.html", {'JednaAmunicja': ammo})


def HomePage(request):
    return render(request, 'home page.html')

def SearchPage(request):
    srh = request.GET['query']
    szukana = Bronie.objects.filter(Nazwa__icontains=srh)
    szukana2 = Amunicja.objects.filter(Nazwa__icontains=srh)
    szukana3 = Bronie.objects.filter(Rodzaj__icontains=srh)
    szukana4 = Bronie.objects.filter(Typ_amunicji__icontains=srh)
    szukana5 = Amunicja.objects.filter(Typ_amunicji__icontains=srh)
    params = {'szukana': szukana, 'search': srh,
              'szukana2': szukana2, 'search2': srh,
              'szukana3': szukana3, 'search3': srh,
              'szukana4': szukana4, 'search4': srh,
              'szukana5': szukana5, 'search5': srh,
              }
    return render(request, 'search page.html', params)


def Update(request):
    wszystkie = Aktualizacja.objects.all()
    return render(request, 'Aktualizacje.html', {'update': wszystkie})

def dodanieAktualizacji(request):
    if request.user.is_superuser:
        formularz = AktualizacjaForm(request.POST or None, request.FILES or None)
        if formularz.is_valid():
            formularz.save()
            return redirect(Update)
        return render(request, 'dodanieAktualizacji.html', {'form': formularz})
    else:
        return render(request, 'NotSuperUser.html')


def edycjaAktualizacji(request, id):
    if request.user.is_superuser:
        update = get_object_or_404(Aktualizacja, pk=id)
        formularz = AktualizacjaForm(request.POST or None, request.FILES or None, instance=update)
        if formularz.is_valid():
            formularz.save()
            return redirect(Update)
        return render(request, 'edycjaAktualizacji.html', {'form': formularz})
    else:
        return render(request, 'NotSuperUser.html')


def usuniecieAktualizacji(request, id):
    if request.user.is_superuser:
        update = get_object_or_404(Aktualizacja, pk=id)
        if request.method == 'POST':
            update.delete()
            return redirect(Update)
        return render(request, 'usuniecieAktualizacji.html', {'id_update': update})
    else:
        return render(request, 'NotSuperUser.html')