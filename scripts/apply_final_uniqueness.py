import json

# Fix American
with open("assets/data/foods/american.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for food in d["foods"]:
    if food["id"] == "us_chili":
        food["image"] = "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80"
    elif food["id"] == "us_biscuits_gravy":
        food["image"] = "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80"
    elif food["id"] == "us_waffle":
        food["image"] = "https://images.unsplash.com/photo-1562376552-0d160a2f238d?auto=format&fit=crop&w=800&q=80"

with open("assets/data/foods/american.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# Fix Italian
with open("assets/data/foods/italian.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for food in d["foods"]:
    if food["id"] == "it_carpaccio":
        food["image"] = "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=800&q=80"

with open("assets/data/foods/italian.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Applied final image uniqueness fixes!")
