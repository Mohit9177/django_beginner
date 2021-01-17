from django.db import models

# Create your models here.
from authentication.models import ModelBase, User


class Grade(ModelBase):
    name = models.CharField(max_length=19)


class Subject(ModelBase):
    name = models.CharField(max_length=19)


class Room(ModelBase):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)


class Report(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    attention = models.DecimalField(decimal_places=2, max_digits=4)