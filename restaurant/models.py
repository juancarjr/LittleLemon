from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    # no_of_guests = models.SmallIntegerField(null=False)

    def __str__(self): 
        return self.name


class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
   inventory = models.SmallIntegerField()
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self):
      return f'{self.title} : {str(self.price)}'
