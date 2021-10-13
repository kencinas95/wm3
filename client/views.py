from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http import HttpResponse

from common.models.item import Item
from common.models.user import Gender


def home(request: HttpRequest) -> HttpResponse:
    items = Item.objects.filter(highlighted=1, itemimage__thumbnail=1)
    context = {
        'highlighted': items,
        'popular': items,
    }
    return render(request, "web/home.html", context=context)


def market(request: HttpRequest) -> HttpResponse:
    return render(request, "web/market.html")


def offers(request: HttpRequest) -> HttpResponse:
    return render(request, "web/offers.html")


def help_page(request: HttpRequest) -> HttpResponse:
    return render(request, "web/help.html")


def login(request: HttpRequest) -> HttpResponse:
    sid = request.META.get('Authentication')
    if not sid:
        return render(request, "web/user/login.html")
    else:
        return redirect('/', request=request)


def register(request: HttpRequest) -> HttpResponse:
    sid = request.session.get('sid')
    if not sid:
        genders = Gender.objects.all()
        context = {
            'genders': genders
        }
        return render(request, "web/user/register.html", context=context)
    else:
        return redirect('/', request=request)


def password_forgot(request: HttpRequest) -> HttpResponse:
    sid = request.session.get('sid')
    if not sid:
        return render(request, "web/user/password-forgot.html")
    else:
        return redirect('/', request=request)

