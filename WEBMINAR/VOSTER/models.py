from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class HW(models.Model):
    toolname=models.CharField(max_length=200)
    insname=models.CharField(max_length=100)
    start=models.DateTimeField("BEGAN FROM")
    
    def __str__(self):
        return self.toolname
    def was_published_recently(self):
        return self.beganfrom>=timezone.now()-datetime.timedelta
class details(models.Model):
    couse=models.ForeignKey(HW, on_delete=models.CASCADE)
    ct=models.CharField(max_length=500)
    your_choice=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.ct)

from django.db import models


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='imag/')

    def __str__(self):
        return self.title