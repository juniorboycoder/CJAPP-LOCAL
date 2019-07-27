
from __future__ import unicode_literals

from django.contrib import admin

from .models import carpentry, tailoring, commenting, UserProfile,UserNotes,tailorcommenting
admin.site.register(carpentry)
admin.site.register(tailoring)
admin.site.register(UserProfile)
admin.site.register(UserNotes)
admin.site.register(tailorcommenting)


class commentingAdmin(admin.ModelAdmin):
    list_display =('user','email','approved')
    
admin.site.register(commenting, commentingAdmin)

# Register your models here.
# Register your models here.
