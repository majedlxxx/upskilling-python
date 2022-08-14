from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is home")
    data = {
        'ids': [1,2,3],
        'name': 'majed'
    }
    return render(request, 'home.html', context=data)


def login(request):
    return render(request, 'login.html')