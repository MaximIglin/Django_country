# Generated by Django 3.2.5 on 2021-08-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_villagepictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='villagepictures',
            name='add_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
