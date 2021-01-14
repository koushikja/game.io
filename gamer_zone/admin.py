from django.contrib import admin
from gamer_zone.models import FinalCheckout, FoodBooked, GameBooked, Game, Kitchen, UserDetail

# Register your models here.

admin.site.register(UserDetail)
admin.site.register(Game)
admin.site.register(Kitchen)
admin.site.register(GameBooked)
admin.site.register(FoodBooked)
admin.site.register(FinalCheckout)
