import pdfplumber
import os

cv_dir = r"C:\Users\Lenovo\Desktop\CVV'S"
for fname in sorted(os.listdir(cv_dir)):
    if fname.endswith('.pdf'):
        print(f'\n\n========== {fname} ==========')
        with pdfplumber.open(os.path.join(cv_dir, fname)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    print(text)
