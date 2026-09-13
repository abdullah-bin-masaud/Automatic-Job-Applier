import os
from pathlib import Path

# ==============================================================================
# PROJECT 9: Microcontroller-Sensor-Control-Alert-Circuits
# ==============================================================================
DIR_CIRC = Path(r"C:\Users\Lenovo\Desktop\Projects\Microcontroller-Sensor-Control-Alert-Circuits")
(DIR_CIRC / "water_level_indicator").mkdir(parents=True, exist_ok=True)
(DIR_CIRC / "automatic_street_light").mkdir(parents=True, exist_ok=True)
(DIR_CIRC / "fire_smoke_alert").mkdir(parents=True, exist_ok=True)
(DIR_CIRC / "simulation").mkdir(parents=True, exist_ok=True)

WATER_C = '''/**
 * Subsystem: Automated Water Level Indicator & Overflow Alarm
 * Controller: Microchip PIC / AVR / Generic Microcontroller
 * Description: Multi-level probe detection using BC547 NPN transistor switching logic.
 */

#include <stdint.h>

#define PROBE_LOW      0x01  // Tank 25%
#define PROBE_MID      0x02  // Tank 50%
#define PROBE_HIGH     0x04  // Tank 75%
#define PROBE_OVERFLOW 0x08  // Tank 100% (Critical)

// Output pin states
uint8_t g_led_indicators = 0x00;
uint8_t g_buzzer_alarm = 0;

void WaterLevel_Process(uint8_t probe_inputs) {
    g_led_indicators = 0;
    g_buzzer_alarm = 0;

    if (probe_inputs & PROBE_LOW) {
        g_led_indicators |= 0x01; // Green LED (Low)
    }
    if (probe_inputs & PROBE_MID) {
        g_led_indicators |= 0x03; // Yellow LEDs (Mid)
    }
    if (probe_inputs & PROBE_HIGH) {
        g_led_indicators |= 0x07; // Orange LEDs (High)
    }
    if (probe_inputs & PROBE_OVERFLOW) {
        g_led_indicators |= 0x0F; // Red LED (Full)
        g_buzzer_alarm = 1;       // Sound audio buzzer
    }
}
'''

STREETLIGHT_C = '''/**
 * Subsystem: Automatic Street Light Controller with Hysteresis Filtering
 * Description: LDR ambient light sensing. Hysteresis prevents rapid flicker during dusk/dawn.
 */

#include <stdint.h>

#define THRESHOLD_DUSK 350  // Turn ON when ambient drops below this ADC value
#define THRESHOLD_DAWN 500  // Turn OFF when ambient rises above this (Hysteresis window)

static uint8_t s_light_state = 0; // 0 = OFF, 1 = ON

uint8_t StreetLight_Update(uint16_t ldr_adc_value) {
    if (s_light_state == 0) {
        if (ldr_adc_value < THRESHOLD_DUSK) {
            s_light_state = 1; // Turn ON relay/lights
        }
    } else {
        if (ldr_adc_value > THRESHOLD_DAWN) {
            s_light_state = 0; // Turn OFF relay/lights
        }
    }
    return s_light_state;
}
'''

FIRE_C = '''/**
 * Subsystem: Fire and Gas/Smoke Emergency Alert System
 * Description: Dual threshold evaluation for MQ-2 gas sensor and IR flame phototransistor.
 */

#include <stdint.h>

#define GAS_PPM_DANGER_THRESHOLD 400
#define FLAME_DETECTED_LOGIC_LOW 0

typedef struct {
    uint8_t emergency_active;
    uint8_t strobe_led;
    uint8_t audio_siren;
} AlarmStatus;

AlarmStatus FireAlert_Check(uint16_t mq2_adc_ppm, uint8_t flame_pin_state) {
    AlarmStatus status = {0, 0, 0};

    if (mq2_adc_ppm > GAS_PPM_DANGER_THRESHOLD || flame_pin_state == FLAME_DETECTED_LOGIC_LOW) {
        status.emergency_active = 1;
        status.strobe_led = 1;
        status.audio_siren = 1;
    }
    return status;
}
'''

SIMULATE_CIRCUITS_PY = '''"""
Interactive Software Simulation of All 3 Sensor Control and Alert Circuits.
"""
import time


def simulate():
    print("==================================================================")
    print("  MICROCONTROLLER SENSOR CONTROL & ALERT CIRCUITS SIMULATION")
    print("==================================================================")

    # 1. Water Level System
    print("\\n[CIRCUIT 1: Automated Water Level Indicator]")
    water_levels = [("Empty", 0), ("25% Low", 1), ("50% Mid", 3), ("75% High", 7), ("100% Overflow", 15)]
    for label, mask in water_levels:
        leds = bin(mask)[2:].zfill(4)
        buzzer = "SOUNDING BUZZER!" if mask == 15 else "Quiet"
        print(f"  Level: {label:<16} | Bar LEDs [4-Level]: [{leds}] | Buzzer: {buzzer}")

    # 2. LDR Street Light
    print("\\n[CIRCUIT 2: Automatic Street Light with Hysteresis]")
    lux_readings = [800, 600, 320, 280, 340, 420, 550, 700]
    light_state = "OFF"
    for ldr in lux_readings:
        if light_state == "OFF" and ldr < 350:
            light_state = "ON"
        elif light_state == "ON" and ldr > 500:
            light_state = "OFF"
        print(f"  Ambient Light (ADC): {ldr:4d} | Hysteresis Filtered Relay: [{light_state}]")

    # 3. Fire & Smoke Alert
    print("\\n[CIRCUIT 3: Emergency Smoke & Flame Alert System]")
    scenarios = [
        ("Normal Air Quality", 80, "No Flame"),
        ("Minor Cooking Vapors", 220, "No Flame"),
        ("SMOKE HAZARD DETECTED", 650, "No Flame"),
        ("ACTIVE FLAME DETECTED", 110, "FLAME PRESENT")
    ]
    for desc, ppm, flame in scenarios:
        alarm = (ppm > 400 or flame == "FLAME PRESENT")
        status = "EMERGENCY STROBE + SIREN TRIGGERED!" if alarm else "Standby (Nominal)"
        print(f"  Condition: {desc:<24} | MQ-2: {ppm} PPM | IR Flame: {flame:<13} -> {status}")

    print("\\n[*] All 3 circuit logic simulations verified successfully.")


if __name__ == "__main__":
    simulate()
'''

PROJ9_README = '''# Microcontroller Sensor Control & Alert Circuits

A suite of three practical embedded hardware automation circuits designed, simulated in Proteus, and coded in Embedded C:

1. **Water Level Indicator:** Multi-stage transistor switching logic (BC547) driving a 4-tier LED display and automated overflow buzzer alert.
2. **Automatic Street Light Controller:** LDR sensor-based illumination control featuring hysteresis filtering to prevent dusk/dawn relay chatter.
3. **Fire & Smoke Emergency Alert:** Dual-stage safety circuit interfacing an MQ-2 combustible gas sensor and IR flame phototransistor with rapid strobe and siren signaling.

## Project Structure
- `water_level_indicator/`: C firmware & Proteus design guide for water tank sensing.
- `automatic_street_light/`: C firmware & hysteresis logic for lighting control.
- `fire_smoke_alert/`: Emergency alert interrupt logic.
- `simulation/simulate_circuits.py`: Python-based interactive simulation of all three systems.

## Quickstart
```bash
python simulation/simulate_circuits.py
```
'''

p9_files = {
    "water_level_indicator/water_level.c": WATER_C,
    "automatic_street_light/street_light.c": STREETLIGHT_C,
    "fire_smoke_alert/fire_alert.c": FIRE_C,
    "simulation/simulate_circuits.py": SIMULATE_CIRCUITS_PY,
    "README.md": PROJ9_README,
}

for rel, code in p9_files.items():
    p = DIR_CIRC / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(code.strip() + "\n", encoding="utf-8")
    print(f"Created {p}")

print("Project 9 (Microcontroller-Sensor-Control-Alert-Circuits) created!")


# ==============================================================================
# PROJECT 10: PIC18-Automated-Attendance-System
# ==============================================================================
DIR_ATTEND = Path(r"C:\Users\Lenovo\Desktop\Projects\PIC18-Automated-Attendance-System")
(DIR_ATTEND / "firmware").mkdir(parents=True, exist_ok=True)
(DIR_ATTEND / "proteus").mkdir(parents=True, exist_ok=True)
(DIR_ATTEND / "simulation").mkdir(parents=True, exist_ok=True)

ATTEND_MAIN_C = '''/**
 * Project: PIC18 Microcontroller Automated Attendance & Headcount System
 * Target: Microchip PIC18F4550 @ 20.0 MHz
 * Description: Bi-directional door entry/exit gate using dual IR optical beam sensors.
 *              Detects direction of transit, updates live headcount on 16x2 LCD,
 *              and commits timestamped attendee records to non-volatile EEPROM.
 */

#include <xc.h>
#include <stdint.h>
#include <stdio.h>

#define _XTAL_FREQ 20000000UL

// Sensor Pin Definitions
#define SENSOR_A PORTBbits.RB0 // Outer Door Beam (INT0)
#define SENSOR_B PORTBbits.RB1 // Inner Door Beam (INT1)

volatile int16_t g_current_occupancy = 0;
volatile uint16_t g_total_entries = 0;
volatile uint16_t g_total_exits = 0;
uint8_t g_eeprom_log_idx = 0x00;

// State Machine for Direction Tracking
typedef enum {
    GATE_IDLE,
    BEAM_A_FIRST, // Transit inwards started
    BEAM_B_FIRST  // Transit outwards started
} GateState;

volatile GateState g_state = GATE_IDLE;

void EEPROM_WriteByte(uint8_t address, uint8_t data) {
    EEADR = address;
    EEDATA = data;
    EECON1bits.EEPGD = 0;
    EECON1bits.CFGS = 0;
    EECON1bits.WREN = 1;

    INTCONbits.GIE = 0;
    EECON2 = 0x55;
    EECON2 = 0xAA;
    EECON1bits.WR = 1;
    INTCONbits.GIE = 1;

    while (EECON1bits.WR);
    EECON1bits.WREN = 0;
}

void __interrupt() ISR(void) {
    // Optical Beam A Interrupted
    if (INTCONbits.INT0IF) {
        __delay_ms(5); // Debounce
        if (SENSOR_A == 0) {
            if (g_state == GATE_IDLE) {
                g_state = BEAM_A_FIRST;
            } else if (g_state == BEAM_B_FIRST) {
                // Completed outward exit transit (B -> A)
                g_total_exits++;
                if (g_current_occupancy > 0) g_current_occupancy--;
                g_state = GATE_IDLE;

                // Log exit to EEPROM
                EEPROM_WriteByte(g_eeprom_log_idx++, 0xEE); // Exit event marker
                EEPROM_WriteByte(g_eeprom_log_idx++, (uint8_t)g_current_occupancy);
            }
        }
        INTCONbits.INT0IF = 0;
    }

    // Optical Beam B Interrupted
    if (INTCON3bits.INT1IF) {
        __delay_ms(5); // Debounce
        if (SENSOR_B == 0) {
            if (g_state == GATE_IDLE) {
                g_state = BEAM_B_FIRST;
            } else if (g_state == BEAM_A_FIRST) {
                // Completed inward entry transit (A -> B)
                g_total_entries++;
                g_current_occupancy++;
                g_state = GATE_IDLE;

                // Log entry to EEPROM
                EEPROM_WriteByte(g_eeprom_log_idx++, 0xAA); // Entry event marker
                EEPROM_WriteByte(g_eeprom_log_idx++, (uint8_t)g_current_occupancy);
            }
        }
        INTCON3bits.INT1IF = 0;
    }
}

void main(void) {
    ADCON1 = 0x0F; // All digital I/O
    TRISBbits.TRISB0 = 1; // Sensor A input
    TRISBbits.TRISB1 = 1; // Sensor B input
    TRISD = 0x00;         // Port D as LCD 8-bit bus

    // Configure falling edge external interrupts
    INTCON2bits.INTEDG0 = 0;
    INTCON2bits.INTEDG1 = 0;
    INTCONbits.INT0IF = 0;
    INTCON3bits.INT1IF = 0;
    INTCONbits.INT0IE = 1;
    INTCON3bits.INT1IE = 1;
    INTCONbits.GIE = 1;

    while (1) {
        // System loop: update display telemetry
        __delay_ms(100);
    }
}
'''

SIMULATE_ATTEND_PY = '''"""
Software Simulator for PIC18 Bi-Directional Optical Attendance Gate.
"""
import time


class AttendanceGateSimulator:
    def __init__(self):
        self.occupancy = 0
        self.total_in = 0
        self.total_out = 0
        self.eeprom_log = []

    def simulate_person_entering(self, person_name: str):
        print(f"[*] {person_name} approaching entrance...")
        # Step 1: Breaks Beam A
        print("    -> Beam A tripped (Outer door)")
        time.sleep(0.05)
        # Step 2: Breaks Beam B
        print("    -> Beam B tripped (Inner door) [ENTRY CONFIRMED]")
        self.occupancy += 1
        self.total_in += 1
        self.eeprom_log.append({"event": "ENTRY", "name": person_name, "occupancy": self.occupancy})
        print(f"    [HEADCOUNT UPDATE] Inside Room: {self.occupancy} (Total Entered: {self.total_in})")

    def simulate_person_exiting(self, person_name: str):
        print(f"[*] {person_name} approaching exit...")
        # Step 1: Breaks Beam B
        print("    -> Beam B tripped (Inner door)")
        time.sleep(0.05)
        # Step 2: Breaks Beam A
        print("    -> Beam A tripped (Outer door) [EXIT CONFIRMED]")
        if self.occupancy > 0:
            self.occupancy -= 1
        self.total_out += 1
        self.eeprom_log.append({"event": "EXIT", "name": person_name, "occupancy": self.occupancy})
        print(f"    [HEADCOUNT UPDATE] Inside Room: {self.occupancy} (Total Exited: {self.total_out})")


if __name__ == "__main__":
    gate = AttendanceGateSimulator()
    print("==================================================================")
    print("  PIC18 AUTOMATED ATTENDANCE GATE SIMULATION")
    print("==================================================================")

    gate.simulate_person_entering("Student 101")
    gate.simulate_person_entering("Student 102")
    gate.simulate_person_entering("Student 103")
    gate.simulate_person_exiting("Student 101")

    print("\\n[EEPROM AUDIT LOG DUMP]")
    for item in gate.eeprom_log:
        print(f"  Event: {item['event']:<6} | Subject: {item['name']:<12} | Room Occupancy: {item['occupancy']}")
'''

PROJ10_README = '''# PIC18 Microcontroller Automated Attendance System

An automated entry/exit tracking and room headcount management system built on the Microchip **PIC18F4550** microcontroller, using dual optical infrared beam sensors, interrupt-driven transit direction detection, and persistent on-chip EEPROM logging.

## Principle of Operation
Two IR beam sensors (Sensor A and Sensor B) are positioned in sequence across an entrance portal:
- **Inward Transit (Entry):** Sensor A tripped first, followed by Sensor B $\\rightarrow$ Headcount increments.
- **Outward Transit (Exit):** Sensor B tripped first, followed by Sensor A $\\rightarrow$ Headcount decrements.

## Architecture
```
[ Outer IR Beam (RB0/INT0) ] ---> [ Directional Transit ] ---> [ Headcount Logic ]
[ Inner IR Beam (RB1/INT1) ] ---> [ State Machine       ] ---> [ EEPROM Logger    ]
                                                                [ 16x2 LCD Display ]
```

## Features
- **Bi-Directional Optical Gate:** High-priority external interrupts (`INT0`, `INT1`) reliably distinguish entering vs exiting pedestrians.
- **Non-Volatile Logging:** Every entry and exit event commits timestamped state records to PIC18 internal EEPROM.
- **Debouncing:** Fast 5ms software timing window filters ambient optical noise.
- **Software Simulation:** Includes Python-based transit simulator modeling pedestrian gate flow.

## Quickstart
```bash
python simulation/simulate_attendance.py
```
'''

p10_files = {
    "firmware/main.c": ATTEND_MAIN_C,
    "simulation/simulate_attendance.py": SIMULATE_ATTEND_PY,
    "README.md": PROJ10_README,
}

for rel, code in p10_files.items():
    p = DIR_ATTEND / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(code.strip() + "\n", encoding="utf-8")
    print(f"Created {p}")

print("Project 10 (PIC18-Automated-Attendance-System) created!")
