from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

from common.models import ItemCategory, Origin, Item, OriginCategory


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "administrator/home.html")


def categories(request: HttpRequest) -> HttpResponse:
    all_categories = ItemCategory.objects.all()
    paginator = Paginator(all_categories, 10)

    page = int(request.GET.get('page', 1))
    pagination = paginator.get_page(page)

    return render(request, "administrator/section/categories.html", {'pagination': pagination})


def origins(request: HttpRequest) -> HttpResponse:
    all_origins = Origin.objects.all()
    paginator = Paginator(all_origins, 10)

    page = int(request.GET.get('page', 1))
    pagination = paginator.get_page(page)

    ctx = {
        'pagination': pagination,
        'types': OriginCategory.objects.all()
    }

    return render(request, "administrator/section/origins.html", ctx)


def inventory(request: HttpRequest) -> HttpResponse:
    all_items = Item.objects.all()
    paginator = Paginator(all_items, 10)

    page = int(request.GET.get('page', 1))
    pagination = paginator.get_page(page)

    ctx = {
        'pagination': pagination,
        'categories': ItemCategory.objects.all(),
        'origins': Origin.objects.all()
    }

    return render(request, "administrator/section/inventory.html", ctx)

