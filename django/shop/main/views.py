from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from .models import *

# Create your views here.
def drugs(request):
    cart = get_cart(request)  # Get or create the session-based cart
    cart_items = cart.cartitem_set.all()  # Fetch all items in the cart
    content = Drugs.objects.all()  # Get all drugs from the database

    return render(request, 'index.html', {
        'drugs': content,
        'cart_items': cart_items,  # Optionally pass cart items to the template
    })


def cart(request):
    cart = get_cart(request)  # Get or create the session-based cart
    cart_items = cart.cartitem_set.all()  # Fetch all items in the cart

    return render(request, 'cart.html', {
        'cart': cart,
        'cart_items': cart_items,
    })


def get_cart(request):
    # Get or create a session ID if it's missing
    session_id = request.session.get('cart_id')

    if not session_id:
        session_id = get_random_string(32)  # Generate a unique session ID
        request.session['cart_id'] = session_id

    # Get or create a cart based on the session ID
    cart, created = Cart.objects.get_or_create(session_id=session_id)
    return cart


def add_to_cart(request, drug_id):
    drug = get_object_or_404(Drugs, id=drug_id)
    cart = get_cart(request)  # Get or create the cart based on the session

    # Check if the item is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, drug=drug)

    if not created:
        cart_item.quantity += 1  # Increment quantity if already exists
        
    cart_item.save()

    return JsonResponse({'message': 'Added to cart', 'cart_total': cart.total_price})