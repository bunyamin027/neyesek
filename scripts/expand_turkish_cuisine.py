import json
import os

# Massive authentic regional dishes for Turkish cuisine across all regions of Turkey
new_turkish_dishes = [
    # ─── GAZİANTEP & GÜNEYDOĞU ───
    {
        "id": "tr_beyran",
        "cuisineId": "turkish",
        "emoji": "🥣",
        "image": "foods/tr_beyran.webp",
        "color": "FFE84545",
        "prepTime": 15,
        "cookTime": 180,
        "difficulty": "medium",
        "calories": 420,
        "servings": 4,
        "isPremium": False,
        "tags": ["soup", "meat", "spicy", "gaziantep"],
        "name": {
            "tr": "Gaziantep Beyran Çorbası",
            "en": "Gaziantep Beyran Soup",
            "es": "Sopa Beyran de Gaziantep",
            "de": "Gaziantep Beyran Suppe"
        },
        "description": {
            "tr": "Gaziantep'in sabah kahvaltılarında bile tüketilen, lif lif kuzu gerdan eti, pirinç, sarımsak ve acı pul biberle bakır sahanda harlı ateşte pişirilen şifa kaynağı çorba.",
            "en": "Gaziantep's legendary breakfast soup made with shredded lamb neck, rice, generous garlic, and spicy red pepper cooked over high flame in copper plates.",
            "es": "Sopa legendaria de Gaziantep elaborada con cuello de cordero deshebrado, arroz, abundante ajo y pimiento rojo picante servida en plato de cobre.",
            "de": "Legendäre Suppe aus Gaziantep mit zartem Lammfleisch, Reis, viel Knoblauch und scharfen Paprikaflocken auf heißem Kupfer geschmort."
        },
        "ingredients": {
            "tr": ["800g kuzu gerdan ve kemikli et", "1 çay bardağı pirinç", "8 diş sarımsak, ezilmiş", "2 yemek kaşığı acı pul biber", "1 yemek kaşığı biber salçası", "2 yemek kaşığı iç yağı veya tereyağı", "Tuz ve et suyu"],
            "en": ["800g lamb neck with bone", "1/2 cup rice", "8 cloves garlic, minced", "2 tbsp spicy red pepper flakes", "1 tbsp red pepper paste", "2 tbsp butter or lamb tallow", "Salt and broth"],
            "es": ["800g cuello de cordero", "1/2 taza de arroz", "8 dientes de ajo picados", "2 cdas hojuelas de pimiento rojo picante", "1 cda pasta de pimiento", "2 cdas mantequilla", "Sal y caldo"],
            "de": ["800g Lammhals mit Knochen", "1/2 Tasse Reis", "8 Knoblauchzehen, gehackt", "2 EL scharfe Paprikaflocken", "1 EL Paprikamark", "2 EL Butter", "Salz und Fleischbrühe"]
        },
        "steps": {
            "tr": [
                "Kuzu gerdan etini bol suyla düdüklü tencerede etler kemikten ayrılana kadar yaklaşık 2 saat haşlayın.",
                "Eti kemiklerinden ayırıp lif lif didikleyin. Et suyunu süzüp kenara alın.",
                "Pirinci ayrı bir tencerede et suyuyla yumuşayana kadar haşlayın.",
                "Bakır sahanın tabanına eritilmiş yağ, biber salçası, ezilmiş sarımsak ve bol pul biber ekleyin.",
                "Üzerine haşlanmış pirinç ve didiklenmiş kuzu etini yerleştirin.",
                "Kaynar et suyundan gezdirip harlı ocak ateşinde 2-3 dakika fokurdatarak sıcak servis yapın."
            ],
            "en": [
                "Boil lamb neck in plenty of water until the meat is extremely tender and falls off the bone (approx 2 hours).",
                "Shred the lamb meat and strain the rich bone broth.",
                "Boil rice in some broth until tender.",
                "In a shallow copper plate, place melted butter, garlic, pepper paste, and generous chili flakes.",
                "Layer boiled rice and shredded lamb on top.",
                "Pour hot boiling broth and simmer over high heat for 2 minutes before serving piping hot."
            ],
            "es": [
                "Hervir el cordero hasta que la carne esté tierna y se desprenda del hueso.",
                "Deshebrar la carne y colar el caldo.",
                "Cocer el arroz en el caldo.",
                "En plato de cobre, calentar mantequilla, ajo, pasta de pimiento y hojuelas picantes.",
                "Agregar arroz y cordero deshebrado.",
                "Verter caldo hirviendo y cocinar a fuego vivo por 2 minutos antes de servir bien caliente."
            ],
            "de": [
                "Lammhals in reichlich Wasser ca. 2 Stunden kochen, bis das Fleisch butterweich zerfällt.",
                "Fleisch zerkleinern und Brühe abseihen.",
                "Reis in der Brühe gar kochen.",
                "In einer flachen Kupferschale Butter, Knoblauch, Paprikamark und Chiliflocken anrösten.",
                "Reis und Lammfleisch darauf anrichten.",
                "Mit kochender Brühe übergießen und auf starker Flamme 2 Minuten aufkochen lassen."
            ]
        }
    },
    {
        "id": "tr_yuvalama",
        "cuisineId": "turkish",
        "emoji": "🍲",
        "image": "foods/tr_yuvalama.webp",
        "color": "FFFF8C00",
        "prepTime": 60,
        "cookTime": 45,
        "difficulty": "hard",
        "calories": 480,
        "servings": 6,
        "isPremium": False,
        "tags": ["soup", "meat", "gaziantep", "dinner"],
        "name": {
            "tr": "Antep Yuvalama Çorbası",
            "en": "Antep Yuvalama Soup",
            "es": "Sopa Yuvalama de Antep",
            "de": "Antep Yuvalama Suppe"
        },
        "description": {
            "tr": "Gaziantep bayram sofralarının baş tacı; nohut büyüklüğünde yuvarlanan pirinçli minik köfteler, kuzu eti, nohut ve süzme yoğurtlu nefis sos.",
            "en": "The crowning jewel of Gaziantep feasts; tiny pea-sized rice & beef dumplings simmered with tender lamb, chickpeas, and a velvety warm yogurt sauce drizzled with mint butter.",
            "es": "Plato festivo de Gaziantep con diminutas albóndigas de arroz y carne cocidas con cordero, garbanzos y cremosa salsa de yogur a la menta.",
            "de": "Festtagssuppe aus Gaziantep mit erbsengroßen Reis-Fleisch-Klößchen, Lammfleisch, Kichererbsen und samtiger Joghurtsauce mit Minzbutter."
        },
        "ingredients": {
            "tr": ["500g kuşbaşı kuzu eti", "1 su bardağı haşlanmış nohut", "1 su bardağı kırık pirinç", "200g az yağlı kıyma", "500g süzme yoğurt", "1 adet yumurta", "1 yemek kaşığı un", "Kuru nane ve tereyağı"],
            "en": ["500g cubed lamb", "1 cup cooked chickpeas", "1 cup broken rice", "200g lean minced beef", "500g strained yogurt", "1 egg", "1 tbsp flour", "Dried mint and butter"],
            "es": ["500g cordero en cubos", "1 taza garbanzos cocidos", "1 taza arroz partido", "200g carne picada", "500g yogur colado", "1 huevo", "1 cda harina", "Menta seca y mantequilla"],
            "de": ["500g Lammgulasch", "1 Tasse gekochte Kichererbsen", "1 Tasse Bruchreis", "200g Rinderhack", "500g stichfester Joghurt", "1 Ei", "1 EL Mehl", "Getrocknete Minze und Butter"]
        },
        "steps": {
            "tr": [
                "Pirinci ıslatıp kurutun ve un haline gelene kadar çekin. Kıyma, tuz ve karabiber ile yoğurup nohut büyüklüğünde minik köfteler yuvarlayın.",
                "Köfteleri buharda 15 dakika pişirin.",
                "Kuşbaşı kuzu etini ve nohutları yumuşayana kadar haşlayın.",
                "Süzme yoğurdu yumurta ve un ile çırparak kısık ateşte ılıtın, kesilmemesi için et suyundan azar azar ekleyin.",
                "Et, nohut ve buharda pişen minik köfteleri yoğurtlu karışıma ilave edip 5 dakika kaynatın.",
                "Üzerine kızgın tereyağında yakılmış kuru nane gezdirip servis yapın."
            ],
            "en": [
                "Grind soaked dried rice finely. Knead with minced meat, salt, and pepper; roll into tiny pea-sized balls.",
                "Steam the dumplings for 15 minutes.",
                "Boil diced lamb and chickpeas until tender.",
                "Whisk strained yogurt with egg and flour over low heat, tempering with hot broth.",
                "Combine meat, chickpeas, dumplings, and yogurt sauce; simmer gently for 5 minutes.",
                "Drizzle sizzling dried mint butter over the top before serving."
            ],
            "es": [
                "Moler el arroz remojado y amasar con carne picada; formar bolitas del tamaño de guisantes.",
                "Cocinar las bolitas al vapor por 15 min.",
                "Hervir el cordero y los garbanzos.",
                "Batir yogur con huevo y harina a fuego suave con caldo caliente.",
                "Combinar todo y cocinar 5 minutos.",
                "Rociar mantequilla fundida con menta seca al servir."
            ],
            "de": [
                "Eingeweichten Reis fein mahlen, mit Hackfleisch verkneten und erbsengroße Bällchen formen.",
                "Klößchen 15 Min. dämpfen.",
                "Lammfleisch und Kichererbsen gar kochen.",
                "Joghurt mit Ei und Mehl verquirlen, mit heißer Brühe angleichen.",
                "Alles zusammenfügen und 5 Minuten köcheln.",
                "Mit zischender Minzbutter beträufeln."
            ]
        }
    },
    {
        "id": "tr_siveydiz",
        "cuisineId": "turkish",
        "emoji": "🧄",
        "image": "foods/tr_siveydiz.webp",
        "color": "FF2ED573",
        "prepTime": 30,
        "cookTime": 45,
        "difficulty": "medium",
        "calories": 410,
        "servings": 4,
        "isPremium": False,
        "tags": ["dinner", "meat", "gaziantep"],
        "name": {
            "tr": "Antep Şiveydiz",
            "en": "Antep Siveydiz",
            "es": "Siveydiz de Antep",
            "de": "Antep Siveydiz"
        },
        "description": {
            "tr": "Gaziantep'te ilkbaharda taze sarımsak ve taze soğanla yapılan, kuzu eti, nohut ve yoğurt soslu nefis bir saray yemeği.",
            "en": "A springtime delicacy from Gaziantep combining sweet fresh young garlic stems, scallions, tender lamb, chickpeas, and velvety yogurt.",
            "es": "Delicadeza primaveral de Gaziantep con tallos de ajo tierno, cebollín, cordero tierno, garbanzos y salsa de yogur.",
            "de": "Frühlingsspezialität aus Gaziantep mit frischem Knoblauchlauch, Frühlingszwiebeln, Lammfleisch, Kichererbsen und samtiger Joghurtsauce."
        },
        "ingredients": {
            "tr": ["500g kuşbaşı kuzu eti", "1 kg taze sarımsak (yeşil saplı)", "500g taze soğan", "1 su bardağı haşlanmış nohut", "500g süzme yoğurt", "1 yumurta", "1 yemek kaşığı un", "Tereyağı ve kuru nane"],
            "en": ["500g cubed lamb", "1 kg fresh green garlic stems", "500g scallions", "1 cup cooked chickpeas", "500g strained yogurt", "1 egg", "1 tbsp flour", "Butter and dried mint"],
            "es": ["500g cordero", "1 kg ajo tierno verde", "500g cebollino", "1 taza garbanzos cocidos", "500g yogur colado", "1 huevo", "1 cda harina", "Mantequilla y menta"],
            "de": ["500g Lammfleisch", "1 kg frischer Grünknoblauch", "500g Frühlingszwiebeln", "1 Tasse Kichererbsen", "500g Joghurt", "1 Ei", "1 EL Mehl", "Butter und Minze"]
        },
        "steps": {
            "tr": [
                "Kuzu etini tencerede nohutlarla birlikte yumuşayana kadar haşlayın.",
                "Taze sarımsak ve soğanların beyaz ve açık yeşil kısımlarını parmak boyunda doğrayıp etin içine ekleyin, 10 dakika pişirin.",
                "Ayrı bir kapta süzme yoğurt, yumurta ve unu çırpıp ılıtarak yemeğe ilave edin.",
                "Tereyağında kızdırılmış nane ile süsleyip sıcak servis yapın."
            ],
            "en": [
                "Boil lamb and chickpeas until tender.",
                "Chop fresh green garlic and scallions into finger-length pieces and simmer with the meat for 10 minutes.",
                "Whisk yogurt with egg and flour, temper with warm broth, and stir into the stew.",
                "Top with sizzling mint butter and serve warm."
            ],
            "es": [
                "Hervir el cordero y garbanzos hasta tiernos.",
                "Cortar ajo tierno y cebolletas; cocinar 10 min en el caldo.",
                "Mezclar yogur, huevo y harina; añadir suavemente.",
                "Rociar mantequilla con menta y servir."
            ],
            "de": [
                "Lamm und Kichererbsen weichkochen.",
                "Grünknoblauch und Frühlingszwiebeln stifteln, 10 Min. mitkochen.",
                "Joghurt mit Ei und Mehl anrühren und unterrühren.",
                "Mit Minzbutter vollenden."
            ]
        }
    },
    {
        "id": "tr_kusleme",
        "cuisineId": "turkish",
        "emoji": "🥩",
        "image": "foods/tr_kusleme.webp",
        "color": "FFFF4757",
        "prepTime": 15,
        "cookTime": 10,
        "difficulty": "easy",
        "calories": 380,
        "servings": 2,
        "isPremium": False,
        "tags": ["meat", "grilled", "gaziantep"],
        "name": {
            "tr": "Antep Küşleme Kebabı",
            "en": "Gaziantep Kusleme Kebab",
            "es": "Kebab Küşleme de Gaziantep",
            "de": "Gaziantep Küşleme Kebab"
        },
        "description": {
            "tr": "Kuzunun omurgasının iki yanında bulunan en yumuşak, yağsız ve sinirsiz etin közde marine edilerek lokum gibi pişirilmesi.",
            "en": "The most tender, sinew-free cut from lamb tenderloin, lightly seasoned with sea salt and grilled over charcoal to butter-like perfection.",
            "es": "El corte más tierno y sin nervios del lomo de cordero, asado a las brasas como un bocado de mantequilla.",
            "de": "Das zarteste, sehnenfreie Filetstück vom Lamm, sanft über Holzkohle zartrosa gegrillt."
        },
        "ingredients": {
            "tr": ["500g kuzu küşleme eti", "2 yemek kaşığı zeytinyağı", "1 çay kaşığı kekik", "1 çay kaşığı pul biber", "Deniz tuzu", "Lavaş ve közlenmiş biber"],
            "en": ["500g lamb tenderloin (küşleme)", "2 tbsp olive oil", "1 tsp oregano", "1 tsp red pepper flakes", "Sea salt", "Lavash bread and grilled peppers"],
            "es": ["500g solomillo de cordero", "2 cdas aceite de oliva", "1 cdta orégano", "1 cdta pimiento rojo", "Sal marina", "Pan lavash"],
            "de": ["500g Lammfilet (Küşleme)", "2 EL Olivenöl", "1 TL Oregano", "1 TL Chiliflocken", "Meersalz", "Fladenbrot"]
        },
        "steps": {
            "tr": [
                "Küşleme etini lokum büyüklüğünde dilimleyin.",
                "Zeytinyağı, kekik ve az pul biberle 30 dakika marine edin.",
                "Şişlere dizip köz ateşte veya döküm ızgarada her iki tarafını 3-4 dakika sulu kalacak şekilde pişirin.",
                "Tuz serpip sıcak lavaş ve köz sebzelerle servis edin."
            ],
            "en": [
                "Slice the tenderloin into thick medallions.",
                "Marinate with olive oil, oregano, and pepper for 30 minutes.",
                "Thread onto flat skewers and grill over hot coals for 3-4 minutes per side keeping it juicy.",
                "Sprinkle sea salt and serve immediately on warm lavash."
            ],
            "es": [
                "Cortar la carne en medallones.",
                "Marinar 30 min con aceite de oliva y especias.",
                "Asar en brochetas a fuego vivo 3-4 minutos por lado.",
                "Sazonar con sal marina y servir con pan lavash caliente."
            ],
            "de": [
                "Das Fleisch in dicke Medaillons schneiden.",
                "Mit Olivenöl und Gewürzen 30 Minuten marinieren.",
                "Auf Spießen über Holzkohle 3-4 Minuten saftig grillen.",
                "Mit Meersalz bestreuen und heiß servieren."
            ]
        }
    },
    {
        "id": "tr_nohut_durumu",
        "cuisineId": "turkish",
        "emoji": "🌯",
        "image": "foods/tr_nohut_durumu.webp",
        "color": "FFFFA502",
        "prepTime": 10,
        "cookTime": 90,
        "difficulty": "easy",
        "calories": 420,
        "servings": 4,
        "isPremium": False,
        "tags": ["street_food", "vegetarian", "gaziantep"],
        "name": {
            "tr": "Gaziantep Nohut Dürümü",
            "en": "Gaziantep Chickpea Wrap",
            "es": "Wrap de Garbanzos de Gaziantep",
            "de": "Gaziantep Kichererbsen-Wrap"
        },
        "description": {
            "tr": "Kemik suyunda pamuk gibi pişirilen nohutların tırnak pideye sarılıp kimyon, pul biber, sumaklı soğan ve taze maydanozla sunulan eşsiz Antep sokak lezzeti.",
            "en": "Melt-in-mouth chickpeas slow-cooked in rich bone broth, wrapped in fresh tırnak pide with cumin, sumac onions, fresh parsley, and chili.",
            "es": "Garbanzos tiernos cocidos en caldo de huesos, envueltos en pan plano con comino, cebolla al zumaque y perejil fresco.",
            "de": "Im Knochenfond butterweich gekochte Kichererbsen, im frischen Pide-Fladenbrot mit Kreuzkümmel, Sumach-Zwiebeln und Petersilie gerollt."
        },
        "ingredients": {
            "tr": ["2 su bardağı nohut (geceden ıslatılmış)", "İlikli dana/kuzu kemiği", "Tırnak pide veya lavaş", "2 tatlı kaşığı kimyon", "2 tatlı kaşığı pul biber", "2 adet kırmızı soğan", "1 demet maydanoz", "Limon ve tuz"],
            "en": ["2 cups chickpeas (soaked overnight)", "Marrow beef/lamb bone", "Tırnak flatbread or lavash", "2 tsp cumin", "2 tsp chili flakes", "2 red onions", "1 bunch parsley", "Lemon and salt"],
            "es": ["2 tazas garbanzos remojados", "Huesos con tuétano", "Pan plano tırnak", "2 cdtas comino", "2 cdtas chile en polvo", "2 cebollas rojas", "1 manojo perejil", "Limón y sal"],
            "de": ["2 Tassen Kichererbsen (eingeweicht)", "Markknochen", "Fladenbrot", "2 TL Kreuzkümmel", "2 TL Chiliflocken", "2 rote Zwiebeln", "1 Bund Petersilie", "Zitrone und Salz"]
        },
        "steps": {
            "tr": [
                "Nohutları ilikli kemiklerle düdüklü tencerede pamuk gibi yumuşayana kadar haşlayın.",
                "Tırnak pidenin ortasına sıcak haşlanmış nohutları bolca yayın ve hafifçe ezin.",
                "Üzerine bol kimyon, pul biber ve tuz serpin.",
                "Piyazlık doğranmış sumaklı soğan ve maydanozu ekleyip üzerine taze limon sıkın.",
                "Sıkıca dürüm yapıp sıcak sıcak servis edin."
            ],
            "en": [
                "Pressure-cook chickpeas with marrow bones until buttery soft.",
                "Spoon hot chickpeas generously onto warm flatbread and lightly mash.",
                "Dust heavily with ground cumin, chili flakes, and salt.",
                "Top with sumac-tossed sliced onions, parsley, and fresh lemon juice.",
                "Roll tightly into a wrap and serve hot."
            ],
            "es": [
                "Cocer los garbanzos con huesos hasta que estén tiernos.",
                "Colocar en pan caliente y machacar ligeramente.",
                "Espolvorear comino, chile y sal.",
                "Añadir cebolla al zumaque, perejil y jugo de limón.",
                "Enrollar y servir caliente."
            ],
            "de": [
                "Kichererbsen mit Markknochen butterweich kochen.",
                "Heiß auf das Fladenbrot geben und leicht andrücken.",
                "Reichlich mit Kreuzkümmel, Chili und Salz würzen.",
                "Mit Sumach-Zwiebeln, Petersilie und Zitronensaft belegen.",
                "Fest rollen und heiß genießen."
            ]
        }
    },
    {
        "id": "tr_alinazik",
        "cuisineId": "turkish",
        "emoji": "🍆",
        "image": "foods/tr_alinazik.webp",
        "color": "FFE84545",
        "prepTime": 25,
        "cookTime": 25,
        "difficulty": "medium",
        "calories": 520,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "gaziantep", "dinner"],
        "name": {
            "tr": "Gaziantep Ali Nazik Kebabı",
            "en": "Gaziantep Ali Nazik Kebab",
            "es": "Kebab Ali Nazik de Gaziantep",
            "de": "Gaziantep Ali Nazik Kebab"
        },
        "description": {
            "tr": "Közlenmiş patlıcanların sarımsaklı süzme yoğurtla harmanlandığı yatak üzerine tereyağında kavrulmuş baharatlı zırh kıyması veya kuzu kuşbaşı eti.",
            "en": "Smoky char-grilled eggplants whipped with garlicky strained yogurt, crowned with sizzling butter-sautéed spiced minced lamb or beef.",
            "es": "Berenjenas asadas al carbón mezcladas con yogur colado al ajo, cubiertas con jugosa carne picada de cordero a la mantequilla.",
            "de": "Rauchige Auberginencreme mit Knoblauchjoghurt, belegt mit saftigem, in Butter angebratenem gewürztem Lammhack."
        },
        "ingredients": {
            "tr": ["4 adet patlıcan (közlenmiş)", "1.5 su bardağı süzme yoğurt", "3 diş sarımsak, ezilmiş", "400g kuzu kıyma veya küçük kuşbaşı et", "2 yemek kaşığı tereyağı", "1 yemek kaşığı biber salçası", "Kırmızı toz biber, pul biber ve tuz"],
            "en": ["4 large eggplants (charred)", "1.5 cups strained yogurt", "3 cloves garlic, minced", "400g minced lamb or diced beef", "2 tbsp butter", "1 tbsp pepper paste", "Paprika, chili flakes, and salt"],
            "es": ["4 berenjenas asadas", "1.5 tazas yogur colado", "3 dientes de ajo", "400g carne de cordero", "2 cdas mantequilla", "1 cda pasta de pimiento", "Pimentón y sal"],
            "de": ["4 Auberginen (gegrillt)", "1.5 Tassen stichfester Joghurt", "3 Knoblauchzehen", "400g Lammhack oder Gulasch", "2 EL Butter", "1 EL Paprikamark", "Paprika, Chili und Salz"]
        },
        "steps": {
            "tr": [
                "Patlıcanları ocakta veya fırında közleyip kabuklarını soyun ve incecik kıyın.",
                "Köz patlıcanları ezilmiş sarımsak ve süzme yoğurtla karıştırıp hafifçe ılıtın.",
                "Tavada tereyağında kıymayı/eti salça, toz biber ve tuz ile suyunu çekene kadar kavurun.",
                "Servis tabağına yoğurtlu patlıcan yatağını yayın.",
                "Üzerine sıcak tereyağlı eti ve köpüren tereyağını döküp sıcak servis yapın."
            ],
            "en": [
                "Char eggplants over open flame, peel, and finely mash.",
                "Mix smoked eggplant with garlic, strained yogurt, and warm gently.",
                "Sauté minced lamb in butter with pepper paste and spices until juicy and browned.",
                "Spread the creamy eggplant-yogurt base across the serving dish.",
                "Top with the sizzling meat and melted spiced butter."
            ],
            "es": [
                "Asar las berenjenas, pelar y picar fino.",
                "Mezclar con ajo y yogur colado.",
                "Saltear la carne con mantequilla, pasta de pimiento y especias.",
                "Extender la crema de berenjena en el plato.",
                "Coronar con la carne caliente y mantequilla fundida."
            ],
            "de": [
                "Auberginen grillen, schälen und fein hacken.",
                "Mit Knoblauch und Joghurt verrühren und leicht erwärmen.",
                "Fleisch in Butter mit Paprikamark und Gewürzen kräftig anbraten.",
                "Auberginen-Joghurt auf einer Platte anrichten.",
                "Mit heißem Fleisch und zerlassener Butter servieren."
            ]
        }
    },
    {
        "id": "tr_firik_pilavi",
        "cuisineId": "turkish",
        "emoji": "🍚",
        "image": "foods/tr_firik_pilavi.webp",
        "color": "FFA4B0BE",
        "prepTime": 15,
        "cookTime": 30,
        "difficulty": "easy",
        "calories": 360,
        "servings": 4,
        "isPremium": False,
        "tags": ["dinner", "vegetarian", "gaziantep"],
        "name": {
            "tr": "Antep Firik Pilavı",
            "en": "Smoked Green Wheat Firik Pilaf",
            "es": "Pilaf de Trigo Ahumado Firik",
            "de": "Gaziantep Firik-Bulgur-Pilaw"
        },
        "description": {
            "tr": "Güneydoğu'nun tütsü kokulu yeşil başak buğdayı firik ve pilavlık bulgurla tereyağında pişirilen nefis aromalı geleneksel pilav.",
            "en": "Traditional Gaziantep pilaf made with smoky flame-roasted green wheat (freekeh), coarse bulgur, butter, and chickpeas.",
            "es": "Pilaf tradicional de Gaziantep con trigo verde tostado al fuego (freekeh), bulgur grueso, mantequilla y garbanzos.",
            "de": "Traditioneller rauchiger Pilaw aus geröstetem grünem Weizen (Freekeh), grobem Bulgur und Butter."
        },
        "ingredients": {
            "tr": ["1.5 su bardağı firik buğdayı", "1/2 su bardağı iri pilavlık bulgur", "1 su bardağı haşlanmış nohut", "1 adet kuru soğan", "2 yemek kaşığı tereyağı", "1 yemek kaşığı biber salçası", "3 su bardağı et suyu", "Karabiber ve tuz"],
            "en": ["1.5 cups freekeh (firik)", "1/2 cup coarse bulgur", "1 cup cooked chickpeas", "1 onion, diced", "2 tbsp butter", "1 tbsp pepper paste", "3 cups meat broth", "Black pepper and salt"],
            "es": ["1.5 tazas trigo freekeh", "1/2 taza bulgur grueso", "1 taza garbanzos", "1 cebolla picada", "2 cdas mantequilla", "1 cda pasta de pimiento", "3 tazas caldo de carne", "Sal y pimienta"],
            "de": ["1.5 Tassen Firik-Weizen", "1/2 Tasse grober Bulgur", "1 Tasse Kichererbsen", "1 Zwiebel", "2 EL Butter", "1 EL Paprikamark", "3 Tassen Fleischbrühe", "Pfeffer und Salz"]
        },
        "steps": {
            "tr": [
                "Firik buğdayını ve bulguru ayıklayıp yıkayın.",
                "Tencerede tereyağında yemeklik doğranmış soğanı pembeleşene kadar kavurun.",
                "Biber salçasını ekleyip kokusu çıkana kadar 1 dakika çevirin.",
                "Firik ve bulguru ekleyip 2-3 dakika kavurun.",
                "Haşlanmış nohut, tuz, karabiber ve sıcak et suyunu ekleyin.",
                "Kısık ateşte suyunu çekene kadar pişirip 15 dakika demlendirin."
            ],
            "en": [
                "Rinse freekeh and coarse bulgur thoroughly.",
                "Sauté diced onions in butter until golden.",
                "Stir in pepper paste for 1 minute.",
                "Add freekeh and bulgur; toast for 2-3 minutes.",
                "Add cooked chickpeas, seasonings, and boiling broth.",
                "Cover and simmer on low heat until liquid is absorbed; rest for 15 minutes."
            ],
            "es": [
                "Lavar el trigo freekeh y bulgur.",
                "Sofreír la cebolla en mantequilla hasta dorar.",
                "Añadir la pasta de pimiento y cocinar 1 min.",
                "Agregar el trigo y tostar 2 minutos.",
                "Verter los garbanzos, caldo y condimentos.",
                "Cocinar a fuego lento hasta absorber el caldo; reposar 15 min."
            ],
            "de": [
                "Firik und Bulgur waschen.",
                "Zwiebeln in Butter goldgelb anbraten.",
                "Paprikamark unterrühren.",
                "Getreide zufügen und 2 Minuten anschwitzen.",
                "Kichererbsen und heiße Brühe zugeben.",
                "Zugedeckt bei schwacher Hitze garen und 15 Minuten ruhen lassen."
            ]
        }
    },
    {
        "id": "tr_katmer",
        "cuisineId": "turkish",
        "emoji": "🥞",
        "image": "foods/tr_katmer.webp",
        "color": "FF2ED573",
        "prepTime": 20,
        "cookTime": 10,
        "difficulty": "medium",
        "calories": 490,
        "servings": 2,
        "isPremium": False,
        "tags": ["dessert", "breakfast", "gaziantep"],
        "name": {
            "tr": "Gaziantep Çıtır Katmeri",
            "en": "Gaziantep Crispy Pistachio Katmer",
            "es": "Katmer Crujiente de Pistacho de Gaziantep",
            "de": "Gaziantep Knuspriges Pistazien-Katmer"
        },
        "description": {
            "tr": "Zar gibi açılan incecik yufka içerisine bol Antep fıstığı, taze kaymak ve şeker konularak taş fırında çıtır çıtır pişirilen efsane tatlı.",
            "en": "Paper-thin hand-stretched filo dough filled with abundant vibrant emerald Gaziantep pistachios, clotted cream (kaymak), and baked until golden and crispy.",
            "es": "Fina masa filo estirada a mano rellena de pistachos de Gaziantep, nata cuajada (kaymak) y azúcar, horneada hasta quedar crujiente.",
            "de": "Hauchdünner Filoteig, gefüllt mit reichlich echten Gaziantep-Pistazien und cremigem Rahm (Kaymak), im Steinofen knusprig gebacken."
        },
        "ingredients": {
            "tr": ["2 adet hazır baklava yufkası veya elde açılmış zar yufka", "150g taze çekilmiş Antep fıstığı içi", "100g taze kaymak", "3 yemek kaşığı toz şeker", "2 yemek kaşığı eritilmiş tereyağı"],
            "en": ["2 sheets ultra-thin filo/baklava pastry", "150g freshly ground Gaziantep pistachios", "100g clotted cream (kaymak)", "3 tbsp sugar", "2 tbsp melted butter"],
            "es": ["2 hojas de masa filo ultrafina", "150g pistachos de Gaziantep molidos", "100g nata cuajada kaymak", "3 cdas azúcar", "2 cdas mantequilla derretida"],
            "de": ["2 Blatt hauchdünner Baklava-Teig", "150g gemahlene grüne Pistazien", "100g Kaymak (Schmand/Rahm)", "3 EL Zucker", "2 EL geschmolzene Butter"]
        },
        "steps": {
            "tr": [
                "Yufkayı düz tezgaha serip hafifçe tereyağı ile yağlayın.",
                "Orta kısmına bolca toz fıstık, parçalar halinde kaymak ve toz şeker serpiştirin.",
                "Zarf şeklinde dört köşesinden katlayın.",
                "Tavada tereyağında veya 200°C fırında her iki tarafı altın sarısı ve çıtır olana kadar 8-10 dakika pişirin.",
                "Dilimleyip üzerine ekstra fıstık serperek sıcak servis yapın."
            ],
            "en": [
                "Spread thin pastry on work surface and brush lightly with butter.",
                "Scatter generous emerald pistachios, dollops of clotted cream, and sugar in the center.",
                "Fold the four edges inward like an envelope.",
                "Bake in pan or 200°C oven for 8-10 minutes until delightfully crisp and golden.",
                "Cut into squares, sprinkle extra pistachios, and serve warm."
            ],
            "es": [
                "Extender la masa y pincelar con mantequilla.",
                "Distribuir pistachos, kaymak y azúcar en el centro.",
                "Doblar como un sobre.",
                "Hornear a 200°C por 8-10 min hasta dorar.",
                "Cortar en cuadrados y servir caliente con pistacho extra."
            ],
            "de": [
                "Teigblatt auslegen und mit Butter bestreichen.",
                "In der Mitte Pistazien, Kaymakflocken und Zucker verteilen.",
                "Wie einen Briefumschlag falten.",
                "Bei 200°C 8-10 Min. backen, bis er goldgelb und kross ist.",
                "In Stücke schneiden und warm genießen."
            ]
        }
    },

    # ─── HATAY & AKDENİZ ───
    {
        "id": "tr_tepsi_kebabi",
        "cuisineId": "turkish",
        "emoji": "🥘",
        "image": "foods/tr_tepsi_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 20,
        "cookTime": 35,
        "difficulty": "easy",
        "calories": 520,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "hatay", "dinner"],
        "name": {
            "tr": "Antakya Tepsi Kebabı (Sini Kebabı)",
            "en": "Antakya Tray Kebab (Sini)",
            "es": "Kebab en Bandeja de Antakya",
            "de": "Antakya Blech-Kebab (Sini)"
        },
        "description": {
            "tr": "Hatay'ın meşhur zırh kıyması, sarımsak, taze biber ve baharatların yuvarlak tepsiye basılıp fırında domates sosuyla nar gibi kızartılması.",
            "en": "Hatay's famous minced meat kneaded with garlic, herbs, and spices, pressed thinly onto a round metal tray and baked with tomato sauce.",
            "es": "Famoso kebab de Hatay con carne picada, ajo y especias extendida en bandeja redonda y horneada con salsa de tomate.",
            "de": "Berühmter Kebab aus Hatay: Gewürztes Hackfleisch auf einem runden Blech flachgedrückt und mit Tomatensauce im Ofen knusprig gebacken."
        },
        "ingredients": {
            "tr": ["600g kuzu-dana karışık kıyma", "1 adet kuru soğan", "4 diş sarımsak", "2 adet kırmızı kapya biber", "1 demet maydanoz", "1 yemek kaşığı biber salçası", "Kimyon, karabiber, pul biber, tuz", "Domates ve sivri biber dilimleri"],
            "en": ["600g mixed lamb-beef mince", "1 onion", "4 cloves garlic", "2 red bell peppers", "1 bunch parsley", "1 tbsp pepper paste", "Cumin, black pepper, chili, salt", "Tomato and green pepper wedges"],
            "es": ["600g carne picada mixta", "1 cebolla", "4 dientes de ajo", "2 pimientos rojos", "1 manojo perejil", "1 cda pasta de pimiento", "Comino, pimienta, sal", "Tomates y pimientos en gajos"],
            "de": ["600g gemischtes Hackfleisch", "1 Zwiebel", "4 Knoblauchzehen", "2 rote Paprika", "1 Bund Petersilie", "1 EL Paprikamark", "Kreuzkümmel, Pfeffer, Salz", "Tomaten- und Paprikaspalten"]
        },
        "steps": {
            "tr": [
                "Soğan, sarımsak, kırmızı biber ve maydanozu zırhla veya incecik doğrayın.",
                "Kıymayı sebzeler ve baharatlarla 10 dakika iyice yoğurun.",
                "Yuvarlak fırın tepsisinin tabanını hafif yağlayıp kıymayı 1 cm kalınlığında eşit şekilde yayın.",
                "Üzerini domates ve biber dilimleriyle süsleyin.",
                "Sulandırılmış salçalı sosu üzerine gezdirip 200°C fırında 30-35 dakika pişirin."
            ],
            "en": [
                "Finely mince onion, garlic, red peppers, and parsley.",
                "Knead minced meat with chopped vegetables and spices for 10 minutes.",
                "Press the mixture evenly into a lightly oiled round baking tray.",
                "Garnish with tomato and pepper slices.",
                "Drizzle diluted tomato paste sauce and bake at 200°C for 30-35 minutes."
            ],
            "es": [
                "Picar finamente cebolla, ajo, pimiento y perejil.",
                "Amasar la carne picada con las verduras y especias.",
                "Extender en bandeja redonda aceitada.",
                "Decorar con rodajas de tomate y pimiento.",
                "Verter salsa de tomate diluida y hornear a 200°C por 35 min."
            ],
            "de": [
                "Gemüse sehr fein hacken.",
                "Mit dem Hackfleisch und Gewürzen kräftig verkneten.",
                "Gleichmäßig auf einem geölten runden Blech ausstreichen.",
                "Mit Tomaten- und Paprikastreifen belegen.",
                "Mit angerührtem Tomatensaft beträufeln und bei 200°C 35 Min. backen."
            ]
        }
    },
    {
        "id": "tr_humus_sicak_pastirmali",
        "cuisineId": "turkish",
        "emoji": "🧆",
        "image": "foods/tr_humus_sicak.webp",
        "color": "FFFFA502",
        "prepTime": 15,
        "cookTime": 10,
        "difficulty": "easy",
        "calories": 440,
        "servings": 4,
        "isPremium": False,
        "tags": ["street_food", "hatay", "dinner"],
        "name": {
            "tr": "Hatay Sıcak Pastırmalı Humus",
            "en": "Hatay Warm Hummus with Pastirma",
            "es": "Hummus Caliente con Pastirma de Hatay",
            "de": "Hatay Warmer Hummus mit Pastirma"
        },
        "description": {
            "tr": "Kabuksuz haşlanmış nohut ve tahinin fırında güveçte ısıtılıp üzerine tereyağında çıtırdatılmış çemenli pastırma ve çam fıstığı dökülerek sunulan Akdeniz başyapıtı.",
            "en": "Silky warm hummus baked in clay dishes, topped with sizzling cured spiced beef (pastirma), toasted pine nuts, and bubbling melted butter.",
            "es": "Cremoso hummus caliente horneado en cazuela de barro, cubierto con pastırma crujiente a la mantequilla y piñones tostados.",
            "de": "Warmer cremiger Hummus im Tontopf gebacken, gekrönt von knusprigem Rinderpastirma und gerösteten Pinienkernen in heißer Butter."
        },
        "ingredients": {
            "tr": ["2 su bardağı haşlanmış kabuksuz nohut", "1/2 su bardağı tahin", "1 limonun suyu", "3 diş sarımsak", "1 çay kaşığı kimyon", "100g pastırma", "2 yemek kaşığı tereyağı", "1 yemek kaşığı çam fıstığı"],
            "en": ["2 cups peeled cooked chickpeas", "1/2 cup tahini", "Juice of 1 lemon", "3 cloves garlic", "1 tsp cumin", "100g pastirma (cured beef)", "2 tbsp butter", "1 tbsp pine nuts"],
            "es": ["2 tazas garbanzos pelados cocidos", "1/2 taza tahini", "Jugo de 1 limón", "3 dientes de ajo", "1 cdta comino", "100g pastirma", "2 cdas mantequilla", "1 cda piñones"],
            "de": ["2 Tassen geschälte Kichererbsen", "1/2 Tasse Tahini", "Saft von 1 Zitrone", "3 Knoblauchzehen", "1 TL Kreuzkümmel", "100g Pastirma", "2 EL Butter", "1 EL Pinienkerne"]
        },
        "steps": {
            "tr": [
                "Sıcak nohutları tahin, limon suyu, sarımsak, kimyon ve zeytinyağı ile pürüzsüz ipeksi bir kıvam alana kadar blenderdan geçirin.",
                "Humusu güveç veya fırın kaplarına yayın ve 180°C fırında 6-8 dakika ısıtın.",
                "Tavada tereyağında çam fıstıklarını ve doğranmış pastırmaları çıtırlaşana kadar soteleyin.",
                "Sıcak humusun üzerine köpüren tereyağlı pastırmayı döküp sıcak pideyle servis yapın."
            ],
            "en": [
                "Blend hot chickpeas with tahini, lemon juice, garlic, and cumin until silky smooth.",
                "Spread into clay dishes and warm in the oven at 180°C for 6-8 minutes.",
                "Sauté pine nuts and sliced pastirma in butter until crispy and aromatic.",
                "Pour sizzling butter and pastirma over the warm hummus; serve immediately with pita."
            ],
            "es": [
                "Triturar los garbanzos con tahini, limón, ajo y comino hasta obtener una crema sedosa.",
                "Hornear en cazuela de barro a 180°C por 6-8 min.",
                "Saltear los piñones y la pastırma en mantequilla caliente.",
                "Verter sobre el hummus caliente y servir con pan de pita."
            ],
            "de": [
                "Kichererbsen mit Tahini, Zitronensaft, Knoblauch und Kreuzkümmel cremig pürieren.",
                "In Tonschalen füllen und 6-8 Min. bei 180°C backen.",
                "Pinienkerne und Pastirma in schäumender Butter anbraten.",
                "Über den warmen Hummus gießen und mit Fladenbrot servieren."
            ]
        }
    },
    {
        "id": "tr_fellah_koftesi",
        "cuisineId": "turkish",
        "emoji": "🧆",
        "image": "foods/tr_fellah_koftesi.webp",
        "color": "FFE84545",
        "prepTime": 30,
        "cookTime": 15,
        "difficulty": "medium",
        "calories": 340,
        "servings": 4,
        "isPremium": False,
        "tags": ["vegetarian", "hatay", "dinner"],
        "name": {
            "tr": "Hatay Fellah Köftesi",
            "en": "Hatay Fellah Bulgur Dumplings",
            "es": "Albóndigas de Bulgur Fellah",
            "de": "Hatay Fellah Bulgurklößchen"
        },
        "description": {
            "tr": "İnce köftelik bulgurla yuvarlanıp ortasına düğme basılan köftelerin haşlanıp bol sarımsaklı domates sosu ve maydanozla harmanlanması.",
            "en": "Small dimpled bulgur dumplings boiled until tender and coated in a rich, garlicky spiced tomato paste sauce with fresh flat-leaf parsley.",
            "es": "Pequeñas albóndigas de bulgur hervidas y bañadas en una salsa de tomate aromatizada con abundante ajo y perejil fresco.",
            "de": "Kleine eingedrückte Bulgurklößchen, serviert in einer pikanten Knoblauch-Tomatensauce mit viel frischer Petersilie."
        },
        "ingredients": {
            "tr": ["2 su bardağı ince köftelik bulgur", "1 su bardağı irmik", "1 yemek kaşığı un", "1 yemek kaşığı biber salçası", "3 adet rendelenmiş domates", "5 diş sarımsak", "1/2 çay bardağı zeytinyağı", "1 demet maydanoz", "Kimyon ve tuz"],
            "en": ["2 cups fine bulgur", "1 cup semolina", "1 tbsp flour", "1 tbsp pepper paste", "3 grated tomatoes", "5 cloves garlic", "1/4 cup olive oil", "1 bunch parsley", "Cumin and salt"],
            "es": ["2 tazas bulgur fino", "1 taza sémola", "1 cda harina", "1 cda pasta de pimiento", "3 tomates rallados", "5 dientes de ajo", "Aceite de oliva", "Perejil y comino"],
            "de": ["2 Tassen feiner Bulgur", "1 Tasse Grieß", "1 EL Mehl", "1 EL Paprikamark", "3 geriebene Tomaten", "5 Knoblauchzehen", "Olivenöl", "Petersilie und Kreuzkümmel"]
        },
        "steps": {
            "tr": [
                "Bulgur ve irmiği sıcak suyla ıslatıp 15 dakika bekletin.",
                "Un, salça, kimyon ve tuz ekleyip macun kıvamına gelene kadar 10 dakika yoğurun.",
                "Fındık büyüklüğünde parçalar yuvarlayıp ortasına parmağınızla çukur (düğme) yapın.",
                "Kaynar tuzlu suda köfteler su yüzeyine çıkana kadar 8-10 dakika haşlayıp süzün.",
                "Zeytinyağında sarımsak ve rendelenmiş domatesi pişirip salçalı sos yapın; köfteleri sosa bulayıp bol maydanozla servis edin."
            ],
            "en": [
                "Soak bulgur and semolina in hot water for 15 minutes.",
                "Knead with flour, paste, and cumin until smooth and pliable.",
                "Roll into hazelnut-sized balls and press a dimple into the center with your pinky.",
                "Boil in salted water for 8-10 minutes until they float to the top.",
                "Toss with warm garlic-tomato olive oil sauce and fresh parsley."
            ],
            "es": [
                "Remojar el bulgur y sémola con agua caliente.",
                "Amasar con harina y especias.",
                "Formar bolitas del tamaño de avellanas y presionar el centro.",
                "Hervir 8-10 minutos hasta que floten.",
                "Mezclar con salsa de tomate al ajo y perejil fresco."
            ],
            "de": [
                "Bulgur und Grieß einweichen.",
                "Mit Mehl und Gewürzen elastisch kneten.",
                "Haselnussgroße Bällchen formen und eine Mulde eindrücken.",
                "In Salzwasser 8-10 Min. kochen.",
                "Mit Knoblauch-Tomatensauce und Petersilie vermengen."
            ]
        }
    },
    {
        "id": "tr_tantuni",
        "cuisineId": "turkish",
        "emoji": "🌯",
        "image": "foods/tr_tantuni.webp",
        "color": "FFFF4757",
        "prepTime": 20,
        "cookTime": 15,
        "difficulty": "medium",
        "calories": 490,
        "servings": 4,
        "isPremium": False,
        "tags": ["street_food", "meat", "dinner"],
        "name": {
            "tr": "Mersin Tantunisi",
            "en": "Mersin Tantuni Wrap",
            "es": "Wrap Tantuni de Mersin",
            "de": "Mersin Tantuni Wrap"
        },
        "description": {
            "tr": "Mersin'in tescilli sokak lezzeti; pamuk gibi haşlanıp özel tantuni tepsisinde pamuk yağı, toz biber ve suyla kavrulan biftek etinin taze lavaşta dürüm yapılması.",
            "en": "Mersin's iconic street food: finely diced tender beef flash-fried in a concave sac pan with spices and broth, rolled tightly in thin lavash with sumac onions and tomatoes.",
            "es": "Plato callejero icónico de Mersin: ternera finamente picada salteada en sartén cóncava con especias y enrollada en pan fino con cebolla al zumaque.",
            "de": "Kult-Streetfood aus Mersin: Fein gewürfeltes Rindfleisch in einer speziellen Pfanne scharf angebraten und in dünnem Fladenbrot mit Sumach-Zwiebeln gerollt."
        },
        "ingredients": {
            "tr": ["500g dana biftek, minik küp doğranmış", "1 çay bardağı sıvı yağ", "1 yemek kaşığı toz kırmızı biber", "1 çay kaşığı sumak", "2 adet domates", "1 demet maydanoz", "2 adet kırmızı soğan", "Taze ince lavaş ve limon"],
            "en": ["500g beef sirloin, finely diced", "1/2 cup cooking oil", "1 tbsp sweet paprika / red pepper", "1 tsp sumac", "2 tomatoes, diced", "1 bunch parsley", "2 red onions, thinly sliced", "Thin lavash bread and lemon"],
            "es": ["500g lomo de ternera picado fino", "1/2 taza aceite", "1 cda pimentón dulce", "1 cdta zumaque", "2 tomates", "1 manojo perejil", "2 cebollas rojas", "Pan lavash y limón"],
            "de": ["500g Rindersteak, feinst gewürfelt", "1/2 Tasse Pflanzenöl", "1 EL Paprikapulver", "1 TL Sumach", "2 Tomaten", "1 Bund Petersilie", "2 rote Zwiebeln", "Dünnes Fladenbrot und Zitrone"]
        },
        "steps": {
            "tr": [
                "Eti tencerede az suyla suyunu çekene kadar haşlayın.",
                "Tantuni tepsisinin ortasında yağı ısıtıp toz biber ekleyin.",
                "Haşlanan etten porsiyon alarak tepsini ortasında az su serpiştirerek hızlıca kavurun.",
                "Lavaşı etin üzerine basıp buharıyla yumuşatın ve yağını çektirin.",
                "Lavaşın içine eti, piyazlık sumaklı soğanı, domatesi ve maydanozu koyup sıkıca sarın; limon sıkarak servis yapın."
            ],
            "en": [
                "Boil diced beef in a little water until fully tender.",
                "Heat oil with paprika in the center of a wide flat pan.",
                "Flash-fry portions of meat with dashes of water to create steam.",
                "Press lavash onto the meat to absorb flavorful steam and juices.",
                "Fill wrap with meat, sumac onions, tomatoes, and parsley; roll tightly and serve with lemon wedges."
            ],
            "es": [
                "Hervir la ternera picada hasta tierna.",
                "Calentar aceite con pimentón en sartén ancha.",
                "Saltear la carne con toques de agua para generar vapor.",
                "Presionar el pan sobre la carne para impregnar sabores.",
                "Rellenar con carne, cebolla al zumaque, tomate y perejil; enrollar y servir con limón."
            ],
            "de": [
                "Rindfleischwürfel kurz vorkochen.",
                "Öl mit Paprika in einer großen Pfanne erhitzen.",
                "Fleisch mit etwas Wasser unter Dampfblasen scharf anbraten.",
                "Fladenbrot auf das Fleisch drücken.",
                "Mit Sumach-Zwiebeln, Tomaten und Petersilie füllen, straff rollen und mit Zitrone genießen."
            ]
        }
    },

    # ─── KARADENİZ & KUZEY ───
    {
        "id": "tr_kuymak",
        "cuisineId": "turkish",
        "emoji": "🧀",
        "image": "foods/tr_kuymak.webp",
        "color": "FFFFA502",
        "prepTime": 5,
        "cookTime": 15,
        "difficulty": "easy",
        "calories": 460,
        "servings": 2,
        "isPremium": False,
        "tags": ["breakfast", "vegetarian", "karadeniz"],
        "name": {
            "tr": "Karadeniz Kuymak (Mıhlama)",
            "en": "Black Sea Kuymak (Mıhlama)",
            "es": "Kuymak del Mar Negro",
            "de": "Schwarzes Meer Kuymak (Mıhlama)"
        },
        "description": {
            "tr": "Karadeniz yaylalarının mis kokulu tereyağı, ince mısır unu ve uzadıkça uzayan tescilli kolot/tel peynirinin tavada buluşması.",
            "en": "Iconic Black Sea breakfast delight made with golden clarified butter, fine cornmeal, and stretchy melted local Kolot cheese that pulls for meters.",
            "es": "Delicia del Mar Negro elaborada con mantequilla dorada, harina de maíz y queso Kolot hilado fundido que se estira infinitamente.",
            "de": "Berühmte Spezialität vom Schwarzen Meer aus nussiger Butter, Maismehl und lang ziehendem Kolot-Käse."
        },
        "ingredients": {
            "tr": ["3 yemek kaşığı yayık tereyağı", "3 yemek kaşığı mısır unu", "1.5 su bardağı ılık su veya süt", "250g Trabzon kolot veya telli çeçil peyniri", "Tuz"],
            "en": ["3 tbsp cultured butter", "3 tbsp fine cornmeal", "1.5 cups warm water or milk", "250g Kolot or string cheese", "Pinch of salt"],
            "es": ["3 cdas mantequilla artesanal", "3 cdas harina de maíz", "1.5 tazas agua tibia o leche", "250g queso Kolot o en hebras", "Sal"],
            "de": ["3 EL gute Bauernbutter", "3 EL Maismehl", "1.5 Tassen warmes Wasser oder Milch", "250g Kolot- oder Fadenkäse", "Prise Salz"]
        },
        "steps": {
            "tr": [
                "Bakır tavada tereyağını eritin.",
                "Mısır ununu ekleyip kokusu çıkıp rengi hafif dönene kadar kavurun.",
                "Ilık suyu yavaş yavaş ekleyip un pürüzsüzleşene ve yağı yüzeye çıkana kadar karıştırarak pişirin.",
                "Peynirleri ekleyip çok fazla karıştırmadan kısık ateşte erimesini ve yağın üzerine çıkmasını bekleyin.",
                "Mısır ekmeğiyle sıcak sıcak bandırarak tüketin."
            ],
            "en": [
                "Melt butter in a copper pan over medium heat.",
                "Add cornmeal and toast until golden and aromatic.",
                "Gradually pour in warm water, stirring continuously until smooth and bubbling.",
                "Add shredded Kolot cheese; allow to melt gently over low heat until butter floats to the top.",
                "Dip crusty bread and enjoy the infinite cheese stretch."
            ],
            "es": [
                "Fundir la mantequilla en sartén de cobre.",
                "Tostar la harina de maíz hasta dorar.",
                "Verter agua tibia lentamente batiendo hasta espesar.",
                "Añadir el queso y dejar fundir a fuego lento sin remover demasiado.",
                "Servir caliente con pan de maíz para untar."
            ],
            "de": [
                "Butter in Kupferschale zerlassen.",
                "Maismehl darin nussig anrösten.",
                "Warmes Wasser einrühren, bis die Masse andickt.",
                "Käse zugeben und bei schwacher Hitze schmelzen lassen, bis Butter aufsteigt.",
                "Mit frischem Brot heiß dippen."
            ]
        }
    },
    {
        "id": "tr_hamsili_pilav",
        "cuisineId": "turkish",
        "emoji": "🐟",
        "image": "foods/tr_hamsili_pilav.webp",
        "color": "FF2ED573",
        "prepTime": 30,
        "cookTime": 40,
        "difficulty": "hard",
        "calories": 480,
        "servings": 4,
        "isPremium": False,
        "tags": ["seafood", "karadeniz", "dinner"],
        "name": {
            "tr": "Fırında Karadeniz Hamsili Pilav",
            "en": "Baked Black Sea Anchovy Rice Cake",
            "es": "Pastel de Arroz con Anchoas del Mar Negro",
            "de": "Überbackener Schwarzmeer Sardellen-Pilaw"
        },
        "description": {
            "tr": "Karadeniz'in taze kılçıksız hamsileriyle kaplanmış fırın kabında, kuş üzümlü, çam fıstıklı ve baharatlı iç pilavın fırında nar gibi kızartılması.",
            "en": "Fresh deboned Black Sea anchovies lining a baking pan, filled with aromatic spiced rice with currants, pine nuts, and baked until golden and crispy.",
            "es": "Anchoas frescas desespinadas cubriendo un molde relleno de arroz aromático con pasas y piñones, horneado hasta dorar.",
            "de": "Frische entgrätete Sardellen umhüllen eine Füllung aus gewürztem Reis mit Korinthen und Pinienkernen, im Ofen knusprig gebacken."
        },
        "ingredients": {
            "tr": ["1 kg taze hamsi (kılçıkları ayıklanmış ve açılmış)", "1.5 su bardağı baldo pirinç", "2 yemek kaşığı çam fıstığı", "2 yemek kaşığı kuş üzümü", "1 adet kuru soğan", "1 tatlı kaşığı yenibahar ve nane", "2 yemek kaşığı tereyağı", "Tuz ve karabiber"],
            "en": ["1 kg fresh anchovies (deboned & butterflied)", "1.5 cups rice", "2 tbsp pine nuts", "2 tbsp currants", "1 onion, diced", "1 tsp allspice and mint", "2 tbsp butter", "Salt and pepper"],
            "es": ["1 kg anchoas frescas limpias", "1.5 tazas arroz", "2 cdas piñones", "2 cdas pasas", "1 cebolla", "1 cdta pimienta de Jamaica y menta", "2 cdas mantequilla", "Sal y pimienta"],
            "de": ["1 kg frische Sardellen (entgrätet)", "1.5 Tassen Reis", "2 EL Pinienkerne", "2 EL Korinthen", "1 Zwiebel", "1 TL Piment und Minze", "2 EL Butter", "Salz und Pfeffer"]
        },
        "steps": {
            "tr": [
                "Hamsilerin kafalarını ve kılçıklarını ayıklayıp yıkayın, süzün.",
                "Tencerede tereyağında soğan ve fıstıkları kavurun. Pirinç, kuş üzümü ve baharatları ekleyip yarı kıvamda iç pilav pişirin.",
                "Fırın kabını tereyağı ile yağlayıp hamsileri derileri dışa gelecek şekilde tabana ve kenarlara dizin.",
                "Hazırlanan iç pilavı doldurup üzerine kalan hamsileri dizerek kapatın.",
                "Üzerine zeytinyağı gezdirip 190°C fırında 35-40 dakika hamsiler kızarana kadar pişirin."
            ],
            "en": [
                "Clean, debone and butterfly the anchovies.",
                "Cook a fragrant half-done spiced rice with onions, pine nuts, currants, and allspice in butter.",
                "Line a buttered baking dish with anchovies (skin-side down).",
                "Fill with the spiced rice and cover completely with remaining anchovies.",
                "Drizzle olive oil and bake at 190°C for 35-40 minutes until crisp and golden."
            ],
            "es": [
                "Limpiar y desespinar las anchoas.",
                "Cocinar el arroz aromatizado con cebolla, piñones, pasas y especias.",
                "Forrar un molde aceitado con las anchoas.",
                "Rellenar con arroz y cubrir con más anchoas.",
                "Hornear a 190°C por 40 min hasta dorar."
            ],
            "de": [
                "Sardellen säubern und entgräten.",
                "Würzigen Reis mit Zwiebeln, Pinienkernen und Korinthen halbgar dünsten.",
                "Auflaufform mit Sardellen auslegen.",
                "Mit Reis füllen und mit Sardellen abschließen.",
                "Bei 190°C ca. 35-40 Minuten goldbraun backen."
            ]
        }
    },
    {
        "id": "tr_akcaabat_koftesi",
        "cuisineId": "turkish",
        "emoji": "🥩",
        "image": "foods/tr_akcaabat_koftesi.webp",
        "color": "FFE84545",
        "prepTime": 20,
        "cookTime": 15,
        "difficulty": "medium",
        "calories": 460,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "karadeniz", "grilled"],
        "name": {
            "tr": "Trabzon Akçaabat Köftesi",
            "en": "Trabzon Akcaabat Meatballs",
            "es": "Albóndigas Akçaabat de Trabzon",
            "de": "Trabzon Akçaabat Köfte"
        },
        "description": {
            "tr": "Trabzon Akçaabat'ın tescilli lezzeti; dana döş eti, böbrek yağı, taze sarımsak ve bayat ekmek içiyle yoğrulup odun kömüründe ızgara edilen efsane köfte.",
            "en": "Trabzon's renowned garlic meatballs made with minced beef brisket, kidney fat, garlic, and bread, grilled juicy over charcoal.",
            "es": "Famosas albóndigas de Trabzon elaboradas con carne de ternera, ajo y pan, asadas a la brasa con gran jugosidad.",
            "de": "Berühmte Frikadellen aus Trabzon mit Knoblauch und Rindfleisch, saftig über Holzkohle gegrillt."
        },
        "ingredients": {
            "tr": ["700g dana döş kıyma", "150g kavram/böbrek yağı", "6 diş sarımsak, ezilmiş", "2 dilim bayat ekmek içi", "Tuz ve karabiber", "Közlenmiş biber ve domates"],
            "en": ["700g beef brisket mince", "150g beef suet/kidney fat", "6 cloves garlic, crushed", "2 slices stale breadcrumbs", "Salt and pepper", "Grilled peppers and tomatoes"],
            "es": ["700g falda de ternera picada", "150g grasa de riñonada", "6 dientes de ajo", "2 rebanadas pan duro", "Sal y pimienta", "Tomates y pimientos"],
            "de": ["700g Rinderbrust-Hack", "150g Rindernierenfett", "6 Knoblauchzehen", "2 Scheiben altbackenes Brot", "Salz und Pfeffer", "Gegrillte Tomaten"]
        },
        "steps": {
            "tr": [
                "Dana kıymayı, çekilmiş böbrek yağı, ezilmiş sarımsak, ıslatılıp sıkılmış ekmek içi ve tuz ile en az 15 dakika sakız gibi olana kadar yoğurun.",
                "Köfte harcını buzdolabında 4 saat dinlendirin.",
                "Yassı yuvarlak köfteler şekillendirin.",
                "Harlı odun kömürü ızgarasında her iki tarafını sık sık çevirerek 8-10 dakika sulu kalacak şekilde pişirin.",
                "Köz biber, domates ve piyaz ile servis edin."
            ],
            "en": [
                "Knead minced beef with ground suet, garlic, soaked bread, and salt for 15 minutes until cohesive.",
                "Rest the mixture in the fridge for 4 hours.",
                "Shape into wide flat round patties.",
                "Grill over hot charcoal for 8-10 minutes, flipping frequently.",
                "Serve with grilled peppers, tomatoes, and white bean piyaz."
            ],
            "es": [
                "Amasar la carne con grasa, ajo, pan y sal por 15 min.",
                "Reposar en refrigerador 4 horas.",
                "Formar hamburguesas planas.",
                "Asar a las brasas 8-10 min volteando seguido.",
                "Servir con verduras asadas y ensalada de alubias."
            ],
            "de": [
                "Hackfleisch mit Fett, Knoblauch, Brot und Salz 15 Min. verkneten.",
                "4 Stunden kühlstellen.",
                "Flache Patties formen.",
                "Über Holzkohle 8-10 Min. saftig grillen.",
                "Mit gegrilltem Gemüse servieren."
            ]
        }
    },
    {
        "id": "tr_karalahana_sarmasi",
        "cuisineId": "turkish",
        "emoji": "🥬",
        "image": "foods/tr_karalahana.webp",
        "color": "FF2ED573",
        "prepTime": 40,
        "cookTime": 45,
        "difficulty": "medium",
        "calories": 390,
        "servings": 4,
        "isPremium": False,
        "tags": ["dinner", "meat", "karadeniz"],
        "name": {
            "tr": "Etli Karadeniz Karalahana Sarması",
            "en": "Black Sea Collard Green Rolls",
            "es": "Rollitos de Berza del Mar Negro",
            "de": "Schwarzmeer Kohlrouladen (Karalahana)"
        },
        "description": {
            "tr": "Karadeniz'in taze karalahana yapraklarının haşlanıp satır kıyması, pirinç, mısır yarması ve baharatlı harçla sarılarak mısır ekmeği ve yoğurtla sunulması.",
            "en": "Tender boiled Black Sea collard greens rolled with spiced minced beef, rice, and cracked corn, simmered gently and served with garlic yogurt.",
            "es": "Hojas de berza fresca del Mar Negro rellenas de carne picada sazonada, arroz y maíz partido, servidas con yogur.",
            "de": "Zarte Schwarzmeer-Kohlblätter, gefüllt mit Rinderhack, Reis und Maisgrieß, serviert mit frischem Joghurt."
        },
        "ingredients": {
            "tr": ["2 bağ taze karalahana", "400g kıyma", "1 su bardağı pirinç", "1/2 su bardağı mısır yarması veya bulgur", "2 adet soğan", "2 yemek kaşığı tereyağı", "1 yemek kaşığı biber salçası", "Nane, pul biber, tuz"],
            "en": ["2 bunches fresh collard greens", "400g minced meat", "1 cup rice", "1/2 cup coarse cracked corn or bulgur", "2 onions", "2 tbsp butter", "1 tbsp pepper paste", "Mint, chili, salt"],
            "es": ["2 manojos berzas frescas", "400g carne picada", "1 taza arroz", "1/2 taza bulgur o maíz", "2 cebollas", "2 cdas mantequilla", "1 cda pasta de pimiento", "Menta y sal"],
            "de": ["2 Bund Grünkohl/Blattkohl", "400g Hackfleisch", "1 Tasse Reis", "1/2 Tasse Maisgrieß oder Bulgur", "2 Zwiebeln", "2 EL Butter", "1 EL Paprikamark", "Minze und Salz"]
        },
        "steps": {
            "tr": [
                "Karalahana yapraklarını kaynar tuzlu suda 3-4 dakika haşlayıp soğuk suya alın, damarlarını kesin.",
                "Kıyma, yıkanmış pirinç, mısır yarması, ince doğranmış soğan, salça ve baharatları yoğurun.",
                "Yapraklara harçtan koyup parmak kalınlığında sarın.",
                "Tencereye dizip üzerine tereyağı parçaları ve sıcak su ekleyin.",
                "Kısık ateşte 40-45 dakika pişirip yoğurtla servis yapın."
            ],
            "en": [
                "Blanch collard greens in boiling water for 3-4 mins; transfer to ice water and trim thick stems.",
                "Mix minced meat, rice, cracked corn, onions, paste, and spices for the filling.",
                "Place filling on leaves and roll tightly into finger-thick rolls.",
                "Pack into a pot, top with butter pats and broth, then weight with a plate.",
                "Simmer on low for 40-45 minutes and serve with cool yogurt."
            ],
            "es": [
                "Blanquear las hojas de berza 4 min y cortar el tallo central.",
                "Mezclar carne, arroz, cebolla, pasta y especias.",
                "Rellenar y enrollar en forma de cilindro.",
                "Cocinar a fuego lento en olla con caldo 45 min.",
                "Servir con yogur."
            ],
            "de": [
                "Kohlblätter 3-4 Min. blanchieren und dicke Blattrippen entfernen.",
                "Füllung aus Hack, Reis, Zwiebeln und Gewürzen mischen.",
                "Zu fingerdicken Rouladen wickeln.",
                "Im Topf mit etwas Brühe und Butter 40-45 Min. sanft garen.",
                "Mit Joghurt servieren."
            ]
        }
    },

    # ─── EGE & BATI ANADOLU ───
    {
        "id": "tr_cokertme_kebabi",
        "cuisineId": "turkish",
        "emoji": "🥩",
        "image": "foods/tr_cokertme_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 25,
        "cookTime": 20,
        "difficulty": "medium",
        "calories": 580,
        "servings": 2,
        "isPremium": False,
        "tags": ["meat", "dinner"],
        "name": {
            "tr": "Bodrum Çökertme Kebabı",
            "en": "Bodrum Cokertme Kebab",
            "es": "Kebab Çökertme de Bodrum",
            "de": "Bodrum Cökertme Kebab"
        },
        "description": {
            "tr": "Kibrit çöpü inceliğinde çıtır kızarmış patateslerin üzerine sarımsaklı süzme yoğurt, marine edilmiş yumuşacık dana antrikot şeritleri ve tereyağlı domates sosu.",
            "en": "Matchstick crisp fried potatoes topped with garlic yogurt, tender marinated beef strips, and rich sizzling tomato butter sauce.",
            "es": "Patatas paja crujientes cubiertas con yogur al ajo, tiras de ternera marinada tierna y salsa de tomate a la mantequilla.",
            "de": "Knusprige Streichholzkartoffeln mit Knoblauchjoghurt, zarten Rinderfiletstreifen und heißer Tomatenbutter."
        },
        "ingredients": {
            "tr": ["400g dana bonfile veya antrikot, jülyen doğranmış", "3 adet büyük patates, kibrit çöpü doğranmış", "1 su bardağı süzme yoğurt", "2 diş sarımsak", "2 yemek kaşığı tereyağı", "1 yemek kaşığı domates salçası", "Kekik, pul biber, tuz"],
            "en": ["400g beef tenderloin, julienned", "3 large potatoes, cut into matchsticks", "1 cup strained yogurt", "2 cloves garlic", "2 tbsp butter", "1 tbsp tomato paste", "Oregano, chili, salt"],
            "es": ["400g lomo de ternera en tiras", "3 patatas grandes cortadas finas", "1 taza yogur colado", "2 dientes de ajo", "2 cdas mantequilla", "1 cda pasta de tomate", "Orégano y sal"],
            "de": ["400g Rinderfilet in Streifen", "3 große Kartoffeln, gestiftelt", "1 Tasse Joghurt", "2 Knoblauchzehen", "2 EL Butter", "1 EL Tomatenmark", "Oregano, Chili, Salz"]
        },
        "steps": {
            "tr": [
                "Kibrit patatesleri nişastası gidene kadar yıkayıp kurulayın ve kızgın yağda altın sarısı çıtır olana kadar kızartın.",
                "Eti zeytinyağı ve kekikle yüksek ateşte suyunu salıp çekene kadar soteleyin.",
                "Tereyağında salçayı kavurup az suyla domates sosunu hazırlayın.",
                "Tabağa çıtır patatesleri yayın, üzerine sarımsaklı süzme yoğurt gezdirin.",
                "En üste sotelenmiş eti ve sıcak domates sosunu döküp servis edin."
            ],
            "en": [
                "Wash, dry, and deep-fry matchstick potatoes until golden and crunchy.",
                "Sear julienned beef in hot pan with olive oil and oregano until tender.",
                "Simmer butter with tomato paste and a splash of water for the sauce.",
                "Layer crispy potatoes on a plate and drizzle with garlic yogurt.",
                "Top with hot beef strips and warm tomato butter sauce."
            ],
            "es": [
                "Freír las patatas paja hasta que estén crujientes.",
                "Saltear la ternera a fuego vivo con orégano.",
                "Cocinar la salsa de tomate con mantequilla.",
                "Montar las patatas en el plato con yogur al ajo.",
                "Coronar con la carne y la salsa caliente."
            ],
            "de": [
                "Kartoffelstifte goldbraun und knusprig frittieren.",
                "Rindfleischstreifen scharf anbraten.",
                "Tomatensauce in Butter aufkochen.",
                "Kartoffeln auf einen Teller geben, Knoblauchjoghurt darüber verteilen.",
                "Mit Fleisch und heißer Sauce anrichten."
            ]
        }
    },
    {
        "id": "tr_sevketi_bostan",
        "cuisineId": "turkish",
        "emoji": "🌿",
        "image": "foods/tr_sevketi_bostan.webp",
        "color": "FF2ED573",
        "prepTime": 25,
        "cookTime": 40,
        "difficulty": "medium",
        "calories": 380,
        "servings": 4,
        "isPremium": False,
        "tags": ["dinner", "meat"],
        "name": {
            "tr": "Ege Kuzu Etli Şevketi Bostan",
            "en": "Aegean Lamb with Blessed Thistle",
            "es": "Cordero Egeo con Cardo Bendito",
            "de": "Ägäisches Lamm mit Benediktenkraut"
        },
        "description": {
            "tr": "Ege topraklarının şifalı yabani otu şevketi bostanın taze kuzu eti, zeytinyağı ve terbiyeli limonlu sos ile ağır ateşte pişirilen asil yemeği.",
            "en": "Traditional Aegean delicacy of wild foraged blessed thistle slow-braised with tender lamb, extra virgin olive oil, and a zesty egg-lemon liaison (terbiye).",
            "es": "Especialidad silvestre del Egeo: cardo bendito estofado lentamente con cordero tierno, aceite de oliva virgen y salsa de limón y huevo.",
            "de": "Ägäischer Gaumenschmaus aus wild gesammeltem Benediktenkraut, geschmort mit zartem Lammfleisch und feiner Zitronen-Ei-Sauce."
        },
        "ingredients": {
            "tr": ["1 kg şevketi bostan (ayıklanmış ve doğranmış)", "500g kemikli veya kuşbaşı kuzu eti", "1 adet kuru soğan", "1/2 çay bardağı sızma zeytinyağı", "1 adet yumurta sarısı", "1/2 limonun suyu", "1 tatlı kaşığı un", "Tuz ve karabiber"],
            "en": ["1 kg blessed thistle (cleaned & chopped)", "500g lamb chunks", "1 onion, chopped", "1/4 cup extra virgin olive oil", "1 egg yolk", "Juice of 1/2 lemon", "1 tsp flour", "Salt and pepper"],
            "es": ["1 kg cardo bendito limpio", "500g cordero", "1 cebolla", "Aceite de oliva virgen extra", "1 yema de huevo", "Jugo de 1/2 limón", "1 cdta harina", "Sal"],
            "de": ["1 kg Benediktenkraut (geputzt)", "500g Lammfleisch", "1 Zwiebel", "1/4 Tasse Olivenöl", "1 Eigelb", "Saft von 1/2 Zitrone", "1 TL Mehl", "Salz und Pfeffer"]
        },
        "steps": {
            "tr": [
                "Tencerede zeytinyağında kuzu etlerini mühürleyip soğanla birlikte soteleyin.",
                "Ayıklanıp limonlu suda bekletilmiş şevketi bostanları etin üzerine ilave edin.",
                "Sıcak su ekleyip etler ve otlar lokum gibi yumuşayana kadar kısık ateşte 40 dakika pişirin.",
                "Yumurta sarısı, limon suyu ve unu çırparak yemeğin suyundan ekleyip ılıtın; tencereye döküp 2 dakika kaynatın.",
                "Sıcak servis yapın."
            ],
            "en": [
                "Sear lamb chunks in olive oil with chopped onions until golden.",
                "Add cleaned wild thistle to the pot.",
                "Add hot water, cover, and braise on low heat for 40 minutes until tender.",
                "Whisk egg yolk, lemon juice, and flour with some hot broth to temper; stir into the stew.",
                "Simmer for 2 minutes and serve warm."
            ],
            "es": [
                "Dorar el cordero con cebolla en aceite de oliva.",
                "Añadir el cardo bendito y agua caliente.",
                "Cocinar a fuego lento 40 min.",
                "Templar la yema con jugo de limón y harina con un poco de caldo; incorporar.",
                "Hervir 2 min y servir."
            ],
            "de": [
                "Lammfleisch in Olivenöl mit Zwiebeln anbraten.",
                "Kraut zufügen und mit heißem Wasser bedecken.",
                "40 Min. sanft schmoren, bis alles weich ist.",
                "Eigelb mit Zitronensaft und Mehl verquirlen, mit Brühe angleichen und einrühren.",
                "Kurz aufkochen und warm servieren."
            ]
        }
    },
    {
        "id": "tr_boyoz",
        "cuisineId": "turkish",
        "emoji": "🥐",
        "image": "foods/tr_boyoz.webp",
        "color": "FFFFA502",
        "prepTime": 40,
        "cookTime": 25,
        "difficulty": "hard",
        "calories": 380,
        "servings": 4,
        "isPremium": False,
        "tags": ["breakfast", "street_food", "vegetarian"],
        "name": {
            "tr": "İzmir Boyozu & Fırın Yumurta",
            "en": "Izmir Boyoz Pastry & Baked Egg",
            "es": "Boyoz de Esmirna y Huevo Asado",
            "de": "Izmir Boyoz Gebäck & Ofen-Ei"
        },
        "description": {
            "tr": "İzmir'in 500 yıllık Sefarad mirası simge kahvaltılığı; kat kat açılan yağlı çıtır hamur işi boyoz ve fırında saatlerce kahverengileşene kadar pişen karabiberli yumurta.",
            "en": "Izmir's iconic 500-year-old Sephardic breakfast pastry: multi-layered flaky dough (boyoz) baked golden, served with slow-baked brown hard-boiled eggs with black pepper.",
            "es": "Emblemático hojaldre sefardí de Esmirna: masa crujiente de múltiples capas servida con huevos horneados a fuego lento y pimienta negra.",
            "de": "Kultgebäck aus Izmir: Blättriger Teigling, goldbraun gebacken und serviert mit langsam geschmortem, braunem Ofen-Ei."
        },
        "ingredients": {
            "tr": ["500g un", "1 tatlı kaşığı tuz", "1 tatlı kaşığı şeker", "1 su bardağı ılık su", "150g tereyağı veya sıvı yağ", "4 adet fırınlanmış yumurta", "Karabiber ve tuz"],
            "en": ["500g flour", "1 tsp salt", "1 tsp sugar", "1 cup warm water", "150g butter or oil", "4 slow-baked brown eggs", "Black pepper and salt"],
            "es": ["500g harina", "1 cdta sal", "1 cdta azúcar", "1 taza agua tibia", "150g mantequilla o aceite", "4 huevos horneados", "Pimienta negra"],
            "de": ["500g Mehl", "1 TL Salz", "1 TL Zucker", "1 Tasse warmes Wasser", "150g Butter/Öl", "4 braun gebackene Eier", "Schwarzer Pfeffer"]
        },
        "steps": {
            "tr": [
                "Un, su, tuz ve şekerle yumuşak bir hamur yoğurup bezelere ayırın ve yağ içinde dinlendirin.",
                "Bezeleri havada çevirerek zar gibi tül inceliğinde açın.",
                "Rulo yapıp salyangoz şeklinde sarın.",
                "Fırın tepsisine dizip 220°C fırında üzeri altın sarısı ve çıtır çıtır olana kadar 20-25 dakika pişirin.",
                "Fırında karabiberle pişmiş sıcak yumurta eşliğinde sıcak tüketin."
            ],
            "en": [
                "Knead a smooth dough with flour, water, and salt; divide into balls and rest in oil.",
                "Stretch each dough ball paper-thin by spinning gently in the air.",
                "Roll up and coil into snail-shaped pastries.",
                "Bake at 220°C for 20-25 minutes until puffed, golden, and super flaky.",
                "Serve immediately with warm slow-baked eggs seasoned with black pepper."
            ],
            "es": [
                "Amasar y dividir en bolas; reposar en aceite.",
                "Estirar cada porción hasta que sea transparente.",
                "Enrollar en forma de espiral.",
                "Hornear a 220°C por 20-25 min hasta dorar.",
                "Comer caliente con huevos duros sazonados con pimienta."
            ],
            "de": [
                "Teig kneten, in Kugeln teilen und in Öl ruhen lassen.",
                "Jede Kugel hauchdünn ausziehen.",
                "Zu Schnecken aufrollen.",
                "Bei 220°C 20-25 Min. knusprig backen.",
                "Mit gepfeffertem Ofenei heiß genießen."
            ]
        }
    },

    # ─── DOĞU & İÇ ANADOLU ───
    {
        "id": "tr_cag_kebabi",
        "cuisineId": "turkish",
        "emoji": "🍢",
        "image": "foods/tr_cag_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 30,
        "cookTime": 25,
        "difficulty": "medium",
        "calories": 530,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "erzurum", "grilled"],
        "name": {
            "tr": "Erzurum Cağ Kebabı",
            "en": "Erzurum Cag Kebab",
            "es": "Kebab Cag de Erzurum",
            "de": "Erzurum Cag Kebab"
        },
        "description": {
            "tr": "Erzurum'un dünyaca ünlü lezzeti; soğan, reyhan ve karabiberle marine edilen kuzu etinin yatık döner şişinde odun ateşinde pişirilip cağ şişlerine takılarak kesilmesi.",
            "en": "Erzurum's legendary wood-fired horizontal rotisserie lamb marinated with wild purple basil, onions, and black pepper, served on individual iron skewers (cag).",
            "es": "Legendario kebab horizontal de cordero de Erzurum marinado con albahaca morada, cebolla y asado a fuego de leña en brochetas individuales.",
            "de": "Legendärer Lammkebab aus Erzurum, auf horizontalem Spieß über Holzfeuer mit wildem Basilikum aromatisch gegrillt."
        },
        "ingredients": {
            "tr": ["1 kg kuzu budu eti", "2 adet büyük kuru soğan (suyu çıkarılmış)", "1 su bardağı yoğurt", "1 yemek kaşığı kurutulmuş reyhan", "1 tatlı kaşığı karabiber ve kaya tuzu", "Lavaş ekmeği"],
            "en": ["1 kg boneless leg of lamb", "2 large onions (juiced)", "1 cup yogurt", "1 tbsp dried purple basil (reyhan)", "1 tsp black pepper and rock salt", "Lavash bread"],
            "es": ["1 kg pierna de cordero", "2 cebollas grandes (jugo)", "1 taza yogur", "1 cda albahaca morada seca", "1 cdta pimienta negra y sal", "Pan lavash"],
            "de": ["1 kg Lammkeule", "2 Zwiebeln (ausgepresst)", "1 Tasse Joghurt", "1 EL getrocknetes Purpurbasilikum (Reyhan)", "1 TL Pfeffer und Steinsalz", "Fladenbrot"]
        },
        "steps": {
            "tr": [
                "Kuzu etini ince yapraklar halinde dilimleyin.",
                "Soğan suyu, yoğurt, kuru reyhan, karabiber ve tuzla eti ovup en az 24 saat buzdolabında marine edin.",
                "Eti şişe sıkıca dizip yatay kömür/odun ateşinde çevirerek dışını nar gibi pişirin.",
                "Pişen dış kısımları 'cağ' adı verilen küçük şişlere takıp döner bıçağıyla kesin.",
                "İsteğe bağlı olarak şişleri ızgarada 1 dakika daha çevirip sıcak lavaş ve közlenmiş biberle servis edin."
            ],
            "en": [
                "Slice lamb leg into thin cutlets.",
                "Marinate with onion juice, yogurt, purple basil, and pepper for 24 hours in the fridge.",
                "Thread tightly onto a horizontal spit and roast over open wood fire.",
                "Skewer the crispy outer meat with small metal skewers (cag) and slice off.",
                "Flash-grill for 1 minute on demand and serve with warm lavash."
            ],
            "es": [
                "Cortar el cordero en filetes finos.",
                "Marinar con jugo de cebolla, yogur, albahaca y pimienta por 24h.",
                "Montar en espiedo horizontal y asar al fuego de leña.",
                "Insertar brochetas pequeñas y cortar las capas crujientes.",
                "Servir inmediatamente con pan lavash caliente."
            ],
            "de": [
                "Lammfleisch in dünne Schnitzel schneiden.",
                "Mit Zwiebelsaft, Joghurt und Purpurbasilikum 24h marinieren.",
                "Auf horizontalen Spieß stecken und über Holzfeuer braten.",
                "Mit kleinen Spießen (Cag) portionieren und abschneiden.",
                "Mit warmem Lavasch-Brot servieren."
            ]
        }
    },
    {
        "id": "tr_etli_ekmek",
        "cuisineId": "turkish",
        "emoji": "🍕",
        "image": "foods/tr_etli_ekmek.webp",
        "color": "FFFF6B35",
        "prepTime": 25,
        "cookTime": 10,
        "difficulty": "medium",
        "calories": 480,
        "servings": 3,
        "isPremium": False,
        "tags": ["dinner", "meat"],
        "name": {
            "tr": "Konya Etli Ekmeği",
            "en": "Konya Etli Ekmek (Crispy Long Flatbread)",
            "es": "Etli Ekmek de Konya",
            "de": "Konya Etli Ekmek"
        },
        "description": {
            "tr": "Konya'nın metrelerce uzayabilen incecik çıtır hamuru üzerine satır kıyması, domates, biber ve maydanoz harcı serilip taş fırında pişirilen geleneksel pidesi.",
            "en": "Konya's legendary ultra-long, wafer-thin crispy flatbread topped with finely minced beef, sweet peppers, tomatoes, and parsley baked in wood-fired stone ovens.",
            "es": "Famoso pan plano crujiente y extralargo de Konya con carne picada fina, tomates y pimientos horneado a la leña.",
            "de": "Konyas hauchdünnes, meterlanges knuspriges Fladenbrot mit feinstem Hackfleischbelag, im Holzofen gebacken."
        },
        "ingredients": {
            "tr": ["400g dana-kuzu kıyma (orta yağlı)", "2 adet domates", "3 adet yeşil biber", "1 adet kuru soğan", "1 demet maydanoz", "Mayalı ekmek hamuru", "Tuz ve pul biber"],
            "en": ["400g minced beef & lamb", "2 ripe tomatoes", "3 green peppers", "1 onion", "1 bunch parsley", "Leavened flatbread dough", "Salt and red pepper flakes"],
            "es": ["400g carne picada", "2 tomates", "3 pimientos verdes", "1 cebolla", "Perejil fresco", "Masa de pan con levadura", "Sal y pimienta"],
            "de": ["400g gemischtes Hackfleisch", "2 reife Tomaten", "3 grüne Paprika", "1 Zwiebel", "Petersilie", "Hefeteig", "Salz und Paprikaflocken"]
        },
        "steps": {
            "tr": [
                "Domates, soğan, biber ve maydanozu zırhla çok ince kıyıp kıyma ve tuzla karıştırın.",
                "Mayalı hamuru elinizle çekerek en az 80-90 cm uzunluğunda çok ince şerit halinde açın.",
                "Kıymalı harcı hamurun üzerine eşit ve ince bir tabaka halinde yayın.",
                "Önceden 250°C'ye ısıtılmış fırında (varsa fırın taşında) çıtır çıtır olana kadar 8-10 dakika pişirin.",
                "Dilimleyip yanında taze yeşillik ve ayranla servis edin."
            ],
            "en": [
                "Finely mince tomatoes, onions, peppers, and parsley; mix with minced meat and salt.",
                "Hand-stretch leavened dough into a paper-thin oblong strip up to 1 meter long.",
                "Evenly smear the meat mixture across the thin dough surface.",
                "Bake at 250°C on a hot pizza stone for 8-10 minutes until delightfully crispy.",
                "Cut into segments and serve with fresh greens and cold ayran."
            ],
            "es": [
                "Picar finamente las verduras y mezclar con la carne.",
                "Estirar la masa con las manos hasta hacerla ultrafina y alargada.",
                "Extender el relleno de carne sobre la masa.",
                "Hornear a 250°C por 8-10 min hasta que esté crujiente.",
                "Cortar en porciones y servir con ayran."
            ],
            "de": [
                "Gemüse sehr fein hacken und mit Fleisch vermischen.",
                "Teig hauchdünn und langziehen.",
                "Fleischmasse dünn darauf verstreichen.",
                "Bei 250°C auf heißem Stein 8-10 Min. kross backen.",
                "In Streifen schneiden und mit kaltem Ayran servieren."
            ]
        }
    },
    {
        "id": "tr_kayseri_yaglamasi",
        "cuisineId": "turkish",
        "emoji": "🥞",
        "image": "foods/tr_kayseri_yaglamasi.webp",
        "color": "FFE84545",
        "prepTime": 30,
        "cookTime": 25,
        "difficulty": "medium",
        "calories": 540,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "dinner"],
        "name": {
            "tr": "Kayseri Yağlaması (Şebit)",
            "en": "Kayseri Yaglama (Meat Layer Cake)",
            "es": "Yağlama de Kayseri",
            "de": "Kayseri Yaglama"
        },
        "description": {
            "tr": "İncecik açılan şebit lavaşlarının kat kat dizilip aralarına kıymalı, domatesli, biberli nefis sos sürülerek sarımsaklı yoğurtla sunulan Kayseri klasiği.",
            "en": "Layers of soft thin flatbreads (sebit) stacked tall with savory spiced minced beef & tomato sauce between each layer, sliced and served with garlic yogurt.",
            "es": "Torre de capas de pan plano fino con salsa especiada de carne picada y tomate entre cada capa, servida con yogur al ajo.",
            "de": "Kayseri Schichttorte aus dünnen Fladenbroten, bestrichen mit würziger Hackfleisch-Tomatensauce und garniert mit Knoblauchjoghurt."
        },
        "ingredients": {
            "tr": ["10-12 adet ince şebit/lavaş ekmeği", "500g kıyma", "2 adet soğan, yemeklik doğranmış", "3 adet yeşil sivri biber", "2 adet domates rendesi", "2 yemek kaşığı biber ve domates salçası", "2 yemek kaşığı tereyağı", "Sarımsaklı yoğurt"],
            "en": ["10-12 thin flatbreads (sebit)", "500g minced beef", "2 onions, diced", "3 green peppers", "2 tomatoes, grated", "2 tbsp tomato & pepper paste", "2 tbsp butter", "Garlic yogurt"],
            "es": ["10-12 panes finos sebit", "500g carne picada", "2 cebollas", "3 pimientos verdes", "2 tomates rallados", "2 cdas pasta de tomate", "2 cdas mantequilla", "Yogur al ajo"],
            "de": ["10-12 dünne Fladenbrote", "500g Rinderhack", "2 Zwiebeln", "3 grüne Paprika", "2 geriebene Tomaten", "2 EL Tomaten- & Paprikamark", "2 EL Butter", "Knoblauchjoghurt"]
        },
        "steps": {
            "tr": [
                "Tavada tereyağında kıymayı suyunu çekene kadar kavurun.",
                "Soğan ve biberleri ekleyip 5 dakika kavurun; salça, domates, tuz ve karabiber ilave edip 1 su bardağı suyla 10 dakika sulu bir sos kıvamında pişirin.",
                "Geniş servis tabağına 1 adet lavaş serip üzerine sıcak kıymalı sostan yayın.",
                "Üzerine diğer lavaşı koyup soslayın; bu şekilde 10-12 kat tamamlayın.",
                "Dörde bölüp ortasına sarımsaklı yoğurt dökerek rulo yapıp afiyetle yiyin."
            ],
            "en": [
                "Brown minced meat in butter until juices evaporate.",
                "Add onions, peppers, tomato paste, grated tomatoes, and 1 cup water to make a rich saucy meat mixture.",
                "Lay one flatbread on a serving platter and spoon meat sauce over it.",
                "Stack another flatbread on top and repeat for all 10-12 layers.",
                "Slice into quarters and serve with cool garlic yogurt in the center."
            ],
            "es": [
                "Dorar la carne picada en mantequilla.",
                "Añadir cebolla, pimientos, pasta de tomate y agua para una salsa jugosa.",
                "Colocar un pan en el plato y cubrir con salsa de carne.",
                "Repetir apilando hasta 12 capas.",
                "Cortar en 4 y servir con yogur al ajo en el centro."
            ],
            "de": [
                "Hackfleisch in Butter anbraten.",
                "Zwiebeln, Paprika, Tomatenmark und Wasser zu einer saftigen Sauce einkochen.",
                "Ein Fladenbrot auf eine Platte legen und mit Fleischsauce bestreichen.",
                "So 10-12 Schichten übereinanderstapeln.",
                "Vierteln und mit Knoblauchjoghurt servieren."
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
    
    for dish in new_turkish_dishes:
        if dish["id"] not in existing_ids:
            data["foods"].append(dish)
            added_count += 1
            print(f"Added: {dish['id']} - {dish['name']['tr']}")
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"\nTotal Turkish dishes now: {len(data['foods'])} (Added: {added_count})")
    
    # Also update cuisines.json foodCount for turkish
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
