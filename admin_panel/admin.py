
# Register your models here.
from django.contrib import admin
from .models import FarmBlock, Worker

admin.site.register(FarmBlock)
admin.site.register(Worker)
