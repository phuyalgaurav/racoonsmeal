import random
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


def random_userdata_13_30():
    age = random.randint(13, 30)
    gender = random.choice(["male", "female"])

    if age <= 17:
        height_cm = random.randint(140, 190)
        bmi = random.uniform(16.5, 26.0)
    else:
        height_cm = random.randint(150, 195)
        bmi = (
            random.uniform(20.0, 28.0)
            if gender == "male"
            else random.uniform(19.0, 30.0)
        )

    weight_kg = round(bmi * (height_cm / 100) ** 2, 1)

    activity_level = random.choice(list(activity_multipliers.keys()))
    goal = random.choice(list(goal_calorie_adjustments.keys()))

    return {
        "height_cm": height_cm,
        "weight_kg": weight_kg,
        "age": age,
        "gender": gender,
        "activity_level": activity_level,
        "goal": goal,
    }


def export_users_to_csv(n_users, filename="userdata.csv"):
    fieldnames = [
        "height_cm",
        "weight_kg",
        "age",
        "gender",
        "activity_level",
        "goal",
    ]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(n_users):
            writer.writerow(random_userdata_13_30())


# example usage
export_users_to_csv(50000, "usersdata_13_30.csv")
