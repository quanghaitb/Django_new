from django.db import models

# Create your models here.


class postForm(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    # short_description = models.TextField()
    # status = models.BooleanField("True")
    created_at = models.DateTimeField(auto_now_add=False)
    
    
    