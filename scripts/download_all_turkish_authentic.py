import urllib.request
import urllib.parse
import json
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'NeYesekFoodApp/1.0 (contact@neyesek.app; iOS Turkish Cuisine Recipe Database)'
}

DISH_SEARCHES = {
    "lahmacun.jpg": "Lahmacun",
    "iskender.jpg": "İskender kebap",
    "doner.jpg": "Doner kebab",
    "kofte.jpg": "Köfte Turkish",
    "kunefe.jpg": "Knafeh or Künefe",
    "kazandibi.jpg": "Kazandibi",
    "su_boregi.jpg": "Su böreği",
    "pide.jpg": "Turkish pide",
    "karniyarik.jpg": "Karnıyarık",
    "imam_bayildi.jpg": "İmam bayıldı",
    "sarma.jpg": "Sarma Turkish",
    "kuymak.jpg": "Kuymak or Muhlama",
    "tantuni.jpg": "Tantuni Mersin",
    "cig_kofte.jpg": "Çiğ köfte",
    "cag_kebabi.jpg": "Cağ kebabı",
    "icli_kofte.jpg": "İçli köfte",
    "beyti.jpg": "Beyti kebab",
    "ali_nazik.jpg": "Alinazik kebab",
    "cacik.jpg": "Cacık",
    "pilav.jpg": "Turkish pilav",
    "hamsili_pilav.jpg": "Hamsili pilav",
    "gozleme.jpg": "Gözleme",
    "boyoz.jpg": "Boyoz",
    "kumru.jpg": "Kumru sandwich",
    "katmer.jpg": "Katmer Gaziantep",
    "kadayif_dolmasi.jpg": "Kadayıf dolması",
    "antalya_piyazi.jpg": "Piyaz Antalya",
    "humus.jpg": "Hummus pastirma",
    "kayseri_yaglamasi.jpg": "Kayseri yağlaması",
    "kelle_paca.jpg": "Kelle paça",
    "tarhana.jpg": "Tarhana soup",
    "beyran.jpg": "Beyran soup",
    "yuvalama.jpg": "Yuvalama",
    "sevketi_bostan.jpg": "Şevket-i bostan",
    "cokertme_kebabi.jpg": "Çökertme kebabı",
    "kabak_cicegi.jpg": "Kabak çiçeği dolması",
    "enginar.jpg": "Zeytinyağlı enginar",
    "hamsi_tava.jpg": "Hamsi tava",
    "tepsi_kebabi.jpg": "Tepsi kebabı",
    "patlican_kebabi.jpg": "Patlıcan kebabı",
}

def search_and_download(filename, query):
    if os.path.exists(os.path.join("assets/images/foods", filename)):
        print(f"Already exists: {filename}")
        return True

    # Search on Wikimedia Commons
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrlimit=5&prop=imageinfo&iiprop=url|mime&format=json"
    req = urllib.request.Request(api_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for _, page in pages.items():
                imageinfo = page.get('imageinfo', [])
                if imageinfo:
                    mime = imageinfo[0].get('mime', '')
                    if 'image/jpeg' in mime or 'image/png' in mime:
                        img_url = imageinfo[0].get('url')
                        filepath = os.path.join("assets/images/foods", filename)
                        img_req = urllib.request.Request(img_url, headers=HEADERS)
                        with urllib.request.urlopen(img_req, context=ctx, timeout=15) as img_resp, open(filepath, 'wb') as f:
                            f.write(img_resp.read())
                        size_kb = os.path.getsize(filepath) / 1024
                        print(f"✓ Downloaded {filename} for '{query}' ({size_kb:.1f} KB)")
                        return True
    except Exception as e:
        print(f"✗ Failed {filename} for '{query}': {e}")
    return False

os.makedirs("assets/images/foods", exist_ok=True)
count = 0
for filename, query in DISH_SEARCHES.items():
    if search_and_download(filename, query):
        count += 1

print(f"\nTotal authentic images in assets/images/foods: {len(os.listdir('assets/images/foods'))}")
