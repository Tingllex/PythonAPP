from django.db import models


class Kategoria(models.Model):
    bronie = models.CharField(max_length=45)
    amunicja = models.CharField(max_length=45)
    popularne = models.CharField(max_length=45)
    akt = models.Boo

    class Meta:
        verbose_name_plural = "Kategoria"


class Bronie(models.Model):
    Nazwa = models.CharField(max_length=45, unique=True, blank=False)
    Rodzaj = models.CharField(max_length=20, blank=False)
    Typ_amunicji = models.CharField(max_length=20, blank=True)
    Cena_broni = models.IntegerField()
    image = models.ImageField(upload_to='Weapons/', null=True)
    class Meta:
        verbose_name_plural = "Bronie"
    def __str__(self):
        return self.Nazwa + ' <' + str(self.Rodzaj) + '>'


class Amunicja(models.Model):
    Nazwa = models.CharField(max_length=20)
    Typ_amunicji = models.CharField(max_length=20)
    Cena_amunicji = models.IntegerField()
    image = models.ImageField(upload_to="Ammo/", null=True)

    class Meta:
        verbose_name_plural = "Amunicja"

    def __str__(self):
        return self.Nazwa + ' <' + str(self.Typ_amunicji) + '>'


class Aktualizacja(models.Model):
    Nazwa = models.CharField(max_length=60)
    Opis = models.CharField(max_length=1000)
    Data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Nazwa + ' <' + str(self.Data) + '> ' + '\n\n' + self.Opis

