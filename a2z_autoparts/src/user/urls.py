from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('home/', TemplateView.as_view(template_name="index.html")),
    path('login/', LoginView.as_view(template_name="login.html")),
    path('logout/', LogoutView.as_view(template_name="logout.html")),
]

