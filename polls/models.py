from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    number = models.CharField(max_length=4)
    question = models.CharField(max_length=300)
    points = models.IntegerField(default=1)
    created = models.DateTimeField('created')
    published = models.DateTimeField('published')

    def __str__(self):
        return f"{self.number}: {self.question}"

    def age(self):
        return timezone.now() - self.published

    def published_recently(self):
        return datetime.timedelta(days=1) >= self.age()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)
    created = models.DateTimeField('created')

    def __str__(self):
        return f"{self.choice}"

