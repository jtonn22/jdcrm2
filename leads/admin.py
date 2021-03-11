from django.contrib import admin

from .models import User, Lead, Agent, UserProfile, Category, FollowUp


class LeadAdmin(admin.ModelAdmin):
    # fields = (
    #     "first_name",
    #     "last_name",
    # )

    list_display = [
        "first_name",
        "last_name",
        "age",
        "email",
        "organisation",
    ]  # of fields to display in the table
    list_display_links = [
        "first_name"
    ]  # list of fields you can use as links to the lead
    list_editable = ["last_name"]  # list of fields that you can edit in the list view
    list_filter = ["category"]  # list of fields that you want to be able to filter by
    search_fields = ["first_name", "last_name", "email"]  # fields to be able to search


# Register your models here.
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Agent)
admin.site.register(FollowUp)