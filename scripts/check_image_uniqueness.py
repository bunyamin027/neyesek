import json
import os

food_dir = "assets/data/foods"
for filename in sorted(os.listdir(food_dir)):
    if not filename.endswith(".json"):
        continue
    filepath = os.path.join(food_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    foods = data.get("foods", [])
    images = [f.get("image", "") for f in foods]
    unique_images = set(images)
    print(f"{filename}: {len(foods)} dishes, {len(unique_images)} unique images")
    if len(foods) != len(unique_images):
        print(f"  ⚠️ Duplicate images found in {filename}!")
        # Find duplicates
        counts = {}
        for img in images:
            counts[img] = counts.get(img, 0) + 1
        for img, count in counts.items():
            if count > 1:
                dup_dishes = [f['name']['tr'] for f in foods if f.get('image') == img]
                print(f"    - Reused ({count}x): {dup_dishes}")
