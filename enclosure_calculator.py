import math

# --- Ported Subwoofer (L-shaped slot port) ---
def stacking_ratio_enclosure(speaker_diameter, clearance, port_height, wall_thickness,
                             clearance_bottom=4, clearance_back=4):
    # Standard volumes and tunings
    standard_values = {
        6.5: (18, 45),
        8:   (28, 38),
        8.75:(30, 38),
        10:  (35, 38),
        12:  (45, 36),
        15:  (70, 32)
    }

    box_volume, tuning_freq = standard_values.get(speaker_diameter, (45, 36))

    # Width = driver diameter (cm) + clearance
    driver_cm = speaker_diameter * 2.54
    internal_width = driver_cm + clearance

    # Height = stacking ratio (≈1.6 × width)
    internal_height = internal_width * 1.6

    # Depth = solve from volume
    internal_depth = (box_volume * 1000) / (internal_width * internal_height)

    # Port calculations
    port_area = port_height * internal_width
    port_length = ((23562.5 * port_area) / (box_volume * tuning_freq ** 2)) - (1.46 * port_height)

    # Horizontal leg length = internal depth − back clearance
    Lh = internal_depth - clearance_back

    # Vertical leg height = total port length − horizontal leg length
    Hv = port_length - Lh

    # Convert wall thickness mm → cm
    wall_thickness_cm = wall_thickness / 10

    external_width = internal_width + (2 * wall_thickness_cm)
    external_height = internal_height + (2 * wall_thickness_cm)
    external_depth = internal_depth + (2 * wall_thickness_cm)

    return {
        "Box Volume (L)": round(box_volume, 2),
        "Tuning Frequency (Hz)": tuning_freq,
        "Internal Dimensions (cm)": {
            "Width": round(internal_width, 2),
            "Height": round(internal_height, 2),
            "Depth": round(internal_depth, 2)
        },
        "External Dimensions (cm)": {
            "Width": round(external_width, 2),
            "Height": round(external_height, 2),
            "Depth": round(external_depth, 2)
        },
        "Port Area (cm²)": round(port_area, 2),
        "Port Length (cm)": round(port_length, 2),
        "Horizontal Leg Length (cm)": round(Lh, 2),
        "Vertical Leg Height (cm)": round(Hv, 2),
        "Port Height (cm)": round(port_height, 2)
    }

def generate_cut_sheet_ported(result):
    # Box panels
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

    # L-shaped port pieces
    internal_width = result["Internal Dimensions (cm)"]["Width"]
    Lh = result["Horizontal Leg Length (cm)"]
    Hv = result["Vertical Leg Height (cm)"]

    cut_sheet["Port Horizontal"] = (internal_width, Lh)
    cut_sheet["Port Vertical"]   = (internal_width, Hv)

    return {k: (round(v[0], 2), round(v[1], 2)) for k, v in cut_sheet.items()}


# --- Sealed Left/Right Channels ---
def sealed_enclosure(speaker_diameter, clearance, wall_thickness):
    # Standard sealed volumes (liters) including 2" and 3"
    sealed_values = {
        2: 1,       # 2" driver → ~1 L
        3: 2,       # 3" driver → ~2 L
        4: 3,
        5.25: 5,
        6.5: 10,
        8: 18
    }

    box_volume = sealed_values.get(speaker_diameter, 10)  # default = 10 L

    # Width = driver diameter (cm) + clearance
    driver_cm = speaker_diameter * 2.54
    internal_width = driver_cm + clearance

    # Height = stacking ratio (≈1.6 × width)
    internal_height = internal_width * 1.6

    # Depth = solve from volume
    internal_depth = (box_volume * 1000) / (internal_width * internal_height)

    # Convert wall thickness mm → cm
    wall_thickness_cm = wall_thickness / 10

    external_width = internal_width + (2 * wall_thickness_cm)
    external_height = internal_height + (2 * wall_thickness_cm)
    external_depth = internal_depth + (2 * wall_thickness_cm)

    return {
        "Box Volume (L)": round(box_volume, 2),
        "Internal Dimensions (cm)": {
            "Width": round(internal_width, 2),
            "Height": round(internal_height, 2),
            "Depth": round(internal_depth, 2)
        },
        "External Dimensions (cm)": {
            "Width": round(external_width, 2),
            "Height": round(external_height, 2),
            "Depth": round(external_depth, 2)
        }
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

    return {k: (round(v[0], 2), round(v[1], 2)) for k, v in cut_sheet.items()}


# --- Interactive Mode ---
if __name__ == "__main__":
    mode = input("Choose mode: (1) Ported Subwoofer, (2) Sealed Left/Right: ")

    if mode == "1":
        speaker_diameter = float(input("Enter speaker diameter (inches): "))
        clearance = float(input("Enter clearance around driver (cm): "))
        port_height = float(input("Enter slot port height (cm): "))
        wall_thickness = float(input("Enter plywood/MDF thickness (mm): "))

        result = stacking_ratio_enclosure(speaker_diameter, clearance, port_height, wall_thickness)
        print("\n--- Ported Subwoofer Results ---")
        for key, value in result.items():
            print(f"{key}: {value}")

        cut_sheet = generate_cut_sheet_ported(result)
        print("\n--- Cut Sheet (Panel Sizes in cm) ---")
        for panel, dims in cut_sheet.items():
            print(f"{panel}: {dims[0]} × {dims[1]}")

    elif mode == "2":
        speaker_diameter = float(input("Enter speaker diameter (inches): "))
        clearance = float(input("Enter clearance around driver (cm): "))
        wall_thickness = float(input("Enter plywood/MDF thickness (mm): "))

        result = sealed_enclosure(speaker_diameter, clearance, wall_thickness)
        print("\n--- Sealed Enclosure Results ---")
        for key, value in result.items():
            print(f"{key}: {value}")

        cut_sheet = generate_cut_sheet_sealed(result)
        print("\n--- Cut Sheet (Panel Sizes in cm) ---")
        for panel, dims in cut_sheet.items():
            print(f"{panel}: {dims[0]} × {dims[1]}")
