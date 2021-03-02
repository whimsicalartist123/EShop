from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

def index(request):
    return render(request, "base.html", {})

urlpatterns = [
    path('', index, name="home"),
    path('cart/', include('apps.cart.urls', namespace='cart')),
    path('order/', include('apps.order.urls', namespace='order')),
    path('products/', include('apps.product.urls')),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('apps.users.urls', namespace='profile')),
    path('admin/', admin.site.urls),

    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
