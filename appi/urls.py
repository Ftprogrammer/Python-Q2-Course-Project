from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('change-password/',views.MypasswordChangeView.as_view(),name='password-change-view'),
    path('change-password/done/',views.MyPasswordResetDoneView.as_view(),name='password-change-done')


]
