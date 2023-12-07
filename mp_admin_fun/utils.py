from faker import Faker
from faker.providers import phone_number
from mp_admin_fun.models import Developer
from random import randint


def populate_developer_model_with_fake_info():
    fake = Faker(locale='en_US')
    fake.add_provider(phone_number)
    for i in range(1000):
        Developer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.basic_phone_number(),
            street_address=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            zip_code=fake.zipcode(),
        )


def assign_devs_to_companies():
    for dev in Developer.objects.all():
        dev.company_id = randint(1,9)
        dev.save()