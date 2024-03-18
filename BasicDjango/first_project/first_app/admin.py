from django.contrib import admin
from first_app.models import Topic, Webpage, AccessToken

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessToken)
