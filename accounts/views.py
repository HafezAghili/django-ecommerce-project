from django.shortcuts import render , redirect
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy 
from django.views import generic

from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import PasswordChangeView

# Create your views here.



class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'
    
class ChangePassView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('login') 


@method_decorator(login_required(login_url='login'), name='dispatch')
class LogoutView(View):
    def get(self, request):
        return render(request, 'registration/logout.html')

    def post(self, request):
        logout(request)
        return redirect('login')