from django.db import models

# Create your models here.

class HomeModel(models.Model):
    appname = models.CharField('appname' , max_length=100)


    def __str__(self):
        return self.appname

    class Meta:
        verbose_name = 'appname'
        verbose_name_plural = 'appnames'
        