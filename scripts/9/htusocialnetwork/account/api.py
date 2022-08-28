from django.http import JsonResponse
from rest_framework.decorators import api_view
from account.serializers import LoginSerializer, SignupSerializer
from rest_framework.authtoken.models import Token
from account.models import Account

@api_view(['POST'])
def login(request):
    login_serializer = LoginSerializer(data=request.data)
    if not login_serializer.is_valid():
        return JsonResponse({
         "errors": login_serializer.errors   
        }, status=400)
    username = login_serializer.validated_data['username']
    password = login_serializer.validated_data['password']
    
    INVALID_CREDENTIALS =  JsonResponse({"error": "Incorrect credentials"}, status=401)
    
    if not Account.objects.filter(username=username).exists():
        print("username is wrong", username)
        return INVALID_CREDENTIALS
    user = Account.objects.get(username=username)
    if not user.check_password(password):
        return INVALID_CREDENTIALS
    
    token = Token.objects.get_or_create(user = user)[0]
    
    return JsonResponse({
        "token": token.key # we can use token.pk to get the token's primary key which is the key itself
    })
    

@api_view(['POST'])
def signup(request):
    signup_serializer = SignupSerializer(data=request.data)
    if not signup_serializer.is_valid():
        return JsonResponse({
         "errors": signup_serializer.errors   
        }, status=400)
    
    username = signup_serializer.validated_data['username']
    password = signup_serializer.validated_data['password']
    password_confirmation = signup_serializer.validated_data['password_confirmation']
    
    if password != password_confirmation:
        return JsonResponse({
            'error': "Passwords don't match"
        }, status=400)
        
    if Account.objects.filter(username=username).exists():
        return JsonResponse({
            "error": "Username is already used"
        }, status=409)
    
    new_user = Account(username=username)
    new_user.set_password(password)
    new_user.save()
    
    return JsonResponse({
        "message": "Created successfully"
    }, status=201)