from django.db import models

# Create your models here.

class NotesMedia(models.Model):
    file_name = models.CharField(max_length=50)
    file_date = models.DateField()
    file = models.FileField(upload_to='notes')
    notes_id = models.CharField(max_length=50,)

    def __str__(self):
        return self.file_name

    @property
    def file_size(self):
        try:
            x = self.file.size
            y = 512000
            if x < y:
                value = round(x / 1000, 1)
                ext = ' KB'
            else:
                value = round(x / 1000000, 1)
                ext = ' MB'
            return str(value) + ext
        except Exception:
            return None

class NotesLink(models.Model):
    n_link = models.CharField(max_length=200)
    n_link_about = models.TextField(max_length=100)
    n_link_id= models.CharField(max_length=50)

    def __str__(self):
        return self.n_link