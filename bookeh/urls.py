from django.contrib import admin
from django.urls import path, include
from bookeh import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('', include('accounts.urls')),
    path('', include('cart.urls')),
]