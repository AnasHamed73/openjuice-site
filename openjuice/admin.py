from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Domain)
admin.site.register(Topic)
admin.site.register(BookResource)

