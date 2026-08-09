import math

def stacking_ratio_enclosure(speaker_diameter, clearance, port_height, wall_thickness):
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

    if port_length > internal_depth:
        folded_length = port_length / 2
        folds = 1
    else:
        folded_length = port_length
        folds = 0

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
        "Folded Port Length (cm)": round(folded_length, 2),
        "Folds": folds
    }

# --- Interactive mode ---
if __name__ == "__main__":
    speaker_diameter = float(input("Enter speaker diameter (inches): "))
    clearance = float(input("Enter clearance around driver (cm): "))
    port_height = float(input("Enter slot port height (cm): "))
    wall_thickness = float(input("Enter plywood/MDF thickness (mm): "))

    result = stacking_ratio_enclosure(speaker_diameter, clearance, port_height, wall_thickness)
    print("\n--- Enclosure Design Results (Stacking Ratio Mode) ---")
    for key, value in result.items():
        print(f"{key}: {value}")

