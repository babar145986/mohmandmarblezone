from django.shortcuts import render
from django.http import HttpResponse
from customadmin.models import add_product, add_top_category, add_mid_category, add_end_category
from django.contrib.auth.decorators import login_required
from customadmin.models import add_logo, add_favicon, add_footer_contact, add_social_media_links

# Create your views here.
from django.shortcuts import render, get_object_or_404

def search_product_category(request, pk):
    top_category = get_object_or_404(add_top_category, pk=pk)
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    mid_categories = add_mid_category.objects.filter(select_top_category=top_category)
    end_categories = add_end_category.objects.filter(select_mid_category__in=mid_categories)
    products = add_product.objects.filter(select_end_category__in=end_categories)
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    print("=================================================================")
    print("Mide Category Element", mid_categories)
    print("=================================================================")
    print("End Level Category : ", end_categories)
    print("=================================================================")
    print("Products : ", products)
    print("=================================================================")
    context = {
        'top_category': top_category,
        'products': products,
        'top_categories': top_categories, 
                'add_mid_category': add_mid_category, 'add_end_category': add_end_category,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'search_product_category.html', context)

from django.db.models import Subquery, OuterRef

def filter_end_category(request, end_category_id):
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    end_category = add_end_category.objects.filter(id=end_category_id).first()
    
    # Check if end category exists
    if not end_category:
        return render(request, 'end_category_not_found.html', {'top_categories': top_categories})
    
    products = add_product.objects.filter(select_end_category_id=end_category_id)
    
    # Another way to filter the products based on the end category ID using a subquery
    # products = add_product.objects.filter(select_end_category=end_category)
    # products = products.annotate(end_category_id=Subquery(add_end_category.objects.filter(id=OuterRef('select_end_category_id')).values('id')[:1]))
    # products = products.filter(end_category_id=end_category_id)
     
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    
    context = {
        'products': products,
        'top_categories': top_categories,
        'get_logo': get_logo,
        'get_favicon': get_favicon,
        'get_footer_contact': get_footer_contact, 
        'get_social_links': get_social_links,
        'end_category': end_category
    }
    return render(request, 'end_category_products.html', context)



def filter_mid_category(request, mid_category_id):
    all_products = add_product.objects.all()
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    all_mid_categories = add_mid_category.objects.all()
    all_end_categories = add_end_category.objects.all()
    mid_category = add_mid_category.objects.get(id=mid_category_id)
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    products = add_product.objects.filter(select_mid_category=mid_category)
    context = {
        'mid_category': mid_category,
        'products': products,
        'all_products': all_products, 'top_categories': top_categories, 
                'add_mid_category': add_mid_category, 'add_end_category': add_end_category,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links
    }
    print("MID Category : ", mid_category.mid_category_name)
    for i in products:
        print(i.product_name)
    return render(request, 'filter_mid_category.html', context)

from customadmin.models import add_slider

def index(request):
    all_sliders = add_slider.objects.all()
    all_products = add_product.objects.filter(is_active=True)
    latest_products = add_product.objects.filter(is_active=True, is_featured=True)
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    all_mid_categories = add_mid_category.objects.all()
    all_end_categories = add_end_category.objects.all()
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'all_products': all_products, 'top_categories': top_categories, 
                'add_mid_category': add_mid_category, 'add_end_category': add_end_category, 
                'latest_products': latest_products, 
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links, 'all_sliders': all_sliders}
    return render(request, 'index.html', context)

def product_category(request):
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    products = add_product.objects.filter(is_active=True)
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'top_categories': top_categories, 'products': products,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'product_category.html', context)

def product_mid_category(request, pk):
    return HttpResponse("Hello")

def product_end_category(request, pk):
    return HttpResponse("Hello")

def about_us(request):
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    all_top_categories = add_top_category.objects.all()
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'all_top_categories': all_top_categories,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links, 'top_categories': top_categories}
    return render(request, 'about_us.html', context)

def faq(request):
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    all_top_categories = add_top_category.objects.all()
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'all_top_categories': all_top_categories,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links, 'top_categories': top_categories}
    return render(request, 'faq.html', context)

def contact_us(request):
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    all_top_categories = add_top_category.objects.all()
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'all_top_categories': all_top_categories,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links, 'top_categories': top_categories}
    return render(request, 'contact_us.html', context)


def single_product(request, pk):
    top_categories = add_top_category.objects.all()
    get_product = add_product.objects.get(id=pk)
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    context = {'get_product': get_product, 'top_categories': top_categories,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'single_product_info.html', context)


def search_product(request):
    top_categories = add_top_category.objects.filter(show_top_menu=True)
    products = add_product.objects.filter(is_active=True)
    get_logo = add_logo.objects.last()
    get_favicon = add_favicon.objects.last()
    get_footer_contact = add_footer_contact.objects.last()
    get_social_links = add_social_media_links.objects.last()
    if request.method == 'GET':
        name = request.GET['search_text']
        products = add_product.objects.filter(product_name__icontains=name)
    context = {'top_categories': top_categories, 'products': products,
                'get_logo': get_logo, 'get_favicon': get_favicon, 'get_footer_contact': get_footer_contact, 
                'get_social_links': get_social_links}
    return render(request, 'search_product.html', context)