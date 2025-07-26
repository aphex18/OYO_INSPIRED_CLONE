# home/seed.py it is a custom function used to seed the database with initial data for testing purposes.
# It creates 100 hotel vendors and 100 hotels with random data using the Faker library.
# use multiple times to create more data if needed.

from django.contrib.auth.models import User
from accounts.models import *
from faker import Faker
fake = Faker()
import random

def createUser():
    for i in range(100):
        email = fake.email()
        HotelVender.objects.create(
            email = email,
            business_name = fake.name(),
            username = email,
            first_name = fake.name(),
            phone_number = random.randint(1111111111, 9999999999)
        )


from random import choice
def createHotel():
    for i in range(100):
        hotel_vendor = choice(HotelVender.objects.all())
        amenities = list(Amenities.objects.all())
        hotel = Hotel.objects.create(
            hotel_name=fake.company(),
            hotel_description=fake.text(),
            hotel_slug=fake.slug(),
            hotel_owner=hotel_vendor,
            hotel_price=fake.random_number(digits=4) / 100.0,
            hotel_offer_price=fake.random_number(digits=4) / 100.0,
            hotel_location=fake.address(),
            is_active=fake.boolean()
        )
        hotel.amenities.set(amenities)