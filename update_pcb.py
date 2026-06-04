"""
BE6502 SBC PCB - Add footprints for RCA and PS/2 ports.
Appends resistor, RCA jack and PS/2 connector footprints to PCB file.
Run AFTER update_board.py (schematic must be updated first).

Usage: python3 update_pcb.py
"""

import os, uuid

PCB_FILE = "/workspaces/MK57/BE6502 SBC/BE6502 SBC.kicad_pcb"

# Timestamps (8-char hex from schematic U 1 1 <ts> lines)
# These MUST match the schematic for KiCad to link PCB<->schematic
TS = {
    'R22': '9255357C', 'R23': '25E1AA8F', 'R24': 'ADE8DC4B',
    'R25': '668D00AB', 'R26': '0E26AE7C', 'R27': 'FA9F5F78',
    'R28': '773A6297', 'R29': 'E0A8B335',
    'J5': 'B4B321D2', 'J6': '3005B9C2',
}

def uid():
    return str(uuid.uuid4())

def path(ts):
    return f"/00000000-0000-0000-0000-0000{ts}"

def resistor(ref, value, x, y, rot, ts, net_left, net_right):
    nl = f'(net "{net_left}")' if net_left else ''
    nr = f'(net "{net_right}")' if net_right else ''
    return f'''\t(footprint "Resistors_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"
\t\t(layer "F.Cu") (uuid "{uid()}") (at {x} {y} {rot})
\t\t(descr "Resistor, Axial_DIN0207, Horizontal, pitch=10.16mm")
\t\t(tags "Resistor Axial_DIN0207")
\t\t(property "Reference" "{ref}" (at 6.985 0 270) (layer "F.SilkS") (uuid "{uid()}") (effects (font (size 1 1) (thickness 0.15))))
\t\t(property "Value" "{value}" (at 3.81 0 180) (layer "F.SilkS") (uuid "{uid()}") (effects (font (size 1 1) (thickness 0.15))))
\t\t(property "Datasheet" "" (at 0 0 0) (layer "F.Fab") (hide yes) (uuid "{uid()}") (effects (font (size 1.27 1.27))))
\t\t(property "Description" "" (at 0 0 0) (layer "F.Fab") (hide yes) (uuid "{uid()}") (effects (font (size 1.27 1.27))))
\t\t(path "{path(ts)}") (attr through_hole) (duplicate_pad_numbers_are_jumpers no)
\t\t(fp_line (start 9.18 0) (end 8.29 0) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start 8.29 1.31) (end 8.29 -1.31) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start 8.29 -1.31) (end 1.87 -1.31) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start 1.87 1.31) (end 8.29 1.31) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start 1.87 -1.31) (end 1.87 1.31) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start 0.98 0) (end 1.87 0) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start 11.25 1.6) (end 11.25 -1.6) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start 11.25 -1.6) (end -1.05 -1.6) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start -1.05 1.6) (end 11.25 1.6) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start -1.05 -1.6) (end -1.05 1.6) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start 10.16 0) (end 8.23 0) (stroke (width 0.1) (type solid)) (layer "F.Fab") (uuid "{uid()}"))
\t\t(fp_line (start 8.23 1.25) (end 8.23 -1.25) (stroke (width 0.1) (type solid)) (layer "F.Fab") (uuid "{uid()}"))
\t\t(fp_line (start 8.23 -1.25) (end 1.93 -1.25) (stroke (width 0.1) (type solid)) (layer "F.Fab") (uuid "{uid()}"))
\t\t(fp_line (start 1.93 1.25) (end 8.23 1.25) (stroke (width 0.1) (type solid)) (layer "F.Fab") (uuid "{uid()}"))
\t\t(fp_line (start 1.93 -1.25) (end 1.93 1.25) (stroke (width 0.1) (type solid)) (layer "F.Fab") (uuid "{uid()}"))
\t\t(fp_line (start 0 0) (end 1.93 0) (stroke (width 0.1) (type solid)) (layer "F.Fab") (uuid "{uid()}"))
\t\t(pad "1" thru_hole circle (at 0 0 {rot}) (size 1.6 1.6) (drill 0.8) (layers "*.Cu" "*.Mask") (remove_unused_layers no) {nl} (uuid "{uid()}"))
\t\t(pad "2" thru_hole oval (at 10.16 0 {rot}) (size 1.6 1.6) (drill 0.8) (layers "*.Cu" "*.Mask") (remove_unused_layers no) {nr} (uuid "{uid()}"))
\t)'''

def rca_jack(ref, value, x, y, rot, ts):
    return f'''\t(footprint "Connector:RCA_Phono_THT"
\t\t(layer "F.Cu") (uuid "{uid()}") (at {x} {y} {rot})
\t\t(descr "RCA Phono connector, 2-pin, through hole")
\t\t(tags "RCA Phono")
\t\t(property "Reference" "{ref}" (at -3 -8 0) (layer "F.SilkS") (uuid "{uid()}") (effects (font (size 1 1) (thickness 0.15))))
\t\t(property "Value" "{value}" (at -3 -10 0) (layer "F.SilkS") (uuid "{uid()}") (effects (font (size 1 1) (thickness 0.15))))
\t\t(property "Datasheet" "" (at 0 0 0) (layer "F.Fab") (hide yes) (uuid "{uid()}") (effects (font (size 1.27 1.27))))
\t\t(property "Description" "" (at 0 0 0) (layer "F.Fab") (hide yes) (uuid "{uid()}") (effects (font (size 1.27 1.27))))
\t\t(path "{path(ts)}") (attr through_hole) (duplicate_pad_numbers_are_jumpers no)
\t\t(fp_circle (center 0 0) (end 4.5 0) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (fill none) (uuid "{uid()}"))
\t\t(fp_line (start -3.5 -5.08) (end 3.5 -5.08) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start -3.5 -7) (end -3.5 -5.08) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start 3.5 -7) (end 3.5 -5.08) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start -3.5 -7) (end 3.5 -7) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (uuid "{uid()}"))
\t\t(fp_line (start -5.5 -7.5) (end 5.5 -7.5) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start 5.5 -7.5) (end 5.5 5) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start 5.5 5) (end -5.5 5) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start -5.5 5) (end -5.5 -7.5) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(pad "1" thru_hole circle (at 0 0 {rot}) (size 2.5 2.5) (drill 1.2) (layers "*.Cu" "*.Mask") (remove_unused_layers no) (net "/PA_SUM") (uuid "{uid()}"))
\t\t(pad "2" thru_hole oval (at 0 -5.08 {rot}) (size 2.5 2.5) (drill 1.2) (layers "*.Cu" "*.Mask") (remove_unused_layers no) (net "GND") (uuid "{uid()}"))
\t)'''

def ps2_jack(ref, value, x, y, rot, ts):
    pins = [
        (1, 10.16, '/PA6'),  (2, 7.62, ''),
        (3, 5.08, 'GND'),    (4, 2.54, 'VCC'),
        (5, 0, '/PA7'),      (6, -2.54, ''),
    ]
    pads = ''
    for num, py, net in pins:
        ns = f'(net "{net}")' if net else ''
        pads += f'''\t\t(pad "{num}" thru_hole oval (at 0 {py} {rot}) (size 2 2) (drill 1) (layers "*.Cu" "*.Mask") (remove_unused_layers no) {ns} (uuid "{uid()}"))\n'''
    return f'''\t(footprint "Connector:PS2-6P_MiniDIN_THT"
\t\t(layer "F.Cu") (uuid "{uid()}") (at {x} {y} {rot})
\t\t(descr "PS/2 6-pin mini-DIN female connector, through hole")
\t\t(tags "PS/2 Mini-DIN 6-pin")
\t\t(property "Reference" "{ref}" (at -5 14 0) (layer "F.SilkS") (uuid "{uid()}") (effects (font (size 1 1) (thickness 0.15))))
\t\t(property "Value" "{value}" (at -5 12 0) (layer "F.SilkS") (uuid "{uid()}") (effects (font (size 1 1) (thickness 0.15))))
\t\t(property "Datasheet" "" (at 0 0 0) (layer "F.Fab") (hide yes) (uuid "{uid()}") (effects (font (size 1.27 1.27))))
\t\t(property "Description" "" (at 0 0 0) (layer "F.Fab") (hide yes) (uuid "{uid()}") (effects (font (size 1.27 1.27))))
\t\t(path "{path(ts)}") (attr through_hole) (duplicate_pad_numbers_are_jumpers no)
\t\t(fp_circle (center 0 3.81) (end 6.5 3.81) (stroke (width 0.12) (type solid)) (layer "F.SilkS") (fill none) (uuid "{uid()}"))
\t\t(fp_line (start -8 14) (end 8 14) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start 8 14) (end 8 -6) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start 8 -6) (end -8 -6) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
\t\t(fp_line (start -8 -6) (end -8 14) (stroke (width 0.05) (type solid)) (layer "F.CrtYd") (uuid "{uid()}"))
{pads}\t)'''


def main():
    # Placement (VPA is at 114.3, 86.36; CPU at 137.16, 86.36)
    # Empty area south of VIA: y=100-130, x=115-170
    # Resistors in a column at x=124
    ry = 101.0
    rd = 3.0

    fps = []
    fps.append(resistor('R22', '1k',   124.0, ry + 0*rd, 0, TS['R22'], '/PA0', ''))
    fps.append(resistor('R23', '2k',   124.0, ry + 1*rd, 0, TS['R23'], '/PA1', ''))
    fps.append(resistor('R24', '4.7k', 124.0, ry + 2*rd, 0, TS['R24'], '/PA2', ''))
    fps.append(resistor('R25', '10k',  124.0, ry + 3*rd, 0, TS['R25'], '/PA3', ''))
    fps.append(resistor('R26', '22k',  124.0, ry + 4*rd, 0, TS['R26'], '/PA4', ''))
    fps.append(resistor('R27', '47k',  124.0, ry + 5*rd, 0, TS['R27'], '/PA5', ''))
    fps.append(rca_jack('J5', 'RCA_VIDEO', 148.0, ry + 2.5*rd, 0, TS['J5']))

    # PS/2 section below
    fps.append(resistor('R28', '4.7k', 124.0, 120.0, 0, TS['R28'], '/PA6', ''))
    fps.append(resistor('R29', '4.7k', 124.0, 124.0, 0, TS['R29'], '/PA7', ''))
    fps.append(ps2_jack('J6', 'PS2_KEYBOARD', 148.0, 122.0, 0, TS['J6']))

    with open(PCB_FILE, 'r') as f:
        content = f.read()

    content = content.rstrip()
    lines = content.split('\n')
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip() == ')':
            insert_at = i
            break
    else:
        print("ERROR: couldn't find closing paren in PCB")
        return

    header = '\n'.join(lines[:insert_at])
    footer = '\n'.join(lines[insert_at:])
    new_content = header + '\n' + '\n'.join(fps) + '\n' + footer

    with open(PCB_FILE, 'w') as f:
        f.write(new_content)

    print(f"✅ Added {len(fps)} footprints to PCB")
    print()
    print("Components placed at (mm):")
    for fp in fps:
        for line in fp.split('\n'):
            if '(at ' in line and not line.strip().startswith('(property'):
                parts = line.split('(at ')[1].split(')')[0].split()
                ref = fp.split('"Reference" "')[1].split('"')[0] if '"Reference" "' in fp else '?'
                x, y = parts[0], parts[1]
                print(f"  {ref:6s}  ({x}, {y})")
                break
    print()
    print("⚠️  PCB routing is NOT included. Open in KiCad and:")
    print("   1. Update PCB from schematic (F8)")
    print("   2. Arrange components optimally")
    print("   3. Route traces between VIA PA pins and new components")
    print()
    print("   Key nets to route:")
    print("     VIA(pad2 PA0) → R22(1) → R22(2) → J5(1) [via summing node]")
    print("     VIA(pad3 PA1) → R23(1) → R23(2) → J5(1)")
    print("     VIA(pad4 PA2) → R24(1) → R24(2) → J5(1)")
    print("     VIA(pad5 PA3) → R25(1) → R25(2) → J5(1)")
    print("     VIA(pad6 PA4) → R26(1) → R26(2) → J5(1)")
    print("     VIA(pad7 PA5) → R27(1) → R27(2) → J5(1)")
    print("     J5(2) → GND")
    print("     VIA(pad8 PA6) → R28(1) + PA6 net")
    print("     R28(2) → VCC + J6(4)")
    print("     VIA(pad9 PA7) → R29(1) + PA7 net")
    print("     R29(2) → VCC + J6(5)")
    print("     J6(1) → PA6")
    print("     J6(3) → GND")

if __name__ == "__main__":
    main()
