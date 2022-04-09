from django.contrib import admin
from doviz_app.models import Kurlar, KurFiyatlari, Wallet_kur, Wallet

admin.site.register(Wallet)
admin.site.register(Wallet_kur)
admin.site.register(KurFiyatlari)