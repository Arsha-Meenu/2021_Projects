from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length = 255)
    age = models.FloatField()
    image = models.CharField(max_length=2500)
    student_id = models.IntegerField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
