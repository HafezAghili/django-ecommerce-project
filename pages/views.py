from django.views.generic import TemplateView , CreateView , ListView , UpdateView  , DetailView , DeleteView
from .models import *
from django.urls import reverse_lazy #for delete

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ComingSoonView(TemplateView):
    template_name = 'ComingSoon.html'


# Product views
class ProductListView(ListView):
    model = Product
    template_name = 'product_view.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


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