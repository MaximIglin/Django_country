# Generated by Django 3.2.5 on 2021-08-11 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0011_delete_villagepictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='VillagePictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('add_date', models.DateField(auto_now=True, null=True)),
                ('village_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.village_data')),
            ],
            options={
                'verbose_name': 'Фото деревень',
                'ordering': ['village_name__title'],
            },
        ),
    ]
