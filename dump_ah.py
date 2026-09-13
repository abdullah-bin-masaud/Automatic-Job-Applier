import pdfplumber

for cv in ["CV__A.pdf", "CV__H.pdf"]:
    print(f"\n==================== {cv} ====================")
    with pdfplumber.open(rf"C:\Users\Lenovo\Desktop\CVV'S\{cv}") as pdf:
        for page in pdf.pages:
            print(page.extract_text())
