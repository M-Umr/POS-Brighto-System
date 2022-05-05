from django.db import models
#from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class POS_Table(models.Model):
    all_brand = [
        ("Brighto", "Brighto"),
        ("Daimond", "Daimond"),
        ("Nippon", "Nippon"), 
    ]
    size = [
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"), 
    ]
    name = models.CharField(_("Name of the Goods"), max_length=100)
    brand = models.CharField(
        choices=all_brand,
        max_length=100
        )
    type = models.CharField(
        max_length=255,
        choices=size,
    )
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.price = self.price*self.quantity
        super().save(*args, **kwargs)