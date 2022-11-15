from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index, name='index'),
    path('cart/',views.cart, name='cart'),
    path('productsingle/<int:id>',views.productsingle, name='productsingle'),
    path('order/',views.order, name='order'),
    path('product/',views.product, name='product'),
    path('product/<int:id>',views.product, name='productsort'),
    
    path('checkout/',views.checkout, name='checkout'),
    path('success/',views.success, name='success'),
    path('oredersingle/<int:id>',views.ordersingle, name='ordersingle'),
    path('add/<int:pk>/', views.cart_add, name='cart_add'),
    path('remove/<int:pk>/',views.cart_remove, name='cart_remove'),
    path('login/',views.signin, name = 'login'),
    path('signup/',views.signup, name= 'signup'),
    path('logout/',views.signout, name='logout')
]
