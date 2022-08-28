from curses.ascii import US
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
import jwt
from account.models import User
from account.serializers import LoginSerializer # pip3 install pyjwt
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.


SECRET = "AKLDFK!TV!"
@api_view(['POST'])
def login(request):
    # request.POST is only used to receive data sent using a POST form
    # username = request.data['username']
    # password = request.data['password']
    
    serializer = LoginSerializer(data=request.data)
    
    if not serializer.is_valid():
        return JsonResponse(serializer.errors, status=400)
    
    
    username = serializer.data['username']
    password = serializer.data['password']
    
    
    if not User.objects.filter(username=username).exists():
        return JsonResponse({
            "error": "Wrong username/password"
        })
    
    user = User.objects.get(username=username)
    if not user.check_password(password):
        return JsonResponse({
            "error": "Wrong username/password"
        })
        
    token = Token.objects.get_or_create(user=user)[0] #In django models you can use get_or_create instead of filtering for something and creating it if it doesn't exist
    return JsonResponse({
        "token": token.key
    })
    
    # if username == "majed" and password == "1234":
    #     return JsonResponse({
    #         "token": jwt.encode({"username": "majed"}, key=SECRET) #request.session['username'] = "majed"
    #     })
    # else:
    #     return JsonResponse({
    #         "result": "Incorrect username/password"
    #     }, status=401)
        
        

@api_view(['GET'])
@permission_classes([IsAuthenticated]) #Makes sure that the user is sending his token
# @authentication_classes([TokenAuthentication]) #Makes sure that the token belongs to a user. / instead of using this decorator for each view we can just set the default authentication_classes in settings.py 
def private(request):
    print(request.user, "************") # request.user knows the user from the token sent in the authorization header
    # Get private info eg: Profile.objects.get(user=request.user)
    return JsonResponse({
        "message": "Welcome here " + request.user.username #https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    })