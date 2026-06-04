"""
BE6502 SBC - Add RCA composite video output and PS/2 keyboard port.

Modifies KiCad schematic and cache library to add composite video 
output (VIA PA0-PA5 -> resistor DAC -> RCA) and PS/2 keyboard 
connector (VIA PA6=DATA, PA7=CLOCK -> mini-DIN).

Usage: python3 update_board.py
"""

import os, re, hashlib

SBC_DIR = "/workspaces/MK57/BE6502 SBC"
SCH_FILE = os.path.join(SBC_DIR, "BE6502 SBC.sch")
CACHE_LIB = os.path.join(SBC_DIR, "BE6502 SBC-cache.lib")

CACHE_ADDITIONS = """#
# conn_Conn_01x02
#
DEF conn_Conn_01x02 J 0 40 Y N 1 F N
F0 "J" 0 150 50 H V C CNN
F1 "conn_Conn_01x02" 0 -200 50 H V C CNN
F2 "" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
$FPLIST
 Connector*:*_??x??_*
 Connector*:*_1x02*
$ENDFPLIST
DRAW
S -50 150 50 -150 1 1 10 f
X Pin_1 1 -200 50 150 R 50 50 1 1 P
X Pin_2 2 -200 -50 150 R 50 50 1 1 P
ENDDRAW
ENDDEF
#
# conn_Conn_01x06
#
DEF conn_Conn_01x06 J 0 40 Y N 1 F N
F0 "J" 0 300 50 H V C CNN
F1 "conn_Conn_01x06" 0 -350 50 H V C CNN
F2 "" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
$FPLIST
 Connector*:*_??x??_*
 Connector*:*_1x06*
$ENDFPLIST
DRAW
S -50 250 50 -250 1 1 10 f
X Pin_1 1 -200 200 150 R 50 50 1 1 P
X Pin_2 2 -200 100 150 R 50 50 1 1 P
X Pin_3 3 -200 0 150 R 50 50 1 1 P
X Pin_4 4 -200 -100 150 R 50 50 1 1 P
X Pin_5 5 -200 -200 150 R 50 50 1 1 P
X Pin_6 6 -200 -300 150 R 50 50 1 1 P
ENDDRAW
ENDDEF
#
"""

SCH_ADDITIONS = r"""# --- Composite Video RCA Output (VIA PA0-PA5 -> Resistor DAC) ---
$Comp
L Device:R R22
U 1 1 00000001
P 5000 9000
F 0 "R22" V 5080 9000 50  0000 C CNN
F 1 "1k" V 5000 9000 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 4930 9000 50  0001 C CNN
F 3 "" H 5000 9000 50  0001 C CNN
	1    5000 9000
	0    1    1    0   
$EndComp
$Comp
L Device:R R23
U 1 1 00000002
P 5000 9150
F 0 "R23" V 5080 9150 50  0000 C CNN
F 1 "2k" V 5000 9150 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 4930 9150 50  0001 C CNN
F 3 "" H 5000 9150 50  0001 C CNN
	1    5000 9150
	0    1    1    0   
$EndComp
$Comp
L Device:R R24
U 1 1 00000003
P 5000 9300
F 0 "R24" V 5080 9300 50  0000 C CNN
F 1 "4.7k" V 5000 9300 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 4930 9300 50  0001 C CNN
F 3 "" H 5000 9300 50  0001 C CNN
	1    5000 9300
	0    1    1    0   
$EndComp
$Comp
L Device:R R25
U 1 1 00000004
P 5000 9450
F 0 "R25" V 5080 9450 50  0000 C CNN
F 1 "10k" V 5000 9450 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 4930 9450 50  0001 C CNN
F 3 "" H 5000 9450 50  0001 C CNN
	1    5000 9450
	0    1    1    0   
$EndComp
$Comp
L Device:R R26
U 1 1 00000005
P 5000 9600
F 0 "R26" V 5080 9600 50  0000 C CNN
F 1 "22k" V 5000 9600 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 4930 9600 50  0001 C CNN
F 3 "" H 5000 9600 50  0001 C CNN
	1    5000 9600
	0    1    1    0   
$EndComp
$Comp
L Device:R R27
U 1 1 00000006
P 5000 9750
F 0 "R27" V 5080 9750 50  0000 C CNN
F 1 "47k" V 5000 9750 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 4930 9750 50  0001 C CNN
F 3 "" H 5000 9750 50  0001 C CNN
	1    5000 9750
	0    1    1    0   
$EndComp
$Comp
L conn:Conn_01x02 J5
U 1 1 00000007
P 6050 9400
F 0 "J5" H 6050 9625 50  0000 C CNN
F 1 "RCA_VIDEO" H 6050 9125 50  0000 C CNN
F 2 "Connector:RCA_PJRA3x2_SMD" H 6050 9400 50  0001 C CNN
F 3 "" H 6050 9400 50  0001 C CNN
	1    6050 9400
	1    0    0    0   
$EndComp
$Comp
L power:GND #PWR032
U 1 1 00000008
P 5850 9350
F 0 "#PWR032" H 5850 9100 50  0001 C CNN
F 1 "GND" H 5850 9200 50  0000 C CNN
F 2 "" H 5850 9350 50  0001 C CNN
F 3 "" H 5850 9350 50  0001 C CNN
	1    5850 9350
	1    0    0    -1  
$EndComp
Text Label 4050 9000 0    60   ~ 0
PA0
Text Label 4050 9150 0    60   ~ 0
PA1
Text Label 4050 9300 0    60   ~ 0
PA2
Text Label 4050 9450 0    60   ~ 0
PA3
Text Label 4050 9600 0    60   ~ 0
PA4
Text Label 4050 9750 0    60   ~ 0
PA5
Wire Wire Line 4050 9000 4850 9000
Wire Wire Line 4050 9150 4850 9150
Wire Wire Line 4050 9300 4850 9300
Wire Wire Line 4050 9450 4850 9450
Wire Wire Line 4050 9600 4850 9600
Wire Wire Line 4050 9750 4850 9750
Wire Wire Line 5150 9000 5800 9000
Wire Wire Line 5150 9150 5800 9150
Wire Wire Line 5150 9300 5800 9300
Wire Wire Line 5150 9450 5800 9450
Wire Wire Line 5150 9600 5800 9600
Wire Wire Line 5150 9750 5800 9750
Wire Wire Line 5800 9000 5800 9750
Connection ~ 5800 9000
Connection ~ 5800 9150
Connection ~ 5800 9300
Connection ~ 5800 9450
Connection ~ 5800 9600
Connection ~ 5800 9750
Wire Wire Line 5800 9450 5850 9450
# --- PS/2 Keyboard Port (VIA PA6=DATA, PA7=CLOCK -> mini-DIN) ---
$Comp
L conn:Conn_01x06 J6
U 1 1 00000009
P 6050 10300
F 0 "J6" H 6050 10600 50  0000 C CNN
F 1 "PS2_KEYBOARD" H 6050 9975 50  0000 C CNN
F 2 "Connector:PS2-6P" H 6050 10300 50  0001 C CNN
F 3 "" H 6050 10300 50  0001 C CNN
	1    6050 10300
	1    0    0    0   
$EndComp
$Comp
L Device:R R28
U 1 1 0000000A
P 5500 10500
F 0 "R28" V 5580 10500 50  0000 C CNN
F 1 "4.7k" V 5500 10500 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 5430 10500 50  0001 C CNN
F 3 "" H 5500 10500 50  0001 C CNN
	1    5500 10500
	0    1    1    0   
$EndComp
$Comp
L Device:R R29
U 1 1 0000000B
P 5500 10100
F 0 "R29" V 5580 10100 50  0000 C CNN
F 1 "4.7k" V 5500 10100 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 5430 10100 50  0001 C CNN
F 3 "" H 5500 10100 50  0001 C CNN
	1    5500 10100
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR033
U 1 1 0000000C
P 5600 10400
F 0 "#PWR033" H 5600 10250 50  0001 C CNN
F 1 "VCC" H 5600 10550 50  0000 C CNN
F 2 "" H 5600 10400 50  0001 C CNN
F 3 "" H 5600 10400 50  0001 C CNN
	1    5600 10400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR034
U 1 1 0000000D
P 5850 10300
F 0 "#PWR034" H 5850 10050 50  0001 C CNN
F 1 "GND" H 5850 10150 50  0000 C CNN
F 2 "" H 5850 10300 50  0001 C CNN
F 3 "" H 5850 10300 50  0001 C CNN
	1    5850 10300
	1    0    0    -1  
$EndComp
Text Label 4050 9900 0    60   ~ 0
PA6
Text Label 4050 10200 0    60   ~ 0
PA7
Wire Wire Line 4050 9900 5000 9900
Wire Wire Line 4050 10200 5050 10200
Wire Wire Line 5000 9900 5000 10500
Wire Wire Line 5050 10200 5050 10100
Wire Wire Line 5000 10500 5850 10500
Wire Wire Line 5050 10100 5850 10100
Wire Wire Line 5600 10400 5650 10400
Wire Wire Line 5650 10400 5650 10500
Wire Wire Line 5650 10400 5650 10100
Wire Wire Line 5600 10400 5600 10200
Wire Wire Line 5600 10200 5850 10200
Connection ~ 5650 10400
Connection ~ 5600 10400
Connection ~ 5850 10500
NoConn ~ 5850 10400
NoConn ~ 5850 10000
"""

def update_cache_lib():
    with open(CACHE_LIB, 'r') as f:
        content = f.read()
    for sym_name in ('conn_Conn_01x02', 'conn_Conn_01x06'):
        if f'DEF {sym_name}' in content:
            print(f"  {sym_name} already in cache.lib")
        else:
            content += '\n' + CACHE_ADDITIONS
            print(f"  Added {sym_name} to cache.lib")
            break
    with open(CACHE_LIB, 'w') as f:
        f.write(content)

def update_schematic():
    with open(SCH_FILE, 'r') as f:
        content = f.read()
    
    marker = "NoConn ~ 1875 1750"
    pos = content.find(marker)
    if pos == -1:
        print("ERROR: insertion point not found!")
        return False
    
    idx = pos + len(marker)
    content = content[:idx] + '\n' + SCH_ADDITIONS + '\n' + content[idx:]
    
    # Fix placeholder timestamps (replace 0000000x with unique values)
    counter = [0]
    def fix_ts(m):
        counter[0] += 1
        prefix = m.group(1) if m.lastindex else m.group(0)[:5]
        return f'{prefix}{hashlib.md5(f"be65{counter[0]:04d}".encode()).hexdigest()[:8].upper()}'
    content = re.sub(r'(U \d \d )0000000[0-9A-F]', fix_ts, content)
    
    with open(SCH_FILE, 'w') as f:
        f.write(content)
    print("  Schematic updated with RCA + PS/2 sections")
    return True

def main():
    print("BE6502 SBC - Adding RCA + PS/2 ports")
    print("=" * 50)
    update_cache_lib()
    update_schematic()
    print("=" * 50)
    print("Done! Schematic changes:")
    print("  RCA: PA0-PA5 -> 6-resistor DAC -> J5 (RCA_VIDEO)")
    print("  PS/2: PA6 -> R28 pull-up -> J6 pin1(DATA)")
    print("        PA7 -> R29 pull-up -> J6 pin5(CLOCK)")
    print("        J6 pin3=GND, pin4=VCC, pins2/6=NC")

if __name__ == "__main__":
    main()
