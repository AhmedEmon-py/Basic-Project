
from django.contrib import admin
from django.urls import path
from myproject.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('homePage/', homePage, name='homePage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('profilePage/', profilePage, name='profilePage'),
    path('addjob/', addjob, name='addjob'),
    path('jobfeed/', jobfeed, name='jobfeed'),
    path('createdJob/', createdJob, name='createdJob'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
