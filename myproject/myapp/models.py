from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    USER=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    usertype=models.CharField(choices=USER,null=True,max_length=100)
    
    def __str__(self):
        return f"{self.username}- {self.first_name}- {self.last_name}"
    

class seekerProfileModel(models.Model):
    
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='seekerProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    
    
class recruiterProfileModel(models.Model):
    
   
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='recruiterProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    

class JobModel(models.Model):
    JOB_TYPE_CHOICES=[
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),
    ]
    user=models.ForeignKey(CustomUser,null=True,blank=True,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200, null=True, blank=True) 
    company_name = models.CharField(max_length=200, null=True, blank=True) 
    location = models.CharField(max_length=200, null=True, blank=True) 
    description = models.TextField(null=True, blank=True) 
    salary = models.PositiveIntegerField(null=True, blank=True)  
    employment_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES, null=True, blank=True) 
    posted_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    application_deadline = models.DateTimeField(null=True, blank=True) 
    
    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
