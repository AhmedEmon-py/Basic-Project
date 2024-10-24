from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from myapp.models import *



def loginPage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(
            
            username=username,
            password=password,   
        )
        if user:
            login(req,user)
            return redirect('homepage')
        
    
    return render(req,"loginPage.html")




def signupPage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        usertype=req.POST.get('usertype')
        
        password=req.POST.get('password')

        user=CustomUser.objects.create_user(
            username=username,
            email=email,
            usertype=usertype,
            
            password=password, 
        )
        return redirect('loginPage')
        
    return render(req,"signupPage.html")




def logoutPage(req):
    
    logout(req)
    
    return redirect("loginPage")


@login_required 

def homePage(req):
    
    return render(req,"homePage.html")



@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")


@login_required
def addjob(request):
    current_user=request.user
    if current_user.usertype == "recruiter":
        if request.method=="POST":
            job=JobModel()
            job.user=current_user
            job.job_title=request.POST.get("job_title")
            job.company_name=request.POST.get("company_name")
            job.location=request.POST.get("location")
            job.description=request.POST.get("description")
            job.salary=request.POST.get("salary")
            job.employment_type=request.POST.get("employment_type")
            job.posted_date=request.POST.get("application_deadline")
            job.save()
            
            
            return redirect("jobfeed")
    
            
           
    return render(request,'addjob.html')


@login_required
def jobfeed(request):
    Job=JobModel.objects.all()
    
    context={
        'Job':Job
    }
    
    
    return render(request,"jobfeed.html",context)
    
            
           
   


@login_required
def createdJob(request):
    current_user=request.user
    
    job=JobModel.objects.filter(user=current_user)
    
    context={
        "Job":job
    }
    return render(request,"createdJob.html",context)
    
            
           
 





