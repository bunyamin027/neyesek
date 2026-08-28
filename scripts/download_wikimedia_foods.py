import urllib.request
import json
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'NeYesekApp/1.0 (contact@neyesek.app; iOS Food Recipe App)'
}

# Real Wikimedia Commons File titles for authentic Turkish dishes
COMMONS_FILES = {
    "baklava.jpg": "File:Baklava(1).png",
    "kunefe.jpg": "File:Künefe in Istanbul.jpg",
    "firinda_sutlac.jpg": "File:Fırın sütlaç.jpg",
    "kazandibi.jpg": "File:Kazandibi.jpg",
    "lokum.jpg": "File:Turkish delight.jpg",
    "adana_kebap.jpg": "File:Adana kebab.jpg",
    "iskender.jpg": "File:İskender kebap.jpg",
    "lahmacun.jpg": "File:Lahmacun - Turkish pizza.jpg",
    "doner.jpg": "File:Döner kebap Istanbul.jpg",
    "kofte.jpg": "File:Akçaabat köftesi 1.jpg",
    "manti.jpg": "File:Kayseri mantısı.jpg",
    "kuzu_tandir.jpg": "File:Kuzu tandır.jpg",
    "beyti.jpg": "File:Beyti kebab.jpg",
    "ali_nazik.jpg": "File:Ali Nazik kebab.jpg",
    "hunkar_begendi.jpg": "File:Hünkarbeğendi.jpg",
    "cag_kebabi.jpg": "File:Cağ kebabı.jpg",
    "icli_kofte.jpg": "File:İçli köfte.jpg",
    "tantuni.jpg": "File:Mersin tantuni.jpg",
    "cig_kofte.jpg": "File:Çiğ köfte dürüm.jpg",
    "pide.jpg": "File:Pide with cheese and sucuk.jpg",
    "su_boregi.jpg": "File:Su böreği.jpg",
    "menemen.jpg": "File:Menemen in pan.jpg",
    "simit.jpg": "File:Turkish simit.jpg",
    "kuymak.jpg": "File:Kuymak Karadeniz.jpg",
    "karniyarik.jpg": "File:Karnıyarık with pilav.jpg",
    "imam_bayildi.jpg": "File:Imam bayildi.jpg",
    "sarma.jpg": "File:Yaprak sarması.jpg",
    "cacik.jpg": "File:Cacık.jpg",
    "pilav.jpg": "File:Turkish rice pilaf.jpg",
    "mercimek_corbasi.jpg": "File:Mercimek çorbası.jpg",
}

def get_direct_url(file_title):
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers=HEADERS)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        for _, page in pages.items():
            imageinfo = page.get('imageinfo', [])
            if imageinfo:
                return imageinfo[0].get('url')
    return None

os.makedirs("assets/images/foods", exist_ok=True)
success = 0
for filename, file_title in COMMONS_FILES.items():
    try:
        direct_url = get_direct_url(file_title)
        if not direct_url:
            print(f"✗ Could not find URL for {file_title}")
            continue
        filepath = os.path.join("assets/images/foods", filename)
        req = urllib.request.Request(direct_url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp, open(filepath, 'wb') as out_f:
            out_f.write(resp.read())
        size_kb = os.path.getsize(filepath) / 1024
        print(f"✓ Downloaded {filename} from {direct_url[:50]}... ({size_kb:.1f} KB)")
        success += 1
    except Exception as e:
        print(f"✗ Error {filename}: {e}")

print(f"\nSuccessfully downloaded: {success}/{len(COMMONS_FILES)}")
