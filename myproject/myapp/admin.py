from django.contrib import admin

from django.contrib import admin
from myapp.models import *

admin.site.register(CustomUser)
admin.site.register(seekerProfileModel)
admin.site.register(recruiterProfileModel)
admin.site.register(JobModel)