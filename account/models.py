from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, company_name, phone_no, address, country, state, city, zip_code, is_admin, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            full_name = full_name, 
            company_name = company_name, 
            phone_no = phone_no, 
            address = address, 
            country = country, 
            state = state, 
            city = city, 
            zip_code = zip_code,
            is_admin = is_admin
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    phone_regex = RegexValidator(
        regex=r'^\d{11}$',
        message="Phone number must be exactly 11 digits."
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    full_name = models.CharField(max_length=100, blank=False, null=False)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(validators=[phone_regex], max_length=11, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=128, blank=False, null=False)
    confirm_password = models.CharField(max_length=128, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return True

from customadmin.models import add_product

class ProductSave(models.Model):
    name = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)
    color = models.CharField(max_length=120, null=True, blank=True)
    size = models.CharField(max_length=120, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    issue_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False, null=True, blank=True)

import uuid

class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid1, editable=False, unique=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(ProductSave, related_name='transactions')
    
class OrderProduct(models.Model):
    status_list = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Not Available', 'Not Available')
    )
    shiping_list = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
    get_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductSave, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=status_list, null=True, blank=True)
    shipping = models.CharField(max_length=20, choices=shiping_list, null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    delivery_type = models.CharField(max_length=120, null=True, blank=True)
    