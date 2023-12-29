"""shopy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='shophome'),
    path('login/', views.login,name="Login"),
    path('contact/', views.contact,name="ContactUs"),
    path('tracker/', views.tracker,name="TrackingStatus"),
    path('search/', views.search,name="Search"),
    path('products/<int:myid>', views.productView,name="ProductView"),
    path('checkout/',views.checkout,name='Checkout')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

