from django import forms
from django.contrib.auth.models import User
from apps.userprofile.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Client, Lead, Invoice, Task

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
        ]
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image'
        ]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

# Task Management 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['client', 'task_id', 'task_name', 'date_issued', 'due_date', 'status']


from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity', 'category', 'image']
