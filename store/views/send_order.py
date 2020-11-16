from django.core.mail import EmailMessage
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from djqscsv import write_csv

from store.models import Order, Product


class SendOrderView(LoginRequiredMixin, TemplateView):
    template_name = "sent.html"
    http_method_names = ["post"]

    def build_msg(self, order: Order, address: str) -> EmailMessage:
        body_init = "New order has just been saved on store. Details in attached file\n"
        body_addr = f"Address: {address}\n"
        body_price = f"Amount to pay: {order.total_amount}\n"
        msg = EmailMessage(f"New Order {order.id}",
                           f"{body_init} Order Data:\n - {body_addr} - {body_price}",
                           "Bernini Store <bernini-store@m.macto.es>",
                           ["Orders <jdct@macto.es>"])
        products = order.products.all()
        with open("products.csv", "wb") as attachment:
             write_csv(products, attachment)
        msg.attach_file("products.csv")

        return msg

    def post(self, request: HttpRequest, *args, **kwargs):
        order = request.POST.get("order_id")
        address = request.POST.get("address")
        notes = request.POST.get("notes")

        email_msg = self.build_msg(Order.objects.get(pk=order), address)
        email_msg.send()

        return render(request, self.template_name, {"order": order, address: "address", notes: "notes"})

