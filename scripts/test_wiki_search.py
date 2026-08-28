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
    'User-Agent': 'NeYesekApp/1.0 (https://neyesek.app; contact@neyesek.app) Python-urllib/3.11'
}

def search_and_download_wiki_commons(query, target_filepath):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": f"{query}",
        "gsrnamespace": "6", # File namespace
        "gsrlimit": "3",
        "prop": "imageinfo",
        "iiprop": "url|mime|size"
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            raw = resp.read().decode('utf-8')
            data = json.loads(raw)
            pages = data.get('query', {}).get('pages', {})
            for page_id, page in pages.items():
                imageinfo = page.get('imageinfo', [])
                if imageinfo:
                    img_url = imageinfo[0].get('url', '')
                    mime = imageinfo[0].get('mime', '')
                    if img_url and ('jpeg' in mime or 'jpg' in mime or 'png' in mime):
                        time.sleep(1.0)
                        img_req = urllib.request.Request(img_url, headers=HEADERS)
                        with urllib.request.urlopen(img_req, context=ctx, timeout=15) as img_resp, open(target_filepath, 'wb') as f:
                            f.write(img_resp.read())
                        size_kb = os.path.getsize(target_filepath) / 1024
                        print(f"✓ Downloaded '{query}' -> {target_filepath} ({size_kb:.1f} KB)")
                        return True
            print(f"✗ No suitable image in search results for '{query}'")
    except Exception as e:
        print(f"✗ API Error for '{query}': {e}")
    return False

# Test for Tantuni
search_and_download_wiki_commons("Mersin tantuni", "assets/images/foods/tr_tantuni.jpg")
