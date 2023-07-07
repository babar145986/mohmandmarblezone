from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyUser
from django.contrib.auth import authenticate, login, logout
from .models import ProductSave
from customadmin.models import add_product
from django.contrib import messages
from .models import Transaction
import uuid
from django.contrib.auth.decorators import login_required
from customadmin.models import add_logo, add_favicon, add_footer_contact, add_social_media_links
from .models import OrderProduct

# Create your views here.

def login_page(request):
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'account/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login_page')

def authenticate_user(request, email, password):
    user = authenticate(request, email=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return True
        return False
    return False

def login_check(request):
    if request.method == 'POST':
        email = request.POST.get('cust_email')
        password = request.POST.get('cust_password')
        user_authenticated = authenticate_user(request, email, password)
        if user_authenticated:
            if request.user.is_admin:
                return redirect('administrator')
            return redirect('user_dashboard')
        else:
            messages.error(request, "Username or password not correct")
            return redirect('login_page')

# ================================================
# ======== USER DASHBOARD ========================
# ================================================

@login_required(login_url="login_page")
def user_dashboard(request):
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'account/dashboard/user_dashboard.html', context)

@login_required(login_url="login_page")
def update_profile(request):
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'account/dashboard/user_update_profile.html', context)

@login_required(login_url="login_page")
def check_out(request, pk):
    get_user = MyUser.objects.get(email=request.user.email)
    get_user_products = ProductSave.objects.get(id=pk)
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    total_price = get_user_products.product.current_price * get_user_products.quantity
    context = {'get_user_products': get_user_products, 'get_user': get_user, 'total_price': total_price,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    print("Count Products : ========== >", get_user_products)
    return render(request, 'account/checkout.html', context)

@login_required(login_url="login_page")
def update_profile_save(request):
    if request.method == 'POST':
        cust_name = request.POST['cust_name']
        cust_cname = request.POST['cust_cname']
        cust_phone = request.POST['cust_phone']
        cust_address = request.POST['cust_address']
        cust_country = request.POST['cust_country']
        cust_city = request.POST['cust_city']
        cust_state = request.POST['cust_state']
        cust_zip = request.POST['cust_zip']
        get_user = MyUser.objects.get(id=request.user.id)
        get_user.full_name = cust_name
        get_user.company_name = cust_cname
        get_user.phone_no = cust_phone
        get_user.address = cust_address
        get_user.country = cust_country
        get_user.city = cust_city
        get_user.state = cust_state
        get_user.zip_code = cust_zip
        get_user.save()
        print(cust_name, cust_cname, cust_phone, get_user)
        messages.success(request, f"{cust_name} - Profile is updated...")
        return redirect('update_profile')

@login_required(login_url="login_page")
def update_billing_shipping(request):
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'account/dashboard/user_update_billing.html', context)

@login_required(login_url="login_page")
def update_password(request):
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'account/dashboard/user_update_password.html', context)

@login_required(login_url="login_page")
def update_password_save(request):
    if request.method == 'POST':
        password = request.POST['cust_password']
        cpassword = request.POST['cust_re_password']
        if password == cpassword:
            get_user = MyUser.objects.get(email=request.user.email)
            get_user.set_password(password)
            get_user.save()
            messages.success(request, "Password Changed")
            return redirect('update_password')
        else:
            messages.error(request, "Password & confirm password didn't match")
            return redirect('update_password')

@login_required(login_url="login_page")
def user_orders(request):
    user = MyUser.objects.get(email=request.user.email)
    order_products = OrderProduct.objects.filter(get_user=user)
    order_productss = OrderProduct.objects.filter(get_user=user).count()
    print("count Products", order_productss)
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'order_products': order_products,
               'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links,}
    return render(request, 'account/dashboard/customer_order.html', context)

from .forms import MyUserForm

from django.core.mail import send_mail

def confirm_email_address(request, id):
    get_email = MyUser.objects.get(id=id)
    print(get_email)
    return HttpResponse('confirmed...')

def register_page(request):
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    form = MyUserForm()
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['confirm_password']
            get_email = form.cleaned_data['email']
            if password != cpassword:
                messages.error(request, "Two password didn't match...")
                return redirect('register_page')
            user = form.save(commit=False)
            
            subject = 'Welcome to My Site'
            message = f'Mohmand Marble Zone Account Created : Email: {get_email}, Password: {password}'
            from_email = 'umargul6852@gmail.com'
            recipient_list = [get_email,]
            print(get_email)
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            messages.success(request, "User Register Successfully...")
            return redirect('login_page')
    context = {'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links, 'form': form}
    return render(request, 'account/register.html', context)

@login_required(login_url="login_page")
def cart(request):
    user = MyUser.objects.get(email=request.user.email)
    saved_products = ProductSave.objects.filter(name=user, status=False)
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    total_price = 0
    all_products = ProductSave.objects.all()
    for product in saved_products:
        total_price += product.price * product.quantity
    context = {'saved_products': saved_products, 'total_price': total_price,
               'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links,}
    return render(request, 'account/cart.html', context)

def cart_increase(request, pk):
    get_quantity
    return HttpResponse("Increased by 1")

from django.http import JsonResponse

@login_required(login_url="login_page")
def delete_saved_product(request, pk):
    saved_product = ProductSave.objects.get(id=pk)
    saved_product.delete()
    return redirect('cart')

def registration_save(request):
    if request.method == 'POST':
        cust_name = request.POST['cust_name']
        cust_cname = request.POST['cust_cname']
        cust_email = request.POST['cust_email']
        cust_phone = request.POST['cust_phone']
        cust_address = request.POST['cust_address']
        cust_country = request.POST['cust_country']
        cust_city = request.POST['cust_city']
        cust_state = request.POST['cust_state']
        cust_zip = request.POST['cust_zip']
        cust_password = request.POST['cust_password']
        cust_re_password = request.POST['cust_re_password']
        if MyUser.objects.filter(email=cust_email):
            messages.error(request, 'Email Account Already Exist')
            return redirect('register_page')
        if cust_password != cust_re_password:
            messages.error(request, "Two Password didn't match")
            return redirect('register_page')
        user = MyUser.objects.create_user(full_name=cust_name, company_name=cust_cname, email=cust_email, phone_no=cust_phone,
                    address=cust_address, country=cust_country,
                    city=cust_city, state=cust_state, zip_code=cust_zip, password=cust_password, is_admin=False)
        user.save()
        messages.success(request, f"{cust_name} : account is created")
        return redirect('login_page')

from django.db import IntegrityError

@login_required(login_url="login_page")
def user_product_save(request, pk):
    get_product = add_product.objects.get(id=pk)
    user = MyUser.objects.get(email=request.user.email)
    try:
        save_product = ProductSave(name=user, product=get_product)
        save_product.save()
        status = 'success'
        message = 'Product saved'
    except IntegrityError:
        status = 'error'
        message = 'Product already saved'
    return redirect('cart')

@login_required(login_url="login_page")
def user_product_save_real(request):
    if request.method == 'POST':
        get_user = MyUser.objects.get(email=request.user.email)
        get_product_id = request.POST['id']
        get_product = add_product.objects.get(id=get_product_id)
        get_color = request.POST['color_name']
        get_size = request.POST['size_name']
        get_current_price = request.POST['p_current_price']
        get_quantity = request.POST['p_qty']
        get_product_quantity = int(get_product.quantity)
        get_id = get_product.id
        if int(get_quantity) > get_product_quantity:
            messages.error(request, "Selected Quantity is more than the available quantity")
            return redirect('single_product', get_id)
        get_total = int(get_current_price) * int(get_quantity)
        print("Size Name : ", get_size)
        print("Color Name : ", get_color)
        data = ProductSave(name=get_user, product=get_product, color=get_color, size=get_size,
                            quantity=get_quantity, price=get_current_price, total = get_total)
        data.save()
        return redirect('cart')
 
def order_product(request, pk):
    get_product = ProductSave.objects.get(id=pk)
    get_product.status = True
    delivery_text = request.GET['delivery-type']
    print("Diverli text ============> : ", delivery_text)
    get_product.save()
    get_user = MyUser.objects.get(email=request.user.email)
    status = "Pending"
    shipping = "Pending"
    data = OrderProduct(get_user=get_user, product=get_product, status=status, delivery_type=delivery_text, shipping=shipping)
    data.save()
    return redirect('user_orders')

@login_required(login_url="login_page")
def get_transaction(request):
    get_user = MyUser.objects.get(email=request.user.email)
    user_transaction = Transaction.objects.filter(user=get_user)
    return HttpResponse("Called...")

@login_required(login_url="login_page")
def check_out_complete(request):
    get_user = MyUser.objects.get(email=request.user.email)
    get_user_products = ProductSave.objects.filter(name=get_user)
    total_price = 0
    transaction = Transaction(
        transaction_id=str(uuid.uuid1()),
        user=get_user, total_price=12
    )
    transaction.save()
    for product in get_user_products:
        total_price += product.price * product.quantity
        transaction.products.add(product)
    context = {'get_user_products': get_user_products, 'get_user': get_user, 'total_price': total_price}
    return HttpResponse("Saved...")

from customadmin.models import user_messages

def user_contact(request):
    if request.method == 'POST':
        name = request.POST['visitor_name']
        email = request.POST['visitor_email']
        phone = request.POST['visitor_phone']
        message = request.POST['visitor_message']
        data = user_messages(user_name=name, email=email, phone_no=phone, message=message)
        data.save()
        messages.error(request, "Message is sent successfully")
        return redirect('contact_us')