# Generated by Django 3.0.8 on 2021-06-18 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doviz_app', '0009_wallet_kur_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurfiyatlari',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='wallet_kur',
            name='kur_fiyat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doviz_app.KurFiyatlari'),
        ),
    ]
