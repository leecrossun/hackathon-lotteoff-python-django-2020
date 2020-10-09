from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class NewProduct(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'image/')
    image_thumnail = ImageSpecField(source='image', processors=[ResizeToFill(150, 100)])

    def __str__(self):
        return self.title

class Apply(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    store_name = models.CharField(max_length=50, null=True)
    date_time = models.CharField(max_length=50, null=True)
    newProduct = models.ForeignKey(NewProduct, on_delete = models.CASCADE)

class Evaluation(models.Model):
    e_title = models.CharField(max_length = 200)
    e_author = models.ForeignKey(User, on_delete = models.CASCADE)
    e_content = models.TextField()
    e_upload_at = models.DateTimeField(auto_now=True)
    e_newProduct = models.ForeignKey(NewProduct, on_delete = models.CASCADE)