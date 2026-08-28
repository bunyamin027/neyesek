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
    'User-Agent': 'NeYesekApp/1.0 (https://neyesek.app; contact@neyesek.app)'
}

def get_wiki_page_image(title, lang="tr"):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=1000"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, page in pages.items():
                thumb = page.get('thumbnail', {})
                if 'source' in thumb:
                    return thumb['source']
    except Exception as e:
        print(f"Error fetching page image for {title}: {e}")
    return None

img_url = get_wiki_page_image("Tantuni", "tr")
print("Tantuni image URL:", img_url)

if img_url:
    req = urllib.request.Request(img_url, headers=HEADERS)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as resp, open("assets/images/foods/tr_tantuni.jpg", "wb") as f:
        f.write(resp.read())
    print("Saved Tantuni photo! Size:", os.path.getsize("assets/images/foods/tr_tantuni.jpg"))
