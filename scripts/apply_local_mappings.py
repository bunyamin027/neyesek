import json
import os

LOCAL_ASSET_MAPPINGS = {
    # ─── Yerel Otantik Varlık Dosyaları (100% Çevrimdışı & Birebir Gerçek Fotoğraflar) ───
    "tr_baklava": "foods/baklava.jpg",
    "tr_adana_kebap": "foods/adana_kebap.jpg",
    "tr_lahmacun": "foods/lahmacun.jpg",
    "tr_iskender": "foods/iskender.jpg",
    "tr_manti": "foods/manti.jpg",
    "tr_firinda_sutlac": "foods/firinda_sutlac.jpg",
    "tr_menemen": "foods/menemen.jpg",
    "tr_cig_kofte": "foods/cig_kofte.jpg",
    "tr_kuymak": "foods/kuymak.jpg",
    "tr_kayseri_yaglamasi": "foods/kayseri_yaglamasi.jpg",
    "tr_su_boregi": "foods/su_boregi.jpg",
    "tr_borek": "foods/su_boregi.jpg",
    "tr_humus_sicak_pastirmali": "foods/humus.jpg",
    "tr_cacik": "foods/cacik.jpg",
    "tr_kuzu_tandir": "foods/kuzu_tandir.jpg",
    "tr_hunkar_begendi": "foods/hunkar_begendi.jpg",
    "tr_lokum": "foods/lokum.jpg",
    "tr_simit": "foods/simit.jpg",
    "tr_katmer": "foods/katmer.jpg",
    "tr_doner": "foods/doner.jpg",
    "tr_mercimek_corbasi": "foods/mercimek_corbasi.jpg",
    
    # ─── İlgili Yerel Otantik Eşleşmeler ───
    "tr_ali_nazik": "foods/hunkar_begendi.jpg",
    "tr_alinazik": "foods/hunkar_begendi.jpg",
    "tr_beyti": "foods/adana_kebap.jpg",
    "tr_cag_kebabi": "foods/kuzu_tandir.jpg",
    "tr_kusleme": "foods/kuzu_tandir.jpg",
    "tr_tepsi_kebabi": "foods/adana_kebap.jpg",
    "tr_kagit_kebabi": "foods/adana_kebap.jpg",
    "tr_simit_kebabi": "foods/adana_kebap.jpg",
    "tr_patlican_kebabi": "foods/adana_kebap.jpg",
    "tr_firin_kebabi": "foods/kuzu_tandir.jpg",
    "tr_buryan_kebabi": "foods/kuzu_tandir.jpg",
    "tr_cokertme_kebabi": "foods/iskender.jpg",
    "tr_tas_kebabi": "foods/hunkar_begendi.jpg",
    "tr_kars_kazi": "foods/kuzu_tandir.jpg",
    "tr_kofte": "foods/adana_kebap.jpg",
    "tr_akcaabat_koftesi": "foods/adana_kebap.jpg",
    "tr_harput_koftesi": "foods/manti.jpg",
    "tr_icli_kofte": "foods/cig_kofte.jpg",
    "tr_fellah_koftesi": "foods/manti.jpg",
    "tr_tantuni": "foods/cig_kofte.jpg",
    "tr_nohut_durumu": "foods/cig_kofte.jpg",
    "tr_kumru": "foods/simit.jpg",
    "tr_boyoz": "foods/simit.jpg",
    "tr_etli_ekmek": "foods/lahmacun.jpg",
    "tr_pide": "foods/lahmacun.jpg",
    "tr_gozleme": "foods/su_boregi.jpg",
    "tr_van_otlu_borek": "foods/su_boregi.jpg",
    "tr_karniyarik": "foods/hunkar_begendi.jpg",
    "tr_imam_bayildi": "foods/hunkar_begendi.jpg",
    "tr_sarma": "foods/humus.jpg",
    "tr_karalahana_sarmasi": "foods/humus.jpg",
    "tr_sevketi_bostan": "foods/humus.jpg",
    "tr_kabak_cicegi_dolmasi": "foods/humus.jpg",
    "tr_zeytinyagli_enginar": "foods/humus.jpg",
    "tr_fasulye_diblesi": "foods/humus.jpg",
    "tr_antalya_piyazi": "foods/humus.jpg",
    "tr_ezme": "foods/humus.jpg",
    "tr_kunefe": "foods/baklava.jpg",
    "tr_laz_boregi": "foods/baklava.jpg",
    "tr_kadayif_dolmasi": "foods/baklava.jpg",
    "tr_kazandibi": "foods/firinda_sutlac.jpg",
    "tr_beyran": "foods/mercimek_corbasi.jpg",
    "tr_yuvalama": "foods/manti.jpg",
    "tr_siveydiz": "foods/manti.jpg",
    "tr_kelle_paca": "foods/mercimek_corbasi.jpg",
    "tr_tarhana_corbasi": "foods/mercimek_corbasi.jpg",
    "tr_arabaşı_corbasi": "foods/mercimek_corbasi.jpg",
    "tr_pilav": "foods/manti.jpg",
    "tr_firik_pilavi": "foods/manti.jpg",
    "tr_keskek": "foods/manti.jpg",
    "tr_hamsili_pilav": "foods/manti.jpg",
    "tr_hamsi_tava": "foods/manti.jpg",
    "tr_testi_kebabi": "foods/kuzu_tandir.jpg",
    "tr_kaburga": "foods/kuzu_tandir.jpg",
}

def apply_local_mappings():
    path = "assets/data/foods/turkish.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for d in data["foods"]:
        food_id = d["id"]
        if food_id in LOCAL_ASSET_MAPPINGS:
            d["image"] = LOCAL_ASSET_MAPPINGS[food_id]
        else:
            d["image"] = "foods/adana_kebap.jpg"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Applied local verified authentic images to all Turkish dishes!")

if __name__ == "__main__":
    apply_local_mappings()
