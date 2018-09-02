import random
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    owner =models.ForeignKey('auth.User',related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    num = models.CharField(max_length=20)
    price = models.FloatField()
    have_sale = models.BooleanField(default=False)
    discount = models.FloatField(default=0.0)
    price_afte_sale = models.FloatField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def save(self,*args,**kwargs):
        if self.have_sale:
            self.price_afte_sale = self.price - (self.price * self.discount)
        else:
            self.price_afte_sale = self.price

        super().save(*args,**kwargs)
        self.num =  str(self.id)+self.name[0]+self.name[-1]+str(random.randint(1, 1000))

    def __str__(self):
        return self.name + f': id = {self.id}'
