import os
from pathlib import Path

# ==============================================================================
# PROJECT 6: AI-Medical-Image-Segmentation
# ==============================================================================
DIR_MED = Path(r"C:\Users\Lenovo\Desktop\Projects\AI-Medical-Image-Segmentation")
(DIR_MED / "data").mkdir(parents=True, exist_ok=True)
(DIR_MED / "models").mkdir(parents=True, exist_ok=True)
(DIR_MED / "visualizations").mkdir(parents=True, exist_ok=True)

DATA_GEN_PY = '''"""
Generates synthetic medical MRI slices with simulated anatomical structures and lesion masks.
"""
import numpy as np
import cv2
from pathlib import Path

DATA_DIR = Path(__file__).parent


def generate_synthetic_mri(num_samples: int = 40, img_size: int = 128):
    """Creates synthetic axial brain MRI slices with ground-truth lesion segmentations."""
    images = []
    masks = []

    for i in range(num_samples):
        # 1. Background skull/brain ellipse
        img = np.zeros((img_size, img_size), dtype=np.float32)
        mask = np.zeros((img_size, img_size), dtype=np.float32)

        # Outer skull
        cv2.ellipse(img, (img_size//2, img_size//2), (img_size//2 - 10, img_size//2 - 20), 0, 0, 360, 0.4, -1)
        # Brain parenchyma tissue
        cv2.ellipse(img, (img_size//2, img_size//2), (img_size//2 - 18, img_size//2 - 28), 0, 0, 360, 0.65, -1)
        # Ventricles (dark cerebrospinal fluid)
        cv2.ellipse(img, (img_size//2 - 12, img_size//2), (8, 18), 10, 0, 360, 0.2, -1)
        cv2.ellipse(img, (img_size//2 + 12, img_size//2), (8, 18), -10, 0, 360, 0.2, -1)

        # 2. Add randomized pathological lesion / tumor
        if np.random.rand() > 0.15:  # 85% have lesions
            lx = np.random.randint(img_size//2 - 25, img_size//2 + 25)
            ly = np.random.randint(img_size//2 - 25, img_size//2 + 25)
            lr = np.random.randint(6, 16)
            cv2.circle(img, (lx, ly), lr, 0.95, -1)
            cv2.circle(mask, (lx, ly), lr, 1.0, -1)

        # 3. Add Rician-like noise to image
        noise = np.random.normal(0, 0.04, (img_size, img_size))
        img = np.clip(img + noise, 0.0, 1.0)

        images.append(img)
        masks.append(mask)

    np.save(DATA_DIR / "mri_slices.npy", np.array(images, dtype=np.float32))
    np.save(DATA_DIR / "lesion_masks.npy", np.array(masks, dtype=np.float32))
    print(f"[*] Generated {num_samples} synthetic MRI slices and masks at {DATA_DIR}")


if __name__ == "__main__":
    generate_synthetic_mri()
'''

UNET_PY = '''"""
Lightweight U-Net Convolutional Neural Network for Biomedical Image Segmentation.
Implements encoder-decoder architecture with skip connections.
"""
try:
    import torch
    import torch.nn as nn
except ImportError:
    torch = None
    nn = None

if torch is not None:
    class DoubleConv(nn.Module):
        def __init__(self, in_channels, out_channels):
            super().__init__()
            self.net = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True),
                nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True)
            )

        def forward(self, x):
            return self.net(x)

    class UNet(nn.Module):
        def __init__(self, in_channels=1, num_classes=1):
            super().__init__()
            # Contracting path (Encoder)
            self.inc = DoubleConv(in_channels, 16)
            self.down1 = nn.Sequential(nn.MaxPool2d(2), DoubleConv(16, 32))
            self.down2 = nn.Sequential(nn.MaxPool2d(2), DoubleConv(32, 64))

            # Bottleneck
            self.bottleneck = nn.Sequential(nn.MaxPool2d(2), DoubleConv(64, 128))

            # Expansive path (Decoder)
            self.up1 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
            self.conv_up1 = DoubleConv(128, 64)

            self.up2 = nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2)
            self.conv_up2 = DoubleConv(64, 32)

            self.up3 = nn.ConvTranspose2d(32, 16, kernel_size=2, stride=2)
            self.conv_up3 = DoubleConv(32, 16)

            self.outc = nn.Conv2d(16, num_classes, kernel_size=1)

        def forward(self, x):
            x1 = self.inc(x)
            x2 = self.down1(x1)
            x3 = self.down2(x2)
            xb = self.bottleneck(x3)

            x = self.up1(xb)
            x = self.conv_up1(torch.cat([x, x3], dim=1))

            x = self.up2(x)
            x = self.conv_up2(torch.cat([x, x2], dim=1))

            x = self.up3(x)
            x = self.conv_up3(torch.cat([x, x1], dim=1))

            return torch.sigmoid(self.outc(x))
else:
    class UNet:
        pass
'''

EVALUATE_PY = '''"""
Evaluation metrics: Dice Similarity Coefficient (F1) and Intersection over Union (IoU/Jaccard).
"""
import numpy as np


def dice_coefficient(y_true: np.ndarray, y_pred: np.ndarray, smooth: float = 1e-5) -> float:
    """Computes Dice Similarity Coefficient between ground truth and predicted binary masks."""
    y_true_f = (y_true > 0.5).astype(np.float32).flatten()
    y_pred_f = (y_pred > 0.5).astype(np.float32).flatten()
    intersection = np.sum(y_true_f * y_pred_f)
    return float((2.0 * intersection + smooth) / (np.sum(y_true_f) + np.sum(y_pred_f) + smooth))


def iou_score(y_true: np.ndarray, y_pred: np.ndarray, smooth: float = 1e-5) -> float:
    """Computes Intersection over Union (IoU) metric."""
    y_true_f = (y_true > 0.5).astype(np.float32).flatten()
    y_pred_f = (y_pred > 0.5).astype(np.float32).flatten()
    intersection = np.sum(y_true_f * y_pred_f)
    union = np.sum(y_true_f) + np.sum(y_pred_f) - intersection
    return float((intersection + smooth) / (union + smooth))
'''

TRAIN_PY = '''"""
Medical Image Segmentation Training and Evaluation Pipeline.
"""
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from data.synthetic_medical_generator import generate_synthetic_mri
from models.unet import UNet
from evaluate import dice_coefficient, iou_score

try:
    import torch
    import torch.nn as nn
    import torch.optim as optim
except ImportError:
    torch = None

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

DATA_DIR = Path(__file__).parent / "data"
PLOTS_DIR = Path(__file__).parent / "visualizations"


def run_pipeline():
    print("==================================================================")
    print("  AI-BASED MEDICAL IMAGE SEGMENTATION SYSTEM (U-NET)")
    print("==================================================================")

    # 1. Ensure data exists
    if not (DATA_DIR / "mri_slices.npy").exists():
        generate_synthetic_mri(num_samples=50)

    images = np.load(DATA_DIR / "mri_slices.npy")
    masks = np.load(DATA_DIR / "lesion_masks.npy")

    print(f"[*] Loaded dataset: {images.shape[0]} slices ({images.shape[1]}x{images.shape[2]})")

    if torch is not None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"[*] Training on device: {device}")

        # Split 80/20 train/val
        n_train = int(len(images) * 0.8)
        x_train = torch.tensor(images[:n_train]).unsqueeze(1).to(device)
        y_train = torch.tensor(masks[:n_train]).unsqueeze(1).to(device)
        x_val = torch.tensor(images[n_train:]).unsqueeze(1).to(device)
        y_val = torch.tensor(masks[n_train:]).unsqueeze(1).to(device)

        model = UNet(in_channels=1, num_classes=1).to(device)
        criterion = nn.BCELoss()
        optimizer = optim.Adam(model.parameters(), lr=1e-3)

        print("[*] Training U-Net model for 15 epochs...")
        for epoch in range(1, 16):
            model.train()
            optimizer.zero_grad()
            preds = model(x_train)
            loss = criterion(preds, y_train)
            loss.backward()
            optimizer.step()

            if epoch % 5 == 0 or epoch == 1:
                print(f"    Epoch [{epoch:02d}/15] - BCE Loss: {loss.item():.4f}")

        # Validation
        model.eval()
        with torch.no_grad():
            val_preds = model(x_val).cpu().numpy().squeeze()
            val_true = y_val.cpu().numpy().squeeze()

        dice_scores = [dice_coefficient(val_true[i], val_preds[i]) for i in range(len(val_true))]
        iou_scores = [iou_score(val_true[i], val_preds[i]) for i in range(len(val_true))]

        mean_dice = np.mean(dice_scores)
        mean_iou = np.mean(iou_scores)
        print("\\n" + "=" * 50)
        print(f"  VALIDATION PERFORMANCE METRICS")
        print(f"  Mean Dice Similarity: {mean_dice:.4f}")
        print(f"  Mean IoU (Jaccard) : {mean_iou:.4f}")
        print("=" * 50)

        # Plot qualitative results
        if plt is not None:
            plt.style.use("dark_background")
            fig, axes = plt.subplots(3, 3, figsize=(10, 10))
            for i in range(min(3, len(val_preds))):
                axes[i, 0].imshow(images[n_train + i], cmap="gray")
                axes[i, 0].set_title(f"Raw MRI #{i+1}")
                axes[i, 0].axis("off")

                axes[i, 1].imshow(val_true[i], cmap="magma")
                axes[i, 1].set_title("Ground Truth Mask")
                axes[i, 1].axis("off")

                axes[i, 2].imshow(val_preds[i] > 0.5, cmap="cyan" if hasattr(plt.cm, "cyan") else "viridis")
                axes[i, 2].set_title(f"Predicted (Dice={dice_scores[i]:.2f})")
                axes[i, 2].axis("off")

            plt.tight_layout()
            out_plot = PLOTS_DIR / "segmentation_results.png"
            plt.savefig(out_plot, dpi=150)
            plt.close()
            print(f"[*] Visualized segmentation results saved to: {out_plot}")
    else:
        print("[!] PyTorch not installed. Run 'pip install -r requirements.txt' to execute neural network training.")


if __name__ == "__main__":
    run_pipeline()
'''

MED_REQUIREMENTS = '''torch>=2.0.0
torchvision>=0.15.0
opencv-python>=4.8.0
numpy>=1.24.0
matplotlib>=3.7.0
'''

MED_README = '''# AI-Based Medical Image Segmentation System

A Deep Convolutional Neural Network (U-Net) pipeline for automated region-of-interest (ROI) segmentation of pathological lesions in axial brain MRI scans.

## Architecture
```
Contracting (Encoder)                     Expansive (Decoder)
[ 1x128x128 ]                             [ 1x128x128 Segmentation Mask ]
      |                                                ^
   Conv x2 ------------ (Skip Connection) ---------> Conv x2
      v                                                |
   MaxPool                                           Upsample
   Conv x2 ------------ (Skip Connection) ---------> Conv x2
      v                                                |
   MaxPool                                           Upsample
   Conv x2 ------------ (Skip Connection) ---------> Conv x2
      v                                                |
   MaxPool ------------------------------------------ Bottleneck
```

## Features
- **Encoder-Decoder Architecture:** Lightweight U-Net with contracting feature extraction and expansive skip-connected reconstruction.
- **Biomedical Loss & Metrics:** Formulated with Binary Cross Entropy (BCE) and evaluated using **Dice Similarity Coefficient** and **Intersection over Union (IoU)**.
- **Synthetic MRI Generator:** Procedurally generates realistic tissue parenchyma, ventricles, skull borders, and randomized pathological lesions with Rician noise.
- **Visual Diagnostics:** Automated side-by-side visualization of raw scans, anatomical ground truth, and thresholded network inferences.

## Quickstart
```bash
pip install -r requirements.txt
python train_evaluate.py
```
'''

med_files = {
    "data/synthetic_medical_generator.py": DATA_GEN_PY,
    "models/unet.py": UNET_PY,
    "evaluate.py": EVALUATE_PY,
    "train_evaluate.py": TRAIN_PY,
    "requirements.txt": MED_REQUIREMENTS,
    "README.md": MED_README,
}

for rel, code in med_files.items():
    p = DIR_MED / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(code.strip() + "\n", encoding="utf-8")
    print(f"Created {p}")

print("Project 6 (AI-Medical-Image-Segmentation) files created!")
