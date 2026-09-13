import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Lenovo\Desktop\Projects\PIC18-Automated-Attendance-System\proteus")
BASE_DIR.mkdir(parents=True, exist_ok=True)

SCHEMATIC_MD = '''# Proteus 8 Design Suite - Automated Attendance System Schematic

## Target Microcontroller
**Microchip PIC18F4550 (40-Pin DIP Package)**

## Complete Bill of Materials (BOM)
| Component ID | Description | Value / Specification | Proteus Library Keyword |
|---|---|---|---|
| U1 | Microcontroller | PIC18F4550 | `PIC18F4550` |
| LCD1 | Alphanumeric Display | 16x2 Character LCD | `LM016L` |
| IR_A | Outer Gate Sensor Pair | Photodiode + 10k pull-up | `PHOTODIODE` / `BUTTON` |
| IR_B | Inner Gate Sensor Pair | Photodiode + 10k pull-up | `PHOTODIODE` / `BUTTON` |
| X1 | Crystal Oscillator | 20.0 MHz | `CRYSTAL` |
| C1, C2 | Oscillator Capacitors | 22 pF Ceramic | `CAP` |
| R1 | Reset Pull-Up | 10 kΩ | `RES` |
| SW_RST | Master Clear Reset | Tactile Pushbutton | `BUTTON` |
| RV1 | LCD Contrast Potentiometer | 10 kΩ Preset | `POT-HG` |
| D1 (Green) | Entry Indicator LED | 5mm LED | `LED-GREEN` |
| D2 (Red) | Exit Indicator LED | 5mm LED | `LED-RED` |
| R2, R3 | Current Limiting Resistors | 330 Ω | `RES` |

## Pin-by-Pin Wiring Interconnect Table

### 1. Power & Oscillator Network
- **Pin 1 (MCLR/VPP):** Connected to SW_RST (to GND) with R1 (10k) pull-up to +5V.
- **Pin 13 (OSC1/CLKI):** Connected to Crystal X1 (Pin 1) + C1 (22pF to GND).
- **Pin 14 (OSC2/CLKO):** Connected to Crystal X1 (Pin 2) + C2 (22pF to GND).
- **Pins 11, 32 (VDD):** Connected to +5V DC Rail.
- **Pins 12, 31 (VSS):** Connected to Ground Rail (GND).

### 2. Bi-Directional Optical Sensors
- **Pin 33 (RB0/INT0):** Connected to Outer Beam Sensor (IR_A) output. Tripped when entering.
- **Pin 34 (RB1/INT1):** Connected to Inner Beam Sensor (IR_B) output. Tripped when exiting.
*(Both lines configured with 10k pull-ups to +5V, normally HIGH, active LOW on beam interruption).*

### 3. 16x2 Character LCD Interface (8-Bit Parallel)
- **Pin 19 (RD0) to Pin 26 (RD7):** Connected to LCD Data lines `D0` through `D7`.
- **Pin 15 (RC0):** Connected to LCD `RS` (Register Select).
- **Pin 16 (RC1):** Connected to LCD `RW` (Read/Write - tied to GND for write-only).
- **Pin 17 (RC2):** Connected to LCD `E` (Enable strobe pulse).
- **LCD Pin 3 (VEE):** Connected to Wiper of RV1 (10k contrast pot).

### 4. Status Visual Indicators
- **Pin 27 (RD4):** Connected through R2 (330Ω) to Green LED (Entry Event Strobe).
- **Pin 28 (RD5):** Connected through R3 (330Ω) to Red LED (Exit Event Strobe).

## Proteus 8 Simulation Setup Instructions
1. Open **Proteus 8 Professional (ISIS Schematic Capture)**.
2. Pick devices using the keywords above and place according to the interconnect table.
3. Double-click the **PIC18F4550** component:
   - Set **Processor Clock Frequency** to `20MHz`.
   - In **Program File**, browse and select the compiled `main.hex` output from MPLAB XC8.
4. For interactive simulation of IR beam breaks, use **interactive logic toggles** or **pushbuttons** tied to RB0 and RB1.
5. Press the **Run Simulation (Play)** button in the lower toolbar.
6. Verify:
   - LCD displays: `Room Occupancy: 0`
   - Triggering RB0 then RB1 increments count to `1` and strobes the Green LED.
   - Triggering RB1 then RB0 decrements count and strobes the Red LED.
'''

(BASE_DIR / "schematic_description.md").write_text(SCHEMATIC_MD.strip() + "\n", encoding="utf-8")
print(f"Created {BASE_DIR / 'schematic_description.md'}")
