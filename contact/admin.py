from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'sname', 'email', 'subject', 'created_on')
    search_fields = ('fname', 'sname', 'email', 'subject', 'body')
    list_filter = ('fname', 'sname', 'email')