# 📦 Speaker Enclosure Calculator (Stacking Ratio Mode)

## Overview
This Python script helps DIY audio builders design **ported speaker enclosures** using the **stacking ratio method**.  
It balances **acoustic performance** ("the beast") with **aesthetic proportions** ("the beauty"), ensuring boxes look elegant while staying tuned for deep bass.

---

## 🎵 Why Stacking Ratio Mode?
- **Width**: Determined by driver diameter + clearance (≈5–7 cm).  
- **Height**: Calculated as `1.6 × width` (stacking ratio).  
- **Depth**: Solved automatically from target box volume.  
- **Port**: Slot port dimensions recalculated to maintain tuning frequency.

This approach ensures enclosures are **portrait‑style** (taller than wide), which looks better in most builds while keeping the math correct.

---

## ⚙️ Features
- Interactive prompts for:
  - Driver diameter (inches)
  - Clearance around driver (cm)
  - Slot port height (cm)
  - Wall thickness (mm)
- Automatic calculation of:
  - Internal & external dimensions
  - Box volume and tuning frequency
  - Slot port area, length, and folds
- Supports fractional driver sizes (e.g., 8.75″).

---

## ▶️ Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/yourname/speaker_calculator.git
   cd speaker_calculator
