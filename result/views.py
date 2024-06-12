from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Work

# Create your views here.
def index(request):
  # work_list = Work.objects.all()
  # output = work_list[0]
  # return HttpResponse(output)

  work_list = Work.objects.all()
  # template = loader.get_template('result/index.html')
  context = {
    'work_list' : work_list,
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'result/result.html', context)

def detail(request, work_id):
  work = Work.objects.get(pk=work_id)
  context = {
    'work' : work
  }
  return render(request, 'result/result.html', context)