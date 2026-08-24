# 📝 Cheat Sheet (Essentials Only)

```bash
# 1. Navigate to project folder
cd ~/Documents/speaker_calculator

# 2. Save the script
nano enclosure_calculator.py
# (Paste script, save with CTRL+O, Enter, exit with CTRL+X)

# 3. Run the script
python3 enclosure_calculator.py

# 4. Initialize Git (first time only)
git init

# 5. Add files to Git
git add enclosure_calculator.py README.md README_SCRIPT.md CHEATSHEET.md

# 6. Commit changes
git commit -m "Initial commit with calculator, READMEs, and cheat sheet"

# 7. Link to GitHub (first time only, replace URL with your repo)
git remote add origin https://github.com/zaaba-byte/speaker_calculator.git
git branch -M main

# 8. Push to GitHub
git push -u origin main

# 9. Check status anytime
git status


# Speaker Calculator Cheat Sheet

## Navigate
cd ~/projects/speaker_calculator

## Dependencies (Termux pkg preferred)
pkg install python-numpy python-scipy python-matplotlib

# OR (pip fallback if pkg fails)
pip install numpy==1.26.4 scipy==1.13.1 matplotlib==3.9.2

## Run main calculator
python3 enclosure_calculator.py

## Run cut sheet tool
python3 round_cut_sheet.py

## Optional aliases (add to ~/.bashrc)
alias calc='cd ~/projects/speaker_calculator && python3 enclosure_calculator.py'
alias cut='cd ~/projects/speaker_calculator && python3 round_cut_sheet.py'
