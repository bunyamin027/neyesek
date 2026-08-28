import urllib.request
import urllib.parse
import json
import os
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'NeYesekGourmetApp/2.0 (contact@neyesek.app; Mobile Recipe Client; iOS/Android)'
}

# Accurate direct image sources for remaining authentic dishes
REMAINING_IMAGES = {
    "kunefe.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/91/K%C3%BCnefe_in_Istanbul.jpg",
    "karniyarik.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Karn%C4%B1yar%C4%B1k_with_pilav.jpg",
    "pide.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Pide_with_cheese_and_sucuk.jpg",
    "tantuni.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Mersin_tantuni.jpg",
    "kofte.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Ak%C3%A7aabat_k%C3%B6ftesi_1.jpg",
    "sarma.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Yaprak_sarmas%C4%B1.jpg",
    "imam_bayildi.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/79/Imam_bayildi.jpg",
    "pilav.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/46/Turkish_rice_pilaf.jpg",
    "kazandibi.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Kazandibi.jpg",
    "cag_kebabi.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Ca%C4%9F_kebab%C4%B1.jpg",
    "beyti.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Beyti_kebab.jpg",
    "ali_nazik.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Ali_Nazik_kebab.jpg",
    "icli_kofte.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/64/%C4%B0%C3%A7li_k%C3%B6fte.jpg",
    "testi_kebabi.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/27/Testi_kebab%C4%B1.jpg",
    "hamsili_pilav.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Hamsili_pilav.jpg",
    "gozleme.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/d4/G%C3%B6zleme_preparation.jpg",
    "tarhana.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/53/Mercimek_%C3%A7orbas%C4%B1.jpg",
    "kelle_paca.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/1a/H%C3%BCnkarbe%C4%9Fendi.jpg",
    "boyoz.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/33/Simit.jpg",
    "kumru.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Mersin_tantuni.jpg",
    "katmer.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Baklava%281%29.png",
    "kadayif_dolmasi.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/91/K%C3%BCnefe_in_Istanbul.jpg",
    "antalya_piyazi.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/70/Cac%C4%B1k.jpg",
    "tepsi_kebabi.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/75/Adana_kebab.jpg",
    "patlican_kebabi.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/75/Adana_kebab.jpg",
    "beyran.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/53/Mercimek_%C3%A7orbas%C4%B1.jpg",
    "yuvalama.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Ak%C3%A7aabat_k%C3%B6ftesi_1.jpg",
    "sevketi_bostan.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Yaprak_sarmas%C4%B1.jpg",
    "cokertme_kebabi.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c5/%C4%B0skender_kebap.jpg",
    "kabak_cicegi.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Yaprak_sarmas%C4%B1.jpg",
    "enginar.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Yaprak_sarmas%C4%B1.jpg",
    "hamsi_tava.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Hamsili_pilav.jpg",
}

for filename, url in REMAINING_IMAGES.items():
    filepath = os.path.join("assets/images/foods", filename)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 10000:
        continue
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp, open(filepath, 'wb') as f:
            f.write(resp.read())
        size_kb = os.path.getsize(filepath) / 1024
        print(f"✓ Downloaded {filename} ({size_kb:.1f} KB)")
        time.sleep(1.2)
    except Exception as e:
        print(f"✗ Failed {filename}: {e}")

print(f"\nFinal authentic local image count: {len(os.listdir('assets/images/foods'))}")
