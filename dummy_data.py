from email.mime import image
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from products.models import Product , Category , Brand
import random
from faker import Faker

def seed_category(n):
    fake =Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    for _ in range(n):
        name = fake.name()
        image = f'category/{images[random.randint(0,4)]}'
        Category.objects.create(
            name = name,
            image = image,
        )
    print(f'successfully Seeded {n} Category')


def seed_brand(n):
    fake =Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    for _ in range(n):
        name = fake.name()
        image = f'brands/{images[random.randint(0,4)]}'
        Brand.objects.create(
            name = name,
            image = image,
            category = Category.objects.get(id=random.randint(17,26))
        )
    print(f'successfully Seeded {n} Brand')


def seed_product(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpeg','4.jpg','5.jpeg','6.jpg','7.png','8.jpg','9.jpg']
    flag_type = ['New','Feature','Sale']
    for _ in range(n):
        name = fake.name()
        image = f'product/{images[random.randint(0,8)]}'
        sku = random.randint(1000,100000)
        subtitle = fake.text(max_nb_chars=500)
        desc = fake.text(max_nb_chars=10000)
        price = round(random.uniform(20.99,99.99),2)
        flag = flag_type[random.randint(0,2)]
        quantity = random.randint(1,100)
        Product.objects.create(
            name = name,
            image = image,
            sku = sku,
            subtitle = subtitle,
            desc = desc,
            price = price,
            flag = flag,
            quantity = quantity,
            brand = Brand.objects.get(id=random.randint(38,47)),
            category = Category.objects.get(id=random.randint(17,26)),   
            
        )
    print(f'successfully Seeded {n} Products')


#seed_category(10)
#seed_brand(10)
#seed_product(1000)