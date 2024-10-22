from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderedItem
from products.models import Product

# Show Cart View
class CartView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        customer = user.customer_profile
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        context = {'cart': cart_obj}
        return render(request, 'cart.html', context)

# Add to Cart View
class AddToCartView(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')

        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product = get_object_or_404(Product, pk=product_id)

        ordered_item, created = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )

        if created:
            ordered_item.qty = quantity
        else:
            ordered_item.qty += quantity
        ordered_item.save()

        return redirect('show_cart')

# Remove Item from Cart View
class RemoveItemView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("pk=",pk)
        item = get_object_or_404(OrderedItem, pk=pk)
        item.delete()
        return redirect('show_cart')
    
# Update Item Quantity View
class UpdateCartItemQuantityView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ordered_item = get_object_or_404(OrderedItem, pk=pk)
        action = request.POST.get('action')

        if action == 'increase':
            ordered_item.qty += 1
        elif action == 'decrease' and ordered_item.qty > 1:
            ordered_item.qty -= 1

        ordered_item.save()
        return redirect('show_cart')
    

