"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from phone import views
from phone_api import views as v1
from ipad import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('showphone/',views.showphone,name='showphone'),
    path('details/<int:id>/',views.details,name='details'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_register/',views.auth_register,name='auth_register'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('aut_logout/',views.aut_logout,name='aut_logout'),
    path('checkout/',views.checkout,name='checkout'),
    path('add_to_cart<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('api/itemlist/all',v1.getallitems,name='itemsall'),
    path('api/list_item_details/details',v1.list_item_details,name='details'),
    path('api/list_item_detailsbyid/details/<int:id>/',v1.list_item_detailsbyid,name='detailsbyid'),
    path('done/',views.done,name='done'),
    path('detailsipad/<int:id>/',v2.detailsipad,name='detailsipad'),
    path('showipad/',v2.showipad,name='showipad'),
    path('add_to_cart_ipad<int:id>/',v2.add_to_cartipad,name='add_to_cart_ipad'),
    path('checkout_ipad/',v2.cipad,name='checkout_ipad'),
    path('pay/',views.pay,name='pay'),
    path('addcarde/',views.addcarde,name='addcarde'),
    path('addcardeipad/',v2.addcardeipad,name='addcardeipad'),
    path('payipad/',v2.payipad,name='pay'),
    path('done_ipad/',v2.doneipad,name='done'),
]