from django.db import models


class Kurlar(models.Model):
    """
    docstring
    """
    kur_adı = models.CharField(
        max_length=128
    )

class KurFiyatlari(models.Model):
    """
    docstring
    """
    kur_adı = models.ForeignKey(
        Kurlar,
        on_delete=models.CASCADE
    )
    fiyat = models.FloatField(
        default=0
    )
    date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )


class Param(models.Model):
    """
    docstring
    """
    donusturulen = models.FloatField(
        default=0
    )
    donusen = models.FloatField(
        default=0
    )
    kur_adı = models.ForeignKey(
        KurFiyatlari,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    kullanıcı = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

class Wallet(models.Model):
    """
    docstring
    """
    name = models.CharField(
        max_length=128
    )
    kur_adı = models.ForeignKey(
        Kurlar,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    kullanıcı = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )
class Wallet_kur(models.Model):
    """
    docstring
    """
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    kur_fiyat = models.ForeignKey(
        KurFiyatlari,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    bakiye = models.FloatField(
        default=0
    )
    date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )