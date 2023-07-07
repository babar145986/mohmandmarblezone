from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import add_mid_category, add_end_category
from .models import add_size, add_color,add_country,add_top_category, add_product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddProductForm
from django.contrib.auth.decorators import user_passes_test
from account.models import MyUser

# Create your views here.

def administrator_login_page(request):
    return render(request, 'admin/admin_login_page.html')

def authenticate_super_user(request, email, password):
    user = authenticate(request, email=email, password=password)
    if user is not None:
        if user.is_admin:
            login(request, user)
            return True
        return False
    return False

def admin_login_check(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_authenticated = authenticate_super_user(request, email, password)
        if user_authenticated:
            return redirect('administrator')
        else:
            messages.error(request, "Email or Password Incorrect")
            return redirect('administrator_login_page')
        
def is_admin(user):
    return user.is_active and user.is_admin

from account.models import OrderProduct

@login_required(login_url='administrator_login_page')
@user_passes_test(lambda u:MyUser.is_admin, login_url='administrator_login_page')
def administrator(request):
    if request.user.is_active and request.user.is_admin:
        all_products = add_product.objects.all().count()
        all_users = MyUser.objects.all().count()
        completed_orders = OrderProduct.objects.filter(status="Completed").count()
        pending_orders = OrderProduct.objects.filter(status="Pending").count()
        not_available_orders = OrderProduct.objects.filter(status="Not Available").count()
        top_categories = add_top_category.objects.all().count()
        mid_categories = add_mid_category.objects.all().count()
        end_categories = add_end_category.objects.all().count()
        context = {'all_products': all_products, 'top_categories': top_categories, 
                    'mid_categories': mid_categories, 'end_categories': end_categories, 
                    'all_users': all_users, 'completed_orders': completed_orders,
                    'pending_orders': pending_orders, 'not_available_orders': not_available_orders}
        return render(request, 'admin/dashboard.html', context)
    else:
        messages.error(request, "Not a Super user")
        return redirect("administrator_login_page")

@login_required(login_url="administrator_login_page")
def super_user_logout(request):
    logout(request)
    messages.error(request, "User Logout")
    return redirect('login_page')

from .models import add_logo, add_favicon, add_footer_contact

@login_required(login_url="administrator_login_page")
def website_settings(request):
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    context = {'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact}
    return render(request, 'admin/settings.html', context)

def upload_logo(request):
    if request.method == 'POST':
        get_logo = request.FILES['photo_logo']
        data = add_logo(upload_logo=get_logo)
        data.save()
        return redirect('website_settings')

def upload_favicon(request):
    if request.method == 'POST':
        get_favicon = request.FILES['photo_favicon']
        data = add_favicon(upload_favicon=get_favicon)
        data.save()
        return redirect('website_settings')

def update_footer_contact(request):
    if request.method == 'POST':
        footer_copyright = request.POST['footer_copyright']
        newsletter_on_off = request.POST['newsletter_on_off']
        contact_address = request.POST['contact_address']
        contact_email = request.POST['contact_email']
        contact_phone = request.POST['contact_phone']
        contact_map_iframe = request.POST['contact_map_iframe']
        data = add_footer_contact(footer_copyright=footer_copyright, contact_address=contact_address,
                                    contact_email=contact_email, contact_no=contact_phone,
                                    map_iframe=contact_map_iframe, status=newsletter_on_off)
        data.save()
        return redirect('website_settings')

# ============ Product Settings ===================================

@login_required(login_url="administrator_login_page")
def product_size(request):
    all_sizes=add_size.objects.all()
    context={'all_sizes':all_sizes}
    return render(request, 'admin/shop_settings/size.html',context)

@login_required(login_url="administrator_login_page")
def add_size_custom(request):
    if request.method == 'POST':
        size_name = request.POST['size_name']
        data = add_size(size_name=size_name)
        data.save()
        return redirect('product_size')
    return render(request, 'admin/shop_settings/add_size_custom.html')

@login_required(login_url="administrator_login_page")
def delete_size(request, pk):
    size = add_size.objects.get(id=pk)
    size.delete()
    return redirect('product_size')

@login_required(login_url="administrator_login_page")
def update_size(request, pk):
    get_size = add_size.objects.get(id=pk)
    if request.method == 'POST':
        size_name = request.POST['size_name']
        get_size.size_name = size_name
        get_size.save()
        return redirect('product_size')
    context = {'get_size': get_size}
    return render(request, 'admin/shop_settings/update_size.html', context)

@login_required(login_url="administrator_login_page")
def product_color(request):
    all_colors= add_color.objects.all()
    context={'all_colors':all_colors}
    return render(request, 'admin/shop_settings/color.html',context)

@login_required(login_url="administrator_login_page")
def add_color_custom(request):
    if request.method == 'POST':
        get_name = request.POST['color_name']
        data = add_color(color_name=get_name)
        data.save()
        return redirect('product_color')
    return render(request, 'admin/shop_settings/add_color.html')

@login_required(login_url="administrator_login_page")
def update_color(request, pk):
    get_color = add_color.objects.get(id=pk)
    if request.method == 'POST':
        get_name = request.POST['color_name']
        get_color.color_name = get_name
        get_color.save()
        return redirect("product_color")
    context = {'get_color': get_color}
    return render(request, 'admin/shop_settings/update_color.html', context)

@login_required(login_url="administrator_login_page")
def delete_color(request,pk):
    get_color=add_color.objects.get(id=pk)
    get_color.delete()
    return redirect('product_color')

@login_required(login_url="administrator_login_page")
def product_country(request):
    all_countries=add_country.objects.all()
    context={"all_countries":all_countries}
    return render(request, 'admin/shop_settings/country.html',context)

@login_required(login_url="administrator_login_page")
def add_country_custom(request):
    if request.method == 'POST':
        get_name = request.POST['country_name']
        data = add_country(country_name=get_name)
        data.save()
        return redirect('product_country')
    return render(request, 'admin/shop_settings/add_country.html')

@login_required(login_url="administrator_login_page")
def update_country(request, pk):
    get_country = add_country.objects.get(id=pk)
    if request.method == 'POST':
        get_name = request.POST['country_name']
        get_country.country_name = get_name
        get_country.save()
        return redirect('product_country')
    context = {'get_country': get_country}
    return render(request, 'admin/shop_settings/update_country.html', context)

@login_required(login_url="administrator_login_page")
def delete_country(request, pk):
    get_country=add_country.objects.get(id=pk)
    get_country.delete()
    return redirect('product_country')

@login_required(login_url="administrator_login_page")
def top_level(request):
    all_top_categories=add_top_category.objects.all()
    context={'all_top_categories':all_top_categories}
    return render(request, 'admin/shop_settings/top_level_category.html',context)

@login_required(login_url="administrator_login_page")
def add_category_custom(request):
    if request.method == 'POST':
        get_category_name = request.POST['tcat_name']
        get_show_on_menu = request.POST['show_on_menu']
        data = add_top_category(top_category_name=get_category_name, show_top_menu=get_show_on_menu)
        data.save()
        return redirect('top_level')
    return render(request, 'admin/shop_settings/add_category.html')

@login_required(login_url="administrator_login_page")
def update_category(request, pk):
    get_category = add_top_category.objects.get(id=pk)
    if request.method == 'POST':
        get_category_name = request.POST['tcat_name']
        get_show_on_menu = request.POST['show_on_menu']
        get_category.top_category_name = get_category_name
        get_category.show_top_menu = get_show_on_menu
        get_category.save()
        return redirect('top_level')
    print(get_category.show_top_menu)
    context = {'get_category': get_category}
    return render(request, 'admin/shop_settings/update_category.html', context)

@login_required(login_url="administrator_login_page")
def delete_category(request, pk):
    get_category = add_top_category.objects.get(id=pk)
    get_category.delete()
    return redirect('top_level')

@login_required(login_url="administrator_login_page")
def mid_level(request):
    all_mid_categories = add_mid_category.objects.all()
    context = {'all_mid_categories': all_mid_categories}
    return render(request, 'admin/shop_settings/mid_level_category.html', context)

@login_required(login_url="administrator_login_page")
def add_mid_level_category(request):
    all_top_categories=add_top_category.objects.all()
    if request.method=="POST":
        top_level=request.POST['tcat_id']
        mid_level=request.POST['mcat_name']
        get_top_category = add_top_category.objects.get(id=top_level)
        data = add_mid_category(select_top_category=get_top_category, mid_category_name=mid_level)
        data.save()
        return redirect('mid_level')
    context={'all_top_categories':all_top_categories}
    return render(request, 'admin/shop_settings/add_mid_level_category.html',context)

@login_required(login_url="administrator_login_page")
def update_mid_category(request, pk):
    get_mid_category = add_mid_category.objects.get(id=pk)
    all_top_categories=add_top_category.objects.all()
    if request.method=="POST":
        top_level=request.POST['tcat_id']
        get_top_category = add_top_category.objects.get(id=top_level)
        mid_level=request.POST['mcat_name']
        get_mid_category.select_top_category = get_top_category
        get_mid_category.mid_category_name = mid_level
        get_mid_category.save()
        return redirect('mid_level')
    context={'all_top_categories':all_top_categories, 'get_mid_category': get_mid_category}
    return render(request, 'admin/shop_settings/update_mid_category.html', context)

@login_required(login_url="administrator_login_page")
def delete_mid_category(request, pk):
    get_mid_category = add_mid_category.objects.get(id=pk)
    get_mid_category.delete()
    return redirect('mid_level')

@login_required(login_url="administrator_login_page")
def end_level(request):
    all_end_categories = add_end_category.objects.all()
    context = {'all_end_categories': all_end_categories}
    return render(request, 'admin/shop_settings/end_level_category.html', context)

@login_required(login_url="administrator_login_page")
def add_end_level_category(request):
    all_top_categories=add_top_category.objects.all()
    all_mid_categories = add_mid_category.objects.all()
    if request.method=="POST":
        top_level=request.POST['tcat_id']
        mid_level=request.POST['mcat_id']
        end_level=request.POST['ecat_name']
        get_top_category = add_top_category.objects.get(id=top_level)
        get_mid_category = add_mid_category.objects.get(id=mid_level)
        data=add_end_category(select_mid_category=get_mid_category, select_top_category=get_top_category, end_category_name=end_level)
        data.save()
        return redirect('end_level')
    context={'all_top_categories':all_top_categories,'all_mid_categories':all_mid_categories}
    return render(request,'admin/shop_settings/add_end_level_category.html',context)

@login_required(login_url="administrator_login_page")
def update_end_category(request, pk):
    get_end_category = add_end_category.objects.get(id=pk)
    all_top_categories = add_top_category.objects.all()
    all_mid_categories = add_mid_category.objects.filter(select_top_category=get_end_category.select_top_category)
    context = {
        'get_end_category': get_end_category,
        'all_top_categories': all_top_categories,
        'all_mid_categories': all_mid_categories
    }
    return render(request, 'admin/shop_settings/update_end_category.html', context)

@login_required(login_url="administrator_login_page")
def delete_end_category(request, pk):
    get_end_category = add_end_category.objects.get(id=pk)
    get_end_category.delete()
    return redirect('end_level')


from .models import add_product, add_size, add_color

@login_required(login_url="administrator_login_page")
def marble_management(request):
    all_products = add_product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'admin/shop_settings/marble_management.html', context)

@login_required(login_url="administrator_login_page")
def add_product_custom(request):
    form = AddProductForm()
    all_top_categories=add_top_category.objects.all()
    all_mid_categories = add_mid_category.objects.all()
    all_end_categories = add_end_category.objects.all()
    all_sizes = add_size.objects.all()
    all_colors = add_color.objects.all()
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("marble_management")
        else:
            return HttpResponse("Invalid data...")
    context = {'all_top_categories': all_top_categories, 'all_mid_categories': all_mid_categories,
                'all_end_categories': all_end_categories, 'all_sizes': all_sizes, 'all_colors': all_colors,
                'form': form}
    return render(request, 'admin/shop_settings/add_product.html', context)

def update_product(request, pk):
    get_product = add_product.objects.get(id=pk)
    form = AddProductForm(instance=get_product)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=get_product)
        form.save()
        return redirect('marble_management')
    context = {'form': form, 'get_product': get_product}
    return render(request, 'admin/shop_settings/update_product.html', context)

@login_required(login_url="administrator_login_page")
def delete_product(request, pk):
    get_product = add_product.objects.get(id=pk)
    get_product.delete()
    return redirect('marble_management')

@login_required(login_url="administrator_login_page")
def delete_product_confirm(request):
    get_id = request.GET['id']
    get_product = add_product.objects.get(id=get_id)
    get_product.delete()
    return redirect('marble_management')

from account.models import MyUser

@login_required(login_url="administrator_login_page")
def registered_users(request):
    all_users = MyUser.objects.filter(is_admin=False)
    context = {'all_users': all_users}
    return render(request, 'admin/shop_settings/register_users.html', context)

def delete_user(request, pk):
    get_user = MyUser.objects.get(id=pk)
    get_user.delete()
    return redirect('registered_users')

def change_user_status(request, pk):
    item = MyUser.objects.get(id=pk)
    if item.is_active == True:
        item.is_active = False
        item.save()
    else:
        item.is_active = True
        item.save()
    return redirect('registered_users')


# ======== Social Media =====================
from .models import add_social_media_links

def add_social_media(request):
    latest_record = add_social_media_links.objects.last()
    context = {'latest_record': latest_record}
    return render(request, 'admin/shop_settings/social_media.html', context)

def add_social_media_save(request):
    if request.method == 'GET':
        facebook = request.GET['facebook']
        twitter = request.GET['twitter']
        youtube = request.GET['youtube']
        whatsapp = request.GET['whatsapp']
        data = add_social_media_links(facebook=facebook, twitter=twitter, youtube=youtube, watsapp=whatsapp)
        data.save()
        print(facebook, twitter)
        return redirect('add_social_media')

from account.models import OrderProduct
    
def order_management(request):
    all_orders = OrderProduct.objects.all()
    context = {'all_orders': all_orders}
    return render(request, 'admin/order_management.html', context)

def order_status_changed(request, pk):
    item = OrderProduct.objects.get(id=pk)
    item.status = "Completed"
    item.save()
    return redirect('order_management')

def shipping_status_changed(request, pk):
    item = OrderProduct.objects.get(id=pk)
    item.shipping = "Completed"
    item.save()
    return redirect('order_management')

from account.models import ProductSave, OrderProduct

def delete_order(request, pk):
    get_order = OrderProduct.objects.get(id=pk)
    get_order.delete()
    return redirect('order_management')

def update_admin_info(request):
    if request.method == 'POST':
        get_user = request.POST['user_id']
        name = request.POST['full_name']
        phone = request.POST['phone']
        get_user_real = MyUser.objects.get(id=get_user)
        get_user_real.full_name = name
        get_user_real.phone_no = phone
        get_user_real.save()
        print(get_user)
        return redirect("update_admin_info")
    return render(request, 'admin/admin_information_update.html')

def update_super_user_password(request):
    if request.method == 'POST':
        get_id = request.POST['user_id']
        get_user = MyUser.objects.get(id=get_id)
        password = request.POST['password']
        cpassword = request.POST['re_password']
        if password == cpassword:
            get_user.set_password(password)
            get_user.save()
            messages.success(request, "Password Changed Please Login Again")
            return redirect('administrator_login_page')
        
from .forms import AddSliderForm
from .models import add_slider
        
def manage_slider(request):
    all_sliders = add_slider.objects.all()
    context = {'all_sliders': all_sliders}
    return render(request, 'admin/manage_slider.html', context)

def add_slider_custom(request):
    form = AddSliderForm()
    if request.method == 'POST':
        form = AddSliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_slider')
        else:
            return HttpResponse("Error")
    context = {'form': form}
    return render(request, 'admin/add_slider.html', context)

def delete_slider(request, pk):
    get_slider = add_slider.objects.get(id=pk)
    get_slider.delete()
    return redirect('manage_slider')

def update_slider(request, pk):
    get_slider = add_slider.objects.get(id=pk)
    form = AddSliderForm(instance=get_slider)
    if request.method == 'POST':
        form = AddSliderForm(request.POST, request.FILES, instance=get_slider)
        if form.is_valid():
            form.save()
            return redirect('manage_slider')
        else:
            return HttpResponse("Error")
    context = {'form': form}
    return render(request, 'admin/update_slider.html', context)

from .models import user_messages

def contact_message_view(request):
    all_messages = user_messages.objects.all()
    context = {'all_messages': all_messages}
    return render(request, 'admin/contact_message_view.html', context)

def delete_user_message(request, pk):
    get_message = user_messages.objects.get(id=pk)
    get_message.delete()
    return redirect('contact_message_view')