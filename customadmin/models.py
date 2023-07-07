from django.db import models

# Create your models here.

class add_top_category(models.Model):
    top_category_name = models.CharField(max_length=120)
    show_top_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.top_category_name
    
    class Meta:
        verbose_name_plural = "1 - Add Top Category"

class add_mid_category(models.Model):
    select_top_category = models.ForeignKey(add_top_category, on_delete = models.CASCADE)
    mid_category_name = models.CharField(max_length=120)
    show_mid_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.mid_category_name 

    class Meta:
        verbose_name_plural = "2 - Add Mid Category"

class add_end_category(models.Model):
    select_top_category = models.ForeignKey(add_top_category, on_delete=models.CASCADE, null=True, blank=True)
    select_mid_category = models.ForeignKey(add_mid_category, on_delete = models.CASCADE)
    end_category_name = models.CharField(max_length=120)
    show_end_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.end_category_name

    class Meta:
        verbose_name_plural = "3 - Add End Category"

class add_size(models.Model):
    size_name = models.CharField(max_length=100)

    def __str__(self):
        return self.size_name
    
    class Meta:
        verbose_name_plural = "4 - Add Size"

class add_color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name_plural = "5 - Add Color"

class add_country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = "6 - Add Country"

class add_product(models.Model):
    select_top_category = models.ForeignKey(add_top_category, on_delete = models.CASCADE)
    select_mid_category = models.ForeignKey(add_mid_category, on_delete = models.CASCADE)
    select_end_category = models.ForeignKey(add_end_category, on_delete = models.CASCADE)
    product_name = models.CharField(max_length=120)
    old_price = models.IntegerField(null=True, blank=True)
    current_price = models.IntegerField()
    quantity = models.IntegerField()
    select_size = models.ManyToManyField(add_size, blank=True)
    select_color = models.ManyToManyField(add_color, blank=True)
    featured_photo = models.ImageField(upload_to="Media/Product_Images/Featured_image")
    photo_1 = models.ImageField(upload_to="Media/Product_Images/Other_Images", null=True, blank=True)
    photo_2= models.ImageField(upload_to="Media/Product_Images/Other_Images", null=True, blank=True)
    photo_3 = models.ImageField(upload_to="Media/Product_Images/Other_Images", null=True, blank=True)
    photo_4 = models.ImageField(upload_to="Media/Product_Images/Other_Images", null=True, blank=True)
    description = models.TextField()
    short_description = models.TextField()
    featured_desc = models.TextField()
    condition_desc = models.TextField()
    return_policy_desc = models.TextField()
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.select_top_category.top_category_name + " --- " + self.select_mid_category.mid_category_name + " --- " + self.select_end_category.end_category_name + " --- " + self.product_name

    class Meta:
        verbose_name_plural = "7 - Add Product"

class add_social_media_links(models.Model):
    facebook = models.CharField(max_length=10000, null=True, blank=True)
    twitter = models.CharField(max_length=10000, null=True, blank=True)
    youtube = models.CharField(max_length=10000, null=True, blank=True)
    watsapp = models.CharField(max_length=10000, null=True, blank=True)

class add_logo(models.Model):
    upload_logo = models.ImageField(upload_to='Media/website_images/')

class add_favicon(models.Model):
    upload_favicon = models.ImageField(upload_to="Media/website_images/")

class add_footer_contact(models.Model):
    footer_copyright = models.CharField(max_length=1000, null=True, blank=True)
    contact_address = models.TextField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_no = models.CharField(max_length=100, null=True, blank=True)
    map_iframe = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    
class add_slider(models.Model):
    image = models.ImageField(upload_to="Media/website_images/slider")
    heading = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=2000, null=True, blank=True)
    button_text = models.CharField(max_length=100, null=True, blank=True)
    button_url = models.CharField(max_length=1000, null=True, blank=True)
    status = models.BooleanField()
    
    def __str__(self):
        return self.heading
    
class user_messages(models.Model):
    user_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    phone_no = models.CharField(max_length=120, null=True, blank=True)
    message = models.CharField(max_length=120, null=True, blank=True)
    
    def __str__(self):
        return self.user_name
    