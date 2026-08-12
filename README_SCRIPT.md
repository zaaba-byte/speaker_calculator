# 📦 Enclosure Calculator (Stacking Ratio Mode + Cut Sheet)

## 📝 Purpose
This Python script helps DIY audio builders design **ported speaker enclosures** using the **stacking ratio method**.  
It automatically calculates internal/external dimensions, slot port tuning, and generates a **cut sheet** (panel sizes) for woodworking.

---

## 🚀 Quick Start

```bash
# 1. Navigate to your project folder
cd ~/Documents/speaker_calculator

# 2. Save the script
nano enclosure_calculator.py
# (Paste the full script, save with CTRL+O, press Enter, exit with CTRL+X)

# 3. Run the script
python3 enclosure_calculator.py

# 4. Enter values when prompted
# Example:
# Enter speaker diameter (inches): 8.75
# Enter clearance around driver (cm): 5
# Enter slot port height (cm): 4
# Enter plywood/MDF thickness (mm): 18

# 5. Commit changes to Git
git add enclosure_calculator.py README.md
git commit -m "Add enclosure calculator with cut sheet"
git push origin main
