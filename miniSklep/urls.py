"""
URL configuration for miniSklep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miniSklepApp.views import index, login_view, add_product, logout_view, delete_product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('add', add_product, name='add_product'),
    path('logout', logout_view, name='logout'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
]
