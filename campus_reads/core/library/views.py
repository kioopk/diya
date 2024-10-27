from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
from .models import Book

def home_page(request):
    # Create a dictionary to store books for each semester
    books_by_semester_half = {}
    # Iterate through each semester
    for semester in range(1, 4):  # Assuming semesters range from 1 to 6
        # Filter books for the current semester
        books = Book.objects.filter(semester=semester)
        if books.count() > 4:
            books = books[:4] 
        # Store the filtered books in the dictionary
        books_by_semester_half[semester] = books
    books_by_semester = {}
    for semester in range(4, 7):  # Assuming semesters range from 1 to 6
        # Filter books for the current semester
        books = Book.objects.filter(semester=semester)
        if books.count() > 4:
            books = books[:4] 
        # Store the filtered books in the dictionary
        books_by_semester[semester] = books
    
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'books_by_sem_1to3': books_by_semester_half,
        'books_by_sem_4to6': books_by_semester,
    }
    return render(request, "library/index.html", context=context)

def books_by_sem(request, sem):
    books = Book.objects.filter(semester=sem)
    context={
        "books": books
    }
    return render(request, "library/book.html", context)