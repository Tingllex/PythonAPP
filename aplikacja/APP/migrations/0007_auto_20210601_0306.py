# Generated by Django 3.2.2 on 2021-06-01 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_auto_20210531_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amunicja',
            name='Cena_amunicji',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bronie',
            name='Cena_broni',
            field=models.IntegerField(),
        ),
    ]