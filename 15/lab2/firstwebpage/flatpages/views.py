from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'index.html')

def hello(request):
    return HttpResponse(u'Привет, Мир!', content_type="text/plain")
# Create your views here.
