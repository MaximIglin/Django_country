# Generated by Django 3.2.5 on 2021-08-11 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_delete_villagepictures'),
        ('main_village', '0002_villagenews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='villagenews',
            options={'ordering': ['date'], 'verbose_name': 'Новости'},
        ),
        migrations.AddField(
            model_name='villagenews',
            name='short_text_of_news',
            field=models.TextField(default='Краткое описание', max_length=300, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='villagenews',
            name='village_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.village_data'),
        ),
    ]
