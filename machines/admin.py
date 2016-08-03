from django.contrib import admin
from machines.models import Machine, MachineDetail


class MachineAdmin(admin.ModelAdmin):
    model = Machine


class MachineDetailsAdmin(admin.ModelAdmin):
    model = MachineDetail

admin.site.register(Machine, MachineAdmin)
admin.site.register(MachineDetail, MachineDetailsAdmin)
