import json
import requests
import datetime
from django.shortcuts import render
from doviz_app.models import Kurlar, KurFiyatlari, Param, Wallet, Wallet_kur
from django.contrib.auth import authenticate
from django.contrib.auth import login as a_log

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_r


@login_required
def doviz_hesapla(request):
    """
    docstring
    """
    # url = "http://data.fixer.io/api/{}?access_key=f84a03e5e72ea64fa315e769592f1cb2&symbols={}&format=1"
    # date = datetime.datetime.now().date()
    # kur_son = Kurlar.objects.filter()
    # kurlar = ""
    # for z in kur_son:
    #     kurlar += z.kur_adı + ','
    # for x in range(50):
    #     date = date - datetime.timedelta(days=x)
    #     date_1 = date.strftime("%Y-%m-%d")
    #     url = url.format(date_1, kurlar)
    #     print("url", url)
    #     req = requests.get(url)
    #     for k in kur_son:
    #         kur_fiyatlari = KurFiyatlari()
    #         fiyatlar = req.json()
    #         print("fiyatlar")
    #         fiyat = fiyatlar.get("rates").get(k.kur_adı)
    #         kur_fiyatlari.kur_adı = k
    #         kur_fiyatlari.fiyat = fiyat
    #         kur_fiyatlari.save()
    
    # lll = KurFiyatlari.objects.filter()
    # print("llllll",lll)
    post = request.GET
    donusen_para_turu = post.get('donusen_para_turu')
    alınan_para_turu = post.get('alınan_para_turu')
    para_miktar = post.get('para_miktar')
    sonuc_parası = 0
    print(donusen_para_turu, alınan_para_turu, para_miktar)

    hata = ""
    if donusen_para_turu:

        # api_url = 'https://api.exchangeratesapi.io/latest?base='
        
        # result = requests.get(api_url+donusen_para_turu)
        # result = json.loads(result.text)
        # print(result)
        # try:
        #     url = "https://api.collectapi.com/economy/exchange?int=10&to=EUR&base=USD"

        #     headers = {
        #         'content-type': "application/json",
        #         'authorization': "apikey 3LCENSdHXcCAUEmcxdwCYp:5yCd2MTzLzFha1WuLaoq6s"
        #     }

        #     # url = url.format(para_miktar, donusen_para_turu, alınan_para_turu)

        #     req = requests.get(url, headers=headers)
        #     print("req", req.json())
        #     req_json = req.json().get("result").get("data")[0].get('rate')

        #     sonuc_parası = float("para_miktar") * req_json
        # except:
        #     hata = "Bir Hata Oluştu Lütfen Daha Sonra Deneyin"

        # print(KurFiyatlari.objects.filter())
        # a = KurFiyatlari.objects.filter()
        # for x in a:
        #     print(x.kur_adı.kur_adı)
        #     print(x.fiyat)

        kur_fiyatlari = KurFiyatlari.objects.filter(kur_adı__kur_adı=alınan_para_turu).first()
        kur_fiyat = kur_fiyatlari.fiyat
        sonuc_parası = float(para_miktar) * kur_fiyat
        param = Param()

        param.kur_adı = kur_fiyatlari
        param.donusturulen = float(para_miktar)
        param.donusen = sonuc_parası
        param.kullanıcı = request.user
        param.save()




    # api_url = 'https://api.exchangeratesapi.io/latest?base='

    # result = requests.get(api_url+)
    # result = json.loads(result.text)
    # for x,y in result['rates'].items():
    #     kur = Kurlar.objects.get_or_create(
    #         kur_adı=x
    #     )
    
    kur_son = Kurlar.objects.filter()
    para = Param.objects.filter(kullanıcı=request.user)
    kurlar = []
    for z in kur_son:
        kurlar.append({
            'kur_adı': z.kur_adı
        })
    pa = []
    for x in para:
        pa.append({ 
            'user': x.kullanıcı.username,
            'kur_adı': x.kur_adı.kur_adı.kur_adı,
            'donusturulen': x.donusturulen,
            'donusen': x.donusen,
            'date': x.date
        })

    return render(request, 'doviz_main.html', {'pa': pa, 'kurlar': kurlar, 'sonuc_parası': sonuc_parası, 'alinan_para':alınan_para_turu, 'hata': hata } )


def login(request):
    post =  request.POST
    user = post.get("login")
    password = post.get("password")
    print("asdfasd",password, user)
    if request.user.username:
        return redirect('home')
    u = authenticate(username=user, password=password)
    hata = ''
    print(u)
    print(user,password)
    if post:
        if u is not None:
            a_log(request, u)
            hata = "hata yok"
            return redirect('home')
        else:
            hata = "Kullanıcı Bulunamadı"
    return render(request, 'login.html', {'hata':hata} )

def kayit(request):
    post =  request.POST
    user1 = post.get("login")
    password = post.get("password")
    password2 = post.get("password2")
    hata = ''

    if not password == password2:
        hata = "Şifreler uyuşmuyor"
    if post:
        userr,re = User.objects.get_or_create(username=user1)
        print(userr,re)
        userr.set_password(password)
        userr.save()
        print(userr)

        a_log(request, userr)
        return redirect('home')
        
    return render(request, 'kayit.html', {'hata': hata})

def logoutUser(request):
    logout_r(request)      
    return redirect('login')
    # Redirect to a success page.

def hesap():
    url = "http://data.fixer.io/api/{}?access_key=f84a03e5e72ea64fa315e769592f1cb2&symbols={}&format=1"
    date = datetime.datetime.now().date()
    kur_son = Kurlar.objects.filter()
    kurlar = ""
    for z in kur_son:
        kurlar += z.kur_adı + ','
    date = date
    date_1 = date.strftime("%Y-%m-%d")
    url = url.format(date_1, kurlar)
    print("url", url)
    req = requests.get(url)
    for k in kur_son:
        kur_fiyatlari = KurFiyatlari()
        fiyatlar = req.json()
        print("fiyatlar")
        fiyat = fiyatlar.get("rates").get(k.kur_adı)
        kur_fiyatlari.kur_adı = k
        kur_fiyatlari.fiyat = fiyat
        kur_fiyatlari.save()

@login_required
def detay(request):
    """
    docstring
    """
    kur_son = Kurlar.objects.filter()
    para = Param.objects.filter(kullanıcı=request.user)
    kurlar = []
    for z in kur_son:
        kurlar.append({
            'kur_adı': z.kur_adı
        })
    pa = []
    for x in para:
        pa.append({ 
            'user': x.kullanıcı.username,
            'kur_adı': x.kur_adı.kur_adı.kur_adı,
            'donusturulen': x.donusturulen,
            'donusen': x.donusen,
            'date': x.date
        })

    return render(request, 'gecmis.html', {'pa': pa} )

@login_required
def wallet_list(request):
    """
    docstring
    """
    wal = Wallet.objects.filter(kullanıcı=request.user)
    wal_list = []
    last_baki = 0
    for x in wal:
        last_baki = 0
        baki = x.wallet_kur_set.filter()
        for ba in baki:
            last_baki += ba.bakiye
        wal_list.append({ 
            'user': x.kullanıcı.username,
            'kur_adı': x.kur_adı.kur_adı if x.kur_adı else '',
            'name': x.name,
            'date': x.date,
            'bakiye': last_baki
        })

    return render(request, 'wallet_list.html', {'wal_list': wal_list} )

def create_wallet(request):
    get = request.GET
    name = get.get('name')
    kur = get.get('kur')
    kur_son = Kurlar.objects.filter()
    kurlar = []
    for z in kur_son:
        kurlar.append({
            'kur_adı': z.kur_adı
        })
    if name:
        kur_son1 = Kurlar.objects.filter()
        print(kur_son1)
        for z in kur_son1:
            print(z.kur_adı)
        kur_son = Kurlar.objects.filter(kur_adı=kur).first()
        print(kur_son)
        cuzdan = Wallet()
        cuzdan.name = name
        cuzdan.kur_adı = kur_son
        cuzdan.kullanıcı = request.user
        cuzdan.save()

        return redirect('wallet_list')
    
    return render(request, 'wallet.html', {'kurlar':kurlar} )


def add_wallet(request):
    get = request.GET
    para = get.get('para')
    cuzdan_adı = get.get('cuzdan_adı')
    cuzdans = Wallet.objects.filter()
    cuzdanlar = []
    for z in cuzdans:
        cuzdanlar.append({
            'name': z.name
        })
    if para:
        cuzdan = Wallet.objects.get(name=cuzdan_adı)
        kur_fiyatlari = KurFiyatlari.objects.filter(kur_adı=cuzdan.kur_adı).last()
        print(kur_fiyatlari)
        cuzdan_bakiye = Wallet_kur()
        cuzdan_bakiye.wallet = cuzdan
        cuzdan_bakiye.bakiye = float(para)
        cuzdan_bakiye.kur_fiyat = kur_fiyatlari
        cuzdan_bakiye.save()

        return redirect('wallet_list')
    
    return render(request, 'add_wallet.html', {'cuzdanlar':cuzdanlar} )


def wallet_kur_list(request):
    wal_kur = Wallet_kur.objects.filter()
    hesap()
    wal_kur_list = []
    last_baki = 0
    for x in wal_kur:
        kur_fiyat = x.kur_fiyat.fiyat
        kur_fiyatlari = KurFiyatlari.objects.filter(kur_adı=x.wallet.kur_adı).last()
        ilk_deger = kur_fiyat * x.bakiye
        last_deger = (kur_fiyatlari.fiyat * x.bakiye) - ilk_deger
        wal_kur_list.append({ 
            'cuzdan_name': x.wallet.name,
            'kur_adı': x.wallet.kur_adı.kur_adı,
            'bakiye': x.bakiye,
            'kur_degeri': kur_fiyat,
            'date': x.date,
            'simdiki_kur_değeri': kur_fiyatlari.fiyat,
            'kar_zarar': round(last_deger, 4)
        })

    return render(request, 'wallet_kur_list.html', {'wal_kur_list': wal_kur_list} )

def sell_wallet(request):
    pass
    # get = request.GET
    # hata = ''
    # para = get.get('para')
    # cuzdan_adı = get.get('cuzdan_adı')
    # cuzdans = Wallet.objects.filter(wallet_kur__isnull=False, wallet_kur__bakiye__gte=0)
    # cuzdanlar = []
    # for z in cuzdans:
    #     cuzdanlar.append({
    #         'name': z.name
    #     })
    # if para:
    #     cuzdan = Wallet.objects.get(name=cuzdan_adı)
    #     print(cuzdan)
    #     cuzdan_bakiye = Wallet_kur()
    #     if cuzdan_bakiye.bakiye < float(para):
    #         hata = 'Yetersiz Bakiye Bakiyeniz: ' + str(cuzdan_bakiye.bakiye) 
    #     else:
    #         cuzdan_bakiye.bakiye = float(-para)
    #         cuzdan_bakiye.wallet = cuzdan
    #         cuzdan_bakiye.save()
    
    # return render(request, 'wallet_sell.html', {'cuzdanlar':cuzdanlar, 'hata': hata} )
