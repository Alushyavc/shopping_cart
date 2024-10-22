from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from .models import Customer

# Sign Out View 
class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

# Account View for Login & Registration 
class AccountView(View):
    def get(self, request):
        storage = messages.get_messages(request)
        storage.used = True
        return render(request, 'account.html')

    def post(self, request):
        context = {}
        if 'register' in request.POST:
            context['register'] = True
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                address = request.POST.get('address')
                email = request.POST.get('email')
                phone = request.POST.get('phone')

                user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                Customer.objects.create(user=user, phone=phone, address=address)

                messages.success(request, "Registration successful!")
                return redirect('index')
            except Exception as e:
                messages.error(request, "Username already exists.")
                return render(request, 'account.html', context)

        if 'login' in request.POST:
            context['register'] = False
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                if user.is_superuser:  
                    return redirect('admin_product_list')
                return redirect('index')
            else:
                messages.error(request, "Invalid credentials.")
        
        return render(request, 'account.html', context)
