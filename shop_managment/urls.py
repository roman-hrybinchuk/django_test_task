from django.urls import path

from shop_managment.views import TradePointList, CreateVisit

app_name = 'shop_managment'

urlpatterns = [
    path('trade-points', TradePointList.as_view(), name='trade-point'),
    path('visit/create', CreateVisit.as_view(), name='create-visit'),
]
