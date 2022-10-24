from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Worker)
admin.site.register(OtherWorker)
admin.site.register(AppService)
admin.site.register(UserSetting)