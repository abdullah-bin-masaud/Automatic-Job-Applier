import subprocess

domains = [
    ("Timeline Digital", "timelinedigi.com"),
    ("Peace Of Life Tech", "polt.pk"),
    ("Pakistan Single Window", "psw.gov.pk"),
    ("Prisma Tech", "prismatechpk.com"),
    ("Aizvi Consulting", "aizvi.com"),
    ("MIA Group", "mia.com.pk"),
    ("Velosi Integrity", "velosiaims.com"),
    ("SkytechINN", "skytechinn.com"),
    ("Intelsense", "intelsense.ai"),
    ("OCyber", "ocyber.work"),
    ("United Sol", "unitedsol.net"),
    ("CARE Pvt Ltd", "carepvtltd.com"),
    ("Taraz Technologies", "taraztechnologies.com"),
    ("Devomech Solutions", "devomech.com"),
    ("MRS Electronic", "mrs-electronic.com"),
    ("Nayatel", "nayatel.com"),
    ("Systems Limited", "systemsltd.com"),
    ("i2c Inc", "i2cinc.com"),
    ("Ufone HQ", "ufone.com"),
]

print("=== CHECKING MX FOR VERIFIED PAKISTAN TECH FIRMS ===")
valid = []
for name, d in domains:
    out = subprocess.getoutput(f"nslookup -type=mx {d}")
    if "mail exchanger" in out:
        valid.append((name, d))
        print(f"[OK] {name:<25} -> {d}")
    else:
        print(f"[FAIL] {name:<25} -> {d}")

print(f"\nTotal Valid MX: {len(valid)} / {len(domains)}")
