from django.db import models
import hashlib
# Create your models here.


class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    hash = models.CharField(max_length=64, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = self.calculate_hash()
        super().save(*args, **kwargs)

    def calculate_hash(self):
        hasher = hashlib.sha256()
        self.file.seek(0)
        for chunks in iter(lambda: self.file.read(8192), b""):
            hasher.update(chunks)
        return hasher.hexdigest()
    
    def __str__(self):
        return f"File: {self.file.name} - Hash: {self.hash}"