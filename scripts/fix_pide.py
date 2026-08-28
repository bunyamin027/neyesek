import urllib.request
import urllib.parse
import json
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'NeYesekApp/3.0 (https://neyesek.app; contact@neyesek.app)'
}

def get_wiki_page_image(title, lang="tr"):
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
        print(f"Error {title}: {e}")
    return None

pide_url = get_wiki_page_image("Karadeniz pidesi", "tr") or get_wiki_page_image("Pide (food)", "en")
print("Pide URL:", pide_url)

if pide_url:
    req = urllib.request.Request(pide_url, headers=HEADERS)
    with urllib.request.urlopen(req, context=ctx, timeout=12) as resp, open("assets/images/foods/tr_pide.jpg", "wb") as f:
        f.write(resp.read())
    print("Updated tr_pide.jpg!")
