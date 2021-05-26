from django.urls import path

from .views import product_list, product_detail, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', product_list, name='list'),
    # path('<int:product_id>/', product_detail, name="detail"),
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),
]
