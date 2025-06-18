# 📁 Clear and Clutter - File Organizer (Python Project)

This is a **Python-based console project** that organizes files in a selected folder (like `Downloads`) by moving them into categorized subfolders like Documents, Images, Videos, Setups, and Others.

---

## 💡 Features

- 🧠 Automatically identifies file types and organizes them into folders:
  - 📄 `Documents`: `.pdf`, `.docx`
  - 🖼️ `Images`: `.jpg`, `.png`
  - 🎥 `Videos`: `.mp4`, `.mkv`
  - ⚙️ `Setups`: `.exe`, `.msi`
  - 🧩 `Others`: Files with other extensions
- 📂 Skips folders (directories) while processing.
- ✅ Creates destination folders if they do not exist.
- 🔄 Handles all moves in a single run and provides user feedback.

---

## 🔧 Requirements

- Python 3.x
- Modules used: `os`, `shutil` (both are built-in)

---

## 🚀 How to Run

1. Open your terminal or IDE.
2. Ensure your source and destination folders are correctly set in the code.
3. Run the script:

```bash
python clear_and_clutter.py
