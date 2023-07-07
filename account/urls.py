from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),

    path('register_page/', views.register_page, name='register_page'),

    path('cart/', views.cart, name='cart'),

    path('cart_increase/<str:pk>/', views.cart_increase, name='cart_increase'),

    path('registration_save/', views.registration_save, name='registration_save'),

    path('login_check/', views.login_check, name='login_check'),

    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),

    path('update_profile/', views.update_profile, name='update_profile'),

    path('update_billing_shipping/', views.update_billing_shipping, name='update_billing_shipping'),

    path('update_password/', views.update_password, name='update_password'),

    path('user_orders/', views.user_orders, name='user_orders'),

    path('update_profile_save/', views.update_profile_save, name='update_profile_save'),

    path('update_password_save/', views.update_password_save, name='update_password_save'),

    path('user_logout/', views.user_logout, name='user_logout'),

    path('user_product_save/<str:pk>/', views.user_product_save, name='user_product_save'),

    path('delete_saved_product/<str:pk>/', views.delete_saved_product, name='delete_saved_product'),

    path('check_out/<str:pk>/', views.check_out, name='check_out'),

    path('user_product_save_real/', views.user_product_save_real, name='user_product_save_real'),

    path('check_out_complete/', views.check_out_complete, name='check_out_complete'),

    path('get_transaction/', views.get_transaction, name='get_transaction'),
    
    path('order_product/<str:pk>/', views.order_product, name='order_product'),
    
    path('confirm_email_address/<str:id>/', views.confirm_email_address, name='confirm_email_address'),
    
    path('user_contact/', views.user_contact, name='user_contact'),
]
