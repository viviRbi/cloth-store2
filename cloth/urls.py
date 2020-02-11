from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('product/create', views.product_create, name='product_create'),
    path('product/edit/<int:id>', views.product_edit, name='product_edit'),
    path('product/delete/<int:id>', views.product_delete, name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# To display the images from static/ media folder
