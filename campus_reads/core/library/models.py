from django.db import models

class Book(models.Model):

    SEMESTER_CHOICES = [
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
    ]

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', default='img/placeholder_book.webp')
    quantity = models.PositiveIntegerField()
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES)

    def __str__(self):
        return self.name
