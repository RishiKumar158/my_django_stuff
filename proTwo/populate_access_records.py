import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proTwo.settings')

import django
django.setup()

import random
from appTwo.models import AccessRecord, Topic, Webpage
from faker import Faker
fakegen = Faker()

topics = ['Games', 'Books', 'News', 'Entertainment', 'Food', 'Health']

def add_topic():
    t = Topic.objects.get_or_create(name = random.choice(topics))[0]
    return t

def populate(N = 5):
    for entry in range(N):
        top = add_topic()

        fake_company = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        webpg = Webpage.objects.get_or_create(topic = top, company = fake_company, url = fake_url)[0]

        AccessRecord.objects.get_or_create(webpage = webpg, date = fake_date)
    
if __name__ == '__main__':
    print('Populating access records!')
    populate(20)
    print('population completed!!')

