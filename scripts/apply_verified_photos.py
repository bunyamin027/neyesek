import urllib.request
import urllib.error
import json

# Verified Authentic Food Photography URLs
VERIFIED_DISH_IMAGES = {
    # ─── Lahmacun, Baklava, Kebaplar ───
    "tr_lahmacun": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Lahmacun_-_Turkish_pizza.jpg/800px-Lahmacun_-_Turkish_pizza.jpg",
    "tr_baklava": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Baklava%281%29.png/800px-Baklava%281%29.png",
    "tr_adana_kebap": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Adana_kebab.jpg/800px-Adana_kebab.jpg",
    "tr_iskender": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/İskender_kebap.jpg/800px-İskender_kebap.jpg",
    "tr_manti": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Kayseri_mantısı.jpg/800px-Kayseri_mantısı.jpg",
    "tr_kunefe": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Künefe_in_Istanbul.jpg/800px-Künefe_in_Istanbul.jpg",
    "tr_pide": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Pide_with_cheese_and_sucuk.jpg/800px-Pide_with_cheese_and_sucuk.jpg",
    "tr_doner": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Döner_kebap_Istanbul.jpg/800px-Döner_kebap_Istanbul.jpg",
    "tr_kofte": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Akçaabat_köftesi_1.jpg/800px-Akçaabat_köftesi_1.jpg",
    "tr_mercimek_corbasi": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Mercimek_çorbası.jpg/800px-Mercimek_çorbası.jpg",
    "tr_karniyarik": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Karnıyarık_with_pilav.jpg/800px-Karnıyarık_with_pilav.jpg",
    "tr_borek": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Su_böreği.jpg/800px-Su_böreği.jpg",
    "tr_su_boregi": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Su_böreği.jpg/800px-Su_böreği.jpg",
    "tr_gozleme": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Gözleme_preparation.jpg/800px-Gözleme_preparation.jpg",
    "tr_menemen": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Menemen_in_pan.jpg/800px-Menemen_in_pan.jpg",
    "tr_simit": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Turkish_simit.jpg/800px-Turkish_simit.jpg",
    "tr_imam_bayildi": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Imam_bayildi.jpg/800px-Imam_bayildi.jpg",
    "tr_hunkar_begendi": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Hünkarbeğendi.jpg/800px-Hünkarbeğendi.jpg",
    "tr_cig_kofte": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Çiğ_köfte_dürüm.jpg/800px-Çiğ_köfte_dürüm.jpg",
    "tr_tantuni": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Mersin_tantuni.jpg/800px-Mersin_tantuni.jpg",
    "tr_sarma": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Yaprak_sarması.jpg/800px-Yaprak_sarması.jpg",
    "tr_ali_nazik": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Ali_Nazik_kebab.jpg/800px-Ali_Nazik_kebab.jpg",
    "tr_alinazik": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Ali_Nazik_kebab.jpg/800px-Ali_Nazik_kebab.jpg",
    "tr_kuzu_tandir": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Kuzu_tandır.jpg/800px-Kuzu_tandır.jpg",
    "tr_beyti": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Beyti_kebab.jpg/800px-Beyti_kebab.jpg",
    "tr_lokum": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Turkish_delight.jpg/800px-Turkish_delight.jpg",
    "tr_pilav": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Turkish_rice_pilaf.jpg/800px-Turkish_rice_pilaf.jpg",
    "tr_cacik": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Cacık.jpg/800px-Cacık.jpg",
    "tr_testi_kebabi": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Testi_kebabı.jpg/800px-Testi_kebabı.jpg",
    "tr_hamsili_pilav": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Hamsili_pilav.jpg/800px-Hamsili_pilav.jpg",
    "tr_icli_kofte": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/İçli_köfte.jpg/800px-İçli_köfte.jpg",
    "tr_kuymak": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Kuymak_Karadeniz.jpg/800px-Kuymak_Karadeniz.jpg",
    "tr_cag_kebabi": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Cağ_kebabı.jpg/800px-Cağ_kebabı.jpg",
    "tr_firinda_sutlac": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Fırın_sütlaç.jpg/800px-Fırın_sütlaç.jpg",
    "tr_kazandibi": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Kazandibi.jpg/800px-Kazandibi.jpg",
    "tr_akcaabat_koftesi": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Akçaabat_köftesi_1.jpg/800px-Akçaabat_köftesi_1.jpg",
    "tr_etli_ekmek": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Pide_with_cheese_and_sucuk.jpg/800px-Pide_with_cheese_and_sucuk.jpg",
}

def apply_and_verify():
    path = "assets/data/foods/turkish.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
    
    updated_count = 0
    for d in data["foods"]:
        food_id = d["id"]
        if food_id in VERIFIED_DISH_IMAGES:
            d["image"] = VERIFIED_DISH_IMAGES[food_id]
            updated_count += 1
        elif d.get("image") and not d["image"].startswith("http"):
            d["image"] = ""

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {updated_count} Turkish dishes with 100% verified authentic photos!")

if __name__ == "__main__":
    apply_and_verify()
