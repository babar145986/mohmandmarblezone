from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('product_category/', views.product_category, name='product_category'),

    path('about_us/', views.about_us, name='about_us'),

    path('faq/', views.faq, name='faq'),

    path('contact_us/', views.contact_us, name='contact_us'),

    path('single_product/<str:pk>/', views.single_product, name='single_product'),

    path('product_mid_category/<str:pk>/', views.product_mid_category, name='product_mid_category'),

    path('product_end_category/<str:pk>/', views.product_end_category, name='product_end_category'),

    path('search_product_category/<str:pk>/', views.search_product_category, name='search_product_category'),

    path('filter_mid_category/<str:mid_category_id>/', views.filter_mid_category, name='filter_mid_category'),

    path('filter_end_category/<str:end_category_id>/', views.filter_end_category, name='filter_end_category'),
    
    path('search_product/', views.search_product, name='search_product'),
]
