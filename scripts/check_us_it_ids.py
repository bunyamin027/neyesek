import json

with open("assets/data/foods/american.json", "r") as f:
    d = json.load(f)
    print("American food IDs:")
    for food in d["foods"]:
        print(f"  {food['id']}: {food['name']['tr']} -> {food.get('image')}")

with open("assets/data/foods/italian.json", "r") as f:
    d = json.load(f)
    print("\nItalian food IDs:")
    for food in d["foods"]:
        print(f"  {food['id']}: {food['name']['tr']} -> {food.get('image')}")
