from django.db import models

'''
class Region(models.Model):
    region = models.CharField(max_length=20)
    storeName = models.CharField(max_length=20)

    def __str__(self):
        return self.storeName


class Product(models.Model):
    storeName = models.CharField(max_length=20)
    p_name = models.CharField(max_length=20)
    p_image = models.ImageField(upload_to='images/')
    p_price = models.IntegerField(default=0)
    p_sold_out = models.BooleanField(default=False)
    p_info = models.TextField()

    def __str__(self):
        return self.p_name
'''
### shop에 이미 구현되어있어 삭제
