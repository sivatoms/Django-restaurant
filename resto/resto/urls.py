"""resto URL Configuration

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
from django.contrib import admin
from django.urls import path
from resto.bawarchi import views
urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.ReservationView.as_view(template_name='reservation.html'), name='reservation'),
    path('reservation/rervationsuccessful/', views.rervationsuccessful, name='rervationsuccessful'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/contactsuccess/', views.contactSuc.as_view(), name='contactsuccess'),
    path('admin/', admin.site.urls),
]
