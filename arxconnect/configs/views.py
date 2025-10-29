from django.shortcuts import render

# Create your views here.

def user_manager(request):
    return render(request, "user_manager.html")