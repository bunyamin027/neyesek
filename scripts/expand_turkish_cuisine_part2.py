import json

more_dishes = [
    {
        "id": "tr_kars_kazi",
        "cuisineId": "turkish",
        "emoji": "🍗",
        "image": "foods/tr_kars_kazi.webp",
        "color": "FFFFA502",
        "prepTime": 30,
        "cookTime": 120,
        "difficulty": "medium",
        "calories": 620,
        "servings": 6,
        "isPremium": False,
        "tags": ["meat", "dinner"],
        "name": {
            "tr": "Fırında Kars Kazı & Bulgur Pilavı",
            "en": "Kars Roasted Goose with Bulgur",
            "es": "Ganso Asado de Kars con Bulgur",
            "de": "Gebratene Kars-Gans mit Bulgur"
        },
        "description": {
            "tr": "Kars'ın dondurucu ayazında kurutulup tuzlanan tescilli kaz etinin fırında nar gibi kızartılması ve kaz suyunda pişen tane tane bulgur pilavı.",
            "en": "Kars's prized wind-cured salt goose slow-roasted until golden and succulent, served over rich bulgur pilaf cooked in goose broth.",
            "es": "Ganso salado y curado al viento de Kars, asado lentamente y servido sobre pilaf de bulgur cocido en su propio jugo.",
            "de": "Kars-Gans, an frostiger Luft gereift, im Ofen knusprig gebraten und auf in Gänseschmalz gekochtem Bulgur-Pilaw serviert."
        },
        "ingredients": {
            "tr": ["1 adet bütün Kars kazı (parçalanmış)", "2 su bardağı iri başbaşı bulgur", "3 su bardağı kaz suyu", "2 yemek kaşığı tereyağı", "Kaya tuzu ve karabiber"],
            "en": ["1 whole Kars cured goose (portioned)", "2 cups coarse bulgur", "3 cups goose cooking broth", "2 tbsp butter", "Rock salt and black pepper"],
            "es": ["1 ganso de Kars troceado", "2 tazas bulgur grueso", "3 tazas caldo de ganso", "2 cdas mantequilla", "Sal marina y pimienta"],
            "de": ["1 Kars-Gans (zerteilt)", "2 Tassen grober Bulgur", "3 Tassen Gänsebrühe", "2 EL Butter", "Steinsalz und Pfeffer"]
        },
        "steps": {
            "tr": [
                "Kaz etini tencerede bol suyla etler yumuşayana kadar yaklaşık 1.5 saat haşlayın, suyunu ayırın.",
                "Haşlanan etleri fırın tepsisine dizip 200°C fırında derisi çıtır çıtır ve altın rengi olana kadar 25-30 dakika kızartın.",
                "Tencerede tereyağında bulguru kavurup süzülmüş sıcak kaz suyunu ekleyin; suyunu çekene kadar pişirip 15 dakika demlendirin.",
                "Geniş tepsiye kaz suyuna doymuş bulgur pilavını yayın, üzerine çıtır kızarmış kaz etlerini dizerek servis yapın."
            ],
            "en": [
                "Boil goose pieces in water for approx 1.5 hours until tender; reserve the flavorful broth.",
                "Place goose pieces in roasting pan and roast at 200°C for 25-30 minutes until skin is deeply golden and crispy.",
                "Cook coarse bulgur in the strained hot goose broth with butter until fluffy; rest 15 minutes.",
                "Spread the savory bulgur across a platter and arrange golden goose pieces on top."
            ],
            "es": [
                "Hervir el ganso 1.5 horas; reservar el caldo.",
                "Hornear a 200°C por 30 min hasta que la piel esté crujiente.",
                "Cocinar el bulgur en el caldo de ganso con mantequilla.",
                "Servir el ganso crujiente sobre el lecho de bulgur."
            ],
            "de": [
                "Gänseteile ca. 1.5 Stunden vorkochen; Brühe auffangen.",
                "Bei 200°C 25-30 Min. knusprig braun braten.",
                "Bulgur in der Gänsebrühe mit Butter ausquellen lassen.",
                "Gans auf dem aromatischen Bulgur anrichten."
            ]
        }
    },
    {
        "id": "tr_buryan_kebabi",
        "cuisineId": "turkish",
        "emoji": "🍖",
        "image": "foods/tr_buryan_kebabi.webp",
        "color": "FFE84545",
        "prepTime": 30,
        "cookTime": 150,
        "difficulty": "hard",
        "calories": 590,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "dinner"],
        "name": {
            "tr": "Bitlis / Siirt Kuyu Büryan Kebabı",
            "en": "Siirt & Bitlis Pit Roasted Buryan Kebab",
            "es": "Kebab Büryan de Pozo de Siirt",
            "de": "Siirt & Bitlis Erdofen Büryan Kebab"
        },
        "description": {
            "tr": "Derin taş kuyu ocaklarında odun ateşinin korunda saatlerce kendi buharı ve yağıyla lokum gibi pişen bütün kuzu eti.",
            "en": "Whole young lamb slowly pit-roasted for hours in deep sealed stone wells with smoldering oak wood, producing intensely juicy, melt-in-mouth meat.",
            "es": "Cordero entero asado lentamente en pozos de piedra sellados con leña de roble, resultando en carne sumamente tierna y jugosa.",
            "de": "Im tiefen gemauerten Erdofen über Eichenglut stundenlang im eigenen Dampf zart geschmortes Lammfleisch."
        },
        "ingredients": {
            "tr": ["1 kg kuzu kaburga ve but eti", "Kaya tuzu", "Tırnak pide ekmeği", "Közlenmiş domates ve biber"],
            "en": ["1 kg lamb ribs & shoulder", "Rock salt", "Fresh tırnak flatbread", "Grilled tomatoes and peppers"],
            "es": ["1 kg costillas y paletilla de cordero", "Sal gorda", "Pan plano tırnak", "Tomates y pimientos asados"],
            "de": ["1 kg Lammrippen und -keule", "Steinsalz", "Pide-Brot", "Gegrillte Tomaten und Paprika"]
        },
        "steps": {
            "tr": [
                "Kuzu etini sadece kaya tuzuyla ovup kancalara asın.",
                "Derin kuyu fırınının dibinde meşe odununu yakıp köz haline getirin.",
                "Etleri kuyunun içine sarkıtıp kapağını çamurla hava almayacak şekilde kapatın; 2.5 saat kendi buharında pişirin.",
                "Lokum gibi pişen eti sıcak tırnak pide üzerine doğrayıp sıcak servis yapın."
            ],
            "en": [
                "Season lamb with rock salt and hang on iron hooks.",
                "Heat deep stone pit with oak wood until embers glow without open flame.",
                "Lower meat into the pit, seal the lid airtight with mud, and slow-roast for 2.5 hours.",
                "Carve succulent meat over fresh flatbread and serve piping hot."
            ],
            "es": [
                "Salar el cordero y colgar en ganchos.",
                "Preparar las brasas de roble en el pozo de piedra.",
                "Bajar la carne, sellar la tapa herméticamente y asar 2.5 horas.",
                "Cortar la carne tierna sobre pan caliente."
            ],
            "de": [
                "Lamm mit Steinsalz einreiben und an Haken hängen.",
                "Im Erdofen Eichenglut vorbereiten.",
                "Fleisch einhängen, Deckel luftdicht verschließen und 2.5 Std. schmoren.",
                "Auf heißem Fladenbrot servieren."
            ]
        }
    },
    {
        "id": "tr_harput_koftesi",
        "cuisineId": "turkish",
        "emoji": "🍲",
        "image": "foods/tr_harput_koftesi.webp",
        "color": "FFE84545",
        "prepTime": 40,
        "cookTime": 25,
        "difficulty": "medium",
        "calories": 420,
        "servings": 4,
        "isPremium": False,
        "tags": ["soup", "meat", "dinner"],
        "name": {
            "tr": "Elazığ Harput Köftesi",
            "en": "Elazig Harput Meatball Soup",
            "es": "Sopa de Albóndigas Harput de Elazığ",
            "de": "Elazig Harput Köfte Suppe"
        },
        "description": {
            "tr": "Elazığ Harput yöresine ait; yağsız kıyma, ince bulgur, reyhan ve baharatlarla yoğrulan minik tekerlek köftelerin salçalı ve tereyağlı nefis sos içinde pişirilmesi.",
            "en": "Traditional Elazig heritage dish of fine bulgur and lean beef dumplings fragrant with wild purple basil (reyhan), simmered in rich tomato-butter broth.",
            "es": "Plato tradicional de Elazığ: albóndigas de bulgur y ternera con albahaca morada cocidas en caldo de tomate a la mantequilla.",
            "de": "Traditionelle Spezialität aus Elazig: Würzige Bulgur-Fleisch-Bällchen mit Purpurbasilikum in butteriger Tomatensauce gekocht."
        },
        "ingredients": {
            "tr": ["400g yağsız dana kıyma", "1.5 su bardağı ince köftelik bulgur", "1 adet rendelenmiş soğan", "2 yemek kaşığı kuru reyhan", "2 yemek kaşığı tereyağı", "2 yemek kaşığı domates ve biber salçası", "Tuz ve pul biber"],
            "en": ["400g lean minced beef", "1.5 cups fine bulgur", "1 grated onion", "2 tbsp dried purple basil (reyhan)", "2 tbsp butter", "2 tbsp tomato & pepper paste", "Salt and chili flakes"],
            "es": ["400g carne picada magra", "1.5 tazas bulgur fino", "1 cebolla rallada", "2 cdas albahaca morada seca", "2 cdas mantequilla", "2 cdas pasta de tomate", "Sal"],
            "de": ["400g mageres Rinderhack", "1.5 Tassen feiner Bulgur", "1 geriebene Zwiebel", "2 EL getrocknetes Purpurbasilikum", "2 EL Butter", "2 EL Tomatenmark", "Salz"]
        },
        "steps": {
            "tr": [
                "Kıyma, bulgur, soğan, bol kuru reyhan ve tuzu hafif su serperek 15 dakika sakız kıvamına gelene kadar yoğurun.",
                "Fındık büyüklüğünde parçalar koparıp yassı yuvarlak tekerlek köfteler yapın.",
                "Tencerede tereyağında salçaları kavurup sıcak su ekleyerek kaynatın.",
                "Kaynayan salçalı suya köfteleri atıp kısık ateşte 15-20 dakika bulgurlar yumuşayana kadar pişirin.",
                "Sıcak çorba kasesinde reyhan aromasıyla servis yapın."
            ],
            "en": [
                "Knead minced beef with bulgur, onion, purple basil, and salt for 15 mins until sticky and smooth.",
                "Shape into small flattened disc-like dumplings.",
                "In a pot, sauté tomato paste in butter and add boiling water to create a rich broth.",
                "Drop dumplings into the simmering broth and cook for 15-20 minutes.",
                "Serve hot in bowls garnished with extra basil."
            ],
            "es": [
                "Amasar la carne con bulgur, cebolla y albahaca morada.",
                "Formar discos pequeños.",
                "Sofreír pasta de tomate en mantequilla y añadir agua hirviendo.",
                "Cocer las albóndigas en el caldo 20 min.",
                "Servir caliente."
            ],
            "de": [
                "Hack mit Bulgur, Zwiebel und Basilikum 15 Min. kneten.",
                "Kleine flache Scheiben formen.",
                "Tomatenmark in Butter anbraten und mit Wasser aufgießen.",
                "Klößchen 15-20 Min. darin gar ziehen lassen.",
                "Heiß servieren."
            ]
        }
    },
    {
        "id": "tr_kadayif_dolmasi",
        "cuisineId": "turkish",
        "emoji": "🥟",
        "image": "foods/tr_kadayif_dolmasi.webp",
        "color": "FFFFA502",
        "prepTime": 25,
        "cookTime": 15,
        "difficulty": "medium",
        "calories": 480,
        "servings": 4,
        "isPremium": False,
        "tags": ["dessert"],
        "name": {
            "tr": "Erzurum Kadayıf Dolması",
            "en": "Erzurum Stuffed Kadayif Rolls",
            "es": "Kadayif Relleno de Erzurum",
            "de": "Erzurum Gefülltes Kadayif-Röllchen"
        },
        "description": {
            "tr": "Taze tel kadayıfın içine bol ceviz içi sarılıp yumurtaya bulanarak çıtır çıtır kızartılması ve soğuk şerbete atılmasıyla yapılan Erzurum'un efsane tatlısı.",
            "en": "Erzurum's iconic dessert: fresh shredded kadayif pastry rolled around crushed walnuts, dipped in whisked eggs, fried golden crisp, and soaked in cold syrup.",
            "es": "Postre emblemático de Erzurum: masa kadayif enrollada con nueces picadas, rebozada en huevo, frita y bañada en almíbar frío.",
            "de": "Berühmtes Erzurum-Dessert: Engelshaar-Teig (Kadayif) gefüllt mit Walnüssen, in Ei gewendet, knusprig frittiert und in kaltem Zuckersirup getränkt."
        },
        "ingredients": {
            "tr": ["400g taze tel kadayıf", "1.5 su bardağı iri kırılmış ceviz içi", "3 adet yumurta", "Kızartmak için sıvı yağ", "Şerbet: 3 su bardağı şeker, 2.5 su bardağı su, 1 dilim limon"],
            "en": ["400g fresh shredded kadayif pastry", "1.5 cups crushed walnuts", "3 eggs, beaten", "Vegetable oil for frying", "Syrup: 3 cups sugar, 2.5 cups water, lemon slice"],
            "es": ["400g masa kadayif fresca", "1.5 tazas nueces picadas", "3 huevos batidos", "Aceite para freír", "Almíbar: 3 tazas azúcar, 2.5 tazas agua, limón"],
            "de": ["400g frischer Kadayif-Teig", "1.5 Tassen Walnüsse", "3 Eier, verquirlt", "Öl zum Frittieren", "Sirup: 3 Tassen Zucker, 2.5 Tassen Wasser, Zitrone"]
        },
        "steps": {
            "tr": [
                "Şerbeti şeker, su ve limonla 15 dakika kaynatıp soğumaya bırakın.",
                "Avuç içi kadar kadayıfı tezgaha açıp ucuna bol ceviz koyun ve sıkı bir rulo (dolma) şeklinde sarın.",
                "Kadayıf dolmalarını çırpılmış yumurtaya bulayıp hafifçe elinizle sıkın.",
                "Kızgın bol sıvı yağda her tarafı nar gibi kızarana kadar pişirin.",
                "Tavadan alır almaz soğuk şerbete atıp 3-4 dakika bekletin ve ılık servis yapın."
            ],
            "en": [
                "Boil sugar, water, and lemon for 15 minutes; let syrup cool completely.",
                "Spread a handful of kadayif, place walnuts on edge, and roll tightly like an egg roll.",
                "Dip each roll into beaten eggs and squeeze gently to hold shape.",
                "Deep-fry in hot oil until deeply golden and crispy on all sides.",
                "Transfer immediately into cold syrup for 3-4 minutes; serve warm and crunchy."
            ],
            "es": [
                "Hervir el almíbar y dejar enfriar.",
                "Extender kadayif, rellenar con nueces y enrollar apretado.",
                "Bañar en huevo batido.",
                "Freír en aceite caliente hasta dorar.",
                "Pasar al almíbar frío 4 min y servir."
            ],
            "de": [
                "Sirup kochen und abkühlen lassen.",
                "Teigstränge auslegen, mit Walnüssen füllen und fest rollen.",
                "In verquirlten Eiern wenden.",
                "In heißem Öl goldbraun frittieren.",
                "Direkt in kalten Sirup tauchen und 3-4 Min. ziehen lassen."
            ]
        }
    },
    {
        "id": "tr_kunefe",
        "cuisineId": "turkish",
        "emoji": "🧀",
        "image": "foods/tr_kunefe.webp",
        "color": "FFFFA502",
        "prepTime": 15,
        "cookTime": 15,
        "difficulty": "medium",
        "calories": 510,
        "servings": 2,
        "isPremium": False,
        "tags": ["dessert", "hatay"],
        "name": {
            "tr": "Hatay Peynirli Künefesi",
            "en": "Hatay Cheese Kunefe",
            "es": "Künefe con Queso de Hatay",
            "de": "Hatay Käse-Künefe"
        },
        "description": {
            "tr": "Tereyağlı çıtır tel kadayıf arasına konulan özel tuzsuz Hatay künefe peynirinin ocakta iki taraflı kızartılıp sıcak şerbet ve Antep fıstığıyla sunumu.",
            "en": "Crispy golden shredded kadayif pastry layered with unsalted melted stringy Hatay cheese, pan-crisped with butter, soaked in hot sugar syrup and dusted with emerald pistachios.",
            "es": "Masa crujiente de kadayif con queso especial de Hatay derretido, dorada a la plancha con mantequilla, bañada en almíbar caliente y pistachos.",
            "de": "Knusprig gebackener Engelshaarteig, gefüllt mit frischem ungesalzenem Hatay-Käse, heiß sirupiert und mit Pistazien bestreut."
        },
        "ingredients": {
            "tr": ["250g taze tel kadayıf", "150g tuzsuz Hatay künefe peyniri (veya dil peyniri)", "100g tereyağı", "Antep fıstığı tozu", "Şerbet: 1.5 su bardağı şeker, 1.5 su bardağı su, birkaç damla limon"],
            "en": ["250g shredded kadayif pastry", "150g unsalted Hatay kunefe cheese", "100g butter", "Crushed pistachios", "Syrup: 1.5 cups sugar, 1.5 cups water, lemon juice"],
            "es": ["250g masa kadayif", "150g queso especial kunefe sin sal", "100g mantequilla", "Pistachos molidos", "Almíbar: 1.5 tazas azúcar, 1.5 tazas agua, limón"],
            "de": ["250g Kadayif-Teig", "150g ungesalzener Kunefe-Käse", "100g Butter", "Pistazien", "Sirup: 1.5 Tassen Zucker, 1.5 Tassen Wasser, Zitrone"]
        },
        "steps": {
            "tr": [
                "Eritilmiş tereyağı ile tel kadayıfları iyice harmanlayıp tel tel ayırın.",
                "Künefe tepsisinin tabanına kadayıfın yarısını bastırarak sıkıca döşeyin.",
                "Üzerine dilimlenmiş peyniri yayın, kalan kadayıfla kapatıp avucunuzla iyice presleyin.",
                "Kısık ocak ateşinde tepsiyi çevirerek tabanı altın sarısı olana kadar 7-8 dakika pişirin, ters çevirip diğer yüzünü de kızartın.",
                "Ocakta sıcakken üzerine ılık şerbeti döküp bol fıstık serperek peyniri uzata uzata sıcak tüketin."
            ],
            "en": [
                "Toss shredded kadayif thoroughly with melted butter.",
                "Press half of the pastry firmly into the bottom of a shallow aluminum pan.",
                "Layer shredded cheese across and cover with remaining pastry, pressing down firmly.",
                "Cook over low flame, rotating pan continuously for 7-8 mins per side until golden brown.",
                "Pour warm syrup over hot pastry, garnish with ground pistachios, and enjoy the cheese pull."
            ],
            "es": [
                "Mezclar el kadayif con mantequilla fundida.",
                "Presionar la mitad en el fondo de la sartén.",
                "Distribuir el queso y cubrir con el resto de masa presionando bien.",
                "Dorar a fuego lento por ambos lados.",
                "Bañar con almíbar caliente y decorar con pistacho."
            ],
            "de": [
                "Kadayif mit geschmolzener Butter zerzupfen.",
                "Hälfte fest in eine Pfanne drücken.",
                "Käse verteilen, restlichen Teig fest daraufpressen.",
                "Auf kleiner Flamme von beiden Seiten goldbraun anbraten.",
                "Mit heißem Sirup übergießen und mit Pistazien heiß servieren."
            ]
        }
    },
    {
        "id": "tr_antalya_piyazi",
        "cuisineId": "turkish",
        "emoji": "🥗",
        "image": "foods/tr_antalya_piyazi.webp",
        "color": "FF2ED573",
        "prepTime": 15,
        "cookTime": 30,
        "difficulty": "easy",
        "calories": 320,
        "servings": 4,
        "isPremium": False,
        "tags": ["vegetarian", "dinner"],
        "name": {
            "tr": "Tahinli Antalya Piyazı",
            "en": "Antalya Tahini White Bean Salad",
            "es": "Ensalada de Alubias con Tahini de Antalya",
            "de": "Antalya Weiße-Bohnen-Salat mit Tahini"
        },
        "description": {
            "tr": "Antalya'nın tescilli ana yemek niteliğindeki piyazı; küçük Çandır kuru fasulyesi, sarımsaklı sirkeli tahin sosu, haşlanmış yumurta ve domatesle sunulur.",
            "en": "Antalya's famous regional salad served with Turkish meatballs: small white beans tossed in a luscious garlicky vinegar-tahini dressing with tomatoes and hard-boiled eggs.",
            "es": "Famosa ensalada de Antalya con alubias blancas pequeñas en cremosa vinagreta de tahini, ajo, huevo duro y tomate.",
            "de": "Antalyas Kult-Bohnensalat: Kleine weiße Bohnen in einem cremigen Knoblauch-Essig-Tahini-Dressing mit Ei und Tomaten."
        },
        "ingredients": {
            "tr": ["2 su bardağı haşlanmış küçük kuru fasulye (Çandır)", "1/2 su bardağı tahin", "1/2 çay bardağı elma sirkesi", "1 limonun suyu", "3 diş sarımsak, ezilmiş", "2 adet haşlanmış yumurta", "2 adet domates", "Maydanoz, sızma zeytinyağı ve tuz"],
            "en": ["2 cups cooked small white beans", "1/2 cup tahini", "1/4 cup apple cider vinegar", "Juice of 1 lemon", "3 cloves garlic, minced", "2 hard-boiled eggs", "2 tomatoes, diced", "Parsley, olive oil, and salt"],
            "es": ["2 tazas alubias blancas cocidas", "1/2 taza tahini", "1/4 taza vinagre", "Jugo de 1 limón", "3 dientes de ajo", "2 huevos duros", "2 tomates", "Perejil y aceite de oliva"],
            "de": ["2 Tassen kleine weiße Bohnen", "1/2 Tasse Tahini", "1/4 Tasse Apfelessig", "Zitronensaft", "3 Knoblauchzehen", "2 gekochte Eier", "2 Tomaten", "Petersilie und Olivenöl"]
        },
        "steps": {
            "tr": [
                "Ilık haşlanmış fasulyeleri servis tabağına alın.",
                "Tahin, sirke, limon suyu, ezilmiş sarımsak, zeytinyağı ve tuzu pürüzsüz akışkan bir sos olana kadar çırpın (gerekirse 2 kaşık ılık su ekleyin).",
                "Tahin sosunu fasulyelerin üzerine bolca döküp harmanlayın.",
                "Üzerini dilimlenmiş domates, haşlanmış yumurta dilimleri ve kıyılmış maydanozla süsleyerek köfte yanında servis edin."
            ],
            "en": [
                "Place warm boiled white beans on a wide serving plate.",
                "Whisk tahini, vinegar, lemon juice, garlic, olive oil, and salt until a smooth creamy dressing forms.",
                "Pour the generous tahini dressing over the beans and mix gently.",
                "Garnish with sliced hard-boiled eggs, fresh tomatoes, and parsley."
            ],
            "es": [
                "Colocar las alubias templadas en el plato.",
                "Batir el tahini con vinagre, limón, ajo y aceite hasta lograr una salsa cremosa.",
                "Verter sobre las alubias.",
                "Decorar con huevo duro en gajos, tomate y perejil."
            ],
            "de": [
                "Warme weiße Bohnen anrichten.",
                "Tahini mit Essig, Zitrone, Knoblauch und Öl cremig rühren.",
                "Dressing großzügig über die Bohnen geben.",
                "Mit Eierspalten, Tomaten und Petersilie garnieren."
            ]
        }
    },
    {
        "id": "tr_kabak_cicegi_dolmasi",
        "cuisineId": "turkish",
        "emoji": "🌼",
        "image": "foods/tr_kabak_cicegi.webp",
        "color": "FF2ED573",
        "prepTime": 30,
        "cookTime": 25,
        "difficulty": "hard",
        "calories": 260,
        "servings": 4,
        "isPremium": False,
        "tags": ["vegetarian", "dinner"],
        "name": {
            "tr": "Zeytinyağlı Kabak Çiçeği Dolması",
            "en": "Aegean Stuffed Squash Blossoms",
            "es": "Flores de Calabacín Rellenas del Egeo",
            "de": "Ägäische Gefüllte Zucchiniblüten"
        },
        "description": {
            "tr": "Ege ve Akdeniz sabahlarının gün doğumunda toplanan narin kabak çiçeklerinin nane, dereotu ve zeytinyağlı aromatik pirinçle doldurulması.",
            "en": "Delicate squash blossoms hand-picked at dawn across Aegean shores, stuffed with aromatic herb rice, pine nuts, and extra virgin olive oil.",
            "es": "Delicadas flores de calabacín recolectadas al amanecer en el Egeo, rellenas de arroz con hierbas aromáticas y aceite de oliva virgen.",
            "de": "Zarte Zucchiniblüten von den Küsten der Ägäis, gefüllt mit duftendem Kräuterreis, Pinienkernen und bestem Olivenöl."
        },
        "ingredients": {
            "tr": ["20 adet taze kabak çiçeği", "1 su bardağı pirinç", "1 adet büyük soğan", "1 yemek kaşığı çam fıstığı", "1 yemek kaşığı kuş üzümü", "1/2 demet dereotu ve taze nane", "1/2 çay bardağı sızma zeytinyağı", "Yenibahar, karabiber, tuz"],
            "en": ["20 fresh squash blossoms", "1 cup rice", "1 onion, finely minced", "1 tbsp pine nuts", "1 tbsp currants", "Fresh dill and mint", "1/4 cup extra virgin olive oil", "Allspice, pepper, salt"],
            "es": ["20 flores de calabacín frescas", "1 taza arroz", "1 cebolla", "1 cda piñones", "1 cda pasas", "Eneldo y menta fresca", "Aceite de oliva virgen", "Especias"],
            "de": ["20 frische Zucchiniblüten", "1 Tasse Reis", "1 Zwiebel", "1 EL Pinienkerne", "1 EL Korinthen", "Dill und Minze", "1/4 Tasse Olivenöl", "Piment und Salz"]
        },
        "steps": {
            "tr": [
                "Kabak çiçeklerinin içindeki sarı tohumcukları zedelemeden dikkatlice çıkarıp yıkayın.",
                "Zeytinyağında soğan ve fıstıkları kavurun; pirinç, kuş üzümü, baharatlar ve yeşilliklerle leziz bir zeytinyağlı iç harç hazırlayın.",
                "Çiçeklerin içine birer tatlı kaşığı harç koyup yapraklarını uçlarından içe doğru katlayarak kapatın.",
                "Tencereye dizip üzerine zeytinyağı, limon suyu ve 1 çay bardağı sıcak su ekleyin.",
                "Kısık ateşte 20-25 dakika pişirip soğuk veya ılık servis yapın."
            ],
            "en": [
                "Gently remove the inner pistils of blossoms without tearing petals; rinse carefully.",
                "Sauté onions and pine nuts in olive oil; mix with rice, currants, herbs, and warm spices.",
                "Spoon a teaspoon of rice mixture into each blossom and fold petal tips inward to seal.",
                "Arrange snugly in a pot, add olive oil, lemon juice, and a splash of water.",
                "Simmer gently for 20-25 mins; serve chilled or room temperature."
            ],
            "es": [
                "Retirar pistilos con cuidado y lavar.",
                "Cocinar el sofrito de arroz con piñones, pasas y hierbas.",
                "Rellenar cada flor y doblar los pétalos hacia dentro.",
                "Cocinar 25 min a fuego lento con aceite y limón.",
                "Servir frío."
            ],
            "de": [
                "Stempel vorsichtig entfernen und Blüten spülen.",
                "Reisfüllung mit Zwiebeln, Pinienkernen und Kräutern anrühren.",
                "Blüten füllen und Blütenblätter einschlagen.",
                "Im Topf mit Olivenöl und Zitrone 20-25 Min. dünsten.",
                "Kalt oder lauwarm servieren."
            ]
        }
    },
    {
        "id": "tr_laz_boregi",
        "cuisineId": "turkish",
        "emoji": "🥧",
        "image": "foods/tr_laz_boregi.webp",
        "color": "FFFFA502",
        "prepTime": 40,
        "cookTime": 35,
        "difficulty": "hard",
        "calories": 440,
        "servings": 6,
        "isPremium": False,
        "tags": ["dessert", "karadeniz"],
        "name": {
            "tr": "Karadeniz Laz Böreği",
            "en": "Black Sea Laz Borek (Custard Filo Pie)",
            "es": "Pastel Laz Böreği del Mar Negro",
            "de": "Schwarzmeer Laz Börek (Pudding-Blätterteig)"
        },
        "description": {
            "tr": "Rize ve Artvin yöresinin tatlı-tuzlu dengesiyle ünlü böreği; tereyağlı çıtır yufkalar arasında karabiberle lezzetlendirilmiş ipeksi muhallebi ve hafif şerbet.",
            "en": "Iconic Black Sea delicacy featuring flaky buttered filo layers stuffed with velvety vanilla custard delicately scented with black pepper, lightly glazed with syrup.",
            "es": "Delicia del Mar Negro con capas de hojaldre crujiente rellenas de natilla cremosa con un sutil toque de pimienta negra y almíbar ligero.",
            "de": "Kultgebäck vom Schwarzen Meer: Knusprige Filoteigschichten mit samtiger Vanille-Puddingfüllung, dezent mit schwarzem Pfeffer gewürzt und sirupiert."
        },
        "ingredients": {
            "tr": ["20 adet baklavalık yufka", "150g eritilmiş tereyağı", "Muhallebi: 1 litre süt, 1 su bardağı şeker, 3 yemek kaşığı un, 2 yemek kaşığı nişasta, 2 yumurta sarısı, 1 çay kaşığı taze çekilmiş karabiber", "Şerbet: 1.5 su bardağı şeker, 1.5 su bardağı su, limon"],
            "en": ["20 sheets filo pastry", "150g melted butter", "Custard: 1L milk, 1 cup sugar, 3 tbsp flour, 2 tbsp starch, 2 egg yolks, 1 tsp black pepper", "Syrup: 1.5 cups sugar, 1.5 cups water, lemon"],
            "es": ["20 hojas de masa filo", "150g mantequilla derretida", "Crema: 1L leche, 1 taza azúcar, 3 cdas harina, 2 yemas, 1 cdta pimienta negra", "Almíbar"],
            "de": ["20 Blatt Filoteig", "150g Butter", "Pudding: 1L Milch, 1 Tasse Zucker, 3 EL Mehl, 2 Eigelb, 1 TL schwarzer Pfeffer", "Sirup"]
        },
        "steps": {
            "tr": [
                "Muhallebi malzemelerini tencerede çırparak koyulaşana kadar pişirin, karabiberi ekleyip ılıtın.",
                "Fırın tepsisine aralarını tereyağı ile yağlayarak 10 kat yufka serin.",
                "Ilık muhallebiyi eşit şekilde yayın.",
                "Kalan 10 kat yufkayı da aralarını yağlayarak üzerine dizin ve kare kare dilimleyin.",
                "180°C fırında üzeri altın sarısı çıtır olana kadar 35 dakika pişirin; fırından çıkınca ılık şerbeti gezdirip servis yapın."
            ],
            "en": [
                "Cook milk, sugar, flour, yolks, and pepper into a thick velvety custard.",
                "Layer 10 sheets of filo in baking dish, brushing each with melted butter.",
                "Spread the warm spiced custard evenly over the pastry base.",
                "Top with remaining 10 buttered filo sheets and slice into squares.",
                "Bake at 180°C for 35 mins until deeply golden; drizzle with warm syrup."
            ],
            "es": [
                "Cocer la crema espesa con pimienta.",
                "Colocar 10 capas de masa filo pincelando con mantequilla.",
                "Extender la crema.",
                "Cubrir con otras 10 capas de masa y cortar en cuadrados.",
                "Hornear 35 min a 180°C y bañar con almíbar."
            ],
            "de": [
                "Puddingcreme mit Pfeffer kochen.",
                "10 gebutterte Teigblätter schichten.",
                "Creme einfüllen.",
                "Mit 10 weiteren gebutterten Blättern abdecken und vorschneiden.",
                "Bei 180°C 35 Min. backen und mit Sirup tränken."
            ]
        }
    },
    {
        "id": "tr_hunkar_begendi",
        "cuisineId": "turkish",
        "emoji": "🥘",
        "image": "foods/tr_hunkar_begendi.webp",
        "color": "FFE84545",
        "prepTime": 30,
        "cookTime": 45,
        "difficulty": "medium",
        "calories": 560,
        "servings": 4,
        "isPremium": False,
        "tags": ["meat", "dinner"],
        "name": {
            "tr": "Osmanlı Saray Usulü Hünkar Beğendi",
            "en": "Sultan's Delight (Hunkar Begendi)",
            "es": "Delicia del Sultán (Hünkar Beğendi)",
            "de": "Des Sultans Wohlgefallen (Hünkar Begendi)"
        },
        "description": {
            "tr": "Osmanlı saray mutfağının başyapıtı; közlenmiş patlıcanlı, kaşarlı ve beşamel soslu enfes 'beğendi' yatağında lokum kıvamında kuzu tas kebabı.",
            "en": "The crowning masterpiece of Ottoman Palace cuisine: melt-in-mouth lamb stew in savory tomato-shallot reduction served over velvety smoked eggplant purée enriched with kaşar cheese.",
            "es": "Obra maestra otomana: estofado tierno de cordero servido sobre suave puré de berenjena ahumada con bechamel y queso.",
            "de": "Kaiserliches osmanisches Hofgericht: Butterweiches Lammgulasch auf samtigem, rauchigem Auberginen-Bechamel-Püree mit Käse."
        },
        "ingredients": {
            "tr": ["600g kuzu kuşbaşı eti", "2 adet soğan", "2 diş sarımsak", "2 adet domates", "1 yemek kaşığı salça", "Beğendi için: 4 adet közlenmiş patlıcan, 2 yemek kaşığı tereyağı, 2 yemek kaşığı un, 1.5 su bardağı süt, 1 su bardağı rendelenmiş kaşar peyniri, muskat rendesi"],
            "en": ["600g cubed lamb", "2 onions", "2 cloves garlic", "2 tomatoes", "1 tbsp tomato paste", "Beğendi: 4 roasted eggplants, 2 tbsp butter, 2 tbsp flour, 1.5 cups milk, 1 cup grated kaşar cheese, pinch nutmeg"],
            "es": ["600g cordero en cubos", "2 cebollas", "2 tomates", "Pasta de tomate", "Puré: 4 berenjenas asadas, 2 cdas mantequilla, 2 cdas harina, 1.5 tazas leche, queso rallado, nuez moscada"],
            "de": ["600g Lammgulasch", "2 Zwiebeln", "2 Tomaten", "Tomatenmark", "Beğendi: 4 gegrillte Auberginen, 2 EL Butter, 2 EL Mehl, 1.5 Tassen Milch, Reibekäse, Muskat"]
        },
        "steps": {
            "tr": [
                "Kuzu etlerini suyunu salıp çekene kadar soteleyin; soğan, sarımsak, salça ve domates ekleyip kısık ateşte et lokum gibi olana kadar 40 dakika pişirin.",
                "Beğendi için: Tereyağında unu hafifçe kavurun, ılık sütü yavaşça ekleyerek pürüzsüz beşamel yapın.",
                "İnce kıyılmış köz patlıcanları, rendelenmiş kaşarı ve muskatı ekleyip peynir eriyene kadar karıştırın.",
                "Tabağa dumanı tüten sıcak beğendiyi yayın, ortasına sulu kuzu tas kebabını yerleştirip servis edin."
            ],
            "en": [
                "Brown lamb cubes with onions, garlic, tomato paste, and tomatoes; simmer gently for 40 minutes until fork-tender.",
                "For Beğendi: make a roux with butter and flour, gradually whisking in milk until smooth and thickened.",
                "Stir in finely chopped smoked eggplant, grated cheese, and a pinch of nutmeg until melted and creamy.",
                "Spoon the velvety eggplant purée onto plates and top with rich, braised lamb."
            ],
            "es": [
                "Cocinar el cordero con cebolla y tomate 40 min.",
                "Hacer bechamel con mantequilla, harina y leche.",
                "Añadir berenjena ahumada picada, queso y nuez moscada.",
                "Servir el estofado sobre la crema de berenjena."
            ],
            "de": [
                "Lammfleisch mit Zwiebeln und Tomaten 40 Min. weichschmoren.",
                "Bechamelsauce aus Butter, Mehl und Milch zubereiten.",
                "Auberginen, Käse und Muskat einrühren.",
                "Fleisch auf dem Auberginenpüree anrichten."
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
    
    for dish in more_dishes:
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
