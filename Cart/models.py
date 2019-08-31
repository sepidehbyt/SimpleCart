from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    # models.TextField , models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name