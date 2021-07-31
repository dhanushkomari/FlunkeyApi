from django.urls import path
from . import views

app_name = 'FlunkeyApp'

urlpatterns = [
    path('', views.selectBot, name = 'select-bot'),
    path('bot/<str:bot>', views.selectTable, name = 'select-table'),
    path('table/<str:table>/delivery', views.DeliveryView, name = 'delivery'),
    path('api-data/latest', views.GetApiView, name = 'get-api'),
    path('api-data/update-bot/<str:id>', views.UpdateBotView, name = 'bot-update'),
    path('api-data/update-table/<str:id>', views.UpdateTableView, name = 'table-update'),

    path('check', views.check)
]
