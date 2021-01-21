from django.db import models
from django.contrib.auth.models import User

# Create your models here.

game_category = {
    ('indoor','indoor games'),
    ('outdoor','outdoor games')
}

item_category = {
    ('drinks','drinks'),
    ('chats','chats'),
    ('snacks','snacks'),
    ('others','others')

}

class UserDetail(models.Model):
    user_info = models.OneToOneField(User , on_delete = models.CASCADE , null=True , blank=True)
    user_phone = models.IntegerField(blank=True , null=True)
    
    def __str__(self):
        return self.user_info.username

class Game(models.Model):
    game_img = models.ImageField(null=True, blank=True, upload_to="projects-images/")
    game_name = models.CharField(max_length=100 , blank=True , null=True)
    game_type = models.CharField(max_length=100 , blank=True , null=True , choices= game_category)
    game_rules = models.TextField(blank=True , null=True)
    game_price = models.IntegerField(blank=True , null=True)

    def __str__(self):
        return self.game_name

class Kitchen(models.Model):
    item_img = models.ImageField(null=True, blank=True, upload_to="projects-images/")
    item_name = models.CharField(max_length=100 , blank=True , null=True)
    item_type = models.CharField(max_length=100 , blank=True , null=True , choices= item_category)
    item_description = models.TextField(blank=True , null=True)
    item_price = models.IntegerField(blank=True , null=True)

    def __str__(self):
        return self.item_name

class GameBooked(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_info = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    game_time = models.CharField(max_length=100 , blank=True , null=True)
    game_time_start = models.TimeField(auto_now_add= True)
    total_game_price = models.IntegerField(blank=True , null=True)

    def __str__(self):
        return f"{self.game_info.game_name} | {self.user_info.username}"

class FoodBooked(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item_info = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=True, blank=True)
    item_quantity = models.CharField(max_length=100 , blank=True , null=True)
    total_item_price = models.IntegerField(blank=True , null=True)

    def __str__(self):
        return f"{self.item_info.item_name} | {self.user_info.username}"

class FinalCheckout(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_game_info = models.ForeignKey(GameBooked, on_delete=models.CASCADE, null=True, blank=True)
    user_item_info = models.ForeignKey(FoodBooked, on_delete=models.CASCADE, null=True, blank=True)
    total_bill_status = models.BooleanField(default=False)
    total_bill_amount = models.IntegerField(blank=True , null=True)

    def __str__(self):
        return self.user_info.username