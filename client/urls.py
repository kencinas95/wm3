from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from client import views



urlpatterns = [
    path('', views.home),
    path('login', views.login),
    path('register', views.register),
    path('password-forgot', views.password_forgot),
    path('market', views.market),
    path('help', views.help_page),
    path('offers', views.offers)
]

# Add statics only in development environment
if settings.DEBUG:
    for static_tuple in settings.STATICFILES_DIR:
        urlpatterns += static(static_tuple[0], document_root=static_tuple[1])
