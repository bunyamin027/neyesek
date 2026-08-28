import json

batch4 = [
    {
        "id": "tr_hamsi_tava",
        "cuisineId": "turkish",
        "emoji": "🐟",
        "image": "foods/tr_hamsi_tava.webp",
        "color": "FF2ED573",
        "prepTime": 20,
        "cookTime": 10,
        "difficulty": "easy",
        "calories": 420,
        "servings": 2,
        "isPremium": False,
        "tags": ["seafood", "karadeniz", "dinner"],
        "name": {
            "tr": "Mısır Unlu Karadeniz Hamsi Tava",
            "en": "Black Sea Crispy Cornmeal Anchovies",
            "es": "Anchoas Crujientes con Harina de Maíz",
            "de": "Schwarzmeer Knusprige Sardellen in Maismehl"
        },
        "description": {
            "tr": "Karadeniz'in gümüş incisi taze hamsilerin sarı mısır ununa bulanıp tavada dairesel dizilerek tek parça halinde çıtır çıtır kızartılması.",
            "en": "Freshly caught glistening Black Sea anchovies dusted in golden coarse cornmeal, arranged in concentric circles in a shallow pan and flipped to crunchy perfection.",
            "es": "Anchoas frescas del Mar Negro rebozadas en harina de maíz y doradas en sartén en círculos concéntricos.",
            "de": "Frische Schwarzmeer-Sardellen in gelbem Maismehl gewendet, kreisförmig in der Pfanne goldbraun und kross gebraten."
        },
        "ingredients": {
            "tr": ["1 kg taze Karadeniz hamsisi (temizlenmiş)", "1 su bardağı sarı mısır unu", "1 çay bardağı sıvı yağ", "Tuz", "Servis için: Kırmızı soğan, roka ve limon"],
            "en": ["1 kg fresh Black Sea anchovies (cleaned)", "1 cup yellow cornmeal", "1/2 cup oil for frying", "Salt", "For serving: Red onion, arugula, lemon"],
            "es": ["1 kg anchoas frescas limpias", "1 taza harina de maíz", "Aceite para freír", "Sal", "Cebolla morada, rúcula y limón"],
            "de": ["1 kg frische Sardellen", "1 Tasse gelbes Maismehl", "Öl zum Braten", "Salz", "Rote Zwiebeln, Rucola und Zitrone"]
        },
        "steps": {
            "tr": [
                "Hamsileri kafalarını ve içlerini temizleyip yıkayın ve iyice süzün.",
                "Tuzlayıp mısır ununa bulayın ve fazla ununu silkeleyin.",
                "Hamsi tavasını hafifçe yağlayıp balıkları kuyrukları içe gelecek şekilde dairesel dizin.",
                "Orta ateşte alt tarafı çıtırlaşana kadar 4-5 dakika pişirin; kapak yardımıyla tek parça halinde çevirip diğer yüzünü de kızartın.",
                "Kırmızı soğan halkaları, taze roka ve limon dilimleriyle sıcak servis yapın."
            ],
            "en": [
                "Clean, decapitate, and gut anchovies; rinse and dry thoroughly.",
                "Season with salt and dredge evenly in cornmeal.",
                "Lightly oil a wide pan and arrange fish snugly in concentric circles with tails towards center.",
                "Fry over medium heat for 4-5 mins until crispy; flip using a lid and crisp the other side.",
                "Serve immediately with red onion slices, crisp arugula, and juicy lemon wedges."
            ],
            "es": [
                "Limpiar las anchoas y secar bien.",
                "Sazonar y rebozar en harina de maíz.",
                "Colocar en círculos en sartén aceitada.",
                "Freír 5 min por lado volteando con una tapa.",
                "Servir caliente con rúcula, cebolla y limón."
            ],
            "de": [
                "Sardellen säubern und abtrocknen.",
                "Salzen und in Maismehl wenden.",
                "Kreisförmig in die gefettete Pfanne schichten.",
                "Von beiden Seiten mit Deckel wenden und 4-5 Min. knusprig braten.",
                "Mit Rucola, Zwiebeln und Zitrone servieren."
            ]
        }
    },
    {
        "id": "tr_van_otlu_borek",
        "cuisineId": "turkish",
        "emoji": "🥟",
        "image": "foods/tr_van_otlu_borek.webp",
        "color": "FFFFA502",
        "prepTime": 25,
        "cookTime": 30,
        "difficulty": "medium",
        "calories": 360,
        "servings": 4,
        "isPremium": False,
        "tags": ["breakfast", "vegetarian"],
        "name": {
            "tr": "Van Usulü Otlu Peynirli Çıtır Börek",
            "en": "Van Herb Cheese Crispy Borek",
            "es": "Börek Crujiente con Queso de Hierbas de Van",
            "de": "Van Knuspriges Kräuterkäse-Börek"
        },
        "description": {
            "tr": "Van yaylalarından toplanan sirmo ve heliz otlarıyla mayalanan meşhur Van otlu peyniri ve tereyağıyla hazırlanan çıtır çıtır tepsi böreği.",
            "en": "Crispy baked pastry packed with authentic Van herb cheese (infused with wild mountain garlic 'sirmo' and wild fennel) and rich butter.",
            "es": "Hojaldre crujiente relleno con el famoso queso de hierbas de Van, aromatizado con ajo silvestre de montaña.",
            "de": "Knuspriges Ofengebäck mit echtem Van-Kräuterkäse, verfeinert mit wildem Berglauch (Sirmo) und Bauernbutter."
        },
        "ingredients": {
            "tr": ["3 adet taze yufka", "350g tescilli Van otlu peyniri", "150g tereyağı (eritilmiş)", "1 çay bardağı süt", "1 adet yumurta sarısı", "Çörek otu"],
            "en": ["3 sheets fresh pastry", "350g authentic Van herb cheese", "150g melted butter", "1/2 cup milk", "1 egg yolk", "Nigella seeds"],
            "es": ["3 hojas de masa fina", "350g queso con hierbas de Van", "150g mantequilla derretida", "1/2 taza leche", "1 yema de huevo", "Semillas de nigella"],
            "de": ["3 Teigblätter", "350g Van-Kräuterkäse", "150g Butter", "1/2 Tasse Milch", "1 Eigelb", "Schwarzkümmel"]
        },
        "steps": {
            "tr": [
                "Eritilmiş tereyağı ve sütü karıştırarak sos hazırlayın.",
                "Tepsiye ilk yufkayı serip sostan sürün.",
                "İkinci yufkayı büzüştürerek serin ve ufalanmış Van otlu peynirini eşit şekilde yayın.",
                "Üçüncü yufkayı üzerine kapatıp kalan sosu sürün ve dilimleyin.",
                "Yumurta sarısı ve çörek otu serpip 190°C fırında üzeri altın rengi olana kadar 30 dakika pişirin."
            ],
            "en": [
                "Whisk melted butter with milk for brushing sauce.",
                "Lay first pastry sheet in baking pan and brush with butter sauce.",
                "Ruffle second sheet into pan and scatter crumbled Van herb cheese evenly.",
                "Top with third sheet, brush with sauce, and slice into squares.",
                "Brush with egg yolk, sprinkle nigella seeds, and bake at 190°C for 30 minutes until golden."
            ],
            "es": [
                "Mezclar mantequilla derretida con leche.",
                "Colocar primera masa y pincelar.",
                "Añadir segunda masa y rellenar con queso de Van.",
                "Cubrir con la última masa, cortar y pintar con yema.",
                "Hornear 30 min a 190°C con semillas de nigella."
            ],
            "de": [
                "Butter und Milch verrühren.",
                "Erstes Blatt einlegen und bestreichen.",
                "Zweites Blatt einlegen und mit Van-Käse bestreuen.",
                "Mit drittem Blatt abschließen, vorschneiden und mit Eigelb bestreichen.",
                "Bei 190°C 30 Min. goldbraun backen."
            ]
        }
    },
    {
        "id": "tr_kumru",
        "cuisineId": "turkish",
        "emoji": "🥪",
        "image": "foods/tr_kumru.webp",
        "color": "FFFFA502",
        "prepTime": 10,
        "cookTime": 10,
        "difficulty": "easy",
        "calories": 520,
        "servings": 1,
        "isPremium": False,
        "tags": ["street_food", "meat"],
        "name": {
            "tr": "İzmir Çeşme Kumrusu",
            "en": "Izmir Cesme Kumru Sandwich",
            "es": "Sándwich Kumru de Çeşme",
            "de": "Izmir Cesme Kumru Sandwich"
        },
        "description": {
            "tr": "İzmir Çeşme'nin simge sandviçi; nohut mayalı çıtır susamlı kumru ekmeğinde kömürde kızaran kasap sucuğu, salam, sosis, eritilmiş kaşar ve kornişon turşu.",
            "en": "Izmir Cesme's iconic charcoal-toasted sandwich served on chickpea-fermented sesame bread with grilled Turkish sucuk, sausages, melted kasar cheese, and pickles.",
            "es": "Sándwich callejero emblemático de Çeşme con pan de sésamo fermentado, sucuk a la brasa, salchichas, queso fundido y pepinillos.",
            "de": "Kult-Sandwich aus Çeşme: Im Sesambrötchen gegrillte Knoblauchwurst (Sucuk), Würstchen, geschmolzener Kasar-Käse und saure Gurken."
        },
        "ingredients": {
            "tr": ["1 adet susamlı kumru ekmeği", "100g kasap sucuk", "4 dilim salam", "2 adet sosis", "3 dilim taze kaşar peyniri", "2 adet domates dilimi", "Kornişon turşu ve tereyağı"],
            "en": ["1 sesame kumru bread bun", "100g Turkish beef sucuk", "4 slices beef salami", "2 small sausages", "3 slices kasar cheese", "Tomato slices", "Pickles and butter"],
            "es": ["1 pan kumru con sésamo", "100g sucuk turco", "Salami y salchichas", "3 lonchas queso kasar", "Tomate, pepinillos y mantequilla"],
            "de": ["1 Kumru-Sesambrot", "100g Rinder-Sucuk", "Salami und Würstchen", "3 Scheiben Kasar-Käse", "Tomaten, Essiggurken und Butter"]
        },
        "steps": {
            "tr": [
                "Kumru ekmeğini ortadan ikiye kesip tereyağı sürerek ızgarada ısıtın.",
                "Sucuk, salam ve sosisleri ızgarada veya tavada çıtırdayana kadar pişirin.",
                "Etlerin üzerine kaşar peynirini koyup erimesini sağlayın.",
                "Sıcak ekmeğin içine etleri, erimiş kaşarı, domates ve turşu dilimlerini yerleştirip sıcak servis yapın."
            ],
            "en": [
                "Split kumru bun, butter lightly, and toast on hot griddle.",
                "Sear sliced sucuk, salami, and sausages until browned and sizzling.",
                "Melt sliced cheese directly over the sizzling meats.",
                "Stuff hot bun with meats, gooey cheese, fresh tomatoes, and crisp pickles."
            ],
            "es": [
                "Tostar el pan con mantequilla.",
                "Dorar el sucuk, salami y salchichas.",
                "Fundir el queso encima.",
                "Rellenar el pan con las carnes, tomate y pepinillos."
            ],
            "de": [
                "Brötchen halbieren und anrösten.",
                "Sucuk, Salami und Würstchen anbraten.",
                "Käse darauf schmelzen lassen.",
                "Mit Tomaten und Gurken ins Brötchen füllen."
            ]
        }
    },
    {
        "id": "tr_firinda_sutlac",
        "cuisineId": "turkish",
        "emoji": "🍮",
        "image": "foods/tr_sutlac.webp",
        "color": "FFFFA502",
        "prepTime": 15,
        "cookTime": 40,
        "difficulty": "easy",
        "calories": 310,
        "servings": 6,
        "isPremium": False,
        "tags": ["dessert", "vegetarian"],
        "name": {
            "tr": "Geleneksel Fırın Sütlaç",
            "en": "Traditional Baked Rice Pudding (Fırın Sütlaç)",
            "es": "Arroz con Leche Horneado Tradicional",
            "de": "Traditioneller Ofen-Milchreis (Fırın Sütlaç)"
        },
        "description": {
            "tr": "Toprak güveç kaplarında pişirilip fırının üst ızgarasında üzeri nar gibi karamelize edilen, bol sütlü ve fındıklı geleneksel Türk sütlacı.",
            "en": "Creamy rich rice pudding baked in individual earthenware cups under high oven broiler until deeply caramelized on top, served chilled with roasted hazelnuts.",
            "es": "Cremoso arroz con leche horneado en cazuelas de barro con superficie caramelizada, servido frío con avellanas tostadas.",
            "de": "In Tonschalen gebackener cremiger Milchreis mit feiner karamellisierter Kruste, serviert mit gerösteten Haselnüssen."
        },
        "ingredients": {
            "tr": ["1 litre tam yağlı taze süt", "1/2 su bardağı pirinç", "1 su bardağı toz şeker", "2 yemek kaşığı buğday nişastası", "1 paket vanilya", "1 adet yumurta sarısı", "Kavrulmuş fındık tozu"],
            "en": ["1L whole milk", "1/2 cup short-grain rice", "1 cup sugar", "2 tbsp wheat starch", "1 tsp vanilla", "1 egg yolk", "Roasted crushed hazelnuts"],
            "es": ["1L leche entera", "1/2 taza arroz", "1 taza azúcar", "2 cdas almidón", "Vainilla", "1 yema de huevo", "Avellanas tostadas"],
            "de": ["1L Vollmilch", "1/2 Tasse Rundkornreis", "1 Tasse Zucker", "2 EL Stärke", "Vanille", "1 Eigelb", "Geröstete Haselnüsse"]
        },
        "steps": {
            "tr": [
                "Pirinci yumuşayana kadar 2 su bardağı suda haşlayın.",
                "Sütü ve şekeri ekleyip kaynamaya bırakın.",
                "Nişastayı, yumurta sarısını ve vanilyayı az sütle açıp tencereye azar azar ekleyerek 10 dakika koyulaşana kadar karıştırın.",
                "Güveç kaplarına paylaştırıp fırın tepsisine dizin; tepsiye yarısına kadar soğuk su koyun.",
                "220°C fırının üst ızgarasında üzeri kahverengi benekler olana kadar 15 dakika fırınlayın; soğutup fındıkla servis yapın."
            ],
            "en": [
                "Boil rice in 2 cups of water until soft.",
                "Add milk and sugar; bring to a gentle simmer.",
                "Dissolve starch, yolk, and vanilla in milk; stir into pot until velvety and thickened.",
                "Ladle into clay bowls placed in a water bath baking tray.",
                "Broil at 220°C for 15 minutes until tops are blistered golden brown; chill and top with hazelnuts."
            ],
            "es": [
                "Cocer el arroz en agua hasta blando.",
                "Añadir leche y azúcar a fuego medio.",
                "Ligar con almidón, yema y vainilla hasta espesar.",
                "Verter en cazuelas de barro en baño maría.",
                "Gratinar a 220°C por 15 min y enfriar."
            ],
            "de": [
                "Reis weichkochen.",
                "Milch und Zucker zufügen.",
                "Stärke mit Eigelb und Vanille anrühren und unterrühren.",
                "In Tonschalen im Wasserbad füllen.",
                "Bei 220°C Oberhitze 15 Min. bräunen; kalt mit Haselnüssen servieren."
            ]
        }
    },
    {
        "id": "tr_kazandibi",
        "cuisineId": "turkish",
        "emoji": "🍮",
        "image": "foods/tr_kazandibi.webp",
        "color": "FFFFA502",
        "prepTime": 15,
        "cookTime": 25,
        "difficulty": "medium",
        "calories": 290,
        "servings": 4,
        "isPremium": False,
        "tags": ["dessert", "vegetarian"],
        "name": {
            "tr": "Geleneksel Karamelize Kazandibi",
            "en": "Caramelized Bottom Milk Pudding (Kazandibi)",
            "es": "Pudín de Leche Caramelizado Kazandibi",
            "de": "Karamellisierter Milchpudding (Kazandibi)"
        },
        "description": {
            "tr": "Osmanlı sarayından günümüze ulaşan; tavukgöğsü veya sübyeli sütün tepsi tabanında pudra şekeriyle yakılarak karamelize edilmesi ve rulo sarılmasıyla yapılan efsane tatlı.",
            "en": "Iconic Ottoman milk pudding deliberately scorched and caramelized on the bottom of copper trays, chilled and rolled into luscious golden-brown rolls.",
            "es": "Pudín tradicional de leche ligeramente caramelizado y quemado a propósito en bandeja, enrollado en porciones individuales.",
            "de": "Osmanischer Milchpudding mit bewusst karamellisiertem, leicht gebräuntem Boden, kühl in zarte Rollen gerollt."
        },
        "ingredients": {
            "tr": ["1 litre süt", "1 su bardağı şeker", "2 yemek kaşığı pirinç unu", "2 yemek kaşığı nişasta", "1 paket vanilya", "Tepsi tabanı için: 2 yemek kaşığı tereyağı ve 3 yemek kaşığı pudra şekeri"],
            "en": ["1L milk", "1 cup sugar", "2 tbsp rice flour", "2 tbsp starch", "1 tsp vanilla", "For pan: 2 tbsp butter and 3 tbsp powdered sugar"],
            "es": ["1L leche", "1 taza azúcar", "2 cdas harina de arroz", "2 cdas almidón", "Vainilla", "Mantequilla y azúcar glas"],
            "de": ["1L Milch", "1 Tasse Zucker", "2 EL Reismehl", "2 EL Stärke", "Vanille", "Butter und Puderzucker"]
        },
        "steps": {
            "tr": [
                "Süt, şeker, pirinç unu ve nişastayı tencerede tel çırpıcıyla koyu muhallebi kıvamına gelene kadar pişirin, vanilya ekleyin.",
                "Fırın tepsisinin tabanını tereyağı ile yağlayıp bol pudra şekeri serpin.",
                "Muhallebiyi tepsiye dökün ve ocak üzerinde tepsiyi çevirerek tabanın karamelize kahverengi olmasını sağlayın.",
                "Oda sıcaklığında ılıtıp buzdolabında en az 4 saat dinlendirin.",
                "Şeritler halinde kesip spatula ile rulo sararak yanık kısmı üstte kalacak şekilde servis yapın."
            ],
            "en": [
                "Cook milk, sugar, rice flour, and starch into a thick velvety pudding; stir in vanilla.",
                "Grease a wide shallow baking dish with butter and coat heavily with powdered sugar.",
                "Pour the pudding into the pan and cook directly over stovetop flames, rotating constantly until bottom is evenly caramelized and brown.",
                "Cool and refrigerate for 4 hours.",
                "Slice into rectangles and spatula-roll with the glossy caramelized crust on top."
            ],
            "es": [
                "Cocer el pudín hasta espesar.",
                "Untar la bandeja con mantequilla y azúcar glas.",
                "Verter la crema y quemar la base sobre fuego girando la bandeja.",
                "Refrigerar 4 horas.",
                "Cortar y enrollar con la base quemada hacia arriba."
            ],
            "de": [
                "Milchpudding cremig kochen.",
                "Blech buttern und mit Puderzucker bestäuben.",
                "Pudding einfüllen und auf der Herdplatte unter Drehen anbräunen.",
                "4 Std. kühlen.",
                "In Streifen schneiden und aufrollen."
            ]
        }
    },
    {
        "id": "tr_tas_kebabi",
        "cuisineId": "turkish",
        "emoji": "🥘",
        "image": "foods/tr_tas_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 20,
        "cookTime": 45,
        "difficulty": "easy",
        "calories": 440,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "dinner"],
        "name": {
            "tr": "Geleneksel Sebzeli Taş Kebabı",
            "en": "Traditional Tas Kebab (Braised Beef Stew)",
            "es": "Tas Kebab Tradicional (Estofado de Ternera)",
            "de": "Traditioneller Tas Kebab (Geschmortes Rindfleisch)"
        },
        "description": {
            "tr": "Dana kuşbaşı etlerinin arpacık soğan, sarımsak, patates ve havuçla domates salçalı zengin sos içinde kısık ateşte lokum kıvamında pişirilmesi.",
            "en": "Classic Turkish homestyle comfort: tender cubed beef braised in aromatic tomato reduction with pearl onions, carrots, and golden potatoes.",
            "es": "Guiso casero clásico turco con tierna ternera en dados estofada con cebollitas francesas, zanahorias y patatas.",
            "de": "Hausgemachter Schmortopf-Klassiker: Zarte Rindfleischwürfel mit Perlzwiebeln, Möhren und Kartoffeln in reichhaltiger Tomatensauce geschmort."
        },
        "ingredients": {
            "tr": ["600g dana kuşbaşı eti", "15 adet arpacık soğan", "2 diş sarımsak", "2 adet patates, küp doğranmış", "1 adet havuç", "1 yemek kaşığı tereyağı", "1.5 yemek kaşığı domates salçası", "Kekik, karabiber ve tuz"],
            "en": ["600g beef stew cubes", "15 pearl onions", "2 cloves garlic", "2 potatoes, cubed", "1 carrot, sliced", "1 tbsp butter", "1.5 tbsp tomato paste", "Thyme, pepper, and salt"],
            "es": ["600g carne de ternera en dados", "15 cebollitas", "2 dientes de ajo", "2 patatas", "1 zanahoria", "Mantequilla y pasta de tomate", "Tomillo y sal"],
            "de": ["600g Rindergulasch", "15 Perlzwiebeln", "2 Knoblauchzehen", "2 Kartoffeln", "1 Möhre", "Butter und Tomatenmark", "Thymian und Salz"]
        },
        "steps": {
            "tr": [
                "Eti tencerede tereyağında suyunu salıp çekene kadar yüksek ateşte mühürleyin.",
                "Arpacık soğanları, sarımsağı ve salçayı ekleyip 2 dakika soteleyin.",
                "Havuçları ve 2 su bardağı sıcak suyu ekleyip kısık ateşte 30 dakika pişirin.",
                "Küp patatesleri ve kekiği ekleyip patatesler yumuşayana kadar 15 dakika daha pişirin.",
                "Tane pirinç pilavı eşliğinde sıcak servis yapın."
            ],
            "en": [
                "Sear beef cubes in butter until browned and moisture evaporates.",
                "Add pearl onions, garlic, and tomato paste; sauté for 2 minutes.",
                "Add carrots and 2 cups boiling water; simmer covered on low for 30 minutes.",
                "Add cubed potatoes and thyme; simmer for another 15 minutes until potatoes are tender.",
                "Serve warm with buttery Turkish rice pilaf."
            ],
            "es": [
                "Dorar la carne en mantequilla.",
                "Añadir cebollitas, ajo y pasta de tomate.",
                "Agregar zanahorias y agua caliente; cocer 30 min.",
                "Añadir patatas y tomillo; cocer 15 min más.",
                "Servir con arroz pilaf."
            ],
            "de": [
                "Rindfleisch in Butter anbraten.",
                "Zwiebeln, Knoblauch und Tomatenmark 2 Min. mitschwitzen.",
                "Möhren und Wasser zugeben, 30 Min. schmoren.",
                "Kartoffeln und Thymian zugeben, 15 Min. fertig garen.",
                "Mit Reis servieren."
            ]
        }
    }
]

def main():
    path = "assets/data/foods/turkish.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    existing_ids = {dish["id"] for dish in data["foods"]}
    added_count = 0
    
    for dish in batch4:
        if dish["id"] not in existing_ids:
            data["foods"].append(dish)
            added_count += 1
            print(f"Added: {dish['id']} - {dish['name']['tr']}")
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"\nTotal Turkish dishes now: {len(data['foods'])} (Added: {added_count})")
    
    # Update cuisines.json
    c_path = "assets/data/cuisines.json"
    with open(c_path, "r", encoding="utf-8") as f:
        c_data = json.load(f)
        
    for c in c_data["cuisines"]:
        if c["id"] == "turkish":
            c["foodCount"] = len(data["foods"])
            
    with open(c_path, "w", encoding="utf-8") as f:
        json.dump(c_data, f, ensure_ascii=False, indent=2)
        
    print(f"Updated cuisines.json with foodCount={len(data['foods'])}")

if __name__ == "__main__":
    main()
