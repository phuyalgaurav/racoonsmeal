from django.conf import settings
from django.db import models


class Meal(models.Model):
    """
    Represents a specific meal/dish.
    Meals can be created by users and shared publicly.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True, help_text="Ingredients, recipe, or notes."
    )
    calories = models.PositiveIntegerField(
        help_text="Approximate calories per serving."
    )
    preview_image = models.URLField(blank=True, null=True)

    # Ownership and Visibility
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_meals",
        help_text="The user who added this meal. Null if system-provided.",
    )
    is_public = models.BooleanField(
        default=True,
        help_text="If True, this meal can be randomly assigned to other users.",
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BaseNutrient(models.Model):
    """
    Defines a standard nutrient type and its daily need.
    e.g. Vitamin C, 90mg
    """

    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20)  # e.g. "mg", "g", "kcal"
    daily_target = models.FloatField(help_text="Recommended daily intake.")

    def __str__(self):
        return f"{self.name} ({self.unit})"


class Nutrient(models.Model):
    """
    Specific amount of a BaseNutrient in a Meal.
    """

    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="nutrients")
    base_nutrient = models.ForeignKey(
        BaseNutrient, on_delete=models.PROTECT, related_name="meal_measurements"
    )
    amount = models.FloatField(help_text="Amount of this nutrient in the meal.")

    class Meta:
        unique_together = ["meal", "base_nutrient"]

    def __str__(self):
        return f"{self.base_nutrient.name}: {self.amount}{self.base_nutrient.unit}"


class MealPlan(models.Model):
    """
    Assigns a Meal to a User for a specific date/time.
    """

    MEAL_TYPE_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("snack", "Snack"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="meal_plans"
    )
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name="planned_meals"
    )
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPE_CHOICES)

    class Meta:
        unique_together = ["user", "date", "meal_type"]
        ordering = ["date", "meal_type"]

    def __str__(self):
        return f"{self.user} - {self.date} - {self.meal_type}"


class UserNutrientRequirement(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="nutrient_requirements",
    )
    base_nutrient = models.ForeignKey(
        BaseNutrient, on_delete=models.CASCADE, related_name="user_requirements"
    )
    daily_target = models.FloatField(help_text="User-specific daily intake target.")
    source = models.CharField(
        max_length=100,
        help_text="Source of this requirement (e.g. 'user_added', 'generated').",
    )

    class Meta:
        unique_together = ["user", "base_nutrient"]
        verbose_name = "User Nutrient Requirement"
        verbose_name_plural = "User Nutrient Requirements"

    def __str__(self):
        return f"{self.user} - {self.base_nutrient.name}: {self.daily_target}{self.base_nutrient.unit} ({self.source})"
