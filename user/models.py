from django.db import models
from administrator.models import Mobile

# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    price_total=models.PositiveBigIntegerField(editable=False,blank=True,null=True)
    user = models.CharField(max_length=120,null=True)
    def save(self,*args,**kwargs):
        self.price_total=self.product.price*self.quantity
        super(Cart, self).save(*args,**kwargs)


class Orders(models.Model):
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    address=models.CharField(max_length=150)
    choices=(
        ('Ordered','Ordered'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    status=models.CharField(max_length=150,choices=choices,default='Ordered')
    user=models.CharField(max_length=120)
