# 5‑CV Master Job Applier

A lightweight, **Python‑only** automation that sends personalized job‑application emails using five prepared CVs:

| CV | Target domain |
|----|----------------|
| `CV__A.pdf` | AI / ML / Computer‑Vision / Data‑Science |
| `CV__H.pdf` | Embedded‑systems / Hardware / Lab‑Engineering |
| `CV__T.pdf` | Telecom / Network / NOC |
| `CV__S.pdf` | Software‑Engineering / QA / Backend |
| `CV_E.pdf`  | BPO / Medical‑Billing / Call‑Center / Operations |

The repository contains:
- **Dispatcher scripts** (`pak_batch*_dispatcher.py`) – each script holds a batch of ~20 target companies with a pre‑filled email template and the CV to attach.
- **Master script** (`pak_5cv_master_dispatcher.py`) that runs the batches sequentially.
- **Helper utilities** for cleaning bounce‑back mails, checking SMTP, etc.
- **LaTeX source** for the fifth CV (`Abdullah_Resume_Medical_Billing_CallCenter_BPO.tex`).
- **README** (this file) with clear, field‑specific usage instructions.

---

## Prerequisites

1. **Python 3.9+** (standard library only – no external packages required for the core dispatcher).  
2. A **Gmail app‑password** for the sending address (already used in the scripts: `abdullahmasaud10@gmail.com`).  
3. The five PDF resumes placed inside `CV_DIR` (by default `C:\Users\Lenovo\Desktop\CVV'S`).  
4. Git (for cloning/pushing the repo).

---

## Quick start (run a single batch)

```bash
# Clone the repo (if you haven't already)
git clone https://github.com/abdullah-bin-masaud/automatic-job-applier.git
cd automatic-job-applier

# Verify the CV directory path in the script (default is:
#   C:\Users\Lenovo\Desktop\CVV'S)
# Adjust if needed.

# Run a specific batch, e.g. batch 6 (IT & BPO opportunities)
python pak_batch6_dispatcher.py
```

The script will:
1. Loop over the `TARGETS` list defined inside the file.
2. Build a short subject line (`Job Application - [Role] - Abdullah Bin Masaud`).
3. Choose the appropriate email body (technical **or** BPO style).
4. Attach the mapped PDF.
5. Send via Gmail SMTP (`smtp.gmail.com:465`).
6. Log the outcome to `applied_tracker.csv`.

---

## Running **all** batches automatically

```bash
python pak_5cv_master_dispatcher.py
```

The master script simply imports each batch dispatcher in order and executes them one after another.  It prints a concise summary after each batch (sent / failed counts).

---

## Adding new targets / creating a new batch

1. **Copy an existing dispatcher** (e.g., `pak_batch6_dispatcher.py`) and rename it, e.g. `pak_batch9_dispatcher.py`.
2. Edit the `TARGETS` list – each entry is a Python dict with the following keys:
   - `company` – display name (for logging)
   - `email` – hiring contact address
   - `domain` – one of `AI`, `HARDWARE`, `TELECOM`, `SOFTWARE`, `BPO`
   - `location` – city/region (used only in the email body)
   - `role` – exact job title you are applying for
   - `subject` – custom subject line (or keep the template format)
   - `body_type` – `"TECH"` for the technical template or `"BPO"` for the operations template
   - `focus` – a short phrase describing the skill focus (appears in the body)
3. Save the file and add an import + call to the master script:
   ```python
   import pak_batch9_dispatcher as batch9
   batch9.main()
   ```
4. Commit and push the changes.

---

## Field‑specific notes

- **IT / Software / AI / Telecom** – use the **technical** body (`body_type = "TECH"`). It mentions your final‑year project *VisionAid* and links to your GitHub/LinkedIn.
- **BPO / Medical‑Billing / Call‑Center** – use the **BPO** body (`body_type = "BPO"`). It highlights your Excel/CRM skills, typing speed, and 24/7 shift availability.
- **Lab‑Engineer / Hardware** – attach `CV__H.pdf` and keep `domain = "HARDWARE"`. The body can be either `TECH` (recommended) or a custom one.

---

## Tracker & troubleshooting

All send attempts are appended to `applied_tracker.csv` with the columns:
```
Timestamp,Company,ContactEmail,Domain,Role,Status
```
If a send fails, the exception message is recorded.  You can re‑run a batch; the script will simply try again (the tracker does **not** de‑duplicate automatically – you may filter manually).

Common issues:
- **Authentication error** – double‑check the Gmail app‑password.
- **Rate‑limit / spam block** – keep the 3‑second `sleep` or increase it.
- **Attachment not found** – verify the `CV_DIR` path and that the PDF filenames match exactly.

---

## License & contribution

This project is released under the **MIT License**.  Feel free to fork, adapt the target lists, or add more CVs.

---

**Happy job hunting!**
