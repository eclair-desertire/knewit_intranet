from django.conf import settings
from django.db import models
from django.utils import timezone

class Video(models.Model):
    name = models.CharField("Название", max_length=100)
    Dis = models.TextField("Описание", max_length=1000)
    file = models.FileField("Видео", upload_to='media/')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name=models.CharField('Название курса',max_length=200)
    price=models.IntegerField('Цена курса')
    videos=models.ForeignKey(Video, on_delete=models.CASCADE)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name
# Create your models here.
