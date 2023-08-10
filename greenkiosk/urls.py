"""
URL configuration for greenkiosk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory/",include("inventory.urls")),
    path("cart/",include("cart.urls")),
    path("customer_management/",include("customer_management.urls")),
    path("payment/",include("payment.urls")),
    path("order/",include("order.urls")),
    path("vendor/",include("vendor.urls")),
    path("review/",include("review.urls")),
    path("cart/",include("cart.urls")),
    path("shipping/",include("shipping.urls")),
    path("discount/",include("discount.urls")),
     
      
]
