from django.views.generic import TemplateView , CreateView , ListView , UpdateView  , DetailView , DeleteView
from .models import *
from django.urls import reverse_lazy #for delete
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ComingSoonView(TemplateView):
    template_name = 'ComingSoon.html'


# Product views
class ProductListView(LoginRequiredMixin , ListView):
    model = Product
    template_name = 'product_view.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['supplier_list'] = self.object.supplier.all()
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = '__all__'

class ProductUpdateView(UpdateView): 
    model = Product
    template_name = 'product_update.html'
    fields =  '__all__'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_view')