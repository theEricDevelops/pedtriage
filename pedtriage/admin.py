from django.contrib import admin
from .models import ChildProfile, Symptom


@admin.register(ChildProfile)
class ChildProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "age", "created_at"]
    list_filter = ["age", "created_at"]
    search_fields = ["user__username", "name"]


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category"]
    search_fields = ["name"]
