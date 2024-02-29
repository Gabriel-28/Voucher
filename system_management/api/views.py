from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
import json
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterBaseSerializer
from system_management.models import CustomUser, Voucher


@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    if request.method == 'POST':
        serializer = RegisterBaseSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            email = serializer.validated_data['email']
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            CustomUser.objects.create(email=email,
                                        password=password,
                                        phone_number=phone_number,
                                        first_name=first_name,
                                        last_name=last_name)
            context = {"status": "success",
                        "message": "Successfully registered"}
            return Response(context, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        response_data = json.dumps({
            "username": username,
            "password": password
        })
        print('response: ', response_data) 
        user = CustomUser.objects.get(email=username)
        if user:
            if password == user.password:
                token, created = Token.objects.get_or_create(user=user)
        user_id = user.id
        response_data = {
            'user_id':user_id,
            'token': token.key,
            "status":"success",
            }
        return Response(response_data, status=status.HTTP_200_OK)
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def redeem_voucher_api(request):
    """
    API endpoint to redeem a voucher.
    """
    try:
        if request.method == 'POST':
            code = request.data.get('code')

            voucher = Voucher.objects.filter(code=code).first()

            if voucher:
                context = {
                    'status': 'success',
                    'message': f'Voucher with code {code} has been successfully redeemed.'
                }
                return Response(context, status=status.HTTP_200_OK)
            else:
                context = {
                    'status': 'error',
                    'message': f'Voucher with code {code} not found.'
                }
                return Response(context, status=status.HTTP_404_NOT_FOUND)

    except Exception as exception:
        return Response({'error': str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["POST"])
def generate_voucher_api(request):
    
    """
        API endpoint to retrieve the user dataset_id so when they upload data,
        the dataset_id will be used to upload to their relevant folder.
    """
    try:
        if request.method == 'GET':
            user_id = request.user.id
            user = CustomUser.objects.get(id=user_id)
            if not user.is_superuser:
                voucher = Voucher.objects.all()
                return Response(voucher, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'POST':
            redemption_type = request.data.get('redemption_type')
            max_redemptions = request.data.get('max_redemptions')
            code = request.data.get('code')
            exp_date = request.data.get('exp_date')

            Voucher.objects.create(
                redemption_type=redemption_type,
                max_redemptions=max_redemptions,
                code=code,
                exp_date=exp_date
            )
            context = {
                'status': 'success',
                'message': 'Voucher has been successfully created.'
            }
            return Response(context, status=status.HTTP_201_CREATED)
    except Exception as exception:
        return Response({'error': str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)