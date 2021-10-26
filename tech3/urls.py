from django.contrib import admin
from django.urls import path, include
from uauth.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('uauth.urls')),
    path('wallet/', include('wallet.urls')),
    path('', index_view, name='index_url'),
]
