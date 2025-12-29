from django.db import models
from django.contrib.auth.models import User


class ChildProfile(models.Model):
    """
    Profile for a child associated with a parent user.
    Allows linking symptoms to specific children.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="child_profiles"
    )
    name = models.CharField(
        max_length=100, blank=True, help_text="Optional name for the child"
    )
    age = models.PositiveIntegerField(help_text="Age in years")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name or 'Child'} ({self.age} years)"

    class Meta:
        verbose_name = "Child Profile"
        verbose_name_plural = "Child Profiles"


class Symptom(models.Model):
    """
    Predefined symptoms for triage forms.
    Managed via admin for consistency.
    """

    name = models.CharField(
        max_length=200, unique=True, help_text="Symptom description"
    )
    category = models.CharField(
        max_length=100, blank=True, help_text="Optional category (e.g., respiratory)"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Symptoms"
