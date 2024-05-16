from django.contrib import admin
from app.models import Maintenance
from app.models import Workers
from app.models import finance
from app.models import project
from app.models import type
# Register your models here.

class contractoradmin(admin.ModelAdmin):
    list_display=['contractor','work','timeperiod','expenses']
admin.site.register(Maintenance,contractoradmin)


class workeradmin(admin.ModelAdmin):
    list_display=['worker','category','joiningdate','worklocation']
admin.site.register(Workers,workeradmin)    

class financeadmin(admin.ModelAdmin):
    list_display=['project','budget','totexp','projloc','amtsac']
admin.site.register(finance,financeadmin)    

class projectadmin(admin.ModelAdmin):
    list_display=['name','company','budget','distance','start','end','lanes','servroad']
admin.site.register(project,projectadmin)  

class typeadmin(admin.ModelAdmin):
   list_display=['Roadtype','company','budget','distance','lanes']
admin.site.register(type,typeadmin)