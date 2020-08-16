from django.db import models
from django.contrib.auth.models import User

EVALUATION_CHOICES = [('良い','良い'),('悪い','悪い')]
class ReviewModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='')
    usefulll_review = models.IntegerField(null=True, blank=True, default=0)
    usefulll_review_record = models.TextField()
    evaluation = models.CharField(max_length=10, choices=EVALUATION_CHOICES)