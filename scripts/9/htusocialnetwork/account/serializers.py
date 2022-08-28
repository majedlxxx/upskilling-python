from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password_confirmation = serializers.CharField()
    
    
