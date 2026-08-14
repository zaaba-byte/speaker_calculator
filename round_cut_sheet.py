#!/usr/bin/env python3
import re

def parse_cut_sheet_block(block_text):
    cut_sheet = {}
    # Each line like "Front Panel: 29.83 × 45.56"
    for line in block_text.strip().splitlines():
        if not line.strip():
            continue
        # Split part name from dimensions
        try:
            part, dims = line.split(":")
            part = part.strip()
            # Extract numbers (handles × or x)
            numbers = re.findall(r"[\d\.]+", dims)
            if len(numbers) >= 2:
                w, h = float(numbers[0]), float(numbers[1])
                cut_sheet[part] = (w, h)
        except ValueError:
            continue
    return cut_sheet

def print_cut_sheet(cut_sheet):
    rounded_sheet = {}
    for k, (w, h) in cut_sheet.items():
        if "Port" in k:  # keep ports more precise
            rounded_sheet[k] = (round(w, 1), round(h, 1))
        else:  # panels can be whole numbers
            rounded_sheet[k] = (round(w), round(h))

    print("\n--- Cut Sheet (Panel Sizes in cm) ---")
    for k in cut_sheet:
        calc_w, calc_h = cut_sheet[k]
        round_w, round_h = rounded_sheet[k]
        print(f"{k}: {calc_w:.2f} × {calc_h:.2f}  (rounded → {round_w} × {round_h})")

def main():
    print("Paste your entire cut sheet block below. End with an empty line, then press Ctrl+D:")
    try:
        block_text = ""
        while True:
            line = input()
            if not line.strip():
                break
            block_text += line + "\n"
    except EOFError:
        pass

    cut_sheet = parse_cut_sheet_block(block_text)
    print_cut_sheet(cut_sheet)

if __name__ == "__main__":
    main()
