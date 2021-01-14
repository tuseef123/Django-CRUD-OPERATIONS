from django.db import models
# Create your models here.
class record(models.Model):
    p_name=models.CharField(max_length=40)
    catagory=models.CharField(max_length=40)
    quantity=models.IntegerField()
    quality=models.CharField(max_length=50)
    room=models.IntegerField()
    def __str__(self):
        return self.p_name

