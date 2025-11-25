# SportZone - Django Veb Tətbiqi

Sport alətləri kataloqu üçün Django ilə hazırlanmış statik veb səhifə.

## Layihə Haqqında

Bu layihə, Laboratoriya işi №4 çərçivəsində Python Django freymvörkü istifadə edərək hazırlanmış sadə bir statik veb səhifədir. Layihədə GitHub-dan əldə edilmiş hazır HTML şablonu Django-ya inteqrasiya edilmişdir.

## Texnologiyalar

- **Python 3.11.0**
- **Django 5.2.8**
- **HTML5**
- **CSS3**
- **Font Awesome 6.0**
- **Google Fonts (Poppins)**

## Layihə Strukturu

```
sportzone_project/
├── catalog/                    # Əsas tətbiq
│   ├── static/                # Statik fayllar
│   │   ├── css/              # CSS faylları
│   │   └── images/           # Şəkil faylları
│   ├── templates/            # HTML şablonları
│   │   └── index.html       # Ana səhifə şablonu
│   ├── views.py             # Görünüş funksiyaları
│   └── urls.py              # URL konfiqurasiyası
├── sportzone_project/         # Layihə konfiqurasiyası
│   ├── settings.py           # Əsas tənzimlər
│   └── urls.py              # Əsas URL konfiqurasiyası
├── screenshots/              # Veb səhifə ekran görüntüləri
├── lab_report.md            # Ətraflı laboratoriya hesabatı
├── test_results.md          # Test nəticələri
└── manage.py                # Django idarəetmə skripti
```

## Quraşdırma və İşə Salma

### 1. Virtual mühit yaratmaq və aktivləşdirmək

```bash
python3.11 -m venv django_env
source django_env/bin/activate
```

### 2. Django quraşdırmaq

```bash
pip install django
```

### 3. Layihə qovluğuna keçmək

```bash
cd sportzone_project
```

### 4. Development serverini başlatmaq

```bash
python manage.py runserver
```

### 5. Brauzerdə açmaq

Brauzerinizə daxil olaraq aşağıdakı ünvana keçin:

```
http://127.0.0.1:8000/
```

## Xüsusiyyətlər

- ✅ Responsive dizayn
- ✅ 6 məhsul kateqoriyası
- ✅ 8 məhsul kartı
- ✅ Newsletter abunəlik forması
- ✅ Sosial media inteqrasiyası
- ✅ Modern və təmiz interfeys

## Ekran Görüntüləri

Layihənin ekran görüntüləri `screenshots/` qovluğunda mövcuddur:

- `homepage_top.webp` - Ana səhifənin yuxarı hissəsi
- `products_section.webp` - Məhsullar bölməsi
- `footer_section.webp` - Footer bölməsi

## Ətraflı Sənədləşmə

Layihənin tam sənədləşməsi və addım-addım izahı üçün `lab_report.md` faylına baxın.

## Müəllif

Manus AI

## Tarix

25 Noyabr 2025
