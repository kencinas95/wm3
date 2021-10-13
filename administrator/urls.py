from django.urls import path

from . import views
from .api import user
from .api import origin


urlpatterns = [
    path('', views.home),
    path('/categories', views.categories),
    path('/origins', views.origins),
    path('/inventory', views.inventory),
    path('/v1/admin/login', user.login),
    path('/v1/origin', origin.handle)
]