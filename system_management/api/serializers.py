from rest_framework import serializers

from system_management.models import Voucher
class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login information.
    Attributes:
    - username: A required character field representing the user's username.
    - password: A required character field representing the user's password.
    Methods:
    - login(validated_data): A method that returns the validated data.
    """
    username = serializers.CharField(required= True)
    password = serializers.CharField(required= True)
    def login(self, validated_data):
        """
        Perform user login.
        This method is responsible for handling user login using the provided validated data.
        It simply returns the validated data as the login process doesn't involve any complex logic.
        Parameters:
        - validated_data (dict): A dictionary containing the validated data,
        including 'username' and 'password'.
        Returns:
        - dict: The same validated data received as input.
        """
        return validated_data

class RegisterBaseSerializer(serializers.Serializer):
    """
    Serializer for user registration with basic information.
    Attributes:
    - email: A required email field representing the user's email address.
    - password: A required character field representing the user's password.
    """
    email = serializers.EmailField(required= True)
    password = serializers.CharField(required= True)
    phone_number = serializers.CharField(required= True)
    first_name = serializers.CharField(required= True)
    last_name = serializers.CharField(required= True)

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'