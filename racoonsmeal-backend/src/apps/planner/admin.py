from django.contrib import admin
from .models import Meal, Nutrient, MealPlan, BaseNutrient, UserNutrientRequirement


@admin.register(BaseNutrient)
class BaseNutrientAdmin(admin.ModelAdmin):
    list_display = ("name", "unit", "daily_target")
    search_fields = ("name",)


class NutrientInline(admin.TabularInline):
    model = Nutrient
    extra = 1


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("name", "calories", "creator", "is_public", "created_at")
    list_filter = ("is_public", "creator")
    search_fields = ("name", "description")
    inlines = [NutrientInline]


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "meal_type", "meal")
    list_filter = ("date", "meal_type", "user")
    date_hierarchy = "date"


@admin.register(UserNutrientRequirement)
class UserNutrientRequirementAdmin(admin.ModelAdmin):
    list_display = ("user", "base_nutrient", "daily_target", "source")
    list_filter = ("source", "user")
    search_fields = ("user__username", "base_nutrient__name")
