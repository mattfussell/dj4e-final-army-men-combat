from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

# Users table
class User(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
  

# Lists table
class Lists(models.Model):
    title = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

# Infantry table
class Infantry(models.Model):
    name = models.CharField(max_length=100)
    weapon_id = models.ForeignKey(models.Weapons, on_delete=models.CASCADE)
    min_squad_count = models.IntegerField(default=0)
    min_squad_points = models.IntegerField(default=0)
    max_squad_count = models.IntegerField(default=0)
    max_squad_points = models.IntegerField(default=0)
    special = models.CharField(max_length=250)
    has_grenade_or_C4 = models.BooleanField(default=False)
    has_bazooka_or_flamethrower = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Vehicle table
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    armor_bonus = models.IntegerField(default=0)
    weapon_id = models.ForeignKey(models.Weapons, on_delete=models.CASCADE)
    special = models.CharField(max_length=250)
    unit_count = models.IntegerField(default=0)
    unit_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Weapons table
class Weapons(models.Model):
    name = models.CharField(max_length=100)
    range = models.IntegerField(default=0)
    min_attack_count = models.IntegerField(default=0)
    max_attack_count = models.IntegerField(default=0)
    doubles_vs_vehicle = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

# Infantry_Upgrades table
class Infantry_Upgrades(models.Model):
    name = models.CharField(max_length=100)
    weapon_id = models.ForeignKey(models.Weapons, on_delete=models.CASCADE)
    upgrade_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

# Vehicle_Upgrades table
class Vehicle_Upgrades(models.Model):
    name = models.CharField(max_length=100)
    transport_bonus = models.IntegerField(default=0)
    armor_bonus = models.IntegerField(default=0)
    upgrade_points = models.IntegerField(default=0)
    weapon_id = models.ForeignKey(models.Weapons, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# User / List join table
class j_user_list(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list_id = models.ForeignKey(Lists, on_delete=models.CASCADE)


# User / List Rating join table
class j_user_list_rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list_id = models.ForeignKey(Lists, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


# List / Entry join table
class j_list_entry(models.Model):
    list_id = models.ForeignKey(Lists, on_delete=models.CASCADE)
    infantry_id = models.ForeignKey(Infantry, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


# Infantry / Upgrade join table
class j_infantry_upgrade(models.Model):
    infantry_id = models.ForeignKey(Infantry, on_delete=models.CASCADE)
    infantry_upgrade_id = models.ForeignKey(Infantry_Upgrades, on_delete=models.CASCADE)


# Vehicle / Upgrade join table
class j_vehicle_upgrade(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_upgrade_id = models.ForeignKey(Vehicle_Upgrades, on_delete=models.CASCADE)