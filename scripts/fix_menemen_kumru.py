import shutil
import urllib.request
import urllib.parse
import json
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'NeYesekApp/4.0 (contact@neyesek.app)'
}

# 1. Overwrite tr_menemen.jpg with authentic pan menemen photo
shutil.copy("assets/images/foods/menemen.jpg", "assets/images/foods/tr_menemen.jpg")
print("✓ Fixed tr_menemen.jpg with authentic skillet Menemen photo!")

# 2. Fetch authentic Kumru sandwich
def fetch_wiki_image(title, lang="tr"):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=1000"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, page in pages.items():
                thumb = page.get('thumbnail', {})
                if 'source' in thumb:
                    return thumb['source']
    except Exception as e:
        print("Error:", e)
    return None

kumru_url = fetch_wiki_image("Kumru (sandviç)", "tr")
if kumru_url:
    req = urllib.request.Request(kumru_url, headers=HEADERS)
    with urllib.request.urlopen(req, context=ctx, timeout=12) as resp, open("assets/images/foods/tr_kumru.jpg", "wb") as f:
        f.write(resp.read())
    print("✓ Fixed tr_kumru.jpg with authentic Çeşme Kumrusu photo!")
