from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonial/")
    rating = models.IntegerField(max_length = 1)

    def __str__(self):
        return self.testimonial
    
class Feedback(models.Model):
    name = models.CharField(max_length=200)
    feedback = models.TextField()
    picture = models.ImageField(upload_to="feedback/",null=True,blank=True)

    def __str__(self):
        return self.feedback
    
class ContactUsForm(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=50)
    Message = models.CharField(max_length=200)


class UploadResearch(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    Profile = models.ImageField(upload_to="researchProfile/",null=True,blank=True)
    paper = models.ImageField(upload_to="researchpaper/",null=True,blank=True)