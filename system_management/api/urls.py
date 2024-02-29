from django.urls import path
from system_management.api.views import generate_voucher_api, login_api, redeem_voucher_api, register_api

urlpatterns = [
    path('login_api/', login_api, name='login_api'),
    path('register_api/', register_api, name='register_api'),
    path('generate_voucher_api/', generate_voucher_api, name='generate_voucher_api'),
    path('redeem_voucher_api/', redeem_voucher_api, name='redeem_voucher_api'),


]