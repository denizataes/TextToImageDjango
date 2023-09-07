from django.db import models

class TextToImage(models.Model):
    query = models.CharField(max_length=255)  # Adjust max_length as needed
    image = models.ImageField(upload_to='static/images/')  # 'static/images/' is the subdirectory where uploaded images will be stored

    def __str__(self):
        return self.query  # This is optional, it defines how the object is displayed in the admin panel

    class Meta:
        verbose_name_plural = 'TextToImages'  # Optional, for better display in the admin panel
