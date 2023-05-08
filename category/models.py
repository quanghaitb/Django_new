from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField()
    parent_cate = models.CharField()
    description = models.TextField()
    image = models.CharField()
    status = models.BooleanField()
    sort_order = models.IntegerField()
    create_at = models.DateTimeField()
    