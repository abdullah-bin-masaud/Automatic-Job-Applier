import subprocess

domains_to_test = [
    # Saudi Arabia
    ("STC Saudi", "stc.com.sa"),
    ("Elm Saudi", "elm.sa"),
    ("Mozn AI Saudi", "mozn.ai"),
    ("Si-Ware Systems", "si-ware.com"),
    ("Tahakom Saudi", "tahakom.com"),
    ("Ejada KSA", "ejada.com"),
    ("Lean Tech KSA", "leantech.me"),
    ("Tamara KSA", "tamara.co"),
    ("Jahez KSA", "jahez.net"),
    # Dubai / UAE
    ("e& Etisalat UAE", "eand.com"),
    ("MBZUAI UAE", "mbzuai.ac.ae"),
    ("G42 UAE", "g42.ai"),
    ("Bayzat Dubai", "bayzat.com"),
    ("Property Finder", "propertyfinder.ae"),
    ("Swvl Dubai", "swvl.com"),
    ("Kitopi Dubai", "kitopi.com"),
    ("Astra Tech Dubai", "astratech.ae"),
    # Global Remote
    ("Canonical Remote", "canonical.com"),
    ("GitLab Remote", "gitlab.com"),
    ("Automattic Remote", "automattic.com"),
    ("BairesDev Remote", "bairesdev.com"),
    ("Crossover Remote", "crossover.com"),
    ("Turing Remote", "turing.com"),
    ("Andela Remote", "andela.com"),
    ("Remotebase Remote", "remotebase.com"),
    # Pakistan High Value
    ("Zones Pakistan", "zones.com"),
    ("Bentley Systems", "bentley.com"),
    ("Ovex Tech", "ovextech.com"),
    ("LMKT NIC", "lmkt.com"),
    ("Shifa IT", "shifa.com.pk"),
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
