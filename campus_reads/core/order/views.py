from django.shortcuts import render, get_object_or_404
from library.models import Book
from .models import Order
from django.contrib.auth.decorators import login_required
import ast
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
@login_required
def add_book_to_cart(request, book_id):
    user = request.user
    book = get_object_or_404(Book, id=book_id)
    
    # Get or create the order for the current user
    order, created = Order.objects.get_or_create(user=user)
    order.add_book(book.name)
    
    books = ast.literal_eval(order.books)
    context={
        "books": books,
    }
    return render(request, "order/cart.html", context=context)

@login_required
def remove_from_cart(request, book_name):
    user = request.user
    
    # Get or create the order for the current user
    order, created = Order.objects.get_or_create(user=user)
    order.remove_book(book_name)
    
    books = ast.literal_eval(order.books)
    context={
        "books": books,
    }
    return render(request, "order/cart.html", context=context)

@login_required
def cart(request):
    user = request.user
    order, created = Order.objects.get_or_create(user=user)
    books = ast.literal_eval(order.books)
    context={
        "books": books,
    }
   
    return render(request, "order/cart.html", context=context)


def send_email(request):
    # uszt negf gzos wlws
    print("hi")
    send_mail("test", "hi msg", "settings.EMAIL_HOST_USER", ["mecoc1011@gmail.com"], fail_silently=False)
    print("bye")
    return render(request, "library/index.html")
    