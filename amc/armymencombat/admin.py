from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Users)
admin.site.register(Lists)
admin.site.register(Infantry)
admin.site.register(Vehicle)
admin.site.register(Weapons)
admin.site.register(Infantry_Upgrades)
admin.site.register(Vehicle_Upgrades)
admin.site.register(j_user_list)
admin.site.register(j_user_list_rating)
admin.site.register(j_list_entry)
admin.site.register(j_infantry_upgrade)
admin.site.register(j_vehicle_upgrade)
admin.site.register(Rules)
