from django.db import models

# Model for themes of site

class Sitesettings(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()
