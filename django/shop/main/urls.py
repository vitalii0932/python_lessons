from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.drugs, name='drugs'),
	path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:drug_id>/', views.add_to_cart, name='add_to_cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)