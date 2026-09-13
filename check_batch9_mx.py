import subprocess

domains_to_test = [
    # Saudi Arabia
    ("Geidea KSA", "geidea.net"),
    ("Foodics KSA", "foodics.com"),
    ("Unifonic KSA", "unifonic.com"),
    ("Salla KSA", "salla.sa"),
    ("Zid KSA", "zid.sa"),
    ("Nearpay KSA", "nearpay.io"),
    # Dubai / UAE
    ("Deriv Dubai", "deriv.com"),
    ("Talabat Dubai", "talabat.com"),
    ("Careem UAE", "careem.com"),
    ("Noon UAE", "noon.com"),
    ("Hub71 Abu Dhabi", "hub71.com"),
    # Pakistan Software & Embedded
    ("Mentor/Siemens EDA", "mentor.com"),
    ("Avanza Solutions", "avanzasolutions.com"),
    ("Autosoft Dynamics", "autosoftdynamics.com"),
    ("TPS Worldwide", "tpsworldwide.com"),
    ("CureMD", "curemd.com"),
    ("Techlogix", "techlogix.com"),
    ("Tkxel", "tkxel.com"),
    ("Confiz", "confiz.com"),
    ("NetSol", "netsoltech.com"),
    # Remote Global
    ("Buffer Remote", "buffer.com"),
    ("Zapier Remote", "zapier.com"),
    ("Doist Remote", "doist.com"),
    ("Toggl Remote", "toggl.com"),
    ("DuckDuckGo Remote", "duckduckgo.com"),
]

valid = []
invalid = []

for name, domain in domains_to_test:
    res = subprocess.getoutput(f"nslookup -type=mx {domain}")
    if "mail exchanger" in res:
        valid.append((name, domain))
        print(f"[MX OK] {name:<25} -> {domain}")
    else:
        invalid.append((name, domain))
        print(f"[MX FAIL] {name:<25} -> {domain}")

print(f"\nTotal Valid MX: {len(valid)} / {len(domains_to_test)}")
