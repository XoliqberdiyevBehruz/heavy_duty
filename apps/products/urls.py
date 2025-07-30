from django.urls import path

from apps.products import views

urlpatterns = [
    path('category/list/', views.ProductCategoryListApiView.as_view()),
    path('category/<uuid:category_id>/product/list/', views.ProductListApiView.as_view()),
    path('product/<uuid:id>/', views.ProductDetailApiView.as_view()),
    path('product/list/', views.ProductApiView.as_view()),

]