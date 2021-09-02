from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is notthing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IUTHGAWMAUBj98U0Y14RaGZz2l32q9BZEOX8m2iULQKF79HqTt47YogQmvZSZRwZbyy4hstD6qNanG6gtsM8AX300TestbLtB',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
