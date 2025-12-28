from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HotelUser(User):
    profile_picture = models.ImageField(upload_to='profile', null=True, blank=True)
    # username = models.CharField(unique=True, max_length=100)
    phone_number = models.CharField(unique=True, max_length=100)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta :
        db_table = "hotel_user"

class HotelVendor(User):
    phone_number = models.CharField(unique=True, max_length=100)
    business_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile')
    email_token = models.CharField(max_length=100, null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta :
        db_table = "hotel_vendor"

class Ameneties(models.Model):
    name = models.CharField(max_length = 1000)
    icon = models.ImageField(upload_to="hotels")

    def __str__(self) -> str:
        return self.name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_discription = models.TextField(max_length=500)
    hotel_slug = models.SlugField(unique=True, max_length=1000)
    hotel_owner = models.ForeignKey(HotelVendor, on_delete=models.CASCADE, related_name='hotels')
    ameneties = models.ManyToManyField(Ameneties)
    hotel_price = models.FloatField()
    hotel_offer_price = models.FloatField()
    hotel_location = models.TextField()
    is_active = models.BooleanField(default=True)
    # hotel_address = models.TextField()
    


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')
    hotel_images = models.ImageField(upload_to='hotel_images')
    # images = models.ImageField(upload_to='hotel_images')
    # hotel_city = models.CharField(max_length=100)
    # hotel_state = models.CharField(max_length=100)
    # hotel_country = models.CharField(max_length=100)
    # hotel_zipcode = models.CharField(max_length=20)
    # hotel_description = models.TextField()
    

class HotelManager(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='managers')
    manager_name = models.CharField(max_length=50)
    manager_contact = models.CharField(max_length=100)

class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE, related_name='bookings')
    booking_user = models.ForeignKey(HotelUser, on_delete=models.CASCADE)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    price = models.FloatField()