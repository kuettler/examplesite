from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SiteData(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateTimeField('date')
    value_a = models.IntegerField(default=0)
    value_b = models.IntegerField(default=0)

    #def __str__(self):
    #    return str(self.date)

