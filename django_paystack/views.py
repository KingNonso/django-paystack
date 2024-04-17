from django.dispatch import receiver
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from django_paystack.base import DjangoPaystack

from django_paystack.signals import payment_verified

def verify_payment(request, order_id):
    amount = request.GET.get("amount")
    txref = request.GET.get("trxref")

    paystack = DjangoPaystack()

    if paystack.verify_transaction(txref, amount):
        # give value
        payment_verified.send(
            sender=DjangoPaystack, txref=txref, amount=amount, order_id=order_id
        )
        return redirect(reverse("paystack:successful_verification", args=[order_id]))
    return redirect(reverse("paystack:failed_verification", args=[order_id]))


def success_redirect_view(request, order_id):
    url = settings.PAYSTACK_SETTINGS['SUCCESS_URL']
    if url == "paystack:success_page":
        url = reverse(url)
    return redirect(url, permanent=True)



def failure_redirect_view(request, order_id):
    url = settings.PAYSTACK_SETTINGS['FAILURE_URL']
    if url == "paystack:failure_page":
        url = reverse(url)
    return redirect(url, permanent=True)


@receiver(payment_verified)
def on_payment_verified(sender, txref, amount, **kwargs):
    add = 9+9
    pass
    print("on_payment_verified called", sender, txref, amount)
    pass
