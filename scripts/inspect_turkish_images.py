import json

with open("assets/data/foods/turkish.json", "r", encoding="utf-8") as f:
    data = json.load(f)

foods = data["foods"]
print(f"Total Turkish foods: {len(foods)}")
for i, f in enumerate(foods, 1):
    print(f"{i:02d}. id: {f['id']} | name: {f['name']['tr']} | current_img: {f.get('image', '')}")
