import subprocess

candidates = [
    # Global Remote Dev Tools & Cloud
    ("Netlify Remote", "netlify.com"),
    ("Retool Remote", "retool.com"),
    ("Linear Remote", "linear.app"),
    ("Notion Remote", "notion.so"),
    ("Figma Remote", "figma.com"),
    ("Railway Remote", "railway.app"),
    ("Render Remote", "render.com"),
    ("Fly.io Remote", "fly.io"),
    ("HashiCorp", "hashicorp.com"),
    ("Twilio Remote", "twilio.com"),
    ("Atlassian Remote", "atlassian.com"),
    ("Coinbase Remote", "coinbase.com"),
    ("Kraken Remote", "kraken.com"),
    ("Chainlink Remote", "chain.link"),
    ("ConsenSys Remote", "consensys.net"),
    # UAE & KSA
    ("Deliveroo UAE", "deliveroo.co.uk"),
    ("Fetchr UAE", "fetchr.us"),
    ("Lenskart UAE", "lenskart.com"),
    ("Aster Healthcare IT", "asterdmhealthcare.com"),
    ("Aramco Digital", "aramco.com"),
    ("SABIC Global", "sabic.com"),
    # Pakistan
    ("SadaPay", "sadapay.pk"),
    ("NayaPay", "nayapay.com"),
    ("Finja", "finja.pk"),
    ("Dukan.pk", "dukan.pk"),
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
