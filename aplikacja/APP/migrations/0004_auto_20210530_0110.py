# Generated by Django 3.2.2 on 2021-05-29 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_amunicja'),
    ]

    operations = [
        migrations.AddField(
            model_name='amunicja',
            name='image',
            field=models.ImageField(null=True, upload_to='Ammo'),
        ),
        migrations.AddField(
            model_name='bronie',
            name='image',
            field=models.ImageField(null=True, upload_to='Weapons'),
        ),
    ]