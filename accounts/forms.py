from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser
from pages.models import City

class CustomUserCreationForm(UserCreationForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    
    class Meta(UserCreationForm.Meta): 
        model = CustomUser 
        fields = UserCreationForm.Meta.fields + ('city', 'phone_number',)

class CustomUserChangeForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    
    class Meta: 
        model = CustomUser 
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'phone_number')