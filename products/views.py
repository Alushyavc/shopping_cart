from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Product
from django.core.paginator import Paginator
from .mixins import AdminRequiredMixin

# Index View
class IndexView(View):
    def get(self, request):
        featured_products = Product.objects.order_by('priority')[:4]
        latest_product = Product.objects.order_by('-id')[:4]
        context = {
            'featured_products': featured_products,
            'latest_product': latest_product,
        }
        return render(request, 'index.html', context)

# Product List View
class ProductListView(View):
    def get(self, request):
        page = request.GET.get('page', 1)
        product_list = Product.objects.order_by('priority')
        paginator = Paginator(product_list, 8)
        products = paginator.get_page(page)
        context = {'products': products}
        return render(request, 'products.html', context)

# Product Detail View
class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, 'product_details.html', context)

# Admin Product List View
class AdminProductListView(AdminRequiredMixin,LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all().order_by('id')
        context = {'products': products}
        return render(request, 'admin_product_list.html', context)

# Admin Add Product View
class AdminAddProductView(AdminRequiredMixin,LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'admin_product_form.html')

    def post(self, request):
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        image = request.FILES.get('image')

        if title and price and description:
            Product.objects.create(
                title=title,
                price=price,
                description=description,
                priority=priority,
                image=image,
            )
            messages.success(request, "Product added successfully!")
            return redirect('admin_product_list')
        else:
            messages.error(request, "All fields are required.")
            return render(request, 'admin_product_form.html')

# Admin Edit Product View
class AdminEditProductView(AdminRequiredMixin,LoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, 'admin_product_form.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.priority = request.POST.get('priority')
        image = request.FILES.get('image')

        if image:
            product.image = image  # Update image only if a new one is uploaded

        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect('admin_product_list')

# Admin Delete Product View
class AdminDeleteProductView(AdminRequiredMixin,LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('admin_product_list')
