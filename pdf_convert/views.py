from django.shortcuts import render
from accounts.models import MyOrders


# Create your views here.

def download_invoice(request, order_id):
    order = MyOrders.objects.filter(cart__razorpay_order_id=order_id).first()
    if order:
        cart_items = order.cart.cart_items.all()

        # Getting Cart total without Coupen

        cart_total_without_coupon = order.cart.payment_done_amount_without_offer 

        # Getting Minimum Amount of Coupon

        coupon = order.cart.coupen
        if coupon:
            minimum_amount = coupon.minimun_amount   
        else:
            minimum_amount = 0
        
        quantity = sum([cart_item.quantity if cart_item.quantity < cart_item.product.product_available_count else 0 for cart_item in cart_items])
        return render(request, "pdf_convert/bill.html", {'cart_items':cart_items, 'order':order, "quantity":quantity, 'minimum_amount':minimum_amount, 'cart_total_without_coupon': cart_total_without_coupon})