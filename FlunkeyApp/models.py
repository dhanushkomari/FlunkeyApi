from django.db import models
from django.urls import reverse


#################################################################
################          BOT MODEL             #################
#################################################################
class Bot(models.Model):
    bot_no = models.IntegerField(unique=True)
    name = models.CharField(max_length = 50, unique=True)
    color = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to = 'flunky_images', blank = True)
    status = models.BooleanField(default=True, help_text="bot working(active or inactive)")   # active or inactive
    avialable = models.BooleanField(default=True, help_text="available or not avialabe for delivery")  # avialabe to serve or not avialable
    ip = models.CharField(max_length=15)
    port = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Bot'
        verbose_name_plural = 'Bots'
        ordering = ('-id',)

    def __str__(self):
        return self.color
    
    def get_url(self):
        return reverse("FlunkeyApp:select-table", args = [self.id])
################################################################
#################       END OF BOT MODEL   #####################
################################################################




#################################################################
################        TABLE MODELS            #################
#################################################################
class Table(models.Model):
    table_number = models.IntegerField(unique = True)   
    avialable = models.BooleanField(default = True)
    image = models.ImageField(upload_to = 'table_images', blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'
        ordering = ('-table_number',)

    def __str__(self):
        return str(self.table_number)

    def get_url(self):
        return reverse("FlunkeyApp:delivery", args=[self.id])
#################       END OF TABLE MODELS   ##################
################################################################
################################################################


    


#################################################################
################     DELIVERY MODEL             #################
#################################################################
class Delivery(models.Model):
    bot_no = models.IntegerField()
    bot_name = models.CharField(max_length=30)
    table_no = models.IntegerField(null = True)
    ip = models.CharField(max_length=20, null = True)
    port = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now = True)
    food_delivered = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Delivery'
        verbose_name = 'Deliveries'
    
    def __str__(self):
        return (str(self.id) + self.bot_name)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
################################################################
#################     END OF DELIVERY MODELS  ##################
################################################################



class DeliveryFinal(models.Model):
    bot_no = models.IntegerField()
    bot_name = models.CharField(max_length=30)
    table_no = models.IntegerField()
    ip = models.CharField(max_length=20)
    port = models.IntegerField(null = True)
    time = models.IntegerField()
    created_at = models.DateTimeField(auto_now = True)
    food_delivered = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'DeliveryFianl'
        verbose_name = 'All Deliveries'
    
    def __str__(self):
        return (str(self.id) + self.bot_name)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})