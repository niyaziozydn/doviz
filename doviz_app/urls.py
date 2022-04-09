from django.contrib import admin
from django.urls import path
from doviz_app import views
from django.contrib.auth import logout


urlpatterns = [
    path('home', views.doviz_hesapla, name='home'),
    path('', views.login, name='login'),
    path('kayit', views.kayit, name="kayit"),
    path('logout', views.logoutUser, name='logout'),
    path('detay', views.detay, name="detay"),
    path('cuzdan/list', views.wallet_list, name="wallet_list"),
    path('create/wallet', views.create_wallet, name="create_wallet"),
    path('add/wallet', views.add_wallet, name="wallet_add"),
    path('sell/wallet', views.sell_wallet, name="wallet_sell"),
    path('wallet/islem/gecmisi', views.wallet_kur_list, name="wallet_kur_list"),

]
