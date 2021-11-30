from django.contrib import admin

# Register your models here.

from .models import owner,renter,earning,flat_details,remain

admin.site.register([owner,renter,earning,flat_details,remain])