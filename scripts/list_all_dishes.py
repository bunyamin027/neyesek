import json
import os

food_dir = "assets/data/foods"
all_dishes = {}

for filename in sorted(os.listdir(food_dir)):
    if not filename.endswith(".json"):
        continue
    cuisine = filename.replace(".json", "")
    with open(os.path.join(food_dir, filename), "r", encoding="utf-8") as f:
        data = json.load(f)
    foods = data.get("foods", [])
    all_dishes[cuisine] = [(f["id"], f["name"].get("tr", ""), f["name"].get("en", "")) for f in foods]

for cuisine, items in all_dishes.items():
    print(f"\n=== {cuisine.upper()} ({len(items)} dishes) ===")
    for fid, tr_name, en_name in items:
        print(f"  {fid}: {tr_name} | {en_name}")
