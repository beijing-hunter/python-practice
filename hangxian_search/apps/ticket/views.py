from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST, require_GET
from django.conf import settings
from django.http import Http404
from apps.ticket.models import *


# Create your views here.

def search(request):
    """查询，返回一个查询页面 """
    q = request.GET.get('q')
    departureDate=request.GET.get('departureDate')
    if q:
        datas = findInfos(q,departureDate)
        if datas:
            addHotSail(datas[0].departureCityName+"到"+datas[0].arrivalCityName)
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
    if not request.session.get('userId', False):
        print("未登录")
        return redirect(reverse('xfzauth:login'))
    else:
        user = {"is_authenticated": True, "username": request.session["userName"], "is_staff": False}
        context["user"] = user
        addSearchRecord(int(request.session["userId"]), q)
        context["records"] = findSearchRecrods(int(request.session["userId"]))
        context["hots"]=findHotSail()
        context["chuFaDate"]=findDepartureDate()
    return render(request, 'news/search.html', context=context)
