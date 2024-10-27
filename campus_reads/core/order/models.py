from django.db import models
from students.models import CustomUser
import json
# Create your models here.
class Order(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    books = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.fullname}'s order"
    
    def add_book(self, book_name):
        if self.books:
            try:
                books_list = json.loads(self.books)
            except json.JSONDecodeError:
                books_list = []
        else:
            books_list = []
        
        if book_name not in books_list:
            books_list.append(book_name)
            self.books = json.dumps(books_list)
            self.save()
    
    def remove_book(self, book_name):
        if self.books:
            try:
                books_list = json.loads(self.books)
                if book_name in books_list:
                    books_list.remove(book_name)
                    self.books = json.dumps(books_list)
                    self.save()
            except json.JSONDecodeError:
                print("sedlife")