from django.views.generic import TemplateView , CreateView , ListView , UpdateView  , DetailView , DeleteView
from .models import *
from django.urls import reverse_lazy #for delete
from django.shortcuts import render , get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import CartForm
from django.contrib import messages
from django.db.models import F , Sum
from django.views.generic import View

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('panel/')
        return super().get(request, *args, **kwargs)

class ComingSoonView(TemplateView):
    template_name = 'ComingSoon.html'

class PanelView(TemplateView):
    template_name = 'panel/panel.html'


#USER VIEWS-------------------
# Product views
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_view.html'

    def get_queryset(self):
        user_city = self.request.user.city
        queryset = super().get_queryset()
        queryset = queryset.filter(inventoryproduct__inventory__city=user_city)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['supplier_list'] = self.object.supplier.all()
        context['cart_form'] = CartForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = CartForm(request.POST)
        if form.is_valid():
            product = self.get_object()
            quantity = form.cleaned_data['quantity']
            user = request.user  # نام کاربری فعلی
            try:
                cart = Cart.objects.get(user=user)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(user=user)
            try:
                cart_item = CartItem.objects.get(cart=cart, product=product)
                cart_item.quantity += quantity
            except CartItem.DoesNotExist:
                cart_item = CartItem(cart=cart, product=product, quantity=quantity)
            cart_item.save()
            cart_pk = cart.pk  # شناسه سبد خرید
            cart_view_url = reverse('cart_view', kwargs={'pk': cart_pk})
            return redirect(cart_view_url)
        else:
            context = self.get_context_data(**kwargs)
            context['cart_form'] = form
        return self.render_to_response(context)


class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'cart_view.html'
    context_object_name = 'cart'
    
    def get_object(self, queryset=None):
        user = self.request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user)
        return cart


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = CartItem.objects.filter(cart=self.object)
        total_prices = cart_items.annotate(total_price=F('quantity') * F('product__price'))
        cart_total = total_prices.aggregate(total=Sum('total_price'))['total']
        context['cart_items'] = zip(cart_items, total_prices)
        context['cart_total'] = cart_total
        return context
    
class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        cart_items_with_status = cart_items
        
        print(cart_items_with_status)  # نمایش محتویات
        
        if cart_items_with_status:
            context = {
                'cart_items': cart_items_with_status,
            }
            return render(request, 'checkout.html', context)
        else:
            return render(request, 'checkout.html', {'message': 'No products to checkout.'})



#ADMIN VIEWS-------------------
# Category views
class CategoryListView(ListView):
    model = Category
    template_name = 'panel/category/category_view.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'panel/category/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'panel/category/category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('category_view')

class CategoryUpdateView(UpdateView): 
    model = Category
    template_name = 'panel/category/category_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('category_view')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'panel/category/category_delete.html'
    success_url = reverse_lazy('category_view')


# Supplier views
class SupplierListView(ListView):
    model = Supplier
    template_name = 'panel/supplier/supplier_view.html'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'panel/supplier/supplier_detail.html'

class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'panel/supplier/supplier_create.html'
    fields = '__all__'
    success_url = reverse_lazy('supplier_view')

class SupplierUpdateView(UpdateView): 
    model = Supplier
    template_name = 'panel/supplier/supplier_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('supplier_view')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'panel/supplier/supplier_delete.html'
    success_url = reverse_lazy('supplier_view')


# City views
class CityListView(ListView):
    model = City
    template_name = 'panel/city/city_view.html'

class CityDetailView(DetailView):
    model = City
    template_name = 'panel/city/city_detail.html'

class CityCreateView(CreateView):
    model = City
    template_name = 'panel/city/city_create.html'
    fields = '__all__'
    success_url = reverse_lazy('city_view')

class CityUpdateView(UpdateView): 
    model = City
    template_name = 'panel/city/city_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('city_view')

class CityDeleteView(DeleteView):
    model = City
    template_name = 'panel/city/city_delete.html'
    success_url = reverse_lazy('city_view')  


# Inventory views
class InventoryListView(ListView):
    model = Inventory
    template_name = 'panel/inventory/inventory_view.html'

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'panel/inventory/inventory_detail.html'

class InventoryCreateView(CreateView):
    model = Inventory
    template_name = 'panel/inventory/inventory_create.html'
    fields = '__all__'
    success_url = reverse_lazy('inventory_view')

class InventoryUpdateView(UpdateView): 
    model = Inventory
    template_name = 'panel/inventory/inventory_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('inventory_view')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'panel/inventory/inventory_delete.html'
    success_url = reverse_lazy('inventory_view') 


# InventoryProduct(stock) views
class StockListView(ListView):
    model = InventoryProduct
    template_name = 'panel/stock/stock_view.html'

class StockDetailView(DetailView):
    model = InventoryProduct
    template_name = 'panel/stock/stock_detail.html'

class StockCreateView(CreateView):
    model = InventoryProduct
    template_name = 'panel/stock/stock_create.html'
    fields = '__all__'
    success_url = reverse_lazy('stock_view')

class StockUpdateView(UpdateView): 
    model = InventoryProduct
    template_name = 'panel/stock/stock_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('stock_view')

class StockDeleteView(DeleteView):
    model = InventoryProduct
    template_name = 'panel/stock/stock_delete.html'
    success_url = reverse_lazy('stock_view')   


# Product views
class ProductListViewAdmin(ListView):
    model = Product
    template_name = 'panel/product/product_view_admin.html'

class ProductDetailViewAdmin(DetailView):
    model = Product
    template_name = 'panel/product/product_detail_admin.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailViewAdmin, self).get_context_data(**kwargs)
        context['supplier_list'] = self.object.supplier.all()
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'panel/product/product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_view_admin')

class ProductUpdateView(UpdateView): 
    model = Product
    template_name = 'panel/product/product_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('product_view_admin')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'panel/product/product_delete.html'
    success_url = reverse_lazy('product_view_admin')
