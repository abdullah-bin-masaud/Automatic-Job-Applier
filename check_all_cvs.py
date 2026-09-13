import pdfplumber
import os

cv_dir = r"C:\Users\Lenovo\Desktop\CVV'S"
for fname in sorted(os.listdir(cv_dir)):
    if fname.endswith(".pdf"):
        print(f"\n==================== {fname} ====================")
        with pdfplumber.open(os.path.join(cv_dir, fname)) as pdf:
            text = "\n".join([p.extract_text() or "" for p in pdf.pages])
            lines = text.split("\n")
            in_proj = False
            for line in lines:
                if "Project" in line:
                    in_proj = True
                elif in_proj and ("Education" in line or "Certifications" in line):
                    in_proj = False
                if in_proj:
                    print("  ", line)
