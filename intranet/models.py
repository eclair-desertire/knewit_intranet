from django.db import models

class Course(models.Model):
    course_name=models.CharField(max_length=200)
    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Video(models.Model):
    name= models.CharField(max_length=500)
    icon=models.ImageField(upload_to='intranet/static/icons/',null=True)
    file= models.FileField(upload_to='intranet/static/videos/', null=True, verbose_name="")
    materials=models.FileField(upload_to='intranet/static/materials',null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

    def get_video_url(self):
        return self.file.url.replace('intranet/','')

    def get_icon_url(self):
        return self.icon.url.replace('intranet/','')

    def get_mat_url(self):
        return self.materials.url.replace('intranet/','')
# Create your models here.
