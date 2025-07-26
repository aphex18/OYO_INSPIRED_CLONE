from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class HotelUser(User):
    profile_picture = models.ImageField(upload_to='images/profile_pics/user/')
    phone_number = models.CharField(max_length=15, unique= True)
    email_token = models.CharField(max_length=100, blank=True, null=True)
    otp = models.CharField(max_length=10, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'hotel_user'

class HotelVender(User):
    profile_picture = models.ImageField(upload_to='images/profile_pics/vendor/')
    business_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, unique= True)
    email_token = models.CharField(max_length=100, blank=True, null=True)
    otp = models.CharField(max_length=10, blank=True, null=True)
    is_verified = models.BooleanField(default=False)


    class Meta:
        db_table = 'hotel_vender'



class Amenities(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/hotels/amenities_icons/')


    def __str__(self):
        return self.name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_description = models.TextField()
    hotel_slug = models.SlugField(max_length=191, unique=True)
    hotel_owner = models.ForeignKey(HotelVender, on_delete=models.CASCADE, related_name='hotels')
    amenities = models.ManyToManyField(Amenities)
    hotel_price = models.FloatField()
    hotel_offer_price = models.FloatField()
    hotel_location = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.hotel_name


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotels_images')
    image = models.ImageField(upload_to='images/hotels/hotel_images/')


class HotelManager(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_managers')
    manager_name = models.CharField(max_length = 100)
    manager_contact = models.CharField(max_length = 100)


class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_bookings')
    booking_user = models.ForeignKey(HotelUser, on_delete=models.CASCADE ,)
    booking_date = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.FloatField()

    class Meta:
        db_table = 'hotel_booking'

    # booking_user = models.ForeignKey(HotelUser, on_delete = models.CASCADE )
    # booking_start_date = models.DateField()
    # booking_end_date = models.DateField()
    # price = models.FloatField()

    # def __str__(self):
    #     return f"Booking for {self.hotel.hotel_name} by {self.booking_user.username}"