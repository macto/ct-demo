from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Order, Product


class OrderView(LoginRequiredMixin, TemplateView):
    template_name = "order.html"
    http_method_names = ["post", "get"]

    def post(self, request: HttpRequest, *args, **kwargs):
        key_products = request.POST.getlist("items_keys")
        num_products = request.POST.getlist("items_values")
        data = []
        total_items = 0
        total_price = 0
        for i, j in zip(key_products, num_products):
            q = int(j) if j else 0
            total_items += q
            data.append({"id": int(i), "quantity": q})
        if total_items is 0:
            error = "None products were selected. Please, retry"
            order = None
        else:
            error = None
            for elem in data:
                if elem["quantity"] > 0:
                    p = Product.objects.get(pk=elem["id"])
                    total_price += p.price * elem["quantity"]

            order = Order.objects.create(total_amount=total_price)
            order.user = self.request.user
            for p in data:
                if p["quantity"] > 0:
                    order.products.add(p["id"], through_defaults={"quantity": p["quantity"]})

            order.save()

        return render(request, self.template_name, {"order": order, "price": total_price, "error": error})

