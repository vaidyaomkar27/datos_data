from django.db import models

# Create your models here.
class File(models.Model):
    """
    This is simple table which will be used for storing information of file which will be uploaded to our system.
    """
    name = models.CharField(max_length=255)
    file = models.FileField(
    )
    type = models.CharField(
        max_length=255
    )