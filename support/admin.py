from django.contrib import admin

from support.models import Issue, Reason, Solution, Complaint, Fault, FaultReason

class IssueAdmin(admin.ModelAdmin):
    model = Issue


class ReasonAdmin(admin.ModelAdmin):
    model = Reason


class SolutionAdmin(admin.ModelAdmin):
    model = Solution


class ComplaintAdmin(admin.ModelAdmin):
    model = Complaint


admin.site.register(Issue, IssueAdmin)
admin.site.register(Reason, ReasonAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Fault)
admin.site.register(FaultReason)
