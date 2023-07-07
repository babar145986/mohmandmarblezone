from django import forms
from .models import MyUser

class MyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone_no = forms.CharField(widget=forms.NumberInput)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}))

    class Meta:
        model = MyUser
        fields = ['email', 'full_name', 'company_name', 'phone_no', 'address', 'country', 'city', 'state', 'zip_code', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_phone_no(self):
        phone_no = self.cleaned_data['phone_no']
        if len(phone_no) != 11:
            raise forms.ValidationError("Phone number must be 11 digits.")
        return phone_no