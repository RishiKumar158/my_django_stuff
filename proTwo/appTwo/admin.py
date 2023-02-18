from django.contrib import admin
from .models import AccessRecord, Topic, User, Webpage

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(User)
admin.site.register(Webpage)