# Generated by Django 3.2.2 on 2021-05-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_alter_bronie_nazwa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amunicja',
            name='Cena_amunicji',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='amunicja',
            name='image',
            field=models.ImageField(null=True, upload_to='Ammo/'),
        ),
        migrations.AlterField(
            model_name='bronie',
            name='Cena_broni',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='bronie',
            name='Typ_amunicji',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='bronie',
            name='image',
            field=models.ImageField(null=True, upload_to='Weapons/'),
        ),
    ]