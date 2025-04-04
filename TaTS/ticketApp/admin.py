from django.contrib import admin
from .models import Ticket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('status', 'assignee')
    list_display = ('id','title', 'assignee', 'status', 'assignee', 'description', 'updated_at')
    search_fields = ('title', 'status')

admin.site.register(Ticket, TicketAdmin)
