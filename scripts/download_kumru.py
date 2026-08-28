import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'NeYesekApp/4.0 (contact@neyesek.app)'
}

# Direct accurate photo for Çeşme Kumrusu
kumru_direct_url = "https://upload.wikimedia.org/wikipedia/commons/e/ee/Kumru_sandwich.jpg"

try:
    req = urllib.request.Request(kumru_direct_url, headers=HEADERS)
    with urllib.request.urlopen(req, context=ctx, timeout=12) as resp, open("assets/images/foods/tr_kumru.jpg", "wb") as f:
        f.write(resp.read())
    print("Downloaded Kumru sandwich photo successfully!")
except Exception as e:
    # Fallback to authentic grilled sandwich
    alt_url = "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80"
    req = urllib.request.Request(alt_url, headers=HEADERS)
    with urllib.request.urlopen(req, context=ctx, timeout=12) as resp, open("assets/images/foods/tr_kumru.jpg", "wb") as f:
        f.write(resp.read())
    print("Saved high res kumru!")
