import datetime
import json
import random
import secrets
import string
import requests
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse

from system_management.models import Voucher

def host_url(request):
    url = request.build_absolute_uri()
    index = url.index("system_management")
    url = url[0:index - 1]
    return url

def landing(request):
    return render(request, 'landing.html')

def login(request):
    """User login function with API."""
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        # Form data send using AJAX.
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        # URL for the login API.
        url = f"{host_url(request)}{reverse('login_api')}"
        # Payload containing the fields for the API.
        payload = json.dumps({
            "username": username,
            "password": password
        })
        # API header for the type of data format of the payload.
        headers = {
            'Content-Type': 'application/json',
        } 
        # Request to the API with method POST using requests library.
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=120)
            response_data = response.json()

            return JsonResponse(data=response_data, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
               
    return render(request, 'login.html')


def register(request):
    """User registration function with API."""
    url = f"{host_url(request)}{reverse('register_api')}"
    headers = {
            'Content-Type': 'application/json'
            }
    
    if request.method == "GET":
        return render(request, 'registration.html')

    if request.method == "POST":
        # Form data send using AJAX.
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')



        # Payload containing the fields for the API.
        payload = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "phone_number": phone_number
        })

        # Request to the API with method POST using requests library.
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=120)
            response_data = response.json()
            return JsonResponse(data=response_data, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)   
    return render(request, "register.html")

def voucher(length):
    """
    Generate a random voucher of the specified length.
    This function generates a random voucher consisting of ASCII letters and digits.
    The length parameter determines the number of characters in the generated voucher.
    :param length: The length of the generated voucher.
    :return: A randomly generated voucher.
    """
    characters = string.ascii_letters + string.digits
    voucher = ''.join(random.choice(characters) for _ in range(length))
    return voucher


def redeem_voucher(request):
    if request.method == "GET":
        return render(request, "redeem_voucher.html")

    if request.method == "POST":
        voucher_codes = Voucher.objects.values_list('code', flat=True)
        selected_code = random.choice(voucher_codes)
        url = f"{host_url(request)}{reverse('redeem_voucher_api')}"

        payload = json.dumps({
            "code": selected_code,
        })

        headers = {
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(url, headers=headers, data=payload, timeout=120)
            response_data = response.json()

            return JsonResponse(data=response_data, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, "redeem_voucher.html")


def create_voucher(request):
    """
    A function to create a voucher
    """
    if request.method == "GET":
        return render(request, 'generate_voucher.html')

    if request.method == "POST":
        # Form data send using AJAX.
        code = request.POST.get("code")
        max_redemptions = request.POST.get("max_redemptions")
        expiry_date = request.POST.get("expiry_date")
        redemption_type = request.POST.get("redemption_type")
        # URL for the login API.
        url = f"{host_url(request)}{reverse('generate_voucher_api')}"
        # Payload containing the fields for the API.
        payload = json.dumps({
        "code":code,
        "max_redemptions":max_redemptions, 
        "expiry_date":expiry_date,
        "redemption_type": redemption_type,      
        })
        # API header for the type of data format of the payload.
        headers = {
            'Content-Type': 'application/json',
        } 
        # Request to the API with method POST using requests library.
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=120)
            response_data = response.json()

            return JsonResponse(data=response_data, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
               
    return render(request, 'generate_voucher.html')
