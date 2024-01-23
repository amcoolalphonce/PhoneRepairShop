from django.shortcuts import render
from .models import Service

def index(request):
        all_services = Service.objects.all()
        context = {'Services' : all_services}
        return render(request, 'store/index.html', context)