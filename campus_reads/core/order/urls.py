from django.urls import path
from .views import add_book_to_cart, remove_from_cart, cart, send_email

app_name = "order"
urlpatterns = [
    path("book/<int:book_id>/", add_book_to_cart, name="add_2_order"),
    path("book/<str:book_name>/", remove_from_cart, name="remove_book"),
    path("book/cart/", cart, name="cart"),
    path("book/mail/", send_email, name="send_mail"),
]