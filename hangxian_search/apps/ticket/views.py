from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.conf import settings
from django.http import Http404
from apps.ticket.models import *


# Create your views here.

def search(request):
    """查询，返回一个查询页面 """
    q = request.GET.get('q')
    if q:
        datas = findInfos(q)
        if datas:
            flag = 2
        else:
            page = int(request.GET.get('p', 1))
            start = settings.ONE_PAGE_NEWS_COUNT * (page - 1)
            end = start + settings.ONE_PAGE_NEWS_COUNT
            datas = []
            flag = 1
    else:
        page = int(request.GET.get('p', 1))
        start = settings.ONE_PAGE_NEWS_COUNT * (page - 1)
        end = start + settings.ONE_PAGE_NEWS_COUNT
        datas = []
        flag = 0

    context = {'newes': datas, 'flag': flag}
    return render(request, 'news/search.html', context=context)
