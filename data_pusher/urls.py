from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('destinations/', include('destinations.urls')),
    path('server/', include('data_handler.urls')),
    path('', home, name='home'),
]
