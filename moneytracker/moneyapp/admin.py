from django.contrib import admin
from moneyapp.models import Statement

class StatementAdmin(admin.ModelAdmin):
    list_display=["name","amount","category"]
    list_per_page = 3
    list_editable=["amount","category"]
    list_filter=["category"]
    search_fields=["name"]

# Register your models here.
admin.site.register(Statement,StatementAdmin)