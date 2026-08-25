# Speaker Calculator

## Overview
This project provides a single Python script (`speaker_calculator.py`) for designing DIY speaker enclosures.  
It supports two modes:
1. Ported Subwoofer (stacking ratio method + slot port geometry)
2. Sealed Left/Right Channels

The script calculates box volume, internal/external dimensions, and generates a cut sheet with woodworking‑friendly corrections (nearest 0.5 cm).

---

## Features
- Interactive prompts for driver diameter, clearance, port height (ported only), and wall thickness.
- Automatic calculation of:
  - Box volume and tuning frequency (ported mode)
  - Internal and external dimensions
  - Slot port area, length, and folds (ported mode)
- Cut sheet generation for all panels.
- Nearest 0.5 cm correction for practical woodworking.

---

## Usage
```bash
# Navigate to project folder
cd ~/projects/speaker_calculator

# Run the script
python3 speaker_calculator.py
