from django.db import models

# Abstract base class
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Abstract base

# Multi-table inheritance
class Person(TimestampedModel):
    name = models.CharField(max_length=100)

class Student(Person):
    student_id = models.CharField(max_length=20)

# Proxy model
class StudentProxy(Student):
    class Meta:
        proxy = True
        ordering = ["student_id"]

    def __str__(self):
        return f"[Proxy] {self.name} - {self.student_id}"
