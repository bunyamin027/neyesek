import json

def verify_and_fix():
    path = "assets/data/foods/turkish.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    dishes = data["foods"]
    print(f"Total Turkish dishes: {len(dishes)}")

    # Specific requested fixes
    for d in dishes:
        if d["id"] in ("tr_yuvalama", "tr_yuvalama_corbasi"):
            d["name"]["tr"] = "Antep Yuvalaması"
            d["name"]["en"] = "Gaziantep Yuvalama"
            d["name"]["es"] = "Yuvalama de Gaziantep"
            d["name"]["de"] = "Gaziantep Yuvalama"

        # Check ingredients format and ensure all are valid
        ingredients = d.get("ingredients")
        steps = d.get("steps")

        # Standardize ingredients to List of dicts if needed
        if isinstance(ingredients, dict):
            # Convert Map of lists to List of maps
            langs = list(ingredients.keys())
            max_len = max(len(ingredients[l]) for l in langs) if langs else 0
            new_ing = []
            for i in range(max_len):
                item = {}
                for l in langs:
                    if i < len(ingredients[l]):
                        item[l] = ingredients[l][i]
                new_ing.append(item)
            d["ingredients"] = new_ing

        if isinstance(steps, dict):
            # Convert Map of lists to List of maps
            langs = list(steps.keys())
            max_len = max(len(steps[l]) for l in langs) if langs else 0
            new_steps = []
            for i in range(max_len):
                item = {}
                for l in langs:
                    if i < len(steps[l]):
                        item[l] = steps[l][i]
                new_steps.append(item)
            d["steps"] = new_steps

    # Check for empty ingredients or steps
    issues = []
    for i, d in enumerate(dishes):
        name = d.get("name", {}).get("tr", d.get("id"))
        ings = d.get("ingredients", [])
        stps = d.get("steps", [])
        if not ings:
            issues.append(f"{d['id']} ({name}): NO INGREDIENTS")
        if not stps:
            issues.append(f"{d['id']} ({name}): NO STEPS")

    if issues:
        print("Issues found:")
        for iss in issues:
            print(" -", iss)
    else:
        print("ALL 75 dishes have fully populated ingredients and steps!")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    verify_and_fix()
