from django.contrib import admin
from .models import Show_Data, User,QuesModel
# Register your models here.
admin.site.register(User)

admin.site.register(QuesModel)
admin.site.register(Show_Data)