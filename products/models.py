from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    """Model definition for Product."""
    objects  = models.Manager()
    title    = models.CharField(default='请输入标题',max_length=50)
    intro    = models.TextField(default='请输入介绍')
    url      = models.CharField(default='',max_length=100)
    icon     = models.ImageField(default='default_icon.png',upload_to='images/')
    image    = models.ImageField(default='default_image.png',upload_to='images/')
    votes    = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
    hunter   = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """Unicode representation of Product."""
        return self.title