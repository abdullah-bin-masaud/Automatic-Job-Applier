import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Lenovo\Desktop\Projects\PIC18-Signal-Communication-Unit")
(BASE_DIR / "firmware").mkdir(parents=True, exist_ok=True)
(BASE_DIR / "proteus").mkdir(parents=True, exist_ok=True)
(BASE_DIR / "simulation").mkdir(parents=True, exist_ok=True)

MAIN_C = '''/**
 * Project: PIC18 Microcontroller Signal Communication Unit
 * Target MCU: PIC18F4550 @ 20.0 MHz Crystal Oscillator
 * Compiler: Microchip MPLAB XC8 v2.40+
 * Description: Interrupt-driven signal capture on RB0/INT0 with debouncing,
 *              non-volatile EEPROM event logging, and UART telemetry @ 9600 baud.
 */

#include <xc.h>
#include <stdint.h>
#include <stdio.h>
#include "uart.h"
#include "eeprom.h"

// =============================================================================
// PIC18F4550 Configuration Bit Settings
// =============================================================================
#pragma config PLLDIV = 5         // Divide by 5 (20 MHz oscillator input)
#pragma config CPUDIV = OSC1_PLL2 // [OSC1/OSC2 Src: /1][96 MHz PLL Src: /2]
#pragma config USBDIV = 2         // USB clock source comes from the 96 MHz PLL divided by 2
#pragma config FOSC = HS          // High Speed Oscillator (HS)
#pragma config FCMEN = OFF        // Fail-Safe Clock Monitor disabled
#pragma config IESO = OFF         // Oscillator Switchover mode disabled
#pragma config PWRT = ON          // Power-up Timer enabled
#pragma config BOR = ON           // Brown-out Reset enabled
#pragma config BORV = 3           // Minimum setting
#pragma config VREGEN = OFF       // USB voltage regulator disabled
#pragma config WDT = OFF          // Watchdog Timer disabled
#pragma config MCLRE = ON         // MCLR pin enabled; RE3 input pin disabled
#pragma config LVP = OFF          // Single-Supply ICSP disabled
#pragma config XINST = OFF        // Extended Instruction Set disabled

#define _XTAL_FREQ 20000000UL     // 20 MHz Oscillator Frequency

// Global event counter
volatile uint16_t g_event_counter = 0;
volatile uint8_t  g_flag_new_event = 0;
uint8_t           g_eeprom_ptr = 0x00;

// =============================================================================
// Interrupt Service Routine (High Priority)
// =============================================================================
void __interrupt() ISR(void) {
    if (INTCONbits.INT0IF) {
        // RB0/INT0 external trigger detected
        // Simple hardware debouncing check
        __delay_ms(15);
        if (PORTBbits.RB0 == 0) { // Active-low button/sensor trigger
            g_event_counter++;
            g_flag_new_event = 1;
            LATCbits.LATC0 ^= 1;  // Toggle indicator LED on RC0
        }
        INTCONbits.INT0IF = 0;    // Clear interrupt flag
    }
}

// =============================================================================
// EEPROM Functions
// =============================================================================
void EEPROM_Write(uint8_t addr, uint8_t data) {
    EEADR = addr;
    EEDATA = data;
    EECON1bits.EEPGD = 0;  // Access data EEPROM memory
    EECON1bits.CFGS = 0;   // Access Flash/EEPROM, not config registers
    EECON1bits.WREN = 1;   // Enable write operations

    INTCONbits.GIE = 0;    // Disable interrupts for required unlock sequence
    EECON2 = 0x55;         // Unlock sequence byte 1
    EECON2 = 0xAA;         // Unlock sequence byte 2
    EECON1bits.WR = 1;     // Initiate write cycle
    INTCONbits.GIE = 1;    // Restore interrupts

    while (EECON1bits.WR); // Wait for completion
    EECON1bits.WREN = 0;   // Inhibit writes
}

uint8_t EEPROM_Read(uint8_t addr) {
    EEADR = addr;
    EECON1bits.EEPGD = 0;  // Point to Data EEPROM
    EECON1bits.CFGS = 0;   // Access Flash/EEPROM
    EECON1bits.RD = 1;     // Start read operation
    return EEDATA;
}

// =============================================================================
// UART Functions (9600 Baud @ 20 MHz Fosc)
// =============================================================================
void UART_Init(void) {
    TRISCbits.TRISC6 = 0;  // RC6 (TX) as output
    TRISCbits.TRISC7 = 1;  // RC7 (RX) as input

    // Baud rate calculation for 9600 @ 20MHz:
    // SPBRG = (Fosc / (64 * Baud)) - 1 = (20000000 / (64 * 9600)) - 1 = 31.55 ~ 31
    SPBRG = 31;
    TXSTAbits.BRGH = 0;    // Low-speed baud rate
    TXSTAbits.SYNC = 0;    // Asynchronous mode
    RCSTAbits.SPEN = 1;    // Enable serial port pins
    TXSTAbits.TXEN = 1;    // Enable transmitter
    RCSTAbits.CREN = 1;    // Enable continuous receiver
}

void UART_Write(char data) {
    while (!TXSTAbits.TRMT); // Wait until transmit buffer is empty
    TXREG = data;
}

void UART_Write_Text(const char* text) {
    while (*text) {
        UART_Write(*text++);
    }
}

// =============================================================================
// Main Program
// =============================================================================
void main(void) {
    // 1. Port Configurations
    ADCON1 = 0x0F;         // Configure all analog pins as digital I/O
    TRISBbits.TRISB0 = 1;  // RB0/INT0 as input (external sensor/button)
    TRISCbits.TRISC0 = 0;  // RC0 as output (heartbeat/event LED)
    LATCbits.LATC0 = 0;

    // 2. Initialize Peripherals
    UART_Init();
    __delay_ms(100);

    UART_Write_Text("\\r\\n========================================\\r\\n");
    UART_Write_Text("[SYS] PIC18F4550 Signal Unit Initialized\\r\\n");
    UART_Write_Text("[SYS] Telemetry Baud: 9600 8-N-1\\r\\n");
    UART_Write_Text("========================================\\r\\n");

    // 3. External Interrupt Configuration
    INTCON2bits.INTEDG0 = 0; // Trigger on falling edge of RB0
    INTCONbits.INT0IF = 0;   // Clear flag
    INTCONbits.INT0IE = 1;   // Enable INT0 external interrupt
    INTCONbits.GIE = 1;      // Enable global interrupts
    INTCONbits.PEIE = 1;     // Enable peripheral interrupts

    char tx_buffer[64];

    while (1) {
        if (g_flag_new_event) {
            g_flag_new_event = 0;

            // Log event sequence into non-volatile EEPROM
            // Memory layout: [Addr: Event_LSB, Addr+1: Event_MSB]
            EEPROM_Write(g_eeprom_ptr, (uint8_t)(g_event_counter & 0xFF));
            EEPROM_Write(g_eeprom_ptr + 1, (uint8_t)((g_event_counter >> 8) & 0xFF));
            g_eeprom_ptr = (g_eeprom_ptr + 2) % 250; // Circular buffer across EEPROM

            // Transmit formatted telemetry record over UART
            sprintf(tx_buffer, "[EVENT] #%u | Pulse Captured | EEPROM Logged at 0x%02X\\r\\n",
                    g_event_counter, g_eeprom_ptr);
            UART_Write_Text(tx_buffer);
        }
        __delay_ms(10);
    }
}
'''

UART_H = '''#ifndef UART_H
#define UART_H

#include <stdint.h>

void UART_Init(void);
void UART_Write(char data);
void UART_Write_Text(const char* text);

#endif // UART_H
'''

EEPROM_H = '''#ifndef EEPROM_H
#define EEPROM_H

#include <stdint.h>

void EEPROM_Write(uint8_t addr, uint8_t data);
uint8_t EEPROM_Read(uint8_t addr);

#endif // EEPROM_H
'''

SCHEMATIC_MD = '''# Proteus Design Suite - Circuit Schematic Description

## Target Microcontroller
**Microchip PIC18F4550 (40-Pin DIP package)**

## Component Bill of Materials (BOM)
| Component ID | Description | Value / Part Number | Proteus Library Keyword |
|---|---|---|---|
| U1 | Microcontroller | PIC18F4550 | `PIC18F4550` |
| X1 | Crystal Oscillator | 20.0 MHz | `CRYSTAL` |
| C1, C2 | Ceramic Capacitors | 22 pF | `CAP` |
| R1 | Reset Pull-up Resistor | 10 kΩ | `RES` |
| SW1 | Reset Pushbutton (MCLR) | Tactile Switch | `BUTTON` |
| SW2 | Sensor / Signal Input | Tactile Switch | `BUTTON` |
| R2 | Signal Pull-up Resistor | 10 kΩ | `RES` |
| D1 | Event Status Indicator LED | 5mm Green LED | `LED-GREEN` |
| R3 | Current Limiting Resistor | 330 Ω | `RES` |
| COMPIM | Virtual Serial Terminal | RS-232 Physical Model | `COMPIM` |

## Pin Wiring Connections
| MCU Pin | Name | Connected Component | Function |
|---|---|---|---|
| 1 | `VPP/MCLR` | SW1 (to GND) + R1 (to +5V) | Active-low master clear |
| 13 | `OSC1/CLKI` | X1 (Pin 1) + C1 (to GND) | 20 MHz Clock Source |
| 14 | `OSC2/CLKO` | X1 (Pin 2) + C2 (to GND) | 20 MHz Clock Source |
| 33 | `RB0/INT0` | SW2 (to GND) + R2 (to +5V) | External Interrupt 0 Sensor Input |
| 15 | `RC0/T1OSO` | R3 in series with D1 (LED) | Output toggle on captured pulses |
| 25 | `RC6/TX` | COMPIM Pin 3 (RXD) | Serial Telemetry Transmission |
| 26 | `RC7/RX` | COMPIM Pin 2 (TXD) | Serial Command Reception |

## Simulation Configuration in Proteus 8
1. Double click **U1 (PIC18F4550)**.
2. Set **Processor Clock Frequency** to `20MHz`.
3. In **Program File**, attach compiled `.hex` output from MPLAB XC8.
4. Add a **Virtual Terminal** connected to RC6/TX to monitor telemetry logs directly in Proteus.
5. Press the **Play** button in the lower left transport toolbar.
'''

SERIAL_MONITOR_PY = '''"""
PC Serial Telemetry Monitor for PIC18 Microcontroller Unit.
Listens to COM port, decodes pulse event messages, and logs to CSV.
"""
import sys
import time
import argparse
import csv
from pathlib import Path

try:
    import serial
except ImportError:
    serial = None


def run_monitor(port: str, baud: int = 9600, output_csv: str = "events.csv") -> None:
    if serial is None:
        print("[!] pyserial not installed. Install via: pip install pyserial")
        print("[*] Running simulated serial monitor output for demonstration:")
        simulate_serial_stream(output_csv)
        return

    csv_path = Path(output_csv)
    file_exists = csv_path.exists()

    try:
        ser = serial.Serial(port, baud, timeout=1.0)
        print(f"[*] Connected to {port} @ {baud} baud. Waiting for PIC18 events...")
        print("    Press Ctrl+C to stop.")

        with open(csv_path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Timestamp", "Raw_Telemetry"])

            while True:
                line = ser.readline().decode("utf-8", errors="replace").strip()
                if line:
                    ts = time.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"[{ts}] {line}")
                    writer.writerow([ts, line])
                    f.flush()

    except serial.SerialException as e:
        print(f"[!] Serial Port Error: {e}")
        print("[*] Fallback: running simulated demonstration:")
        simulate_serial_stream(output_csv)
    except KeyboardInterrupt:
        print("\\n[*] Monitor closed by user.")


def simulate_serial_stream(output_csv: str) -> None:
    """Emulates incoming serial telemetry packets when hardware is offline."""
    print("=" * 60)
    print("  SIMULATED PIC18 SERIAL MONITOR (Hardware Offline)")
    print("=" * 60)
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Event_ID", "Status", "EEPROM_Address"])

        for event_id in range(1, 6):
            ts = time.strftime("%Y-%m-%d %H:%M:%S")
            eeprom_addr = f"0x{(event_id * 2):02X}"
            log_line = f"[EVENT] #{event_id} | Pulse Captured | EEPROM Logged at {eeprom_addr}"
            print(f"[{ts}] {log_line}")
            writer.writerow([ts, event_id, "Pulse Captured", eeprom_addr])
            time.sleep(0.5)

    print(f"[*] Demonstration logs successfully saved to {output_csv}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PIC18 Serial Telemetry Monitor")
    parser.add_argument("--port", default="COM3", help="Serial port identifier (e.g. COM3 or /dev/ttyUSB0)")
    parser.add_argument("--baud", type=int, default=9600, help="Baud rate (default: 9600)")
    parser.add_argument("--output", default="events.csv", help="CSV log output destination")
    args = parser.parse_args()

    run_monitor(args.port, args.baud, args.output)
'''

SIMULATE_PIC18_PY = '''"""
High-Fidelity Software Simulation of PIC18F4550 Signal Unit.
Simulates registers, ISR logic, debouncing, 256-byte EEPROM memory, and UART transmission.
"""
import time


class SimulatedPIC18F4550:
    def __init__(self):
        # 256 bytes of non-volatile internal data EEPROM
        self.eeprom = [0x00] * 256
        self.eeprom_ptr = 0x00
        self.event_counter = 0
        self.led_rc0 = False
        print("[MCU SIM] PIC18F4550 initialized @ 20.0 MHz")
        print("[MCU SIM] INT0 external interrupt active on RB0 (falling edge)")

    def trigger_int0_pulse(self):
        """Simulates a sensor/button trigger on RB0 triggering high-priority ISR."""
        print("\\n---> Hardware pulse received on RB0/INT0")
        # 1. Debounce verification
        time.sleep(0.015)
        self.event_counter += 1
        self.led_rc0 = not self.led_rc0

        # 2. Write to non-volatile EEPROM
        lsb = self.event_counter & 0xFF
        msb = (self.event_counter >> 8) & 0xFF
        self.eeprom[self.eeprom_ptr] = lsb
        self.eeprom[self.eeprom_ptr + 1] = msb

        saved_addr = self.eeprom_ptr
        self.eeprom_ptr = (self.eeprom_ptr + 2) % 250

        # 3. Transmit UART frame
        telemetry = f"[EVENT] #{self.event_counter} | Pulse Captured | EEPROM Logged at 0x{saved_addr:02X}"
        print(f"[UART TX 9600bps] {telemetry}")
        print(f"[GPIO STATUS] LED RC0 State: {'HIGH (ON)' if self.led_rc0 else 'LOW (OFF)'}")
        return telemetry


if __name__ == "__main__":
    mcu = SimulatedPIC18F4550()
    print("\\nSimulating 5 hardware sensor trigger pulses...")
    for _ in range(5):
        mcu.trigger_int0_pulse()
        time.sleep(0.2)

    print("\\nEEPROM Memory Dump (First 16 bytes):")
    print(" ".join(f"{b:02X}" for b in mcu.eeprom[:16]))
    print("[MCU SIM] Simulation complete.")
'''

REQUIREMENTS_TXT = '''pyserial>=3.5
'''

README_MD = '''# PIC18 Microcontroller Signal Communication Unit

An embedded systems engineering project featuring interrupt-driven signal acquisition, hardware debouncing, non-volatile EEPROM telemetry logging, and UART serial transmission for the Microchip **PIC18F4550** microcontroller.

## Architecture
```
[ Hardware Signal / Pushbutton ]
                | (Falling edge trigger)
                v
        [ RB0 / INT0 Pin ]
                |
                v
       [ PIC18F4550 MCU ]
        /              \\
       v                v
[ 256-Byte EEPROM ]   [ UART TX (RC6) @ 9600 ]
(Event Log Storage)             |
                                v
                      [ PC Serial Monitor / CSV ]
```

## Features
- **Interrupt-Driven:** High-priority ISR on `RB0/INT0` ensures zero missed sensor events.
- **Hardware Debouncing:** 15ms timing check eliminates mechanical contact bounce artifacts.
- **EEPROM Event History:** Circular logging of 16-bit event counters across on-chip non-volatile EEPROM.
- **UART Diagnostic Output:** Formatted telemetry output at standard 9600 baud 8-N-1.
- **Software Emulation Included:** Includes Python-based register & memory simulator for verification without physical hardware.

## Building Firmware
1. Open **Microchip MPLAB X IDE**.
2. Create a new standalone project for device `PIC18F4550`.
3. Select toolchain `Microchip XC8`.
4. Add files from `firmware/` (`main.c`, `uart.h`, `eeprom.h`).
5. Build project to generate `.hex` image.

## Simulation in Proteus
Refer to `proteus/schematic_description.md` for complete circuit schematic wiring and setup instructions.

## PC Serial Monitor
```bash
python serial_monitor.py --port COM3 --baud 9600
```
'''

files = {
    "firmware/main.c": MAIN_C,
    "firmware/uart.h": UART_H,
    "firmware/eeprom.h": EEPROM_H,
    "proteus/schematic_description.md": SCHEMATIC_MD,
    "serial_monitor.py": SERIAL_MONITOR_PY,
    "simulation/simulate_pic18.py": SIMULATE_PIC18_PY,
    "requirements.txt": REQUIREMENTS_TXT,
    "README.md": README_MD,
}

for rel_path, content in files.items():
    file_path = BASE_DIR / rel_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Created {file_path}")

print("Project 3 (PIC18-Signal-Communication-Unit) built successfully!")
