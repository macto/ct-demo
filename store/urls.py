from django.conf.urls import include, url
from django.urls import path

from store.views import home, order, send_order, api

urlpatterns = [
    path('', home.HomeStore.as_view(), name="index"),
    path('order', order.OrderView.as_view(), name="order"),
    path('send-order', send_order.SendOrderView.as_view(), name="send_order"),
    path('api/products/', api.ProductList.as_view()),
    path('api/products/<int:pk>/', api.ProductsOne.as_view()),

    url('accounts/', include("django.contrib.auth.urls")),
]