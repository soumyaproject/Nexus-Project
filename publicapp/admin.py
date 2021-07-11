from django.contrib import admin
from publicapp.models import Contractor,Companies,Job
# Register your models here.
class Contractoradmin(admin.ModelAdmin):
    list_display=['id','name','city','zip_code']
admin.site.register(Contractor,Contractoradmin)
class Companiesadmin(admin.ModelAdmin):
    list_display=['id','name','city','zip_code']
admin.site.register(Companies,Companiesadmin)
class Jobadmin(admin.ModelAdmin):
    list_display=['id','title','price','company','contractor','date','time']
admin.site.register(Job,Jobadmin)