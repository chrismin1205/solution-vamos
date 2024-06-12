from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import WorkName

# Create your views here.
def index(request):
  list_work = WorkName.objects.order_by()[:5]
  count = len(list_work)
  context = {
    'list_work' : list_work,
    'count' : count,
  }
  
  return render(request, 'search/index.html', context)