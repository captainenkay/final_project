from django.urls import path
from django.conf.urls import url


from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name='index'),
    path('shopcart', views.shop_cart_list, name='shopcart'),
    path('addtocart/<int:proid>', views.shop_cart_add, name='addtocart'),
    url(r'^updatecart/(?P<proid>\d+)/$', views.shop_cart_add, name='updatecart'),
    path('deletefromcart/<int:id>', views.shop_cart_delete, name='deletefromcart'),
    path('detail/<int:id>', views.order_detail, name='orderdetail'),
    path('checkout', views.shop_cart_checkout, name='checkout'),
    ]