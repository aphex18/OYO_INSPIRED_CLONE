from django.contrib import admin
from  .models import *
# Register your models here.

admin.site.register(HotelUser)
admin.site.register(HotelVender)
admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelBooking)