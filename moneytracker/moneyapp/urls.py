from django.urls import path
from moneyapp import views

urlpatterns = [
    path('',views.index),
    path('account',views.account)
]
