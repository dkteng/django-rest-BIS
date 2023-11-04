from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    borrow_date = models.DateTimeField(null=True, blank=True)
    due_date =  models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.title



