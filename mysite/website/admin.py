from django.contrib import admin
from .models import Contact
from  .models import Commet



class contactview(admin.ModelAdmin):
        list_display = [
            'name',
            'email',
            'subject',
            'message'
        ]
        list_filter =('name',)
        search_fields = ('name',)

class commentview(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'message',
    ]
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Contact,contactview)
admin.site.register(Commet,commentview)
# Register your models here.
