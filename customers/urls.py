from django.urls import path
from .views import AccountView, SignOutView

urlpatterns = [
    path('account/', AccountView.as_view(), name='showaccount'),
    path('logout/', SignOutView.as_view(), name='signout'),
]
