from django.shortcuts import render

# Create your views here.

def dashboards_view(request):
    return render (request, 'power_bi.html')
