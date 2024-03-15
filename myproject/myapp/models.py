from django.db import models

# Create your models here.
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True) 
    # Optionally, add more fields such as description, timestamps, etc.
    
    def delete(self, *args, **kwargs):
        # You have to prepare the path to your file
        # Here we are using the 'path' attribute of the FileField
        storage, path = self.video.storage, self.video.path
        # Delete the model before the file
        super().delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)