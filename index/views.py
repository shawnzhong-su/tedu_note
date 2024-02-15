from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .templates import *


# Create your views here.
def index_views(request):
    return render(request, 'index.html')

