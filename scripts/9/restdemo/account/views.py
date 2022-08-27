import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
import jwt

from account.serializers import LoginSerializer # pip3 install pyjwt
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
    
    if username == "majed" and password == "1234":
        return JsonResponse({
            "token": jwt.encode({"username": "majed"}, key=SECRET) #request.session['username'] = "majed"
        })
    else:
        return JsonResponse({
            "result": "Incorrect username/password"
        }, status=401)
        
        
