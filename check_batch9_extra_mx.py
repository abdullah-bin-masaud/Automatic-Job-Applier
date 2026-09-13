import subprocess

candidates = [
    # Saudi Arabia
    ("Tabby KSA & UAE", "tabby.ai"),
    ("HungerStation KSA", "hungerstation.com"),
    ("Bupa Arabia KSA", "bupa.com.sa"),
    ("Alinma Bank KSA", "alinma.com"),
    ("Thiqah KSA", "thiqah.sa"),
    ("SAL Logistics KSA", "sal.sa"),
    # Dubai / UAE
    ("Sarwa Dubai", "sarwa.co"),
    ("Tarabut Gateway", "tarabutgateway.com"),
    ("Postpay Dubai", "postpay.io"),
    ("Grubtech Dubai", "grubtech.com"),
    ("Baraka Dubai", "getbaraka.com"),
    # Pakistan
    ("Gaditek Pakistan", "gaditek.com"),
    ("Genetech Solutions", "genetechsolutions.com"),
    ("Creative Chaos", "creativechaos.co"),
    ("TRG Pakistan", "trgworld.com"),
    # Global Remote Tech
    ("Supabase Remote", "supabase.com"),
    ("Vercel Remote", "vercel.com"),
    ("Postman Remote", "postman.com"),
    ("Elastic Remote", "elastic.co"),
    ("Cloudflare Remote", "cloudflare.com"),
    ("HashiCorp Remote", "hashicorp.com"),
    ("DigitalOcean Remote", "digitalocean.com"),
    ("Stripe Remote", "stripe.com"),
    ("GitHub Remote", "github.com"),
]

valid = []
invalid = []

for name, domain in candidates:
    res = subprocess.getoutput(f"nslookup -type=mx {domain}")
    if "mail exchanger" in res:
        valid.append((name, domain))
        print(f"[MX OK] {name:<25} -> {domain}")
    else:
        invalid.append((name, domain))
        print(f"[MX FAIL] {name:<25} -> {domain}")

print(f"\nTotal Valid MX: {len(valid)} / {len(candidates)}")
