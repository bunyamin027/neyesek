import urllib.request
import urllib.parse
import json
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Wikipedia page titles in Turkish/English to fetch their lead image
WIKI_PAGES = {
    "lahmacun.jpg": ("Lahmacun", "tr"),
    "iskender.jpg": ("İskender kebap", "tr"),
    "doner.jpg": ("Döner", "tr"),
    "kunefe.jpg": ("Künefe", "tr"),
    "su_boregi.jpg": ("Su böreği", "tr"),
    "karniyarik.jpg": ("Karnıyarık", "tr"),
    "pide.jpg": ("Pide", "tr"),
    "tantuni.jpg": ("Tantuni", "tr"),
    "cig_kofte.jpg": ("Çiğ köfte", "tr"),
    "kuymak.jpg": ("Kuymak", "tr"),
    "icli_kofte.jpg": ("İçli köfte", "tr"),
    "sarma.jpg": ("Sarma (yemek)", "tr"),
    "imam_bayildi.jpg": ("İmam bayıldı", "tr"),
    "kofte.jpg": ("Akçaabat köftesi", "tr"),
    "cacik.jpg": ("Cacık", "tr"),
    "pilav.jpg": ("Pilav", "tr"),
    "kazandibi.jpg": ("Kazandibi", "tr"),
    "katmer.jpg": ("Katmer", "tr"),
    "cag_kebabi.jpg": ("Cağ kebabı", "tr"),
    "beyti.jpg": ("Beyti kebabı", "tr"),
    "ali_nazik.jpg": ("Ali Nazik kebabı", "tr"),
    "hamsili_pilav.jpg": ("Hamsili pilav", "tr"),
    "hamsi_tava.jpg": ("Hamsi", "tr"),
    "antalya_piyazi.jpg": ("Antalya piyazı", "tr"),
    "humus.jpg": ("Humus (yemek)", "tr"),
    "kayseri_yaglamasi.jpg": ("Yağlama (yemek)", "tr"),
    "kelle_paca.jpg": ("Kelle paça", "tr"),
    "tarhana.jpg": ("Tarhana çorbası", "tr"),
    "beyran.jpg": ("Beyran", "tr"),
    "yuvalama.jpg": ("Yuvalama", "tr"),
    "sevketi_bostan.jpg": ("Şevket-i bostan", "tr"),
    "cokertme_kebabi.jpg": ("Çökertme kebabı", "tr"),
    "kabak_cicegi.jpg": ("Kabak çiçeği dolması", "tr"),
    "enginar.jpg": ("Enginar", "tr"),
    "tepsi_kebabi.jpg": ("Tepsi kebabı", "tr"),
    "patlican_kebabi.jpg": ("Patlıcan kebabı", "tr"),
    "gozleme.jpg": ("Gözleme", "tr"),
    "boyoz.jpg": ("Boyoz", "tr"),
    "kumru.jpg": ("Kumru (sandviç)", "tr"),
    "kadayif_dolmasi.jpg": ("Kadayıf dolması", "tr"),
}

os.makedirs("assets/images/foods", exist_ok=True)

def fetch_wiki_lead_image(title, lang="tr"):
    api_url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(title)}"
    req = urllib.request.Request(api_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            orig = data.get('originalimage', {})
            if orig and 'source' in orig:
                return orig['source']
            thumb = data.get('thumbnail', {})
            if thumb and 'source' in thumb:
                return thumb['source']
    except Exception as e:
        # Try English fallback
        if lang != "en":
            return fetch_wiki_lead_image(title, "en")
    return None

for filename, (title, lang) in WIKI_PAGES.items():
    filepath = os.path.join("assets/images/foods", filename)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 10000:
        print(f"Skipping already verified {filename}")
        continue
    img_url = fetch_wiki_lead_image(title, lang)
    if img_url:
        try:
            req = urllib.request.Request(img_url, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp, open(filepath, 'wb') as f:
                f.write(resp.read())
            size_kb = os.path.getsize(filepath) / 1024
            print(f"✓ Downloaded {filename} for '{title}' ({size_kb:.1f} KB)")
        except Exception as e:
            print(f"✗ Failed download for {filename}: {e}")
    else:
        print(f"✗ No image found for '{title}'")

print(f"\nFinal count in assets/images/foods: {len(os.listdir('assets/images/foods'))}")
