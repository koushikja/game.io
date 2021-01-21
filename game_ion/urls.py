from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from gamer_zone.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('login/', signin),
    path('logout/', signout),
    path('<int:user_id>/games/', games),
    path('<int:user_id>/games/indoor/', indoorGames),
    path('<int:user_id>/games/outdoor/', outdoorGames),
    path('<int:user_id>/kitchen/', kitchen),
    path('<int:user_id>/home/', home),
    path('<int:user_id>/games/<int:game_id>/', game),
    path('<int:user_id>/games/<int:game_id>/playgame/', playgame),
    path('<int:user_id>/kitchen/<int:item_id>/', food),
    path('<int:user_id>/kitchen/<int:item_id>/placeorder/', placeOrder),
    path('<int:user_id>/finalbill/', finalBill),
    path('<int:user_id>/finalbill/pay/', payBill),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
