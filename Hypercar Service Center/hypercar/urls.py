"""hypercar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from tickets.views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='welcome/', permanent=False)),
    path('welcome/', WelcomeView.as_view(), name="welcome"),
    path('menu/', MenuView.as_view(), name="menu"),
    path('get_ticket/<service>', TicketView.as_view(), name="tickets"),
    path('processing', ProcView.as_view(), name="processing"),
    path('processing/', RedirectView.as_view(url='/processing')),
    path('next', NextView.as_view(), name='next')
]