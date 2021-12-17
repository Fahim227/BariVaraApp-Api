from django.contrib import admin

# Register your models here.

from .models import owner,renter,earning,flat_details,remain,request_for_rent

admin.site.register([owner,renter,earning,flat_details,remain,request_for_rent])