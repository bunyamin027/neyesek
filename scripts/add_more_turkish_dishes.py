import json

extra_dishes = [
    {
        "id": "tr_patlican_kebabi",
        "cuisineId": "turkish",
        "emoji": "🍆",
        "image": "foods/tr_patlican_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 25,
        "cookTime": 30,
        "difficulty": "medium",
        "calories": 510,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "gaziantep", "grilled"],
        "name": {
            "tr": "Antep / Birecik Patlıcan Kebabı (Balcan Kebabı)",
            "en": "Gaziantep Eggplant Kebab (Balcan)",
            "es": "Kebab de Berenjena de Gaziantep",
            "de": "Gaziantep Auberginen-Kebab (Balcan)"
        },
        "description": {
            "tr": "Gaziantep ve Birecik'in meşhur kebabı; bir dilim taze patlıcan, bir köfte zırh kıyması şeklinde şişe dizilip közde pişirilen, lavaş arasında terletilip soyularak yenen şölen yemeği.",
            "en": "Gaziantep's legendary summer feast: alternating slices of sweet purple eggplant and juicy spiced ground lamb skewered and charcoal-grilled to tender perfection.",
            "es": "Legendario plato veraniego de Gaziantep con rodajas de berenjena intercaladas con albóndigas de cordero asadas al carbón.",
            "de": "Kult-Sommergericht aus Gaziantep: Abwechselnd Auberginenscheiben und gewürztes Lammhack auf Spießen saftig über Holzkohle gegrillt."
        },
        "ingredients": {
            "tr": ["4 adet kemer patlıcan", "600g orta yağlı kuzu zırh kıyması", "1 tatlı kaşığı karabiber", "Kaya tuzu", "Közlemek için domates ve sivri biber", "Tırnak pide ve lavaş"],
            "en": ["4 slender purple eggplants", "600g ground lamb mince", "1 tsp black pepper", "Rock salt", "Tomatoes and peppers for grilling", "Pita and lavash bread"],
            "es": ["4 berenjenas", "600g carne de cordero picada", "1 cdta pimienta negra", "Sal marina", "Tomates y pimientos", "Pan plano"],
            "de": ["4 Auberginen", "600g Lammhackfleisch", "1 TL Pfeffer", "Steinsalz", "Tomaten und Paprika", "Fladenbrot"]
        },
        "steps": {
            "tr": [
                "Kıymayı sadece tuz ve karabiberle yoğurun.",
                "Patlıcanları iki parmak kalınlığında yuvarlak dilimleyin.",
                "Şişe bir dilim patlıcan, bir ceviz büyüklüğünde köfte dizin.",
                "Köz ateşte patlıcanlar yumuşayana ve etler kızarana kadar çevirerek pişirin.",
                "Tepsiye alıp üzerini lavaşla kapatarak 10 dakika terletin; patlıcan kabuklarını soyup sıcak lavaşla dürüm yapın."
            ],
            "en": [
                "Knead minced lamb with rock salt and black pepper.",
                "Cut eggplants into 2-inch thick thick rounds.",
                "Thread alternating eggplant slices and walnut-sized meatballs onto skewers.",
                "Grill over glowing coals, rotating continuously until eggplant is buttery soft.",
                "Rest under warm flatbread for 10 minutes to steam; peel skin and roll into succulent wraps."
            ],
            "es": [
                "Amasar la carne con sal y pimienta.",
                "Cortar las berenjenas en rodajas gruesas.",
                "Insertar en brochetas alternando berenjena y carne.",
                "Asar a las brasas hasta que la berenjena esté tierna.",
                "Dejar reposar 10 min tapado con pan plano antes de servir."
            ],
            "de": [
                "Lammhack mit Salz und Pfeffer verkneten.",
                "Auberginen in dicke Scheiben schneiden.",
                "Abwechselnd Auberginen und Fleischbällchen aufspießen.",
                "Über Glut weich grillen.",
                "10 Min. unter warmem Fladenbrot dämpfen lassen und als Wrap genießen."
            ]
        }
    },
    {
        "id": "tr_simit_kebabi",
        "cuisineId": "turkish",
        "emoji": "🍢",
        "image": "foods/tr_simit_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 25,
        "cookTime": 15,
        "difficulty": "medium",
        "calories": 490,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "gaziantep", "grilled"],
        "name": {
            "tr": "Gaziantep Simit Kebabı (Oruk Kebabı)",
            "en": "Gaziantep Simit Kebab (Bulgur Lamb Skewers)",
            "es": "Kebab Simit de Gaziantep",
            "de": "Gaziantep Simit-Kebab (Bulgur-Lamm-Spieße)"
        },
        "description": {
            "tr": "Gaziantep'te ince bulgura 'simit' denir; zırh kıyması, simit (ince bulgur), taze nane, sarımsak ve Antep fıstığıyla yoğrulup şişte közde pişirilen nefis aromatik kebap.",
            "en": "Authentic Gaziantep specialty combining fine bulgur (locally called simit), ground lamb, fresh mint, garlic, and pine nuts, grilled over open coals.",
            "es": "Especialidad de Gaziantep con bulgur fino (simit), carne picada de cordero, menta fresca y ajo, asada a la brasa en brochetas.",
            "de": "Gaziantep-Klassiker aus feinem Bulgur (Simit), Lammhackfleisch, frischer Minze und Knoblauch auf Spießen gegrillt."
        },
        "ingredients": {
            "tr": ["500g yağlı kuzu kıyma", "1 çay bardağı simit (ince köftelik bulgur)", "1 baş sarımsak, ezilmiş", "1 demet taze nane", "2 yemek kaşığı kuru nane", "1 tatlı kaşığı pul biber ve karabiber", "Tuz ve lavaş"],
            "en": ["500g minced lamb (fatty)", "1/2 cup fine bulgur (simit)", "1 head garlic, minced", "1 bunch fresh mint", "2 tbsp dried mint", "1 tsp chili flakes & black pepper", "Salt and lavash"],
            "es": ["500g carne de cordero picada", "1/2 taza bulgur fino", "1 cabeza de ajo", "Menta fresca y seca", "Pimienta y chile", "Pan lavash"],
            "de": ["500g fettes Lammhack", "1/2 Tasse feiner Bulgur (Simit)", "1 Knoblauchknolle", "Frische und getrocknete Minze", "Pfeffer und Chili", "Fladenbrot"]
        },
        "steps": {
            "tr": [
                "Simiti ılık suyla ıslatıp 10 dakika bekletin.",
                "Kıyma, simit, ezilmiş sarımsak, ince kıyılmış taze nane, kuru nane ve baharatları 15 dakika iyice yoğurun.",
                "Yassı şişlere eti sıkarak dizin.",
                "Kızgın köz ateşinde her iki yüzünü 8-10 dakika sulu kalacak şekilde pişirin.",
                "Taze nane ve sumaklı soğan eşliğinde sıcak servis yapın."
            ],
            "en": [
                "Soak fine bulgur with warm water for 10 minutes.",
                "Knead lamb, bulgur, garlic, chopped fresh mint, dried mint, and spices for 15 minutes.",
                "Shape onto flat metal skewers firmly.",
                "Grill over hot coals for 8-10 minutes keeping it juicy.",
                "Serve with fresh mint leaves, sumac onions, and warm flatbread."
            ],
            "es": [
                "Remojar el bulgur 10 min.",
                "Amasar la carne con bulgur, ajo, menta y especias 15 min.",
                "Montar en brochetas planas.",
                "Asar a las brasas 8-10 min.",
                "Servir con menta fresca y pan plano."
            ],
            "de": [
                "Bulgur 10 Min. einweichen.",
                "Fleisch mit Bulgur, Knoblauch, Minze und Gewürzen 15 Min. verkneten.",
                "Auf flache Spieße formen.",
                "Über Glut 8-10 Min. saftig grillen.",
                "Mit frischer Minze und Zwiebeln servieren."
            ]
        }
    },
    {
        "id": "tr_kagit_kebabi",
        "cuisineId": "turkish",
        "emoji": "📄",
        "image": "foods/tr_kagit_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 20,
        "cookTime": 25,
        "difficulty": "easy",
        "calories": 480,
        "servings": 2,
        "isPremium": False,
        "tags": ["meat", "hatay", "dinner"],
        "name": {
            "tr": "Antakya Kağıt Kebabı",
            "en": "Antakya Paper Kebab",
            "es": "Kebab en Papel de Antakya",
            "de": "Antakya Papier-Kebab"
        },
        "description": {
            "tr": "Antakya taş fırınlarında yağlı kasap kağıdına incecik basılan zırh kıyması, sarımsak ve biber harcının kendi suyunda nar gibi pişmesi.",
            "en": "Antakya's butcher specialty: hand-minced spiced beef & garlic pressed thinly onto parchment paper and baked in stone ovens in its own fragrant juices.",
            "es": "Especialidad de carnicería de Antakya: carne picada especiada extendida sobre papel de horno y horneada en su propio jugo.",
            "de": "Antakya-Spezialität: Auf Backpapier hauchdünn ausgestrichenes gewürztes Rinderhack, im Steinofen im eigenen Saft saftig gegart."
        },
        "ingredients": {
            "tr": ["400g kuzu-dana zırh kıyması", "1 adet kırmızı kapya biber", "4 diş sarımsak", "1/2 demet maydanoz", "Karabiber, kimyon, tuz", "Yağlı kasap kağıdı", "Tırnak pide"],
            "en": ["400g minced beef/lamb", "1 red bell pepper", "4 cloves garlic", "1/2 bunch parsley", "Black pepper, cumin, salt", "Baking parchment paper", "Pita bread"],
            "es": ["400g carne picada", "1 pimiento rojo", "4 dientes de ajo", "Perejil", "Comino, pimienta, sal", "Papel vegetal", "Pan pita"],
            "de": ["400g Rinder-/Lammhack", "1 rote Paprika", "4 Knoblauchzehen", "Petersilie", "Kreuzkümmel, Pfeffer, Salz", "Backpapier", "Pide-Brot"]
        },
        "steps": {
            "tr": [
                "Biber, sarımsak ve maydanozu zırhla incecik kıyıp kıyma ve baharatlarla yoğurun.",
                "Yağlı kağıdı yuvarlak fırın tepsisi boyutunda kesip kıymayı üzerine 0.5 cm inceliğinde yayın.",
                "Üzerine domates ve sivri biber dilimleri yerleştirin.",
                "220°C fırında 20-25 dakika kendi suyunda cızırdayana kadar pişirin.",
                "Kağıdıyla birlikte sıcak sıcak tırnak pide üzerinde servis yapın."
            ],
            "en": [
                "Finely mince red pepper, garlic, and parsley; knead thoroughly with meat and spices.",
                "Cut parchment paper to circle size and press meat onto it in a thin 0.5 cm layer.",
                "Top with tomato wedges and green chili strips.",
                "Bake at 220°C for 20-25 minutes until sizzling in its natural juices.",
                "Serve straight on the paper over warm flatbread."
            ],
            "es": [
                "Picar pimiento, ajo y perejil; amasar con la carne y condimentos.",
                "Extender la carne finamente sobre papel vegetal.",
                "Decorar con tomate y pimiento verde.",
                "Hornear a 220°C por 20-25 min.",
                "Servir directamente sobre el papel con pan caliente."
            ],
            "de": [
                "Paprika, Knoblauch und Petersilie hacken und mit Hackfleisch verkneten.",
                "Hauchdünn auf Backpapier ausstreichen.",
                "Mit Tomaten- und Paprikaspalten belegen.",
                "Bei 220°C ca. 20-25 Min. saftig backen.",
                "Direkt auf dem Papier mit Fladenbrot servieren."
            ]
        }
    },
    {
        "id": "tr_firin_kebabi",
        "cuisineId": "turkish",
        "emoji": "🍖",
        "image": "foods/tr_firin_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 15,
        "cookTime": 240,
        "difficulty": "easy",
        "calories": 610,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "dinner"],
        "name": {
            "tr": "Konya Fırın Kebabı (Taş Fırında Kuzu)",
            "en": "Konya Stone Oven Lamb Kebab",
            "es": "Kebab al Horno de Piedra de Konya",
            "de": "Konya Steinofen Lamm-Kebab"
        },
        "description": {
            "tr": "Konya'nın Selçuklu mirası asırlık lezzeti; kuzu etinin sadece kendi yağı ve tuzuyla meşe odunlu taş fırında bakır leğenlerde 4-5 saat ağır ağır pişerek kemiğinden ayrılması.",
            "en": "Konya's centuries-old Seljuk culinary treasure: succulent lamb shoulder slow-braised in copper cauldrons with oak wood fire for 5 hours until falling off the bone.",
            "es": "Tesoro culinario de Konya: cordero estofado lentamente durante 5 horas en calderos de cobre a fuego de leña hasta quedar ultra tierno.",
            "de": "Jahrhundertealtes Seldschuken-Gericht aus Konya: Lammfleisch im Kupferkessel 5 Stunden über Eichenholz geschmort, bis es butterzart vom Knochen fällt."
        },
        "ingredients": {
            "tr": ["1.5 kg kuzu kol veya gerdan eti", "Kaya tuzu", "Tırnak pide ekmeği", "Kuru soğan ve közlenmiş biber"],
            "en": ["1.5 kg lamb shoulder or neck", "Rock salt", "Pita flatbread", "Raw sweet onions and roasted peppers"],
            "es": ["1.5 kg paletilla o cuello de cordero", "Sal gorda", "Pan plano", "Cebollas y pimientos asados"],
            "de": ["1.5 kg Lammkeule oder -hals", "Steinsalz", "Fladenbrot", "Zwiebeln und gegrillte Paprika"]
        },
        "steps": {
            "tr": [
                "Kuzu etlerini bakır tencereye veya fırın tepsisine dizip sadece kaya tuzu serpin.",
                "Hiç su veya ekstra yağ eklemeden, taş fırında meşe odunu közünde 4-5 saat kendi yağıyla pişirin.",
                "Pişen nar gibi lokum etleri sıcak tırnak pide üzerine yerleştirin.",
                "Yanında kuru soğan, közlenmiş biber ve soğuk yayık ayranıyla servis edin."
            ],
            "en": [
                "Place lamb pieces in a heavy copper pot; sprinkle only with rock salt.",
                "Without adding water or oil, slow-roast in wood-fired oven for 4-5 hours in its natural rendered fat.",
                "Transfer the fork-tender roasted meat over fresh flatbread.",
                "Serve with crisp onions, charred peppers, and iced ayran."
            ],
            "es": [
                "Colocar el cordero en olla de cobre con sal gorda.",
                "Hornear lentamente durante 4-5 horas sin agua añadida.",
                "Colocar la carne tierna sobre pan plano caliente.",
                "Servir con cebolla y pimientos asados."
            ],
            "de": [
                "Lammfleisch in einen Kupfertopf schichten und mit Steinsalz bestreuen.",
                "Ohne Wasserzugabe im Ofen 4-5 Stunden im eigenen Fett butterzart schmoren.",
                "Auf Fladenbrot anrichten.",
                "Mit rohen Zwiebeln und gegrilltem Gemüse servieren."
            ]
        }
    },
    {
        "id": "tr_arabaşı_corbasi",
        "cuisineId": "turkish",
        "emoji": "🥣",
        "image": "foods/tr_arabasi.webp",
        "color": "FFE84545",
        "prepTime": 30,
        "cookTime": 60,
        "difficulty": "medium",
        "calories": 360,
        "servings": 6,
        "isPremium": False,
        "tags": ["soup", "dinner"],
        "name": {
            "tr": "İç Anadolu Arabaşı Çorbası & Hamuru",
            "en": "Central Anatolian Arabasi Soup & Dough",
            "es": "Sopa Arabasi con Masa de Anatolia Central",
            "de": "Zentralanatolische Arabasi-Suppe mit Teig"
        },
        "description": {
            "tr": "İç Anadolu'nun kış gecelerinin simgesi; acı pul biberli ve tereyağlı tavuk/hindi çorbasının yanında özel soğuk ipeksi yutulan hamuruyla tüketilen geleneksel şifa.",
            "en": "Central Anatolia's winter ritual: piping-hot spicy chicken broth with butter and chili, swallowed together with cool silky soft dough without chewing.",
            "es": "Ritual de invierno de Anatolia: caldo picante de pollo servido con una masa fría y sedosa que se ingiere directamente con la sopa.",
            "de": "Wintertradition aus Zentralanatolien: Scharfe Hühnersuppe, die zusammen mit weichem kaltem Teig ohne Kauen geschluckt wird."
        },
        "ingredients": {
            "tr": ["1 adet bütün köy tavuğu (haşlanmış ve didiklenmiş)", "3 yemek kaşığı un", "2 yemek kaşığı tereyağı", "2 yemek kaşığı acı biber salçası", "2 yemek kaşığı acı pul biber", "1 limonun suyu", "Hamuru: 1 su bardağı un, 5 su bardağı su, tuz"],
            "en": ["1 whole chicken (boiled and shredded)", "3 tbsp flour", "2 tbsp butter", "2 tbsp hot pepper paste", "2 tbsp chili flakes", "Juice of 1 lemon", "Dough: 1 cup flour, 5 cups water, salt"],
            "es": ["1 pollo entero hervido y deshebrado", "3 cdas harina", "2 cdas mantequilla", "2 cdas pasta de chile picante", "Jugo de limón", "Masa: 1 taza harina, 5 tazas agua"],
            "de": ["1 Huhn (gekocht und zerzupft)", "3 EL Mehl", "2 EL Butter", "2 EL scharfes Paprikamark", "Chiliflocken", "Zitronensaft", "Teig: 1 Tasse Mehl, 5 Tassen Wasser"]
        },
        "steps": {
            "tr": [
                "Hamur için: Unu suyla pürüzsüz çırpıp ocakta koyulaşana kadar pişirin, ıslatılmış tepsiye döküp soğuyup jöleleşmesi için dinlendirin ve baklava dilimi kesin.",
                "Çorba için: Tereyağında unu hafif kavurun, salça ve pul biber ekleyin.",
                "Haşlanan tavuk suyunu ve didiklenmiş tavuk etlerini ekleyip kısık ateşte 20 dakika kaynatın, bol limon sıkın.",
                "Kaşığa bir parça soğuk hamur alıp kaynar çorbaya batırarak çiğnemeden yutarak tüketin."
            ],
            "en": [
                "For dough: Whisk flour with water and cook until thick and gelatinous; pour into a wet tray, cool until firm, and slice into diamonds.",
                "For soup: Toast flour in butter, stir in pepper paste and generous chili flakes.",
                "Add hot chicken broth and shredded chicken meat; simmer for 20 mins and squeeze lemon juice.",
                "Scoop a cube of cool dough into your spoon, dip into the boiling soup, and swallow together."
            ],
            "es": [
                "Masa: Cocer harina con agua hasta espesar; enfriar en bandeja y cortar en rombos.",
                "Sopa: Tostar harina en mantequilla con pasta de chile.",
                "Añadir caldo de pollo y pollo deshebrado; hervir 20 min con limón.",
                "Tomar un trozo de masa fría en la cuchara y sumergir en la sopa caliente para tragar juntos."
            ],
            "de": [
                "Teig: Mehl mit Wasser aufkochen, auf ein Blech gießen, fest werden lassen und rautenförmig schneiden.",
                "Suppe: Mehl in Butter rösten, Paprikamark zufügen.",
                "Mit Hühnerbrühe aufgießen, Hühnerfleisch zugeben und 20 Min. kochen.",
                "Ein Teigstück auf den Löffel nehmen, in die heiße Suppe tauchen und zusammen schlucken."
            ]
        }
    },
    {
        "id": "tr_kelle_paca",
        "cuisineId": "turkish",
        "emoji": "🥣",
        "image": "foods/tr_kelle_paca.webp",
        "color": "FFE84545",
        "prepTime": 20,
        "cookTime": 180,
        "difficulty": "hard",
        "calories": 490,
        "servings": 4,
        "isPremium": False,
        "tags": ["soup", "meat"],
        "name": {
            "tr": "Geleneksel Kelle Paça Çorbası",
            "en": "Traditional Kelle Paca Soup",
            "es": "Sopa Tradicional Kelle Paça",
            "de": "Traditionelle Kelle Paca Suppe"
        },
        "description": {
            "tr": "Doğal kolajen deposu; saatlerce kaynayan kuzu kelle ve ayak etlerinin sarımsaklı sirke ve kızgın tereyağlı pul biberle harmanlandığı şifa dolu geleneksel lezzet.",
            "en": "Rich collagen-packed powerhouse: slow-simmered lamb head and trotters served with aromatic garlic-vinegar reduction and sizzling chili butter.",
            "es": "Plato reconstituyente rico en colágeno con carne de cabeza y manitas de cordero, aliñado con vinagre al ajo y mantequilla picante.",
            "de": "Kollagenreiche Heilspeise: Stundenlang gekochtes Lammfleisch mit Knoblauch-Essig-Sauce und schäumender Paprikabutter."
        },
        "ingredients": {
            "tr": ["1 adet temizlenmiş kuzu kellesi ve 4 adet paça", "8 diş sarımsak", "1 çay bardağı üzüm sirkesi", "2 yemek kaşığı tereyağı", "1 yemek kaşığı pul biber", "Terbiye: 1 yumurta sarısı, 2 yemek kaşığı un, 1/2 limon suyu", "Kaya tuzu"],
            "en": ["1 cleaned lamb head and trotters", "8 cloves garlic, crushed", "1/2 cup grape vinegar", "2 tbsp butter", "1 tbsp chili flakes", "Liaison: 1 egg yolk, 2 tbsp flour, lemon juice", "Rock salt"],
            "es": ["Cabeza y manitas de cordero limpias", "8 dientes de ajo", "Vinagre de uva", "Mantequilla y chile", "Yema de huevo, harina y limón", "Sal"],
            "de": ["Lammkopf und -füße", "8 Knoblauchzehen", "Traubenessig", "Butter und Chiliflocken", "Eigelb, Mehl, Zitrone", "Steinsalz"]
        },
        "steps": {
            "tr": [
                "Kelle ve paçaları bol suyla düdüklüde etler kemikten kendiliğinden düşene kadar 2.5-3 saat haşlayın.",
                "Etleri ayıklayıp küçük parçalar halinde doğrayın, et suyunu süzün.",
                "Yumurta sarısı, un ve limon suyunu et suyuyla ılıtarak çorbaya ekleyin.",
                "Etleri çorbaya katıp 10 dakika kaynatın.",
                "Bol sarımsaklı sirke ve tavada yakılmış tereyağlı pul biber sosuyla sıcak servis edin."
            ],
            "en": [
                "Boil lamb head and trotters in pressure cooker for 2.5-3 hours until meat slides off bones.",
                "Pick meat clean, dice finely, and strain the gelatinous broth.",
                "Whisk egg yolk, flour, and lemon juice with hot broth to temper and stir into pot.",
                "Simmer meat in the soup for 10 minutes.",
                "Serve piping hot with crushed garlic in vinegar and sizzling chili butter."
            ],
            "es": [
                "Hervir la carne 3 horas hasta que se desprenda del hueso.",
                "Desmenuzar la carne y colar el caldo gelatinoso.",
                "Ligar el caldo con yema, harina y limón.",
                "Añadir la carne y hervir 10 min.",
                "Servir con salsa de ajo en vinagre y mantequilla con chile."
            ],
            "de": [
                "Fleisch ca. 3 Stunden weichkochen.",
                "Entbeinen, zerkleinern und Brühe abseihen.",
                "Brühe mit Eigelb, Mehl und Zitrone legieren.",
                "Fleisch zugeben und 10 Min. ziehen lassen.",
                "Mit Knoblauchessig und Chilibutter heiß genießen."
            ]
        }
    },
    {
        "id": "tr_tarhana_corbasi",
        "cuisineId": "turkish",
        "emoji": "🥣",
        "image": "foods/tr_tarhana.webp",
        "color": "FFFF8C00",
        "prepTime": 10,
        "cookTime": 15,
        "difficulty": "easy",
        "calories": 240,
        "servings": 4,
        "isPremium": False,
        "tags": ["soup", "vegetarian", "dinner"],
        "name": {
            "tr": "Ev Yapımı Köy Tarhana Çorbası",
            "en": "Traditional Village Tarhana Soup",
            "es": "Sopa Tradicional de Tarhana Casera",
            "de": "Traditionelle Dorf-Tarhana-Suppe"
        },
        "description": {
            "tr": "Güneşte kurutulmuş fermente yoğurt, domates, biber ve taze nane tozuyla yapılan, bol tereyağı ve sarımsakla pişen Türk mutfağının en kadim çorbası.",
            "en": "An ancient fermented staple made from sun-dried yogurt, tomatoes, herbs, and flour, simmered with golden butter, garlic, and dried mint.",
            "es": "Sopa ancestral turca a base de yogur fermentado secado al sol, tomate y hierbas, cocida con mantequilla, ajo y menta.",
            "de": "Jahrtausendealte Suppentradition aus sonnengetrocknetem fermentiertem Joghurt, Gemüse und Kräutern, zubereitet mit Knoblauchbutter und Minze."
        },
        "ingredients": {
            "tr": ["4 yemek kaşığı ev yapımı toz tarhana", "1 yemek kaşığı tereyağı", "1 yemek kaşığı domates salçası", "2 diş sarımsak, ezilmiş", "1 tatlı kaşığı kuru nane", "5 su bardağı et veya tavuk suyu", "Tuz ve pul biber"],
            "en": ["4 tbsp dry village tarhana powder", "1 tbsp butter", "1 tbsp tomato paste", "2 cloves garlic, crushed", "1 tsp dried mint", "5 cups chicken or beef broth", "Salt and chili flakes"],
            "es": ["4 cdas tarhana en polvo", "1 cda mantequilla", "1 cda pasta de tomate", "2 dientes de ajo", "Menta seca", "5 tazas caldo", "Sal"],
            "de": ["4 EL Tarhana-Pulver", "1 EL Butter", "1 EL Tomatenmark", "2 Knoblauchzehen", "Getrocknete Minze", "5 Tassen Brühe", "Salz"]
        },
        "steps": {
            "tr": [
                "Toz tarhanayı 1 su bardağı ılık suda 10 dakika ıslatıp çözdürün.",
                "Tencerede tereyağında sarımsak ve salçayı 1 dakika kokusu çıkana kadar kavurun.",
                "Kalan soğuk suyu/et suyunu ve çözünmüş tarhanayı ekleyip tel çırpıcıyla sürekli karıştırarak kaynatın.",
                "Kaynayınca kuru nane ve tuz ekleyip kısık ateşte 5 dakika pişirin.",
                "Kıtır ekmek küpleriyle sıcak servis edin."
            ],
            "en": [
                "Dissolve tarhana powder in 1 cup lukewarm water for 10 minutes.",
                "Melt butter in a saucepan; sauté garlic and tomato paste for 1 minute.",
                "Pour in broth and dissolved tarhana; whisk continuously over medium heat until it comes to a boil.",
                "Stir in dried mint and salt; simmer on low for 5 minutes.",
                "Serve warm with crispy bread croutons."
            ],
            "es": [
                "Disolver la tarhana en 1 taza de agua tibia.",
                "Sofreír el ajo y la pasta de tomate en mantequilla.",
                "Verter el caldo y la tarhana; batir constantemente hasta que hierva.",
                "Añadir menta y sal; cocer 5 min a fuego suave.",
                "Servir con picatostes."
            ],
            "de": [
                "Tarhana in lauwarmem Wasser anrühren.",
                "Knoblauch und Tomatenmark in Butter anschwitzen.",
                "Brühe und Tarhana einrühren, unter ständigem Rühren aufkochen.",
                "Minze zugeben und 5 Min. köcheln lassen.",
                "Mit Croûtons heiß servieren."
            ]
        }
    },
    {
        "id": "tr_su_boregi",
        "cuisineId": "turkish",
        "emoji": "🥟",
        "image": "foods/tr_su_boregi.webp",
        "color": "FFFFA502",
        "prepTime": 45,
        "cookTime": 40,
        "difficulty": "hard",
        "calories": 420,
        "servings": 8,
        "isPremium": False,
        "tags": ["breakfast", "vegetarian", "dinner"],
        "name": {
            "tr": "Geleneksel Tereyağlı Su Böreği",
            "en": "Traditional Butter Water Borek (Su Böreği)",
            "es": "Su Böreği Tradicional a la Mantequilla",
            "de": "Traditionelles Wasser-Börek (Su Böreği)"
        },
        "description": {
            "tr": "El açması taze yufkaların sıcak suda haşlanıp soğuk sudan geçirildikten sonra kat kat eritilmiş tereyağı ve yağlı beyaz peynirle tepside fırınlanması.",
            "en": "The monarch of Turkish pastries: hand-stretched dough sheets blanched in boiling water, layered with melted clarified butter and rich aged white cheese, baked to golden perfection.",
            "es": "El rey de los hojaldres turcos: masa fresca escaldada en agua hirviendo y horneada con mantequilla derretida y queso blanco curado.",
            "de": "Königliche Teigspeise: Hauchdünne Teigblätter in kochendem Wasser blanchiert, mit viel Butter und Schafskäse geschichtet und goldgelb gebacken."
        },
        "ingredients": {
            "tr": ["6 adet elde açılmış börek yufkası", "200g tereyağı (eritilmiş)", "400g yağlı Ezine beyaz peyniri", "1/2 demet maydanoz", "Haşlamak için kaynar tuzlu su ve soğuk su"],
            "en": ["6 large hand-stretched pastry sheets", "200g clarified butter, melted", "400g aged white feta/Ezine cheese", "1/2 bunch parsley", "Boiling salted water and ice bath"],
            "es": ["6 hojas de masa casera", "200g mantequilla clarificada", "400g queso blanco curado", "Perejil fresco", "Agua hirviendo con sal y agua con hielo"],
            "de": ["6 frische Teigblätter", "200g Butterschmalz", "400g Schafskäse (Ezine)", "Petersilie", "Kochendes Salzwasser und Eiswasser"]
        },
        "steps": {
            "tr": [
                "İlk yufkayı haşlamadan yağlanmış fırın tepsisine taban olarak serin ve tereyağı sürün.",
                "Diğer yufkaları sırayla kaynar tuzlu suda 30-40 saniye haşlayıp hemen buzlu suya atın, suyunu süzüp büzüştürerek tepsiye serin ve aralarına tereyağı sürün.",
                "Orta kata çatalla ezilmiş peynir ve kıyılmış maydanozu yayın.",
                "Kalan yufkaları da aynı şekilde haşlayıp tereyağlayarak dizin, en üst yufkayı kuru serin.",
                "Ocakta çevirerek veya 200°C fırında altı ve üstü nar gibi kızarana kadar 35-40 dakika pişirin."
            ],
            "en": [
                "Lay the first unboiled dough sheet in buttered pan and brush with melted butter.",
                "Boil remaining sheets one by one for 30-40 secs, plunge into ice bath, drain, and ruffle into pan with butter between layers.",
                "Spread crumbled cheese and parsley across the middle layer.",
                "Finish remaining layers and top with an unboiled sheet brushed with butter.",
                "Bake at 200°C for 35-40 minutes until golden, flaky, and puffed."
            ],
            "es": [
                "Colocar una masa cruda en la base aceitada.",
                "Escaldar las demás masas 30 seg, enfriar en agua helada y colocar con mantequilla.",
                "Rellenar el centro con queso y perejil.",
                "Cubrir con las capas restantes y hornear a 200°C por 40 min."
            ],
            "de": [
                "Erstes Blatt ungekocht auf das gebutterte Blech legen.",
                "Restliche Blätter 30-40 Sek. kochen, abschrecken und mit Butter schichten.",
                "In der Mitte Käse und Petersilie verteilen.",
                "Fertig schichten und bei 200°C 35-40 Min. backen."
            ]
        }
    },
    {
        "id": "tr_fasulye_diblesi",
        "cuisineId": "turkish",
        "emoji": "🌱",
        "image": "foods/tr_fasulye_diblesi.webp",
        "color": "FF2ED573",
        "prepTime": 20,
        "cookTime": 30,
        "difficulty": "easy",
        "calories": 290,
        "servings": 4,
        "isPremium": False,
        "tags": ["vegetarian", "karadeniz", "dinner"],
        "name": {
            "tr": "Karadeniz Taze Fasulye Diblesi",
            "en": "Black Sea Green Bean Dible",
            "es": "Dible de Judías Verdes del Mar Negro",
            "de": "Schwarzmeer Bohnen-Dible mit Reis"
        },
        "description": {
            "tr": "Giresun ve Trabzon mutfağının vazgeçilmezi; ince doğranmış taze çalı fasulyesi ve pirincin tereyağında kavrulup kendi buharında demlendiği nefis yöresel lezzet.",
            "en": "Black Sea vegetarian favorite: finely sliced fresh green runner beans braised gently with rice, sweet onions, and golden farm butter.",
            "es": "Especialidad vegetariana del Mar Negro con judías verdes finamente cortadas, arroz y mantequilla dorada.",
            "de": "Vegetarischer Klassiker vom Schwarzen Meer aus fein geschnittenen grünen Bohnen, Reis und goldener Bauernbutter."
        },
        "ingredients": {
            "tr": ["1 kg taze çalı fasulye (ince kıyılmış)", "1 çay bardağı baldo pirinç", "2 adet kuru soğan", "3 yemek kaşığı tereyağı", "1 tatlı kaşığı toz şeker", "Tuz ve karabiber"],
            "en": ["1 kg fresh flat runner beans, thinly sliced", "1/2 cup rice", "2 onions, diced", "3 tbsp butter", "1 tsp sugar", "Salt and black pepper"],
            "es": ["1 kg judías verdes planas picadas finas", "1/2 taza arroz", "2 cebollas", "3 cdas mantequilla", "Sal y pimienta"],
            "de": ["1 kg grüne Bohnen, feingehackt", "1/2 Tasse Reis", "2 Zwiebeln", "3 EL Butter", "Salz und Pfeffer"]
        },
        "steps": {
            "tr": [
                "Tencerenin tabanına doğranmış fasulyelerin yarısını yayın.",
                "Üzerine yıkanmış pirinci ve doğranmış soğanları serpiştirin.",
                "Kalan fasulyeleri en üste kapatın.",
                "Tuz, şeker, tereyağı parçaları ve yarım çay bardağı su ekleyip kapağını kapatın.",
                "Kısık ateşte fasulyeler ve pirinç yumuşayana kadar 30 dakika pişirip karıştırarak sıcak/ılık servis yapın."
            ],
            "en": [
                "Layer half of the sliced green beans on the bottom of a wide pot.",
                "Scatter washed rice and diced onions evenly over the beans.",
                "Cover with the remaining sliced green beans.",
                "Add salt, sugar, butter pats, and a tiny splash of water; seal with lid.",
                "Simmer on lowest heat for 30 minutes until beans are tender; stir gently and serve."
            ],
            "es": [
                "Colocar la mitad de judías en el fondo de la olla.",
                "Añadir arroz y cebollas.",
                "Cubrir con el resto de judías.",
                "Añadir mantequilla, sal y un poco de agua; cocer a fuego lento 30 min.",
                "Servir templado."
            ],
            "de": [
                "Hälfte der Bohnen in den Topf schichten.",
                "Reis und Zwiebeln darüber verteilen.",
                "Restliche Bohnen daraufgeben.",
                "Butter, Salz und etwas Wasser zugeben und zugedeckt 30 Min. dünsten.",
                "Umrühren und lauwarm servieren."
            ]
        }
    },
    {
        "id": "tr_zeytinyagli_enginar",
        "cuisineId": "turkish",
        "emoji": "🌿",
        "image": "foods/tr_enginar.webp",
        "color": "FF2ED573",
        "prepTime": 20,
        "cookTime": 30,
        "difficulty": "easy",
        "calories": 220,
        "servings": 4,
        "isPremium": False,
        "tags": ["vegetarian", "dinner"],
        "name": {
            "tr": "Zeytinyağlı Garnitürlü Enginar",
            "en": "Aegean Olive Oil Braised Artichoke Bottoms",
            "es": "Fondos de Alcachofa al Aceite de Oliva",
            "de": "Ägäische Artischockenböden in Olivenöl"
        },
        "description": {
            "tr": "Ege mutfağının karaciğer dostu şifalı yemeği; çanak enginarların taze havuç, patates, bezelye ve portakallı zeytinyağı sosunda pişirilip taze dereotuyla sunumu.",
            "en": "Aegean culinary crown jewel: whole artichoke hearts braised in extra virgin olive oil and fresh orange juice, crowned with spring peas, carrots, potatoes, and fresh dill.",
            "es": "Especialidad del Egeo: corazones de alcachofa cocidos con aceite de oliva virgen y jugo de naranja, rellenos de guisantes, zanahoria y eneldo.",
            "de": "Ägäisches Meisterwerk: Zarte Artischockenböden in nativem Olivenöl und Orangensaft pochiert, gefüllt mit Frühlingsgemüse und frischem Dill."
        },
        "ingredients": {
            "tr": ["4 adet soyulmuş çanak enginar", "1 su bardağı garnitür (bezelye, küp havuç, patates)", "1 adet taze portakal suyu", "1/2 limon suyu", "1/2 çay bardağı sızma zeytinyağı", "1 tatlı kaşığı toz şeker", "1 demet taze dereotu", "Tuz"],
            "en": ["4 cleaned artichoke hearts", "1 cup diced peas, carrots & potatoes", "Juice of 1 fresh orange", "Juice of 1/2 lemon", "1/4 cup extra virgin olive oil", "1 tsp sugar", "Fresh dill", "Salt"],
            "es": ["4 fondos de alcachofa", "1 taza guisantes, zanahorias y patatas", "Jugo de 1 naranja", "Jugo de limón", "Aceite de oliva virgen", "Eneldo fresco y sal"],
            "de": ["4 Artischockenböden", "1 Tasse Erbsen, Karotten und Kartoffeln", "Saft von 1 Orange", "Zitronensaft", "1/4 Tasse Olivenöl", "Frischer Dill und Salz"]
        },
        "steps": {
            "tr": [
                "Enginar çanaklarını limonlu suda bekletip geniş bir yayvan tencereye dizin.",
                "Çanakların ortasına haşlanmış garnitürleri doldurun.",
                "Portakal suyu, limon suyu, sızma zeytinyağı, şeker ve tuzu çırpıp tencereye dökün.",
                "Kısık ateşte enginarlar çatal batacak kadar yumuşayana kadar 25-30 dakika pişirin.",
                "Oda sıcaklığında soğutup üzerine bol taze dereotu serperek soğuk servis yapın."
            ],
            "en": [
                "Place cleaned artichoke hearts hollow-side up in a shallow pan.",
                "Fill each center with diced vegetable medley.",
                "Whisk orange juice, lemon juice, olive oil, sugar, and salt; pour over artichokes.",
                "Cover and simmer on low heat for 25-30 minutes until fork-tender.",
                "Cool to room temperature, top with fresh dill, and serve chilled."
            ],
            "es": [
                "Colocar los fondos de alcachofa en la sartén.",
                "Rellenar el centro con verduras en cubos.",
                "Bañar con jugo de naranja, limón y aceite de oliva.",
                "Cocer 25-30 min a fuego lento.",
                "Enfriar y servir con eneldo fresco."
            ],
            "de": [
                "Artischockenböden in den Topf setzen.",
                "Mit gewürfeltem Gemüse füllen.",
                "Mit Orangen-Zitronen-Olivenöl-Sud übergießen.",
                "Zugedeckt 25-30 Min. garen.",
                "Abkühlen lassen und mit reichlich Dill servieren."
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
    
    for dish in extra_dishes:
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
