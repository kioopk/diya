from django.urls import path
from .views import home_page, books_by_sem

app_name = "library"
urlpatterns = [
    path("", home_page, name="home_page"),
    path('sem/<int:sem>/', books_by_sem, name='books_details'),
]