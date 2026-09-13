import subprocess

candidates = [
    # Saudi Arabia
    ("Nana KSA", "nana.sa"),
    ("Mrsool KSA", "mrsool.co"),
    ("Sabbar KSA", "sabbar.com"),
    ("Qoyod KSA", "qoyod.com"),
    ("Floward KSA", "floward.com"),
    # Dubai / UAE
    ("Dubizzle UAE", "dubizzle.com"),
    ("Trukker UAE", "trukker.com"),
    ("Desertcart UAE", "desertcart.com"),
    # Pakistan
    ("Nextbridge", "nextbridge.com"),
    ("Rolustech", "rolustech.com"),
    ("SSI (Strategic Systems)", "ssidecisions.com"),
    ("Tintash", "tintash.com"),
    ("Ebryx", "ebryx.com"),
    ("Zepto Systems", "zeptosystems.com"),
    # Global Remote Tech
    ("Sourcegraph Remote", "sourcegraph.com"),
    ("Grafana Labs Remote", "grafana.com"),
    ("Datadog Remote", "datadoghq.com"),
    ("MongoDB Remote", "mongodb.com"),
    ("Redis Remote", "redis.com"),
    ("Sentry Remote", "sentry.io"),
    ("Docker Remote", "docker.com"),
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
