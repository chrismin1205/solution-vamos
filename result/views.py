from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader

from .models import Work

# Create your views here.
def index(request):
  work_list = Work.objects.all()
  context = {
    'work_list' : work_list,
  }
  return render(request, 'result/result.html', context)

def search_result(request):
  # if request.method == 'POST':
  #   searched = request.POST['searched']        
  #   works = Work.objects.filter(work_name=searched)

  #   context = {
  #       'searched': searched, 
  #       'works': works
  #       }

  #   return render(request, 'result/search_result.html', context)
  # else:
  #   return render(request, 'result/search_none.html', {})

  # if request.method == 'POST':
  #     keyword = request.POST['searched'] # keyword를 입력받음
  #     tag = Work.objects.filter(work_name=keyword) # 해당 키워드를 가진 tag 클래스 오픈
  #     post= Work.objects.filter(work_name__icontains = tag).order_by('-pub_date') # 해당 태그를 가진 post 저장

  #     return render(request, 'result/search_result.html', {'post': post, 'keyword':keyword})
  # elif request.method == 'GET':
  #     return redirect('/')

  keywords = Work.objects.order_by('-pub_date').all()

  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      keywords = keywords.filter(id__icontains=keyword)

  context = {
    'keywords' : keywords,
  }

  return render(request, 'result/search_result.html', context)


def detail(request, pk):
  work_list = Work.objects.all()
  pk = Work.objects.get(pk=pk)
  context = {
    'work_list' : work_list,
    'pk' : pk,
  }
  return render(request, 'result/detail.html', context)