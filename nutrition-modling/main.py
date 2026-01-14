import csv

activity_multipliers = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very_active": 1.9,
}

goal_calorie_adjustments = {
    "cut": 0.80,
    "maintain": 1.0,
    "gain": 1.15,
}

goal_protein_multipliers = {
    "cut": 2.2,
    "maintain": 1.8,
    "gain": 2.0,
}


def calculate_bmr(height_cm: float, weight_kg: float, age: int, gender: str) -> float:
    if gender.lower() == "male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161


def compute_nutrition_for_user(user: dict) -> dict:
    # Parse + normalize
    height_cm = float(user["height_cm"])
    weight_kg = float(user["weight_kg"])
    age = int(float(user["age"]))
    gender = str(user["gender"]).strip().lower()

    activity_level = str(user["activity_level"]).strip()
    goal = str(user["goal"]).strip()

    if activity_level not in activity_multipliers:
        raise ValueError(f"Unknown activity_level: {activity_level}")
    if goal not in goal_calorie_adjustments or goal not in goal_protein_multipliers:
        raise ValueError(f"Unknown goal: {goal}")
    if gender not in ("male", "female"):
        raise ValueError(f"Unknown gender: {gender}")

    bmr = calculate_bmr(height_cm, weight_kg, age, gender)
    tdee = bmr * activity_multipliers[activity_level]
    calories_needed = tdee * float(goal_calorie_adjustments[goal])

    protein_g = weight_kg * goal_protein_multipliers[goal]
    protein_kcal = protein_g * 4

    fat_min = 50 if gender == "male" else 40

    def fat_carb_correction(fat_factor: float = 0.8):
        fat_g = max(weight_kg * fat_factor, fat_min)
        fat_kcal = fat_g * 9
        carbs_kcal = calories_needed - (protein_kcal + fat_kcal)
        carbs_g = carbs_kcal / 4

        # If carbs too low, reduce fat and retry once more
        if carbs_g < 50 and fat_factor > 0.6:
            return fat_carb_correction(0.6)

        return fat_g, fat_kcal, carbs_g, carbs_kcal, fat_factor

    fat_g, fat_kcal, carbs_g, carbs_kcal, used_fat_factor = fat_carb_correction()

    # Return enriched row (keep inputs + add outputs)
    out = dict(user)
    out.update(
        {
            "bmr": round(bmr, 2),
            "tdee": round(tdee, 2),
            "calories_needed": round(calories_needed, 2),
            "protein_g": round(protein_g, 2),
            "protein_kcal": round(protein_kcal, 2),
            "fat_g": round(fat_g, 2),
            "fat_kcal": round(fat_kcal, 2),
            "carbs_g": round(carbs_g, 2),
            "carbs_kcal": round(carbs_kcal, 2),
            "fat_factor_used": used_fat_factor,
        }
    )
    return out


def enrich_users_csv(input_csv: str, output_csv: str) -> None:
    with open(input_csv, "r", newline="") as f_in:
        reader = csv.DictReader(f_in)
        input_fieldnames = reader.fieldnames or []

        extra_fields = [
            "bmr",
            "tdee",
            "calories_needed",
            "protein_g",
            "protein_kcal",
            "fat_g",
            "fat_kcal",
            "carbs_g",
            "carbs_kcal",
            "fat_factor_used",
        ]
        fieldnames = list(input_fieldnames) + [
            c for c in extra_fields if c not in input_fieldnames
        ]

        with open(output_csv, "w", newline="") as f_out:
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                enriched = compute_nutrition_for_user(row)
                writer.writerow(enriched)


def main():
    enrich_users_csv("usersdata_13_30.csv", "userdata_enriched.csv")


if __name__ == "__main__":
    main()
