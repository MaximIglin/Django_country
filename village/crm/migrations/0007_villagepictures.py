# Generated by Django 3.2.5 on 2021-08-09 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20210803_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='VillagePictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('village_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.village_data')),
            ],
        ),
    ]
