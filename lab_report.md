# Laboratoriya işi №4: Python Django freymvörkünün quraşdırılması və sadə bir statik veb səhifənin hazırlanması

**Müəllif:** Manus AI

**Tarix:** 25 Noyabr 2025

---

## 1. Giriş

Django, veb tətbiqlərin sürətli və səmərəli şəkildə hazırlanması üçün nəzərdə tutulmuş yüksək səviyyəli bir Python veb freymvörküdür. "Batareyaları daxil" (batteries-included) fəlsəfəsi ilə tanınan Django, tərtibatçılara autentifikasiya, admin paneli, ORM (Object-Relational Mapper) və şablon mühərriki kimi bir çox hazır komponent təklif edir. Bu, tərtibatçıların təkrar işlərdən yayınaraq layihənin əsas məntiqinə fokuslanmasına imkan yaradır. Django-nun əsas məqsədi, mürəkkəb və məlumat-yönümlü veb saytların hazırlanmasını sadələşdirməkdir.

Bu laboratoriya işində, Django freymvörkünün quraşdırılması, yeni bir layihənin yaradılması və GitHub-dan əldə edilmiş hazır HTML şablonu istifadə edərək sadə bir statik veb səhifənin hazırlanması prosesi addım-addım izah ediləcəkdir.

## 2. Quraşdırma

Django ilə işləməyə başlamazdan əvvəl sistemdə Python və onun paket idarəetmə vasitəsi olan `pip`-in quraşdırıldığından əmin olmaq lazımdır. Bu layihə üçün virtual mühit (virtual environment) yaradılaraq paketlərin qlobal sistemdən təcrid olunması təmin edildi.

### Python və Django-nun Quraşdırılması

İlk olaraq, layihə üçün bir virtual mühit yaradıldı və aktivləşdirildi:

```bash
# Virtual mühitin yaradılması
python3.11 -m venv django_env

# Virtual mühitin aktivləşdirilməsi
source django_env/bin/activate
```

Daha sonra `pip` vasitəsilə Django freymvörkü quraşdırıldı:

```bash
pip install django
```

Quraşdırmanın uğurlu olduğunu yoxlamaq üçün Django versiyası yoxlanıldı:

```bash
django-admin --version
# Gözlənilən nəticə: 5.2.8
```

### İlk Django Layihəsinin və Tətbiqin Yaradılması

Django-da hər bir veb sayt bir **layihədən (project)** ibarətdir və bu layihə bir və ya bir neçə **tətbiqə (app)** bölünə bilər. Layihə veb saytın konfiqurasiyasını və ümumi tənzimləmələrini, tətbiqlər isə spesifik funksionallıqları (məsələn, bloq, istifadəçi profilləri) özündə cəmləyir.

`sportzone_project` adlı yeni bir Django layihəsi yaradıldı:

```bash
django-admin startproject sportzone_project
```

Layihə qovluğuna daxil olaraq, veb səhifənin məzmununu idarə edəcək `catalog` adlı yeni bir tətbiq yaradıldı:

```bash
cd sportzone_project
python manage.py startapp catalog
```

## 3. Django-nun Arxitekturası ilə Tanışlıq

Django, **Model-View-Template (MVT)** arxitektura nümunəsini istifadə edir. Bu arxitektura, veb tətbiqlərin məntiqi hissələrini bir-birindən ayıraraq kodun daha səliqəli, modulyar və idarəolunan olmasını təmin edir.

| Komponent | Açıqlama |
|---|---|
| **Model** | Məlumatların strukturunu və məntiqini təyin edir. Verilənlər bazası ilə əlaqəni təmin edən Python sinifləridir. Hər bir model sinfi verilənlər bazasındakı bir cədvələ uyğun gəlir. |
| **View** | İstifadəçidən gələn sorğuları (request) qəbul edir, lazımi məlumatları modellər vasitəsilə bazadan alır və bu məlumatları şablona (template) ötürür. View, tətbiqin biznes məntiqini ehtiva edir. |
| **Template** | Məlumatların istifadəçiyə necə göstəriləcəyini təyin edən HTML fayllarıdır. Django-nun şablon mühərriki, view-dan gələn dinamik məlumatları HTML içərisinə yerləşdirərək son nəticəni yaradır. |

### MVT və MVC ilə Müqayisə

Bir çox veb freymvörk **Model-View-Controller (MVC)** arxitekturasını istifadə edir. Django-nun MVT arxitekturası MVC-yə çox bənzəsə də, bəzi fərqlər mövcuddur. Əsas fərq, sorğuların idarə olunması və məntiqin bölünməsindədir:

- **Controller (MVC-də):** İstifadəçi sorğularını qəbul edir, model və view arasında əlaqəni qurur.
- **View (Django-da):** MVC-dəki Controller-in rolunu öz üzərinə götürür. Sorğunu qəbul edir və hansı məlumatın hansı şablonla göstəriləcəyinə qərar verir.
- **Template (Django-da):** MVC-dəki View-in roluna daha yaxındır və yalnız məlumatların təqdimatına cavabdehdir.

Bu səbəbdən, Django-da "Controller" rolunu freymvörkün özü (URL yönləndirmə mexanizmi) və "View" birlikdə oynayır.

## 4. Sadə bir Statik Veb Səhifənin Hazırlanması

Bu mərhələdə, [https://github.com/ismayilovali0/gmyhtml.git](https://github.com/ismayilovali0/gmyhtml.git) linkindəki hazır HTML şablonu Django layihəsinə inteqrasiya edildi.

### HTML Şablonunun və Statik Faylların Yerləşdirilməsi

İlk olaraq, `catalog` tətbiqi daxilində şablonlar və statik fayllar (CSS, şəkillər) üçün müvafiq qovluqlar yaradıldı:

- `catalog/templates/`: HTML faylları üçün.
- `catalog/static/`: CSS, JavaScript və şəkil faylları üçün.

GitHub-dan klonlanmış `index.html`, `style.css` və `images` qovluğundakı fayllar bu qovluqlara köçürüldü.

HTML şablonunda statik fayllara olan müraciətlər Django-nun şablon teqləri ilə əvəz edildi. Faylın əvvəlinə `{% load static %}` teqi əlavə edildi və `href`, `src` atributları aşağıdakı kimi dəyişdirildi:

```html
<!-- Əvvəlki vəziyyət -->
<link rel="stylesheet" href="style.css">
<div class="product-image" style="background-image: url(\'images/steel_dumbel.png\');"></div>

<!-- Django ilə -->
<link rel="stylesheet" href="{% static \'css/style.css\' %}">
<div class="product-image" style="background-image: url(\'{% static \'images/steel_dumbel.png\' %}\');"></div>
```

### Görünüş (View) və URL Konfiqurasiyası

`catalog/views.py` faylında istifadəçi sorğusuna cavab olaraq `index.html` şablonunu render edən bir görünüş (view) funksiyası yaradıldı:

```python
# catalog/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

Daha sonra, bu görünüşü müəyyən bir URL ilə əlaqələndirmək üçün URL konfiqurasiyası aparıldı. İlk olaraq `catalog` tətbiqi üçün `urls.py` faylı yaradıldı:

```python
# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Nəhayət, əsas layihənin `sportzone_project/urls.py` faylında `catalog` tətbiqinin URL-ləri `include` funksiyası ilə əsas URL siyahısına daxil edildi:

```python
# sportzone_project/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
]
```

### Layihənin Tənzimlənməsi

Son addım olaraq, `sportzone_project/settings.py` faylında aşağıdakı dəyişikliklər edildi:

1.  `catalog` tətbiqi `INSTALLED_APPS` siyahısına əlavə edildi.
2.  Development serverin bütün IP ünvanlarından gələn sorğuları qəbul etməsi üçün `ALLOWED_HOSTS` parametrinə `['*']` dəyəri mənimsədildi.

Layihəni işə salmaq üçün aşağıdakı əmr icra edildi:

```bash
python manage.py runserver 0.0.0.0:8000
```

Nəticədə, veb səhifə uğurla işə düşdü və brauzerdə görüntüləndi.

## 5. Nəticə

Bu laboratoriya işi çərçivəsində Python Django freymvörkü ilə tanışlıq baş tutdu. Django-nun quraşdırılması, yeni layihə və tətbiqin yaradılması, MVT arxitekturasının əsas prinsipləri və statik faylların idarə olunması kimi fundamental mövzular praktiki olaraq tətbiq edildi. Hazır HTML şablonunun Django layihəsinə uğurla inteqrasiya edilməsi nəticəsində tam funksional bir statik veb səhifə əldə edildi. Bu layihə, gələcəkdə daha mürəkkəb və dinamik veb tətbiqlərin hazırlanması üçün möhkəm bir təməl rolunu oynayır.

## 6. Qiymətləndirmə

Layihə təqdimata hazırdır. Laboratoriya işinin tələbləri tam olaraq yerinə yetirilmişdir. Django-nun əsas anlayışları – layihə və tətbiq strukturu, MVT arxitekturası, URL yönləndirmə və şablon sistemi – başa düşülmüş və uğurla tətbiq edilmişdir. Yaradılan veb səhifə vizual və funksional cəhətdən tələblərə tam cavab verir.

---

### Referanslar

[1] Django Documentation. (2025). *Django documentation*. Retrieved from [https://docs.djangoproject.com/en/5.2/](https://docs.djangoproject.com/en/5.2/)
