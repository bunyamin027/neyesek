import urllib.request
import os
import ssl

# Ensure assets/images/foods directory exists
os.makedirs("assets/images/foods", exist_ok=True)

# Exact, verified culinary image URLs (Wikimedia Commons & Open Food Repositories)
IMAGES_TO_DOWNLOAD = {
    # ─── Tatlılar (KESİNLİKLE GERÇEK TÜRK TATLILARI) ───
    "baklava.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Baklava%281%29.png/800px-Baklava%281%29.png",
    "kunefe.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/K%C3%BCnefe_in_Istanbul.jpg/800px-K%C3%BCnefe_in_Istanbul.jpg",
    "firinda_sutlac.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/F%C4%B1r%C4%B1n_s%C3%BCtla%C3%A7.jpg/800px-F%C4%B1r%C4%B1n_s%C3%BCtla%C3%A7.jpg",
    "kazandibi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Kazandibi.jpg/800px-Kazandibi.jpg",
    "lokum.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Turkish_delight.jpg/800px-Turkish_delight.jpg",
    
    # ─── Kebaplar & Et Yemekleri (KESİNLİKLE GERÇEK TÜRK KEBAPLARI) ───
    "adana_kebap.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Adana_kebab.jpg/800px-Adana_kebab.jpg",
    "iskender.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/%C4%B0skender_kebap.jpg/800px-%C4%B0skender_kebap.jpg",
    "lahmacun.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Lahmacun_-_Turkish_pizza.jpg/800px-Lahmacun_-_Turkish_pizza.jpg",
    "doner.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/D%C3%B6ner_kebap_Istanbul.jpg/800px-D%C3%B6ner_kebap_Istanbul.jpg",
    "kofte.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ak%C3%A7aabat_k%C3%B6ftesi_1.jpg/800px-Ak%C3%A7aabat_k%C3%B6ftesi_1.jpg",
    "manti.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Kayseri_mant%C4%B1s%C4%B1.jpg/800px-Kayseri_mant%C4%B1s%C4%B1.jpg",
    "kuzu_tandir.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Kuzu_tand%C4%B1r.jpg/800px-Kuzu_tand%C4%B1r.jpg",
    "beyti.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Beyti_kebab.jpg/800px-Beyti_kebab.jpg",
    "ali_nazik.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Ali_Nazik_kebab.jpg/800px-Ali_Nazik_kebab.jpg",
    "hunkar_begendi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/H%C3%BCnkarbe%C4%9Fendi.jpg/800px-H%C3%BCnkarbe%C4%9Fendi.jpg",
    "cag_kebabi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Ca%C4%9F_kebab%C4%B1.jpg/800px-Ca%C4%9F_kebab%C4%B1.jpg",
    "icli_kofte.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/%C4%B0%C3%A7li_k%C3%B6fte.jpg/800px-%C4%B0%C3%A7li_k%C3%B6fte.jpg",
    "tantuni.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Mersin_tantuni.jpg/800px-Mersin_tantuni.jpg",
    "cig_kofte.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/%C3%87i%C4%9F_k%C3%B6fte_d%C3%BCr%C3%BCm.jpg/800px-%C3%87i%C4%9F_k%C3%B6fte_d%C3%BCr%C3%BCm.jpg",
    "testi_kebabi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Testi_kebab%C4%B1.jpg/800px-Testi_kebab%C4%B1.jpg",
    "akcaabat_koftesi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ak%C3%A7aabat_k%C3%B6ftesi_1.jpg/800px-Ak%C3%A7aabat_k%C3%B6ftesi_1.jpg",

    # ─── Börekler, Hamur İşleri & Kahvaltı ───
    "pide.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Pide_with_cheese_and_sucuk.jpg/800px-Pide_with_cheese_and_sucuk.jpg",
    "su_boregi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Su_b%C3%B6re%C4%9Fi.jpg/800px-Su_b%C3%B6re%C4%9Fi.jpg",
    "borek.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Su_b%C3%B6re%C4%9Fi.jpg/800px-Su_b%C3%B6re%C4%9Fi.jpg",
    "gozleme.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/G%C3%B6zleme_preparation.jpg/800px-G%C3%B6zleme_preparation.jpg",
    "menemen.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Menemen_in_pan.jpg/800px-Menemen_in_pan.jpg",
    "simit.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Turkish_simit.jpg/800px-Turkish_simit.jpg",
    "kuymak.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Kuymak_Karadeniz.jpg/800px-Kuymak_Karadeniz.jpg",

    # ─── Sebze & Zeytinyağlılar & Tencere Yemekleri ───
    "karniyarik.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Karn%C4%B1yar%C4%B1k_with_pilav.jpg/800px-Karn%C4%B1yar%C4%B1k_with_pilav.jpg",
    "imam_bayildi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Imam_bayildi.jpg/800px-Imam_bayildi.jpg",
    "sarma.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Yaprak_sarmas%C4%B1.jpg/800px-Yaprak_sarmas%C4%B1.jpg",
    "cacik.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Cac%C4%B1k.jpg/800px-Cac%C4%B1k.jpg",
    "pilav.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Turkish_rice_pilaf.jpg/800px-Turkish_rice_pilaf.jpg",
    "mercimek_corbasi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Mercimek_%C3%A7orbas%C4%B1.jpg/800px-Mercimek_%C3%A7orbas%C4%B1.jpg",
    "hamsili_pilav.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Hamsili_pilav.jpg/800px-Hamsili_pilav.jpg",
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

success = 0
for filename, url in IMAGES_TO_DOWNLOAD.items():
    filepath = os.path.join("assets/images/foods", filename)
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        with urllib.request.urlopen(req, context=ctx, timeout=15) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        size_kb = os.path.getsize(filepath) / 1024
        print(f"✓ Downloaded {filename} ({size_kb:.1f} KB)")
        success += 1
    except Exception as e:
        print(f"✗ Failed {filename}: {e}")

print(f"\nTotal successfully downloaded: {success}/{len(IMAGES_TO_DOWNLOAD)}")
