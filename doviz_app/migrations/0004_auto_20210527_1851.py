# Generated by Django 3.0.8 on 2021-05-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doviz_app', '0003_kurfiyatlari'),
    ]

    operations = [
        migrations.RenameField(
            model_name='param',
            old_name='param',
            new_name='donusen',
        ),
        migrations.AddField(
            model_name='param',
            name='donusturulen',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='kurfiyatlari',
            name='fiyat',
            field=models.FloatField(default=0),
        ),
    ]
