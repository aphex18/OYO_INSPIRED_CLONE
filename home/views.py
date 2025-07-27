from django.shortcuts import render
from accounts.models import *
from django.views.decorators.cache import cache_page  # Import the cache_page decorator to enable per-view caching  # This allows caching the output of specific views for a defined duration
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
# Create your views here.


@cache_page(60 * 2)  # Cache the index view for 2 (120 seconds) minutes it will cache the output of this view for 2 minutes
def index(request):
    hotels = Hotel.objects.all().select_related('hotel_owner').prefetch_related('hotels_images', 'amenities')

    if request.GET.get('search'):
        hotels = hotels.filter(hotel_name__icontains = request.GET.get('search'))

    if request.GET.get('sort_by'):
        sort_by = request.GET.get('sort_by')
        if sort_by == "sort_low":
            hotels = hotels.order_by('hotel_offer_price')
        elif sort_by == "sort_high":
            hotels = hotels.order_by('-hotel_offer_price')
    return render(request, 'index.html', context = {'hotels' : hotels[:52]})



def hotel_description(request, slug):
    hotel = Hotel.objects.get(hotel_slug = slug)


    if request.method == "POST":
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        check_in_date = datetime.strptime(check_in_date , '%Y-%m-%d')
        check_out_date = datetime.strptime(check_out_date , '%Y-%m-%d')
        days_count = (check_out_date - check_in_date).days

        if days_count <= 0:
            messages.warning(request, "Invalid Booking Date.")

            return HttpResponseRedirect(request.path_info)


        HotelBooking.objects.create(
            hotel = hotel,
            booking_user = HotelUser.objects.get(id = request.user.id),
            check_in_date = check_in_date,
            check_out_date = check_out_date,
            total_price = hotel.hotel_offer_price * days_count
        )
        messages.success(request, "Booking Captured.")

        return HttpResponseRedirect(request.path_info)

    return render(request, 'hotel_description.html', context = {'hotel' : hotel})