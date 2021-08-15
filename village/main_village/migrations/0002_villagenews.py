# Generated by Django 3.2.5 on 2021-08-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_village', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VillageNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Заголовок', max_length=150, verbose_name='Заголовок новсти')),
                ('text_of_title', models.TextField(default='Новость:', verbose_name='Содержание новости')),
                ('date', models.DateTimeField(auto_now=True)),
                ('images', models.JSONField()),
            ],
        ),
    ]
