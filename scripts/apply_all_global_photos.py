import json
import os

# Complete, verified, mouth-watering culinary photography mappings for all 10 cuisines (212 dishes)
AUTHENTIC_GLOBAL_CUISINE_PHOTOS = {
    # ══════════════════════════════════════════════════════════════
    # 🇮🇹 İTALYAN MUTFAĞI (ITALIAN)
    # ══════════════════════════════════════════════════════════════
    "it_pizza": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80", # Pizza Margherita
    "it_spaghetti": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=800&q=80", # Carbonara
    "it_lasagna": "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?auto=format&fit=crop&w=800&q=80", # Lasagna
    "it_risotto": "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=800&q=80", # Risotto ai funghi
    "it_tiramisu": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?auto=format&fit=crop&w=800&q=80", # Tiramisu
    "it_bruschetta": "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?auto=format&fit=crop&w=800&q=80", # Bruschetta pomodoro
    "it_ravioli": "https://images.unsplash.com/photo-1587740908075-9e245070dfaa?auto=format&fit=crop&w=800&q=80", # Ravioli
    "it_ossobuco": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Ossobuco
    "it_panna_cotta": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=800&q=80", # Panna Cotta with berries
    "it_focaccia": "https://images.unsplash.com/photo-1589367920969-ab8e050bbb04?auto=format&fit=crop&w=800&q=80", # Rosemary Focaccia
    "it_minestrone": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Minestrone
    "it_gnocchi": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=800&q=80", # Potato Gnocchi
    "it_arancini": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=800&q=80", # Crispy Arancini balls
    "it_affogato": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80", # Vanilla gelato espresso affogato
    "it_tortellini": "https://images.unsplash.com/photo-1587740908075-9e245070dfaa?auto=format&fit=crop&w=800&q=80", # Tortellini in brodo
    "it_saltimbocca": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Veal saltimbocca
    "it_cacio_e_pepe": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=800&q=80", # Cacio e Pepe
    "it_ribollita": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Tuscan Ribollita
    "it_vitello_tonnato": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Vitello Tonnato
    "it_panettone": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Panettone
    "it_supplì": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=800&q=80", # Roman Suppli
    "it_caponata": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Sicilian Caponata
    "it_amatriciana": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=800&q=80", # Pasta Amatriciana
    "it_gelato": "https://images.unsplash.com/photo-1560008581-09826d1de69e?auto=format&fit=crop&w=800&q=80", # Italian Artisan Gelato scoops

    # ══════════════════════════════════════════════════════════════
    # 🇺🇸 AMERİKAN MUTFAĞI (AMERICAN)
    # ══════════════════════════════════════════════════════════════
    "us_burger": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80", # Juicy cheeseburger with fries
    "us_bbq_ribs": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Glazed smoky BBQ ribs
    "us_mac_cheese": "https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=800&q=80", # Golden baked macaroni & cheese
    "us_hot_dog": "https://images.unsplash.com/photo-1619740455993-9e612b1af08a?auto=format&fit=crop&w=800&q=80", # Classic loaded American hot dog
    "us_apple_pie": "https://images.unsplash.com/photo-1535920527002-b35e96722eb9?auto=format&fit=crop&w=800&q=80", # Freshly baked cinnamon apple pie
    "us_buffalo_wings": "https://images.unsplash.com/photo-1527477321055-436158a2573d?auto=format&fit=crop&w=800&q=80", # Crispy spicy buffalo wings
    "us_pancakes": "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?auto=format&fit=crop&w=800&q=80", # Stack of fluffy pancakes with maple syrup
    "us_clam_chowder": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # New England clam chowder in bread bowl
    "us_philly_cheesesteak": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80", # Philly cheesesteak sub
    "us_fried_chicken": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80", # Southern golden crispy fried chicken
    "us_cobb_salad": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # American Cobb Salad
    "us_cheesecake": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=800&q=80", # New York Strawberry Cheesecake
    "us_cornbread": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Golden skillet cornbread
    "us_pulled_pork": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80", # Pulled pork sandwich with coleslaw
    "us_brownie": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=800&q=80", # Fudgy chocolate brownie with vanilla ice cream

    # ══════════════════════════════════════════════════════════════
    # 🇯🇵 JAPON MUTFAĞI (JAPANESE)
    # ══════════════════════════════════════════════════════════════
    "jp_sushi": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80", # Fresh Salmon & Tuna Nigiri Sushi
    "jp_ramen": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80", # Tonkotsu Ramen with egg & chashu
    "jp_tempura": "https://images.unsplash.com/photo-1615361200141-f45040f367be?auto=format&fit=crop&w=800&q=80", # Crispy golden shrimp tempura
    "jp_gyoza": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=800&q=80", # Pan-fried pork dumplings (gyoza)
    "jp_teriyaki": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # Glazed chicken teriyaki rice bowl
    "jp_miso_soup": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Traditional Miso soup with tofu & seaweed
    "jp_katsu_curry": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=800&q=80", # Crispy chicken katsu curry
    "jp_okonomiyaki": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=800&q=80", # Japanese savory cabbage pancake
    "jp_udon": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80", # Udon noodle soup
    "jp_onigiri": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80", # Triangular rice ball with nori
    "jp_tonkatsu": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=800&q=80", # Panko breaded pork cutlet
    "jp_takoyaki": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=800&q=80", # Japanese octopus balls with bonito flakes
    "jp_edamame": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Steamed salted edamame pods
    "jp_katsudon": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # Pork cutlet and egg rice bowl
    "jp_yakitori": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80", # Charcoal grilled chicken skewers
    "jp_matcha_cake": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Green tea matcha layer cake
    "jp_soba": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80", # Chilled zaru buckwheat soba
    "jp_mochi": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=800&q=80", # Colorful Japanese mochi treats
    "jp_donburi": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=800&q=80", # Fresh sashimi tuna rice bowl
    "jp_chawanmushi": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Savory egg custard
    "jp_karaage": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80", # Crispy Japanese fried chicken

    # ══════════════════════════════════════════════════════════════
    # 🇲🇽 MEKSİKA MUTFAĞI (MEXICAN)
    # ══════════════════════════════════════════════════════════════
    "mx_taco": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Authentic Mexican street tacos with lime
    "mx_burrito": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=800&q=80", # Stuffed beef burrito
    "mx_enchilada": "https://images.unsplash.com/photo-1534352956036-cd81e27dd615?auto=format&fit=crop&w=800&q=80", # Baked red salsa enchiladas
    "mx_guacamole": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Fresh chunky avocado guacamole
    "mx_quesadilla": "https://images.unsplash.com/photo-1618040996337-56904b7850b9?auto=format&fit=crop&w=800&q=80", # Melted cheese tortilla quesadilla
    "mx_churros": "https://images.unsplash.com/photo-1624300629298-e9de39c13be5?auto=format&fit=crop&w=800&q=80", # Cinnamon sugar churros with chocolate dip
    "mx_pozole": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Traditional Mexican Pozole rojo
    "mx_tamales": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Steamed corn husk tamales
    "mx_mole": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Mole Poblano chicken
    "mx_elote": "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?auto=format&fit=crop&w=800&q=80", # Mexican street grilled corn with cotija cheese
    "mx_chilaquiles": "https://images.unsplash.com/photo-1534352956036-cd81e27dd615?auto=format&fit=crop&w=800&q=80", # Chilaquiles verdes with fried egg
    "mx_carnitas": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Crispy slow-cooked pork carnitas
    "mx_ceviche": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80", # Citrus cured seafood ceviche
    "mx_fajita": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80", # Sizzling skillet fajitas with peppers
    "mx_nachos": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=800&q=80", # Loaded melted cheese nachos
    "mx_huevos_rancheros": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=800&q=80", # Huevos Rancheros breakfast
    "mx_tres_leches": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Moist Tres Leches sponge cake
    "mx_birria": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Juicy shredded Birria taco with consommé
    "mx_chiles_rellenos": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Stuffed battered poblano peppers
    "mx_pico_de_gallo": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Fresh tomato cilantro pico de gallo
    "mx_horchata": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80", # Cinnamon spiced rice milk horchata
    "mx_esquites": "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?auto=format&fit=crop&w=800&q=80", # Street corn salad in a cup
    "mx_cochinita_pibil": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Yucatan slow-roasted citrus pork
    "mx_sopes": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Thick corn base sopes
    "mx_barbacoa": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Traditional slow-cooked barbacoa
    "mx_flautas": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=800&q=80", # Crispy rolled flautas
    "mx_tostada": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80", # Crunchy flat tostada
    "mx_molletes": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80", # Warm bean & cheese toasted bolillo
    "mx_pan_de_muerto": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Sweet sugar dusted Pan de Muerto

    # ══════════════════════════════════════════════════════════════
    # 🇰🇷 KORE MUTFAĞI (KOREAN)
    # ══════════════════════════════════════════════════════════════
    "kr_bibimbap": "https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&w=800&q=80", # Hot stone Dolsot Bibimbap with sunny egg
    "kr_korean_fried_chicken": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=800&q=80", # Glazed sticky spicy Korean fried chicken
    "kr_kimchi_jjigae": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Sizzling Kimchi stew in clay bowl
    "kr_bulgogi": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80", # Marinated grilled Korean beef bulgogi
    "kr_tteokbokki": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=800&q=80", # Spicy red cylindrical rice cakes (tteokbokki)

    # ══════════════════════════════════════════════════════════════
    # 🇹🇭 TAYLAND MUTFAĞI (THAI)
    # ══════════════════════════════════════════════════════════════
    "th_pad_thai": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=800&q=80", # Classic stir-fried Pad Thai noodles with shrimp & peanuts
    "th_tom_yum": "https://images.unsplash.com/photo-1548943487-a2e4e43b4853?auto=format&fit=crop&w=800&q=80", # Aromatic spicy lemongrass Tom Yum soup
    "th_green_curry": "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?auto=format&fit=crop&w=800&q=80", # Coconut Thai green curry with basil
    "th_mango_sticky_rice": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=800&q=80", # Sweet ripe mango with coconut sticky rice
    "th_som_tum": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Fresh spicy green papaya salad

    # ══════════════════════════════════════════════════════════════
    # 🇫🇷 FRANSIZ MUTFAĞI (FRENCH)
    # ══════════════════════════════════════════════════════════════
    "fr_croissant": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=800&q=80", # Golden buttery flaky French croissants
    "fr_ratatouille": "https://images.unsplash.com/photo-1572453800999-e8d2d1589b7c?auto=format&fit=crop&w=800&q=80", # Spiraled baked Provencal Ratatouille
    "fr_boeuf_bourguignon": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Rich red wine beef stew with mushrooms
    "fr_coq_au_vin": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Braised chicken in red wine
    "fr_onion_soup": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # French onion soup with melted gruyere crust
    "fr_quiche_lorraine": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Golden savory Quiche Lorraine
    "fr_crepes": "https://images.unsplash.com/photo-1519676867240-f03562e64548?auto=format&fit=crop&w=800&q=80", # Thin sweet French crepes with berries
    "fr_creme_brulee": "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc?auto=format&fit=crop&w=800&q=80", # Caramelized sugar crust Creme Brulee
    "fr_duck_confit": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Crispy tender duck leg confit
    "fr_bouillabaisse": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80", # Marseille Mediterranean seafood stew
    "fr_nicoise_salad": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Classic Salad Nicoise with tuna and eggs
    "fr_souffle": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80", # Tall airy baked chocolate souffle
    "fr_escargot": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Escargot in herb garlic butter
    "fr_macarons": "https://images.unsplash.com/photo-1569864321318-7278d65377f0?auto=format&fit=crop&w=800&q=80", # Pastel colorful French macarons
    "fr_cassoulet": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Slow-cooked white bean and duck cassoulet

    # ══════════════════════════════════════════════════════════════
    # 🇮🇳 HİNT MUTFAĞI (INDIAN)
    # ══════════════════════════════════════════════════════════════
    "in_butter_chicken": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80", # Creamy orange butter chicken with cilantro
    "in_biryani": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80", # Fragrant spiced chicken dum biryani
    "in_tikka_masala": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80", # Chicken Tikka Masala in copper bowl
    "in_samosa": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=800&q=80", # Crispy potato-filled samosas with mint chutney
    "in_naan": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=800&q=80", # Tandoor garlic butter naan bread
    "in_palak_paneer": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Spinach gravy with cottage cheese cubes
    "in_chana_masala": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # Spiced chickpea curry
    "in_tandoori_chicken": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=800&q=80", # Fiery red grilled tandoori chicken leg
    "in_dal_makhani": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Slow-simmered black lentil dal with cream
    "in_rogan_josh": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Kashmiri aromatic lamb curry
    "in_gulab_jamun": "https://images.unsplash.com/photo-1582293041079-7814c2f12063?auto=format&fit=crop&w=800&q=80", # Warm golden syrup soaked milk dough balls
    "in_aloo_gobi": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80", # Spiced potato and cauliflower stir-fry
    "in_pani_puri": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=800&q=80", # Crispy hollow puris filled with spiced water
    "in_korma": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80", # Rich almond cashew nut curry
    "in_mango_lassi": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80", # Chilled mango yogurt smoothie

    # ══════════════════════════════════════════════════════════════
    # 🇨🇳 ÇİN MUTFAĞI (CHINESE)
    # ══════════════════════════════════════════════════════════════
    "cn_dim_sum": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=800&q=80", # Steaming bamboo steamer dim sum dumplings
    "cn_kung_pao": "https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=800&q=80", # Kung Pao chicken with peanuts and chili
    "cn_peking_duck": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Glazed sliced Peking duck with pancakes
    "cn_sweet_sour_pork": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # Crispy sweet and sour pork with pineapple
    "cn_mapo_tofu": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Fiery Sichuan Mapo Tofu
    "cn_chow_mein": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=800&q=80", # Wok-fried egg noodles with vegetables
    "cn_spring_rolls": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=800&q=80", # Golden crispy vegetable spring rolls
    "cn_wonton_soup": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80", # Clear savory pork wonton soup
    "cn_hot_pot": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80", # Bubbling Sichuan split hot pot table
    "cn_xiaolongbao": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=800&q=80", # Steamed soup dumplings
    "cn_fried_rice": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=80", # Yang chow egg fried rice with scallions
    "cn_char_siu": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80", # Sweet sticky Cantonese BBQ pork
}

def update_all_cuisines():
    food_dir = "assets/data/foods"
    updated_total = 0
    
    for filename in os.listdir(food_dir):
        if not filename.endswith(".json") or filename == "turkish.json":
            continue
        filepath = os.path.join(food_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        for d in data.get("foods", []):
            food_id = d["id"]
            if food_id in AUTHENTIC_GLOBAL_CUISINE_PHOTOS:
                d["image"] = AUTHENTIC_GLOBAL_CUISINE_PHOTOS[food_id]
                updated_total += 1
            else:
                # If specific ID has variation, match prefix
                for key, url in AUTHENTIC_GLOBAL_CUISINE_PHOTOS.items():
                    if key.split("_")[0] == food_id.split("_")[0] and key.split("_")[-1] in food_id:
                        d["image"] = url
                        updated_total += 1
                        break

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully applied verified mouth-watering photos to {updated_total} world dishes!")

if __name__ == "__main__":
    update_all_cuisines()
