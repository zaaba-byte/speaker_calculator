#!/usr/bin/env python3
import math

def round_to_half_cm(value):
    return round(value * 2) / 2

# --- Ported Subwoofer ---
def stacking_ratio_enclosure(speaker_diameter, clearance, port_height, wall_thickness,
                             clearance_bottom=4, clearance_back=4):
    standard_values = {
        6.5: (18, 45),
        8:   (28, 38),
        8.75:(30, 38),
        10:  (35, 38),
        12:  (45, 36),
        15:  (70, 32)
    }
    box_volume, tuning_freq = standard_values.get(speaker_diameter, (45, 36))
    driver_cm = speaker_diameter * 2.54
    internal_width = driver_cm + clearance
    internal_height = internal_width * 1.6
    internal_depth = (box_volume * 1000) / (internal_width * internal_height)
    port_area = port_height * internal_width
    port_length = ((23562.5 * port_area) / (box_volume * tuning_freq ** 2)) - (1.46 * port_height)
    Lh = internal_depth - clearance_back
    Hv = port_length - Lh
    wall_thickness_cm = wall_thickness / 10
    external_width = internal_width + (2 * wall_thickness_cm)
    external_height = internal_height + (2 * wall_thickness_cm)
    external_depth = internal_depth + (2 * wall_thickness_cm)
    return {
        "Box Volume (L)": box_volume,
        "Tuning Frequency (Hz)": tuning_freq,
        "Internal Dimensions (cm)": {"Width": internal_width, "Height": internal_height, "Depth": internal_depth},
        "External Dimensions (cm)": {"Width": external_width, "Height": external_height, "Depth": external_depth},
        "Port Area (cm²)": port_area,
        "Port Length (cm)": port_length,
        "Horizontal Leg Length (cm)": Lh,
        "Vertical Leg Height (cm)": Hv,
        "Port Height (cm)": port_height
    }

def generate_cut_sheet_ported(result):
    width = result["External Dimensions (cm)"]["Width"]
    height = result["External Dimensions (cm)"]["Height"]
    depth = result["External Dimensions (cm)"]["Depth"]
    cut_sheet = {
        "Front Panel":  (width, height),
        "Back Panel":   (width, height),
        "Top Panel":    (width, depth),
        "Bottom Panel": (width, depth),
        "Left Side":    (depth, height),
        "Right Side":   (depth, height),
        "Port Horizontal": (result["Internal Dimensions (cm)"]["Width"], result["Horizontal Leg Length (cm)"]),
        "Port Vertical":   (result["Internal Dimensions (cm)"]["Width"], result["Vertical Leg Height (cm)"])
    }
    return cut_sheet

def print_cut_sheet(cut_sheet):
    print("\n--- Cut Sheet (Panel Sizes in cm) ---")
    for k, (w, h) in cut_sheet.items():
        print(f"{k}: {w:.2f} × {h:.2f}  (nearest 0.5 → {round_to_half_cm(w)} × {round_to_half_cm(h)})")

# --- Sealed Enclosure ---
def sealed_enclosure(speaker_diameter, clearance, wall_thickness):
    sealed_values = {2:1, 3:2, 4:3, 5.25:5, 6.5:10, 8:18}
    box_volume = sealed_values.get(speaker_diameter, 10)
    driver_cm = speaker_diameter * 2.54
    internal_width = driver_cm + clearance
    internal_height = internal_width * 1.6
    internal_depth = (box_volume * 1000) / (internal_width * internal_height)
    wall_thickness_cm = wall_thickness / 10
    external_width = internal_width + (2 * wall_thickness_cm)
    external_height = internal_height + (2 * wall_thickness_cm)
    external_depth = internal_depth + (2 * wall_thickness_cm)
    return {
        "Box Volume (L)": box_volume,
        "Internal Dimensions (cm)": {"Width": internal_width, "Height": internal_height, "Depth": internal_depth},
        "External Dimensions (cm)": {"Width": external_width, "Height": external_height, "Depth": external_depth}
    }

def generate_cut_sheet_sealed(result):
    width = result["External Dimensions (cm)"]["Width"]
    height = result["External Dimensions (cm)"]["Height"]
    depth = result["External Dimensions (cm)"]["Depth"]
    cut_sheet = {
        "Front Panel":  (width, height),
        "Back Panel":   (width, height),
        "Top Panel":    (width, depth),
        "Bottom Panel": (width, depth),
        "Left Side":    (depth, height),
        "Right Side":   (depth, height)
    }
    return cut_sheet

# --- Interactive Mode ---
if __name__ == "__main__":
    mode = input("Choose mode: (1) Ported Subwoofer, (2) Sealed Left/Right: ")
    if mode == "1":
        d = float(input("Enter speaker diameter (inches): "))
        c = float(input("Enter clearance around driver (cm): "))
        ph = float(input("Enter slot port height (cm): "))
        wt = float(input("Enter plywood/MDF thickness (mm): "))
        result = stacking_ratio_enclosure(d, c, ph, wt)
        print("\n--- Ported Subwoofer Results ---")
        for k,v in result.items(): print(f"{k}: {v:.2f}" if isinstance(v,float) else f"{k}: {v}")
        cut_sheet = generate_cut_sheet_ported(result)
        print_cut_sheet(cut_sheet)
    elif mode == "2":
        d = float(input("Enter speaker diameter (inches): "))
        c = float(input("Enter clearance around driver (cm): "))
        wt = float(input("Enter plywood/MDF thickness (mm): "))
        result = sealed_enclosure(d, c, wt)
        print("\n--- Sealed Enclosure Results ---")
        for k,v in result.items(): print(f"{k}: {v:.2f}" if isinstance(v,float) else f"{k}: {v}")
        cut_sheet = generate_cut_sheet_sealed(result)
        print_cut_sheet(cut_sheet)
