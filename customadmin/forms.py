from django import forms
from .models import add_product, add_slider

class AddProductForm(forms.ModelForm):
    class Meta:
        model = add_product
        fields = '__all__'
        widgets = {
            'select_top_category': forms.Select(attrs={'class': 'form-control'}),
            'select_mid_category': forms.Select(attrs={'class': 'form-control'}),
            'select_end_category': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'old_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'select_size': forms.CheckboxSelectMultiple(),
            'select_color': forms.CheckboxSelectMultiple(),
            'featured_photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_1': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_2': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_3': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_4': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_desc': forms.Textarea(attrs={'class': 'form-control'}),
            'condition_desc': forms.Textarea(attrs={'class': 'form-control'}),
            'return_policy_desc': forms.Textarea(attrs={'class': 'form-control'}),
            'is_active': forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-control'}),
            'is_featured': forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-control'}),
        }
        
class AddSliderForm(forms.ModelForm):
    class Meta:
        model = add_slider
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'heading': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'button_text': forms.TextInput(attrs={'class': 'form-control'}),
            'button_url': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-control'}),
        }
