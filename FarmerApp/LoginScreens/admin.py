from django.contrib import admin
from .models import farmer,scholar
# Register your models here.

class Farmeradmin(admin.ModelAdmin):
    list_display = ('Farmer_name','Contact_num','Email_id','Password')

admin.site.register(farmer)
admin.site.register(scholar)