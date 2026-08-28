import json

with open("assets/data/foods/italian.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for food in d["foods"]:
    if food["id"] == "it_carpaccio":
        food["image"] = "https://images.unsplash.com/photo-1514933651103-005eec06c04b?auto=format&fit=crop&w=800&q=80"

with open("assets/data/foods/italian.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Updated it_carpaccio image!")
