from django.contrib import admin

from data.models import Dataset

class DatasetAdmin(admin.ModelAdmin):
    model = Dataset

admin.site.register(Dataset, DatasetAdmin)
