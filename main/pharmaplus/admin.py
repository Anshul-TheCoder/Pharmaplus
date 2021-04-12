from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(City)
admin.site.register(Stores)
admin.site.register(Medicine)
admin.site.register(Availability)
admin.site.register(FeedBack)

