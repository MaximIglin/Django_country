# Generated by Django 3.2.5 on 2021-08-09 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_villagepictures_add_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='villagepictures',
            options={'ordering': ['village_name'], 'verbose_name': 'Фото деревень'},
        ),
    ]
