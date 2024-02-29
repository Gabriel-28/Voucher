from django.urls import path
from system_management.views import create_voucher, login, redeem_voucher, register

urlpatterns = [
    
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('create_voucher/',create_voucher, name='create_voucher'),
    path('redeem_voucher/',redeem_voucher, name='redeem_voucher'),


]