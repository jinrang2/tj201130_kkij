from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
def homeView(request):
    #return HttpResponse("<h1>Hello,Django!</h1>")
    return render(request, 'index.html')

