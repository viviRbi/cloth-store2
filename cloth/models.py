from django.db import models

class Category(models.Model):
    name= models.CharField(default='', max_length=25)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(default='', max_length=100)
    des=models.TextField(default='')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField()
    img=models.ImageField(default='', upload_to='cloth_product', unique=True, blank=True)
    created=models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, default='', on_delete= models.CASCADE,related_name='products')

    def __str__(self):
        return self.name