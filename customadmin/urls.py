from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrator_login_page, name='administrator_login_page'),

    path('admin_login_check/', views.admin_login_check, name='admin_login_check'),
    
    path('administrator_dashboard/', views.administrator, name='administrator'),

    path('super_user_logout/', views.super_user_logout, name='super_user_logout'),

    # ======= Website Setting ==============================================

    path('website_settings/', views.website_settings, name='website_settings'),
    path('upload_logo/', views.upload_logo, name='upload_logo'),
    path('upload_favicon/', views.upload_favicon, name='upload_favicon'),
    path('update_footer_contact/', views.update_footer_contact, name='update_footer_contact'),

    # ================== Product Settings ===================================

    path('product_size/', views.product_size, name='product_size'),
    path('add_size_custom/', views.add_size_custom, name='add_size_custom'),
    path('delete_size/<str:pk>/', views.delete_size, name='delete_size'),
    path('update_size/<str:pk>/', views.update_size, name='update_size'),

    path('product_color/', views.product_color, name='product_color'),
    path('add_color_custom/', views.add_color_custom, name='add_color_custom'),
    path('update_color/<str:pk>/', views.update_color, name='update_color'),
    path('delete_color/<str:pk>/', views.delete_color, name='delete_color'),

    path('product_country/', views.product_country, name='product_country'),
    path('add_country_custom/', views.add_country_custom, name='add_country_custom'),
    path('update_country/<str:pk>/', views.update_country, name='update_country'),
    
    path('delete_country/<str:pk>/', views.delete_country, name='delete_country'),

    path('top_level/', views.top_level, name='top_level'),
    path('add_category_custom/', views.add_category_custom, name='add_category_custom'),
    path('update_category/<str:pk>/', views.update_category, name='update_category'),
    path('delete_category/<str:pk>/', views.delete_category, name='delete_category'),

    path('mid_level/', views.mid_level, name='mid_level'),
    path('add_mid_level_category/', views.add_mid_level_category, name='add_mid_level_category'),
    path('update_mid_category/<str:pk>/', views.update_mid_category, name='update_mid_category'),
    path('delete_mid_category/<str:pk>/', views.delete_mid_category, name='delete_mid_category'),

    path('end_level/', views.end_level, name='end_level'),
    path('add_end_level_category/', views.add_end_level_category, name='add_end_level_category'),
    path('update_end_category/<str:pk>/', views.update_end_category, name='update_end_category'),
    path('delete_end_category/<str:pk>/', views.delete_end_category, name='delete_end_category'),

    path('marble_management/', views.marble_management, name='marble_management'),
    path('add_product_custom/', views.add_product_custom, name='add_product_custom'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product'),
    path('delete_product_confirm/', views.delete_product_confirm, name='delete_product_confirm'),
    path('update_product/<str:pk>/', views.update_product, name='update_product'),

    path('registered_users/', views.registered_users, name='registered_users'),
    path('delete_user/<str:pk>/', views.delete_user, name='delete_user'),
    path('change_user_status/<str:pk>/', views.change_user_status, name='change_user_status'),


    # Social Media
    path('add_social_media/', views.add_social_media, name='add_social_media'),
    path('add_social_media_save/', views.add_social_media_save, name='add_social_media_save'),
    
    path('order_management/', views.order_management, name='order_management'),
    path('order_status_changed/<str:pk>/', views.order_status_changed, name='order_status_changed'),
    path('shipping_status_changed/<str:pk>/', views.shipping_status_changed, name='shipping_status_changed'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
    
    path('update_admin_info/', views.update_admin_info, name='update_admin_info'),
    path('update_super_user_password/', views.update_super_user_password, name='update_super_user_password'),
    
    path('manage_slider/', views.manage_slider, name='manage_slider'),
    path('add_slider/', views.add_slider_custom, name='add_slider'),
    path('delete_slider/<str:pk>/', views.delete_slider, name='delete_slider'),
    path('update_slider/<str:pk>/', views.update_slider, name='update_slider'),
    
    path('contact_message_view/', views.contact_message_view, name='contact_message_view'),
    path('delete_user_message/<str:pk>/', views.delete_user_message, name='delete_user_message'),
]