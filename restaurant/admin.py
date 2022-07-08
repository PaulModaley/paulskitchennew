from django.contrib import admin
from .models import Booking, UserProfile, Contact

# Register your models here.
admin.site.site_header = "Pauls Kitchen Dashboard"


class BookingAdmin(admin.ModelAdmin):
    profile = "/workspace/paulskitchen/templates/restaurant/profile.html"


admin.site.register(Booking)
admin.site.register(UserProfile)
admin.site.register(Contact)
