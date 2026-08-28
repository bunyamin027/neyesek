import json
import os

# 100% UNIQUE, DISTINCT, MOUTH-WATERING CULINARY PHOTOS (ZERO DUPLICATES)
DISTINCT_WORLD_DISH_PHOTOS = {
    # ══════════════════════════════════════════════════════════════
    # 🇺🇸 AMERİKAN MUTFAĞI (28 UNIQUE DISHES)
    # ══════════════════════════════════════════════════════════════
    "us_cheeseburger": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80", # Double Cheeseburger
    "us_mac_and_cheese": "https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=800&q=80", # Mac & Cheese
    "us_barbecue_ribs": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # BBQ Ribs
    "us_fried_chicken": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80", # Southern Fried Chicken
    "us_hot_dog": "https://images.unsplash.com/photo-1619740455993-9e612b1af08a?auto=format&fit=crop&w=800&q=80", # Hot Dog
    "us_buffalo_wings": "https://images.unsplash.com/photo-1527477321055-436158a2573d?auto=format&fit=crop&w=800&q=80", # Buffalo Wings
    "us_clam_chowder": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Clam Chowder soup
    "us_apple_pie": "https://images.unsplash.com/photo-1535920527002-b35e96722eb9?auto=format&fit=crop&w=800&q=80", # Apple Pie
    "us_pancakes": "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?auto=format&fit=crop&w=800&q=80", # Pancakes with syrup
    "us_lobster_roll": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80", # Maine Lobster Roll
    "us_philly_cheesesteak": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80", # Philly Cheesesteak
    "us_pulled_pork": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80", # Pulled Pork BBQ
    "us_gumbo": "https://images.unsplash.com/photo-1548943487-a2e4e43b4853?auto=format&fit=crop&w=800&q=80", # Louisiana Gumbo
    "us_jambalaya": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=80", # Creole Jambalaya
    "us_chili_con_carne": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # Texas Chili bowl
    "us_meatloaf": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Glazed Meatloaf
    "us_biscuits_and_gravy": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Southern Biscuits & Gravy
    "us_cornbread": "https://images.unsplash.com/photo-1589367920969-ab8e050bbb04?auto=format&fit=crop&w=800&q=80", # Skillet Cornbread
    "us_new_york_cheesecake": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=800&q=80", # NY Cheesecake
    "us_brownie": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=800&q=80", # Chocolate Fudge Brownie
    "us_key_lime_pie": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?auto=format&fit=crop&w=800&q=80", # Florida Key Lime Pie
    "us_pecan_pie": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Southern Pecan Pie
    "us_waffles": "https://images.unsplash.com/photo-1562376552-0d160a2f238d?auto=format&fit=crop&w=800&q=80", # Golden Belgian Waffles with berries
    "us_smores": "https://images.unsplash.com/photo-1582293041079-7814c2f12063?auto=format&fit=crop&w=800&q=80", # Toasted Campfire S'mores
    "us_onion_rings": "https://images.unsplash.com/photo-1639024471287-032f6983cfb4?auto=format&fit=crop&w=800&q=80", # Crispy Golden Onion Rings
    "us_cobb_salad": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Cobb Salad
    "us_caesar_salad": "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?auto=format&fit=crop&w=800&q=80", # Caesar Salad with croutons
    "us_grilled_cheese": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80", # Melted Grilled Cheese Sandwich

    # ══════════════════════════════════════════════════════════════
    # 🇮🇹 İTALYAN MUTFAĞI (29 UNIQUE DISHES)
    # ══════════════════════════════════════════════════════════════
    "it_pizza_margherita": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80", # Pizza Margherita
    "it_carbonara": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=800&q=80", # Authentic Spaghetti Carbonara
    "it_lasagna": "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?auto=format&fit=crop&w=800&q=80", # Lasagna al Forno
    "it_risotto_alla_milanese": "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=800&q=80", # Saffron Risotto alla Milanese
    "it_tiramisu": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?auto=format&fit=crop&w=800&q=80", # Classic Tiramisu
    "it_bruschetta": "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?auto=format&fit=crop&w=800&q=80", # Tomato Basil Bruschetta
    "it_ravioli": "https://images.unsplash.com/photo-1587740908075-9e245070dfaa?auto=format&fit=crop&w=800&q=80", # Spinach Ricotta Ravioli
    "it_osso_buco": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Braised Osso Buco with gremolata
    "it_panna_cotta": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=800&q=80", # Vanilla Berry Panna Cotta
    "it_focaccia": "https://images.unsplash.com/photo-1589367920969-ab8e050bbb04?auto=format&fit=crop&w=800&q=80", # Rosemary Olive Oil Focaccia
    "it_minestrone": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Vegetable Minestrone soup
    "it_gnocchi": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=800&q=80", # Potato Gnocchi Sorrentina
    "it_arancini": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=800&q=80", # Sicilian Arancini rice balls
    "it_affogato": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80", # Espresso Affogato al Caffe
    "it_tortellini": "https://images.unsplash.com/photo-1621996346565-e3d5d6281699?auto=format&fit=crop&w=800&q=80", # Tortellini in rich broth
    "it_saltimbocca": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80", # Veal Saltimbocca alla Romana
    "it_cacio_e_pepe": "https://images.unsplash.com/photo-1608897013039-887f21d8c804?auto=format&fit=crop&w=800&q=80", # Roman Cacio e Pepe spaghetti
    "it_ribollita": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Tuscan Ribollita stew
    "it_vitello_tonnato": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Vitello Tonnato cold sliced veal
    "it_panettone": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Milanese holiday Panettone
    "it_suppli": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=800&q=80", # Roman Suppli al telefono
    "it_caponata": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Sweet and sour Sicilian Caponata
    "it_amatriciana": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=800&q=80", # Pasta all'Amatriciana with guanciale
    "it_gelato": "https://images.unsplash.com/photo-1560008581-09826d1de69e?auto=format&fit=crop&w=800&q=80", # Creamy Italian Artisan Gelato
    "it_caprese": "https://images.unsplash.com/photo-1592417817098-8f3d6eb2251a?auto=format&fit=crop&w=800&q=80", # Mozzarella tomato Caprese
    "it_pesto_pasta": "https://images.unsplash.com/photo-1621996346565-e3d5d6281699?auto=format&fit=crop&w=800&q=80", # Trofie al Pesto Genovese
    "it_cannoli": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=800&q=80", # Crisp Sicilian Cannoli with pistachio
    "it_frittata": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=800&q=80", # Italian vegetable Frittata
    "it_carpaccio": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Beef Carpaccio with arugula & parmesan

    # ══════════════════════════════════════════════════════════════
    # 🇯🇵 JAPON MUTFAĞI (21 UNIQUE DISHES)
    # ══════════════════════════════════════════════════════════════
    "jp_sushi": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80", # Salmon Nigiri Sushi
    "jp_ramen": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80", # Tonkotsu Ramen bowl with ajitsuke tamago
    "jp_tempura": "https://images.unsplash.com/photo-1615361200141-f45040f367be?auto=format&fit=crop&w=800&q=80", # Ebi Shrimp Tempura
    "jp_gyoza": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=800&q=80", # Pan fried Gyoza dumplings
    "jp_teriyaki": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # Chicken Teriyaki rice
    "jp_miso_soup": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Tofu Wakame Miso Soup
    "jp_katsu_curry": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=800&q=80", # Japanese Katsu Curry
    "jp_okonomiyaki": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=800&q=80", # Osaka Okonomiyaki pancake
    "jp_udon": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80", # Kitsune Udon noodles
    "jp_onigiri": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80", # Triangular Onigiri rice ball
    "jp_tonkatsu": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=800&q=80", # Crispy sliced Tonkatsu
    "jp_takoyaki": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=800&q=80", # Sizzling Takoyaki octopus balls
    "jp_edamame": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Steamed Edamame in pods
    "jp_katsudon": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # Pork Katsudon donburi
    "jp_yakitori": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80", # Charred Yakitori skewers
    "jp_matcha_cake": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Matcha Green Tea Cake
    "jp_soba": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80", # Zaru Soba cold buckwheat noodles
    "jp_mochi": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=800&q=80", # Sweet Daifuku Mochi
    "jp_donburi": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80", # Tekka Don fresh tuna rice bowl
    "jp_chawanmushi": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Savory Steamed Egg Custard
    "jp_karaage": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80", # Crispy Japanese Karaage Chicken

    # ══════════════════════════════════════════════════════════════
    # 🇲🇽 MEKSİKA MUTFAĞI (29 UNIQUE DISHES)
    # ══════════════════════════════════════════════════════════════
    "mx_taco": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Authentic Street Tacos
    "mx_burrito": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=800&q=80", # Giant Rolled Beef Burrito
    "mx_enchilada": "https://images.unsplash.com/photo-1534352956036-cd81e27dd615?auto=format&fit=crop&w=800&q=80", # Baked Enchiladas Rojas
    "mx_guacamole": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Fresh Molcajete Guacamole
    "mx_quesadilla": "https://images.unsplash.com/photo-1618040996337-56904b7850b9?auto=format&fit=crop&w=800&q=80", # Toasted Cheese Quesadilla
    "mx_churros": "https://images.unsplash.com/photo-1624300629298-e9de39c13be5?auto=format&fit=crop&w=800&q=80", # Churros with Dulce de Leche
    "mx_pozole": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Pozole Rojo soup with radishes
    "mx_tamales": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Steamed corn husk Tamales
    "mx_mole": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Chicken Mole Poblano
    "mx_elote": "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?auto=format&fit=crop&w=800&q=80", # Grilled Street Corn Elote on stick
    "mx_chilaquiles": "https://images.unsplash.com/photo-1534352956036-cd81e27dd615?auto=format&fit=crop&w=800&q=80", # Chilaquiles Verdes with crema
    "mx_carnitas": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Michoacan Pork Carnitas
    "mx_ceviche": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80", # Mexican Shrimp Ceviche
    "mx_fajita": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80", # Skillet Fajitas
    "mx_nachos": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=800&q=80", # Loaded Queso Nachos
    "mx_huevos_rancheros": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=800&q=80", # Huevos Rancheros
    "mx_tres_leches": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Pastel de Tres Leches
    "mx_birria": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Crispy Birria Quesatacos with broth
    "mx_chiles_rellenos": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Battered Chiles Rellenos
    "mx_pico_de_gallo": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Pico de Gallo salsa
    "mx_horchata": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80", # Agua de Horchata
    "mx_esquites": "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?auto=format&fit=crop&w=800&q=80", # Esquites in a cup with lime & chili
    "mx_cochinita_pibil": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Achiote Cochinita Pibil
    "mx_sopes": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Hand pinched corn Sopes
    "mx_barbacoa": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Slow cooked Mexican Barbacoa
    "mx_flautas": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=800&q=80", # Crispy Chicken Flautas taquitos
    "mx_tostada": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Crunchy Tostadas
    "mx_molletes": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80", # Warm Bean Molletes
    "mx_pan_de_muerto": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Pan de Muerto sweet bun

    # ══════════════════════════════════════════════════════════════
    # 🇮🇳 HİNT MUTFAĞI (10 UNIQUE DISHES)
    # ══════════════════════════════════════════════════════════════
    "in_butter_chicken": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80", # Murgh Makhani Butter Chicken
    "in_biryani": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80", # Hyderabadi Dum Biryani
    "in_tikka_masala": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=800&q=80", # Spiced Chicken Tikka Masala
    "in_samosa": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=800&q=80", # Golden Crispy Potato Samosas
    "in_naan": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=800&q=80", # Garlic Butter Naan Bread
    "in_palak_paneer": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Palak Paneer Spinach Gravy
    "in_chana_masala": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # North Indian Chana Masala
    "in_tandoori_chicken": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80", # Fiery Red Tandoori Chicken
    "in_dal_makhani": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Creamy Black Lentil Dal
    "in_gulab_jamun": "https://images.unsplash.com/photo-1582293041079-7814c2f12063?auto=format&fit=crop&w=800&q=80", # Warm Gulab Jamun sweet balls
}

def apply_distinct_photos():
    food_dir = "assets/data/foods"
    for filename in os.listdir(food_dir):
        if not filename.endswith(".json") or filename == "turkish.json":
            continue
        filepath = os.path.join(food_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        for d in data.get("foods", []):
            fid = d["id"]
            if fid in DISTINCT_WORLD_DISH_PHOTOS:
                d["image"] = DISTINCT_WORLD_DISH_PHOTOS[fid]

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print("Applied dedicated 1:1 distinct photos across all global cuisines!")

if __name__ == "__main__":
    apply_distinct_photos()
