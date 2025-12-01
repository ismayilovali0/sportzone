from django.core.management.base import BaseCommand
from catalog.models import Product

class Command(BaseCommand):
    help = 'Loads initial product data into the database'

    def handle(self, *args, **options):
        Product.objects.all().delete() # Əvvəlki məlumatları silmək

        products_data = [
            {
                "name": "Premium Qantel Dəsti",
                "description": "Peşəkar məşqlər üçün yüksək keyfiyyətli qantellər. Evdə və ya idman zalında istifadə üçün idealdır.",
                "category": "Qantellər",
                "image_url": "images/steel_dumbel.png",
                "meta_info": "20 kq",
                "rating": 4.8
            },
            {
                "name": "Premium Ştanq",
                "description": "Ağır çəki qaldırma məşqləri üçün yüksək keyfiyyətli, möhkəm ştanq. Olimpiya standartlarına uyğundur.",
                "category": "Barbellər",
                "image_url": "images/barbell-png.png",
                "meta_info": "20kg",
                "rating": 4.5
            },
            {
                "name": "Çəki Daşı",
                "description": "Sabit dəmir çəki daşı. Funksional məşqlər və güc artımı üçün əla seçimdir.",
                "category": "Çəki Daşları",
                "image_url": "images/15-kg-Set-.png",
                "meta_info": "15kg",
                "rating": 4.9
            },
            {
                "name": "Bench Masası",
                "description": "Rahat və möhkəm bench press masası. Tənzimlənən arxa dayağı ilə müxtəlif məşqlər etmək mümkündür.",
                "category": "Trenajorlar",
                "image_url": "images/becnh.png",
                "meta_info": "Tənzimlənən",
                "rating": 4.9
            },
            {
                "name": "Müqavimət Rezinləri Dəsti",
                "description": "Müxtəlif səviyyəli müqavimət üçün rezinlər. Reabilitasiya və ya əlavə məşq üçün idealdır.",
                "category": "Aksesuarlar",
                "image_url": "images/resistance.png",
                "meta_info": "5 səviyyə",
                "rating": 4.7
            },
            {
                "name": "Professional Qaşış Maşını",
                "description": "Yüksək sürət və uzun məsafəli qaçışlar üçün nəzərdə tutulmuş professional qaçış maşını.",
                "category": "Kardio",
                "image_url": "images/runforestrun.png",
                "meta_info": "20 km/saat",
                "rating": 4.6
            },
            {
                "name": "Yoga və Pilates Matı",
                "description": "Rahat və sürüşməyən məşq matı. Yoga, pilates və digər döşəmə məşqləri üçün mükəmməldir.",
                "category": "Aksesuarlar",
                "image_url": "images/yogamat.png",
                "meta_info": "10mm qalınlıq",
                "rating": 4.9
            },
            {
                "name": "İdman Butulkası",
                "description": "Su için. İdman zamanı su ehtiyacınızı ödəmək üçün böyük həcmli və davamlı butulka.",
                "category": "Aksesuarlar",
                "image_url": "images/bottle.png",
                "meta_info": "1 litr",
                "rating": 4.4
            },
        ]

        for data in products_data:
            Product.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {Product.objects.count()} products.'))
